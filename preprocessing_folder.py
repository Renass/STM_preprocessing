import glob
from spym.io import rhksm4
import numpy as np
from matplotlib import pyplot as plt
import os
import sati
from IPython.display import clear_output
from scipy.stats import norm

def listdirs(rootdir):
    result = []
    for it in os.scandir(rootdir):
        if it.is_dir():
            result.append(it.path)
            #print(it.path)
            for inner_path in listdirs(it):
                result.append(inner_path)
    return result

def equalize(num, x1=1, x2=99):
    nums = num.reshape(num.shape[0]*num.shape[1])
    nums = np.sort(nums)
    x1 = nums[int(x1/100*len(nums))]
    x2 = nums[int(x2/100*len(nums))]
    num = num.clip(x1, x2)
    num = 255*(num-np.min(num))/(np.max(num)-np.min(num))
    return num

def sm4_microscopy_preprocess(dir, cmap, eq1, eq2):
    print('\n\nMicroscopy script:')
    path = os.getcwd()
    try:
        os.mkdir(path+'/sm4_microscopy_image')
    except OSError as error:
        pass
    if dir == 'current':
        names = glob.glob(path+'\\*.SM4')
    elif dir == 'inner':
        names = glob.glob(path+'\\*.SM4')
        for inner_path in listdirs(path):
            for name in glob.glob(inner_path+'\\*.SM4'):
                names.append(name)



    for name in names:
        title = name.split('\\')[-1].split('.')[0]
        print('\n\n'+title)
        try:
            f = rhksm4.load(name)
            for page in f:
                #print(page.label)
                if (page.label == ('Topography_Forward') or page.label == ('Aux_1__Forward')):
                    #print('\n\n'+title)
                    print(page.label)
                    num = np.array(page.data[:,::-1])    
                    num = (num-np.min(num))/(np.max(num)-np.min(num))
                    img1 = num*255
                    size1 = img1.shape[0]
                    size2 = img1.shape[1]
                    img1_p1 = img1[0:size1//2,0:size2//2] 
                    img1_p2 = img1[size1//2:size1,0:size2//2] 
                    img1_p3 = img1[0:size1//2,size2//2:size2] 
                    img1_p4 = img1[size1//2:size1,size2//2:size2]
                        
                    initrsp1 = sati.GuessInitRsp(img1_p1, n=1, threshold=254.5)
                    initrsp2 = sati.GuessInitRsp(img1_p2, n=1, threshold=254.5)
                    initrsp3 = sati.GuessInitRsp(img1_p3, n=1, threshold=254.5)
                    initrsp4 = sati.GuessInitRsp(img1_p4, n=1, threshold=254.5)
                    m1 = sati.Model(img1_p1, rsp=initrsp1.guess, dist=sati.distributions.Norm(), 
                                    poly=sati.planes.Poly())
                    m2 = sati.Model(img1_p2, rsp=initrsp2.guess, dist=sati.distributions.Norm(), 
                                    poly=sati.planes.Poly())
                    m3 = sati.Model(img1_p3, rsp=initrsp3.guess, dist=sati.distributions.Norm(), 
                                    poly=sati.planes.Poly())
                    m4 = sati.Model(img1_p4, rsp=initrsp4.guess, dist=sati.distributions.Norm(), 
                                    poly=sati.planes.Poly())
                    m1.optimize()
                    m2.optimize()
                    m3.optimize()
                    m4.optimize()

                    m1.subtracted= equalize(m1.subtracted,eq1,eq2)
                    m2.subtracted= equalize(m2.subtracted,eq1,eq2)
                    m3.subtracted= equalize(m3.subtracted,eq1,eq2)
                    m4.subtracted= equalize(m4.subtracted,eq1,eq2)

                    if cmap == 0:
                        fig,axs=plt.subplots(2,2,figsize=(7,7))
                        axs[0,0].imshow(m1.subtracted).set_cmap('afmhot')
                        axs[1,0].imshow(m2.subtracted).set_cmap('afmhot')
                        axs[0,1].imshow(m3.subtracted).set_cmap('afmhot')
                        axs[1,1].imshow(m4.subtracted).set_cmap('afmhot')
                    if cmap == 1:
                        fig,axs=plt.subplots(2,2,figsize=(7,7))
                        axs[0,0].imshow(m1.subtracted).set_cmap('hot')
                        axs[1,0].imshow(m2.subtracted).set_cmap('hot')
                        axs[0,1].imshow(m3.subtracted).set_cmap('hot')
                        axs[1,1].imshow(m4.subtracted).set_cmap('hot')    
                    plt.close(fig)
                    fig.savefig(path+'/sm4_microscopy_image/'+title+page.label+'.jpg')
        except:
            print('Error in '+title)
    #clear_output(wait=False)





def sm4_spectroscopy_preprocess(dir):
    print('\n\nSpectroscopy script:')
    
    path = os.getcwd()
    try:
        os.mkdir(path+'/sm4_spectroscopy_image')
    except OSError as error:
        pass
    if dir == 'current':
        names = glob.glob(path+'\\*.SM4')
    elif dir == 'inner':
        names = glob.glob(path+'\\*.SM4')
        for inner_path in listdirs(path):
            for name in glob.glob(inner_path+'\\*.SM4'):
                names.append(name)
    
    
    
    for name in names:
        title = name.split('\\')[-1].split('.')[0]
        print('\n\n'+title)
        try:
            f = rhksm4.load(name)
            for page in f:
                if (page.label == ('Aux_1_') or page.label == ('Current_')):
                    print(page.label)
                    numX = np.array(page.coords[1][1])
                    num = np.array(page.data)
                    #print(num[0][::-1])
                    fig,axs=plt.subplots(1,figsize=(10,10))
                    axs.plot(numX, num[0])
                    axs.grid()
                    #axs[0].set_xticklabels('xyZ',fontsize=15)
                    axs.plot(numX, num[1])
                         

 
                    plt.close(fig)
                    fig.savefig(path+'/sm4_spectroscopy_image/'+title+'__'+page.label+'.jpg')
        except:
            print('Error in '+title)

if __name__ == "__main__":
    #sm4_microscopy_preprocess('current',1, 5, 95) 
    sm4_spectroscopy_preprocess('current')