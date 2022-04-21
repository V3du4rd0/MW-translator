# MW-translator
### Maya-Wolfram translator (minimal area optimizer)

This Python script can be used to extract the data of a triangulated polygon in Maya, send it to a Wolfram script execution and recover the output to send it back to Maya.

This code was conceived to call Wolfram's [Douglas-Plateau problem solver](https://community.wolfram.com/groups/-/m/t/1341653) and create minimal area patches in Maya.

To run this code you need to:

1. Select (in object mode) a _triangulated_ mesh in your Maya scene.
  
2. Modify the variable "func" in line 70 (minimalOPT_v01.py), this variable must contain the wolfram script as a string. The "Implementation" section in Wolfram's post includes all the required code (you only need to copy and merge everything as a single string preserving the Wolfram syntax).
  
3. Use Maya Script Editor to run the modified python code.
  

Note: Please check [Wolfram's post](https://community.wolfram.com/groups/-/m/t/1341653) , there are some conditions that your model and some parameters must hold --face size, stepsize_, steps_, etc--.

You can find an obj file inside "Test" directory. Import this file in Maya to get four working models (see the pictures below).


![c](https://user-images.githubusercontent.com/36924228/91630664-d1a87380-e998-11ea-8e63-dfe5a415db1f.png)

![ch](https://user-images.githubusercontent.com/36924228/91630677-e1c05300-e998-11ea-9ff6-5f8e58c4f651.png)

![sh](https://user-images.githubusercontent.com/36924228/91630681-eb49bb00-e998-11ea-9fa9-c4af44784a69.png)
