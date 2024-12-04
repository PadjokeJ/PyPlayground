from copy import copy
import os
from time import sleep

import math

import datetime

# init screen
col = [0 for i in range(21)]
screen = [copy(col) for i in range(21)]

def cls(s):
    for x in range(len(s)):
        for y in range(len(s)):
            s[x][y] = 0
    return s

# 
def render(s):
    for x in range(len(s)):
        for y in range(len(s)):
            if s[x][y]:
                print('&&', end='')
            else:
                print('__', end = '')
        print()

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
#
screen[10][10] = 1
render(screen)

while True:
    screen = cls(screen)
    
    now = datetime.datetime.now()
    s = now.time().second
    dx = math.cos(math.pi * (-s/60 + .5) * 2) * 8
    dy = math.sin(math.pi * (-s/60 + .5) * 2) * 8
    
    # bresenham
    x0, x1 = 10, 10 + int(dx)
    y0, y1 = 10, 10 + int(dy)
    
    dx = abs(dx)
    sx = -1
    if x0 < x1:
        sx = 1
    dy = -abs(dy)
    sy = -1
    if y0 < y1:
        sy = 1
    error = dx + dy
    
    while True:
        screen[x0][y0] = 1
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * error
        if e2 >= dy:
            if x0 == x1:
                break
            error += dy
            x0 += sx
        if e2 <= dx:
            if y0 == y1:
                break
            error += dx
            y0 += sy
        
        
    
    sleep(1)
    clear()
    render(screen)
    print(s)