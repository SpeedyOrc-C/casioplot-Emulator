from casioplot import *

for x in range(128):
    for y in range(64):
        if (x//4 + y//4) % 2 == 0:
            set_pixel(x, y)

show_screen()
