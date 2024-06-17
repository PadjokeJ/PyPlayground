from PIL import Image
from copy import copy
from random import randint
from math import *
print("opening image")
img = Image.open("image.png")
print("choose scale (300 gives best result)")
a = input("int:")
i = int(a)
print("compressing")
img = img.resize((i * 3, i * 4))
size = width, height = img.size
print("getting ready")
pixels = img.load()
print ("enter conversion mode \n(lines, that, flip, red, noise, deflate, uv, aa)")
a = input("mode:")
if a == "lines" or a == "1" or a == "2":
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        step = 0
        for pix in range(width):
            step += 1
            if step == 3:
                p = pixels[pix, row]
                pixels[pix - 2, row] = (p[0], 0, 0)
                pixels[pix - 1, row] = (0, p[1], 0)
                pixels[pix, row] = (0, 0, p[2])
                step = 0
if a== "flip":
    print("initialising")
    img2 = copy(img)
    print("duplicating pixels")
    pixels2 = img2.load()
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels2[x, row]
            pixels[x, height - row - 1] = (p[0], p[1], p[2])
if a== "that" or a == "1":
    print("choose steps")
    b = input("int:")
    i = int(b)
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (int(p[0]/i)*i, int(p[1]/i)*i, int(p[2]/i)*i)
if a== "red":
    print("choose bg")
    b = input("int:")
    i = int(b)
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (p[0], i, i)
if a== "noise":
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (p[0], randint(0, 255), randint(0, 255))
if a== "deflate":
    print("enter scale (the higher, the less the effect shows)")
    a = input("int:")
    i = int(a)
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (int((p[0] * i + p[1] + p[2])/(2 + i)), int((p[0] + p[1] * i + p[2])/(2 + i)), int((p[0] + p[1] + p[2] * i)/(2 + i)))
if a== "uv" or a == "2":
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (int((x/width)*255), p[1], int((row/height)*255))
if a== "aa":
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            if x > 1:
                p = pixels[x, row]
                p2 = pixels[x-1, row]
                p3 = pixels[x-2, row]
                pixels[x, row] = (int((pixels[x, row][0] + pixels[x - 1, row][0] + pixels[x - 2, row][0])/3), int((pixels[x, row][1] + pixels[x - 1, row][1] + pixels[x - 2, row][1])/3), int((pixels[x, row][2] + pixels[x - 1, row][2] + pixels[x - 2, row][2])/3))
if a== "hot":
    print("enter value")
    b = input("int:")
    i = int(b)
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (max(min(p[0] + i, 255), 0), p[1], p[2])
if a== "greener":
    print("enter value")
    b = input("int:")
    i = int(b)
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (p[0], max(min(p[1] + i, 255), 0), p[2])

if a== "cold":
    print("enter value")
    b = input("int:")
    i = int(b)
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (p[0], p[1], max(min(p[2] + i, 255), 0))

if a== "washed":
    print("copying image")
    img2 = copy(img)
    print("loading")
    p2 = img2.load()
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        p = []
        for x in range(width):
            p.append(p2[x, row])
            i = 0
            col = r, g, b = 0, 0, 0
            for item in p:
                i+=1
                r += item[0]
                g += item[1]
                b += item[2]
            r = r / i
            g = g / i
            b = b / i
            r = int(r)
            g = int(g)
            b = int(b)
            pixels[x, row] = (r, g, b)
if a== "washed2":
    print("copying image")
    img2 = copy(img)
    print("loading")
    p2 = img2.load()
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        i = 0
        r, g, b = 0, 0, 0
        for x in range(width):
            p = p2[x, row]
            i = i + 1
            r += p[0]
            g += p[1]
            b += p[2]
            pixels[x, row] = (int(r/i), int(g/i), int(b/i))
if a== "out":
    print("copying image")
    img2 = copy(img)
    pix = img2.load()
    print("enter value")
    i = int(input("int:"))
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (p[0], p[1], p[2])
            if x > 0:
                p2 = pix[x - 1, row]
                if abs(p2[0] - p[0]) > i or abs(p2[1] - p[1]) > i or abs(p2[2] - p[2]) > i:
                    pixels[x, row] = (0, 0, 0)
            if row > 0:
                p2 = pix[x, row - 1]
                if abs(p2[0] - p[0]) > i or abs(p2[1] - p[1]) > i or abs(p2[2] - p[2]) > i:
                    pixels[x, row] = (0, 0, 0)
if a== "ascii":
    print("loading")
    img = img.convert("L")
    lis = ["..", "-", " i", "o", "a", "m", "0", "M", "#"]
    pixels = img.load()
    print("starting")
    i = 0
    for row in range(height):
        print("")
        for x in range(width):
            i += 1
            p = pixels[x, row]
            print(lis[int(p/30)], end = "")
    print("\n" + str(i))
print("Saving...")
img.save("im2.png")
print("100%")
