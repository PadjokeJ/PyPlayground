from physics import v2
import pygame
from copy import deepcopy
import fps as debug

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
game = True


class bone:
    locked = False
    def __init__(self, pos, length):
        self.pos = pos
        self.length = length
    def set_target(self, v2):
        self.target = v2
    def lock(self):
        self.locked = True
    def update(self):
        self.pos2 = self.target
        if not self.locked:
            self.pos.remove(self.pos2).normalize().scale(self.length).add(self.pos2)
    def render(self, surface, color):
        pygame.draw.line(surface, color, self.pos.tuple(), self.pos2.tuple(), 5)

mouse = v2(0, 0)

half = v2(width/2, height/2)
def create_arm(dummypos, target, length, ammount):
    arms = []
    arms.append(bone(deepcopy(dummypos), length))
    arms[0].set_target(mouse)
    arms[0].update()
    for i in range(1, ammount):
        arms.append(bone(deepcopy(dummypos), length))
        arms[i].set_target(arms[i - 1].pos)
        arms[i].update()
    return arms

ammount = 2000
length = 1
arms = create_arm(half, mouse, length, ammount)

list = []
list.append(str(ammount) + " arms")
list.append(str(length) + "length")

while game:
    delta = clock.tick() / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            break
    
    mouse.lerp(v2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 0.9)
    for i in arms:
        #i.pos.add(v2(0, 10))
        i.update()
    screen.fill("white")
    pygame.draw.circle(screen, "blue", arms[-1].pos.tuple(), 10)
    pygame.draw.circle(screen, "red", pygame.mouse.get_pos(), 10)
    
    for i in range(len(arms)):
        col = 255*i//len(arms)
        arms[i].render(screen, (col, 255 - col, col)) #(col, 255 - col, col)
    
    debug.render_mult(screen, list)
    
    debug.frames(screen, clock, "black")
    pygame.display.flip()
pygame.quit()
exit()
