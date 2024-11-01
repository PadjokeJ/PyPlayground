from PIL import Image
from copy import copy
from random import randint, shuffle
from math import *
import os
print("opening image")
img = Image.open("image.png")
print("choose image scale (0 - 1)")
a = input("int:")
i = float(a)
print("compressing")
size = img.size
img = img.resize((int(i * size[0]), int(i * size[1])))
size = width, height = img.size
print("getting ready")
pixels = img.load()
try:
    dir = "images/"
    os.mkdir("images")
except:
    dir = "images/"

# ----------------- DEFINITIONS ----------------- 

def lines():
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

def flip():
    print("initialising")
    img2 = copy(img)
    print("duplicating pixels")
    pixels2 = img2.load()
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels2[x, row]
            pixels[x, height - row - 1] = (p[0], p[1], p[2])

def round():
    print("choose steps")
    b = input("int:")
    i = int(b)
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (int(p[0]/i)*i, int(p[1]/i)*i, int(p[2]/i)*i)

def redify():
    print("choose bg")
    b = input("int:")
    i = int(b)
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (p[0], i, i)

def noisify():
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (p[0], randint(0, 255), randint(0, 255))

def deflate():
    print("enter scale (the higher, the less the effect shows)")
    a = input("int:")
    i = int(a)
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (int((p[0] * i + p[1] + p[2])/(2 + i)), int((p[0] + p[1] * i + p[2])/(2 + i)), int((p[0] + p[1] + p[2] * i)/(2 + i)))

def uv():
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (int((x/width)*255), p[1], int((row/height)*255))

def antialiasing():
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            if x > 1:
                p = pixels[x, row]
                p2 = pixels[x-1, row]
                p3 = pixels[x-2, row]
                pixels[x, row] = (int((pixels[x, row][0] + pixels[x - 1, row][0] + pixels[x - 2, row][0])/3), int((pixels[x, row][1] + pixels[x - 1, row][1] + pixels[x - 2, row][1])/3), int((pixels[x, row][2] + pixels[x - 1, row][2] + pixels[x - 2, row][2])/3))

def hot():
    print("enter value")
    b = input("int:")
    i = int(b)
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (max(min(p[0] + i, 255), 0), p[1], p[2])

def greenify():
    print("enter value")
    b = input("int:")
    i = int(b)
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (p[0], max(min(p[1] + i, 255), 0), p[2])

def cold():
    print("enter value")
    b = input("int:")
    i = int(b)
    print("starting")
    for row in range(height):
        print(str(int(100*row/height)) + "%")
        for x in range(width):
            p = pixels[x, row]
            pixels[x, row] = (p[0], p[1], max(min(p[2] + i, 255), 0))

def wash():
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
            
def wash2():
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

def outline():
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
def ascii(img):
    print("loading")
    img = img.convert("L")
    lis = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]
    pixels = img.load()
    print("starting")
    i = 0
    f = open("ascii_art.txt", "w")
    txt = ""
    for row in range(0, height, 2):
        txt = ""
        print("")
        for x in range(width):
            i += 1
            p = pixels[x, row]
            print(lis[int(p//25)], end = "")
            txt += lis[int(p//25)]
        
        f.write(txt + "\n")
    f.close()
    
    print("\n" + str(i))
    
def shuffle():
    pixels = img.load()
    for y in range(height):
        _pixels = []
        for x in range(width):
            _pixels.append(pixels[x, y])
        shuffle(_pixels)
        for x in range(width):
            pixels[x, y] = _pixels[x]
    for x in range(width):
        _pixels = []
        for y in range(height):
            _pixels.append(pixels[x, y])
        shuffle(_pixels)
        for y in range(width):
            pixels[x, y] = _pixels[y]
            
def sort():
    pixels = img.load()
    for y in range(height):
        _pixels = []
        for x in range(width):
            _pixels.append(pixels[x, y])
        _pixels.sort()
        for x in range(width):
            pixels[x, y] = _pixels[x]
            
def imgsort():
    print("enter value")
    i = int(input("int:"))
    for y in range(height):
        _pixels = []
        inception = []
        for x in range(width):
            p = pixels[x, y]
            inception.append(p)
            if x > 0:
                p2 = pixels[x - 1, y]
                if abs(p2[0] - p[0]) > i or abs(p2[1] - p[1]) > i or abs(p2[2] - p[2]) > i:
                    inception.sort()
                    for item in inception:
                        _pixels.append(item)
                    inception.clear()
        inception.sort()
        for item in inception:
            _pixels.append(item)
        for x in range(width):
            pixels[x, y] = _pixels[x]
            
# ----------------- MAIN CODE  ----------------- 
            
modes = ["lines", "flip", "round", "red", "green", "sort", "imgsort", "shuffle", "outline", "ascii", "wash", "wash2", "hot", "cold", "antialiasing", "uv", "deflate", "noisify"] 
iteration = 0
for mode in modes:
    print(f"[{iteration}] : {mode}")
    iteration += 1
    
def mode_select():
    try:
        type = modes[int(input("mode:"))]
        return type
    except:
        mode_select()
        
type = mode_select()

match type:
    case "lines": lines()
    case "flip": flip()
    case "round": round()
    case "red": redify()
    case "green": greenify()
    case "sort": sort()
    case "imgsort": imgsort()
    case "shuffle": shuffle()
    case "outline": outline()
    case "ascii": ascii(img)
    case "wash": wash()
    case "wash2": wash2()
    case "cold": cold()
    case "hot": hot()
    case "antialiasing": antialiasing()
    case "uv": uv()
    case "deflate": deflate()
    case "noisify": noisify()

print("Saving...")
for root, dirs, files in os.walk("images"):
    int = len(files) + 1
    break
img.save(f"{dir}im{int}.png")
img.show()
print("100%")

exit()
