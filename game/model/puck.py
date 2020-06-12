import pygame
import random
from math import sin, cos, pi, atan
from game.config.constants import *
from game.model.utils import dist, signal


class Puck:
    def __init__(self, x = WIDTH/2, y = HEIGHT/2, crazy_mode = False) -> None:
        self.x = x
        self.y = y
        self.radius = PUCK_SIZE
        self.speed = 0
        self.time_delta = TIME_DELTA
        self.field_height = HEIGHT
        self.field_width = WIDTH
        self.angle = 0
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

        if dist(self.get_pos(), paddle.get_pos()) <= (self.radius + paddle.radius):
            self.paddle_collision(paddle)
            self.correct_position(paddle)

    def correct_position(self, paddle) -> None:

        position = [0, 0]
        position[0] = paddle.get_pos()[0] + (self.get_pos()[0]-paddle.get_pos()[0])*(self.radius + paddle.radius + EPSILON)/dist(self.get_pos(), paddle.get_pos())
        position[1] = paddle.get_pos()[1] + (self.get_pos()[1]-paddle.get_pos()[1])*(self.radius + paddle.radius + EPSILON)/dist(self.get_pos(), paddle.get_pos())
        self.set_position(position)

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
        if(self.speed == 0):
            betha = atan((self.y - py)/(self.x - px))
            if betha == 0:
                if self.x < px:
                    self.angle = pi
                else:
                    self.angle = 0
            elif betha > 0:
                self.angle = -pi + betha
            else:
                self.angle = pi + betha
        else:
            if self.x == px:
                self.angle = -self.angle
            elif self.x > px:
                betha = atan((self.y - py)/(self.x - px))
                if betha == 0:
                    self.angle = pi - self.angle
                elif betha > 0:
                    self.angle = -self.angle + 2*betha - pi
                else:
                    self.angle = -self.angle + 2*betha + pi
            else:
                betha = -atan((self.y - py)/(self.x - px))
                if betha == 0:
                    self.angle = pi - self.angle
                elif betha > 0:
                    self.angle = -self.angle - 2*betha + pi
                else:
                    self.angle = -self.angle - 2*betha - pi
        self.speed = PUCK_SPEED*(self.radius + paddle.radius)/(dist(self.get_pos(), paddle.get_pos()))

    def update(self, left_paddle, rigth_paddle) -> None:

        self.check_vertical_bounds()
        self.check_left_boundary()
        self.check_right_boundary()
        self.check_paddle(left_paddle)
        self.check_paddle(rigth_paddle)
        self.move()

    def reset(self, player,option):
        self.speed = 0
        self.angle = 0
        #game reset
        if option==1:
            self.x = WIDTH / 2
            self.y = HEIGHT/ 2

        #round reset
        if option==2:
            if player == 1:
                self.x = 3*WIDTH/4
            elif player == 2:
                self.x = WIDTH/4
            self.y = HEIGHT/2
                    