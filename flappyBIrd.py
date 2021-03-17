import pygame
import os
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

IMAGE_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
IMAGE_FLOOR = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
IMAGE_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
IMAGES_BIRD = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))
]

pygame.font.init()
SCORE = pygame.font.SysFont("arial", 50) 


class Bird:
    IMGS = IMAGES_BIRD
    # rotation animation
    ROTATION_MAX = 25
    ROTATION_SPEED = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.height = self.y
        self.time = 0
        self.image_count = 0
        self.image = self.IMGS[0]

    def pular(self):
        self.speed = -10.5
        self.time = 0
        self.height = self.y

    def move(self):
    # calculate the displacement
        self.time += 1
        displacement = 1.5 * (self.time**2) + self.speed * self.time

    # restrict the displacement
        if displacement > 16:
            displacement = 16
        elif displacement < 0:
            displacement -= 2

        self.y += displacement

    # bird's angle
        if displacement < 0 or self.y < (self.height + 50):
            if self.angle < self.ROTATION_MAX:
                self.angle = self.ROTATION_MAX
        else:
            if self.angle > -90:
                self.angle -= self.ROTATION_SPEED
    
    def draw(self, screen):
    # define image that will use
        self.image_count += 1

        if self.image_count < self.ANIMATION_TIME:
            self.image = self.IMGS[0]
        elif self.image_count < self.ANIMATION_TIME*2:
            self.image = self.IMGS[1]
        elif self.image_count < self.ANIMATION_TIME*3:
            self.image = self.IMGS[2]
        elif self.image_count < self.ANIMATION_TIME*4:
            self.image = self.IMGS[1]
        elif self.image_count >= self.ANIMATION_TIME*4 + 1:
            self.image = self.IMGS[0]
            self.image_count = 0 

    # if bird is falling, it won't flap its wings 
        if self.angle <= -80:
            self.image = self.IMGS[1]
            self.image_count = self.ANIMATION_TIME*2

    # draw the image
        image_rotation = pygame.transform.rotate(self.image, self.angle)
        image_position_center = self.image.get_rect(topleft=(self.x, self.y )).center
        rectangle = image_rotation.get_rect(center=image_position_center)
        screen.blit(image_rotation, rectangle.topleft)

    def get_mask(self):
        pygame.mask.from_surface(self.image)


class Pipe:
    DISTANCE = 200
    SPEED = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.position_top = 0
        self.position_bottom = 0
        self.PIPE_TOP = pygame.transform.flip(IMAGE_PIPE, False, True)
        self.PIPE_BOTTOM = IMAGE_PIPE
        self.pass = False
        self.set_height()

    def set_height(self):
        self.altura = random.randrange(50, 450)
        self.position_top = self.height - self.PIPE_TOP.get_height()
        self.position_bottom = self.height + self.DISTANCE

    def move(self):
        pass # checkpoint

        

class Floor:
    pass