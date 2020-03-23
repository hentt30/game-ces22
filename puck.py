import pygame
import game
import math
import constants

Class Puck :

    #Incializar 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = constants.PUCK_SIZE
        self.speed = constants.PUCK_SPEED
        self.mass = constants.PUCK_MASS
        self.angle = 0

    #Definir condições de movimento
    def move(self, time_delta):
        self.x = self.x + math.sin(self.angle) * self.speed * time_delta
        self.y = self.y - math.cos(self.angle) * self.speed * time_delta

        self.speed = self.speed * constants.FRICTION


    def function update( vx, vy)
    """
        It receives the velocity values and update the puck
    """

        # Determinar o angulo e a velocidade do puck apos a colisão
        self.speed=  math.hypot(vx, vy)
        self.angle = math.pi / 2 - math.atan2(vy, vx)

        # Limitar a velocidade
        if self.speed > constants.MAX_SPEED:
            self.speed = constants.MAX_SPEED
