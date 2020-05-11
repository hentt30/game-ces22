import pygame
import random
from math import sin, cos, pi, atan
from game.config.constants import *
from utils import dist, signal


class Puck:
    def __init__(self, x = WIDTH/2, y = HEIGHT/2, crazy_mode = False) -> None:
        self.x = x
        self.y = y
        self.radius = PUCK_SIZE
        self.speed = PUCK_SPEED
        self.time_delta = TIME_DELTA
        self.field_height = HEIGHT
        self.field_width = WIDTH
        self.angle = pi/2
        self.crazy_mode = crazy_mode

    def set_position(self, position) -> None:
        self.x = position[0]
        self.y = position[1]

    def check_vertical_bounds(self) -> None:
        
        if (self.y - self.radius <= 0):
            self.y = self.radius
            self.wall_collision('BOTTOM')
        elif (self.y + self.radius > self.field_height):
            self.y = self.field_height - self.radius
            self.wall_collision('TOP')

    def check_left_boundary(self) -> None:

        if (self.x - self.radius <= 0):
            self.x = self.radius
            self.wall_collision('LEFT')

    def check_right_boundary(self) -> None:

        if (self.x + self.radius > self.field_width):
            self.x = self.field_width - self.radius
            self.wall_collision('RIGHT')

    def check_paddle(self, paddle) -> None:

        if dist(self.get_pos(), paddle.get_pos()) <= self.radius + paddle.radius:
            self.paddle_collision(paddle)

    def move(self) -> None:

        self.x += cos(self.angle) * self.speed * self.time_delta
        self.y += sin(self.angle) * self.speed * self.time_delta

    def get_pos(self) -> tuple:

        return self.x, self.y

    def wall_collision(self, obj) -> None:

        if self.crazy_mode:
            if obj == 'RIGHT':
                self.angle = random.uniform(pi/2, 3*pi/2)
            elif obj == 'LEFT':
                self.angle = random.uniform(-pi/2, pi/2)
            elif obj == 'TOP':
                self.angle = random.uniform(-pi, 0)
            else:
                self.angle = random.uniform(0, pi)

        else:    
            if obj == 'RIGHT' or obj == 'LEFT':
                self.angle = pi - self.angle
            elif obj == 'TOP' or obj == 'BOTTOM':
                self.angle = -self.angle

    def paddle_collision(self, paddle) -> None:

        px = paddle.get_pos()[0]
        py = paddle.get_pos()[1]
        if self.x == px:
            self.angle = -self.angle
        elif self.x > px:
            betha = atan((self.y - py)/(self.x - px))
            if betha == 0:
                self.angle = pi - self.angle
            elif betha > 0:
                self.angle = -self.angle - 2*betha + pi
            else:
                self.angle = -self.angle + 2*betha + pi
        else:
            betha = -atan((self.y - py)/(self.x - px))
            if betha == 0:
                self.angle = pi - self.angle
            elif betha > 0:
                self.angle = -self.angle - 2*betha + pi
            else:
                self.angle = -self.angle + 2*betha + pi

    def update(self, left_paddle, rigth_paddle) -> None:

        self.check_vertical_bounds()
        self.check_left_boundary()
        self.check_right_boundary()
        self.check_paddle(left_paddle)
        self.check_paddle(rigth_paddle)
        self.move()