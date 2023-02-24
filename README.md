# SM4 STM_preprocessing

This repository contains program for quick observation .SM4 - format microscopy data as jpg images.
You can briefly see STM, AFM results of measurements for whole folder. 

![image](https://user-images.githubusercontent.com/65440465/221204555-7dd88d97-9160-43b7-8283-6e4d5bb3d549.png)

![image](https://user-images.githubusercontent.com/65440465/221223950-ac6bd5dd-725d-470c-a620-27de376792ee.png)



It has UI widget with initial settings:
1. SM4 object type - Microscopy (STM, AFM) option creates surface image, whereas Spectroscopy maps energy distribution into a basic graph.
2. Equalizing parameter - (microscopy option) - All intensivity values are sorted ascending and values between (lower threshold limit) and (higher threshold limit) only would be mapped evenly on colormap. This option may set up no colorshift of the colormap on too big and too low values of intensivity. With loosing info outside of this gap, values inside the gap would be distrbuted by colormap more. 
3. Colormap - (microscopy option) - color distribution to visualize data.
4. Directory - mode of gathering files to operate
"Only current directory" - operate all sm4 files within the same directory, where script started
"Include inner directories" - operate all sm4 files within working directory and all directories inside it in full depth     


# How to use
https://drive.google.com/file/d/1lsD7TAXyUosX0bgq8DyBYU9KQM22PfUm/view?usp=sharing
1. Download single executable file .exe (All dependencies included)
2. Copy that file in the folder with sm4 files
3. Select settings on a UI (like on the image above) and press "Start"
4. Folder with jpg images will appear on the same folder, where executable started, names are the same with the original sm4 files.

# Repo content
1. .ui files - widget templates made by QtDesigner
2. cmaps.jpg - colormap visualization image in widget
3. preprocessing_folder.ipynb - Development Jupyter workfile
4. preprocessing_folder.py - Python version of the program - Backend without UI
5. main2.py - Python version of the project with UI (needs cmaps and ui in the same folder to work, needs Python installed and dependency packages)  

https://drive.google.com/file/d/1lsD7TAXyUosX0bgq8DyBYU9KQM22PfUm/view?usp=sharing - Single-file compiled executable (Python-independent version of the project)

 
