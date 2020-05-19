import pygame
import math
from game.config.constants import *


class Paddle:
    def __init__(self, x, y, side) -> None:
        self.x = x
        self.y = y
        self.radius = PADDLE_SIZE
        self.speed = PADDLE_SPEED
        self.side = side  # 0 left and 1 right
        self.time_delta = TIME_DELTA
        self.field_height = HEIGHT
        self.field_width = WIDTH
        self.angle = 0

    def check_vertical_bounds(self) -> None:
        # top
        if (self.y - self.radius <= 0):
            self.y = self.radius
        elif (self.y + self.radius > self.field_height):
            self.y = self.field_height - self.radius

    def check_left_boundary(self) -> None:
        if (self.x - self.radius <= 0):
            self.x = self.radius
        elif (self.x + self.radius > int(self.field_width / 2)
              and self.side == LEFT):
            self.x = int(self.field_width / 2) - self.radius

    def check_right_boundary(self) -> None:

        if (self.x + self.radius > self.field_width):
            self.x = self.field_width - self.radius

        elif (self.x - self.radius < int(self.field_width / 2)
              and self.side == RIGHT):
            self.x = int(self.field_width / 2) + self.radius

    def move(self, up, down, left, right) -> None:
        dx, dy = self.x, self.y
        self.x += (right - left) * self.speed * self.time_delta
        self.y += (down - up) * self.speed * self.time_delta

        dx = self.x - dx
        dy = self.y - dy

        self.angle = math.atan2(dy, dx)

    def get_pos(self) -> tuple:
        return self.x, self.y

    def update(self) -> None:
        key_presses = key_presses = pygame.key.get_pressed()
        if (self.side == LEFT):
            up = key_presses[pygame.K_w]
            down = key_presses[pygame.K_s]
            right = key_presses[pygame.K_d]
            left = key_presses[pygame.K_a]
        else:
            up = key_presses[pygame.K_UP]
            down = key_presses[pygame.K_DOWN]
            right = key_presses[pygame.K_RIGHT]
            left = key_presses[pygame.K_LEFT]

        self.move(up, down, left, right)
        self.check_vertical_bounds()
        self.check_left_boundary()
        self.check_right_boundary()

    ###
    def reset(self, first_x, first_y):
        self.x = first_x
        self.y = first_y
    ###

