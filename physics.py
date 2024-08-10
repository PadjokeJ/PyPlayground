import math
from pygame import Rect as Collider
import pygame.rect as rect

class v2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def tuple(self):
        return (self.x, self.y)
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def distance(self, vec):
        x = self.x - vec.x
        y = self.y - vec.y
        return v2(x, y).magnitude()
    def normalize(self):
        scale = self.magnitude()
        if scale == 0:
            scale = 0.1
        self.x = self.x / scale
        self.y = self.y / scale
        return self
    def scale(self, float):
        self.x *= float
        self.y *= float
        return self
    def add(self, v2):
        self.x += v2.x
        self.y += v2.y
        return self
    def remove(self, v2):
        self.x -= v2.x
        self.y -= v2.y
        return self
    def from_tuple(self, tuple):
        self.x = tuple[0]
        self.y = tuple[1]
        return self
    def lerp(self, vec, ammount):
        max = self.magnitude()
        self.remove(vec).scale(ammount).add(vec)
        return self
    def copy(self, v2):
        self.x = v2.x
        self.y = v2.y
        return self
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) +")"

class Rigidbody_2d:
    vel = v2(0, 0)
    forces = v2(0, 0)
    gravity = 9.81
    drag_coeff = 0.9 #scalar
    ground = []
    grounded = False
    terminal_vel = v2(20, 20)
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.rect = Collider(pos.tuple(), size.tuple())
    def tick(self):
        self.vel.add(self.forces)
        if self.vel.magnitude() > self.terminal_vel.magnitude():
            self.vel.normalize().scale(self.terminal_vel.magnitude())
        self.pos.add(self.vel)
        self.rect.update(self.pos.tuple(), self.size.tuple())
        self.forces.scale(0)
        return self
    def ground_check(self):
        self.grounded = self.rect.collidelist(self.ground) != -1
        print(self.grounded)
    def grav_update(self):
        self.ground_check()
        if not self.grounded:
            self.forces.add(v2(0, self.gravity))
        else:
            self.vel.scale(0)
            self.pos = v2(self.pos.x, self.ground[self.rect.collidelist(self.ground)].y - self.size.y)
        self.tick()
    def __str__(self):
        return f"physics object\nposition: {self.pos}\nvelocity: {self.vel}"

def v2Lerp(v2_1, v2_2, ammount):
    return v2(0, 0).copy(v2_1).lerp(v2_2, 1-ammount)