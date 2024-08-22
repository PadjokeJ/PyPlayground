import pygame
from physics import v2, v2Lerp
from icons import save
from icons import eraser, pen
import fps as debug
import os


pygame.init()
#screen size
scr = (width, height) = (0, 0)
screen = pygame.display.set_mode(scr)
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
#init clock for fps manipulation
clock = pygame.time.Clock()
#feel free to edit the fps of your game
fps = 60

try:
    dir = "drawings/"
    os.mkdir("drawings")
except:
    dir = "drawings/"
class ToolButton:
    color = "blue"
    def __init__(self, tool, pos, size):
        self.tool = tool
        self.pos = pos
        self.size = size
        self.rect = pygame.Rect(pos.tuple(), size.tuple())
    def icon(self, icon):
        
        for i in icon.points:
            i.scale(20)
            i.add(v2(0, 0).copy(self.pos).add(v2(10, 10)))
        icon.to_tuple()
        self.icon = icon
        return self
    def check(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed(3)[0]:
            self.color = "black"
            return self.tool
        else:
            self.color = "blue"
    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        try:
            pygame.draw.lines(surface, "white", False, self.icon.pts, 5)
        except:
            pass

canvas = pygame.Surface((width - 80, height - 280))
ui = pygame.Rect((40, height - 200), (width - 80, 200))
canvas.fill("white")
prev = v2(0, 0)
mouse = v2(0, 0).from_tuple(pygame.mouse.get_pos())
prev.copy(mouse)
screen.fill("white")
color = "black"
clicked = False

buttons = []

buttons.append(ToolButton("eraser", v2(80, height - 160), v2(120, 120)).icon(eraser))
buttons.append(ToolButton("pen", v2(240, height - 160), v2(120, 120)).icon(pen))
buttons.append(ToolButton("clear", v2(400, height - 160), v2(120, 120)))
buttons.append(ToolButton("save", v2(width - 200, height - 160), v2(120, 120)).icon(save))


tool = "pen"
max_size = 100
if tool == "pen":
    size = 10
    color = "black"
if tool == "eraser":
    size = 20
    color = "white"

sizeSliderStart = v2(560, height - 150)
sizeSliderEnd = v2(width - 240, height - 150)
sizeKnob = v2Lerp(sizeSliderStart, sizeSliderEnd, size/max_size)

def line(surface, color, start, end, thickness):
    length = start.distance(end)
    length = int(length)
    dir = v2(0, 0).copy(end).remove(start).normalize()
    pos = v2(0, 0).copy(start)
    pygame.draw.circle(surface, color, pos.tuple(), thickness//2)
    for i in range(length):
        pygame.draw.circle(surface, color, pos.tuple(), thickness//2)
        pos.add(dir)

canvas_active = True
canvmouse = v2(0, 0)

from datetime import datetime
from datetime import date
def save(image):
    _date = str(date.today().day) + "." + str(date.today().month) + "." + str(date.today().year)
    _time = str(datetime.now().hour) + "." + str(datetime.now().minute) + "." + str(datetime.now().second)
    pygame.image.save(image, f"{dir}drawing_{_date}_{_time}.png")

print("start loop")
while True:
    #
    clock.tick()
    screen.fill("black")
    pygame.draw.rect(screen, "gray", ui)
    for button in buttons:
        if button.check() != None:
            tool = button.check()
            if tool == "pen":
                size = 10
                color = "black"
            if tool == "eraser":
                size = 20
                color = "white"
            if tool == "clear":
                canvas.fill("white")
                tool = "pen"        
            if tool == "save":
                save(canvas)
                tool = "pen"
        button.render(screen)
    # ui mouse
    mouse.from_tuple(pygame.mouse.get_pos())
    pygame.draw.circle(screen, "red", mouse.tuple(), 20, 5)
    
    pygame.draw.line(screen, "black", sizeSliderStart.tuple(), sizeSliderEnd.tuple(), 10)
    if mouse.distance(sizeKnob) < 100:
        if mouse.x > sizeKnob.x:
            size += int(abs(mouse.x - sizeKnob.x))//10
        else:
            size -= int(abs(mouse.x - sizeKnob.x))//10
    sizeKnob = v2Lerp(sizeSliderStart, sizeSliderEnd, size/max_size)
    pygame.draw.circle(screen, "black", sizeKnob.tuple(), 20)
    
    #canvas mouse
    
    if canvas_active:
        canvmouse.copy(mouse).remove(v2(40, 40))
        
        if clicked != pygame.mouse.get_pressed(3)[0]:
            prev.copy(canvmouse)
            clicked = not clicked
        if clicked:
            #pygame.draw.circle(canvas, color, canvmouse.tuple(), int(size/2))
            line(canvas, color, prev, canvmouse, size)
        prev.copy(canvmouse)
        
        screen.blit(canvas, (40, 40))
        pygame.draw.circle(screen, "black", mouse.tuple(), size//2 + 2, 5)
    debug.frames(screen, clock, "white")
    pygame.display.flip()