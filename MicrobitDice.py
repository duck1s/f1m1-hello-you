from microbit import *

x_offset = 2
y_offset = 2

while True:
    x = int(accelerometer.get_x() / 250 + x_offset)
    y = int(accelerometer.get_y() / 250 + x_offset)
    if x > 4: x = 4
    if x < 0: x = 0
    if y > 4: y = 4
    if y < 0: y = 0
    display.set_pixel(x,y,5)
    if button_a.is_pressed():
        display.clear()