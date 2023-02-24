# STM_preprocessing
![image](https://user-images.githubusercontent.com/65440465/221204555-7dd88d97-9160-43b7-8283-6e4d5bb3d549.png)


This repository contains program for quick observation .SM4 - format microscopy data as jpg images.

It has UI widget with initial settings:
1. SM4 object type - Microscopy (STM, AFM) option creates surface image, whereas Spectroscopy maps energy distribution into a basic graph.
2. Equalizing parameter - (microscopy option) - All intensivity values are sorted ascending and values between (lower threshold limit) and (higher threshold limit) only would be mapped evenly on colormap. This option may set up no colorshift of the colormap on too big and too low values of intensivity. With loosing info outside of this gap, values inside the gap would be distrbuted by colormap more. 
3. Colormap - (microscopy option) - color distribution to visualize data.
4. Directory - mode of gathering files to operate
"Only current directory" - operate all sm4 files within the same directory, where script started
"Include inner directories" - operate all sm4 files within working directory and all directories inside it in full depth     


# How to use
