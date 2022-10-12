# Volume_Control_With_Potentiometer

This project helps you control the volume on your computer using potentiometer connected to Arduino board.

--------------------------------------------
Run: "volume_control.ino" on your Arduino board then "volume_control.py" on your PC.
--------------------------------------------

# Requirments
Hardware:
- Windows PC
- Arduino board (Nano in this case)
- Compatible USB cable
- Potentiometer
- Jumper wires

Software:
- Windows 10
- Python language
- Arduino sketch

Python dependencies:
- pip install pyserial
- pip install pycaw

# Workings
- The Arduino board gets values from the potentiometer and sends it to your PC running Python via serial (USB).
- The Python code on your PC gets the data from arduino using the pyserial library.
- Audio modules from the pycaw library are then utilized to macth the potentiometer values to your PC volume values. 
