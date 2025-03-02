# Bluepad32 in Blocks Pybricks
Here you find some examples for using the BluePad32 firmware together with the Block-based pybricks. First you need to install the `bluepad.py` from the [Library directory](https://github.com/ste7anste7an/bluepad/tree/main/Library) of this repo.

## Tutorial

Head over to [antonsmindstorms.com](https://www.antonsmindstorms.com) to see a number of tutorials about Bluepad32 in combination with Pybricks. The tutorial [Gamepad remote control with PyBricks Block coding](https://www.antonsmindstorms.com/2024/01/04/gamepad-remote-control-with-pybricks-block-coding/) specifically shows how to yhe Bluepad32 in Pybirkcs Block language.

## Template
The `bp_template.py` contains the blocks needed for importing the bluepad library in the blocks version of PyBricks. When using this template, the user can deploy the following functions:
* bluepad_init
  
![image](https://github.com/user-attachments/assets/60961c0a-f46a-4b18-801f-147c37ab5f32)

It needs a parameter indicating the port ("A", as a string) to which the LMS-ESP32 is connected.

* gamepad
  
![image](https://github.com/user-attachments/assets/0c842f8b-2118-473d-ab3a-d7802d915278)


This function reads the current gamepad values and returns an array with left and right joustick x- and y-positions and the buttons and dpad states. 

* get_left_stick_horizontal
  
![image](https://github.com/user-attachments/assets/bbd5b148-321e-42f9-94d6-303c4ce07d48)

Reads the left stick x position

* get_left_stick_vertical
  
![image](https://github.com/user-attachments/assets/d71b1d7d-7cfc-487b-a4f5-79707c0678ad)

Reads the left stick y-coordinate.
* get_left_stick_horizontal

![image](https://github.com/user-attachments/assets/271f37d5-4b5f-4119-bc25-33c17ed3e916)

Reads the right stick x-coordinate.
* get_left_stick_vertical

![image](https://github.com/user-attachments/assets/e99b8797-ae2c-45b4-8252-261655366af1)


Reads the right stick y-coordinate.

* get_buttons

![image](https://github.com/user-attachments/assets/4868346e-ae95-4900-a318-d6feaadea178)

Read the integer value representing the bttons that are pressed. Each button is represented by a specific bit value. You can figure out the values for your gamepad, by printing the `get_button` values in a loop.

* get_direction_pad

![image](https://github.com/user-attachments/assets/390bcd17-3e03-44b3-a0d4-aa57b8c2d7d6)

Read the integer value representing the dpad buttons that are pressed. Each button is represented by a specific bit value. You can figure out the values for your gamepad, by printing the `get_direction_pad` values in a loop.

* neopixel_init
  
![image](https://github.com/user-attachments/assets/44b7292f-4537-49ba-ab6d-9a936032999a)

Initializes the NeoPixel with a number of pixels (first parameter) and the hardware GPIO port to which the NeoPixels are connected (second parameter).

* neopixel_set
  
![image](https://github.com/user-attachments/assets/00be6242-3739-4a79-b881-89ae61f1e367)

Set a NeoPixel at number `n` (first parameter, strating with 0) to a color with optionally a third parameter giving the intensity (between 0 and 1, default 1) and the optional fourth parameter is a boolean that determines whether the pixels are written to the physical neopixels, default is True.

* neopixel_fill
  
![image](https://github.com/user-attachments/assets/fa8edf10-af6d-43e7-98cb-97908b51de30)

Fills all NeoPixels with the same color defined by `Color`. Optionally a second parameters is the intensity (between 0 and 1, default 1) and the optional fourth parameter is a boolean that determines whether the pixels are written to the physical neopixels, default is True.

* servo
  
![image](https://github.com/user-attachments/assets/7fc64498-d516-4640-975e-6cc3a5b29166)

The first parameter indicates the servo motor number `n` ( where servo number 0 to 3 which is mapped to GPIO pins 21, 22, 23, and 25 for LMS-ESP32v1 and to GPIO pins 19, 20, 21, and 22). The second parameter `angle` is the angle to which the servo is set (usually between 0 and 180).

