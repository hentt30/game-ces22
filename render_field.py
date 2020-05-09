import sys
import pygame
import screen
import constants


def render_field (screen, game):
    """
    this function renders some aspects of the field
    """
    # simplify variable names
    width, height = constants.WIDTH, constants.HEIGHT

    # fill the context with the background color
    screen.fill (game.background_color)

    # draw the center of circle
    pygame.draw.circle(screen, constants.WHITE, (int(width / 2), int(height / 2)), 70, 5)

    # draw the rectangle of field
    pygame.draw.rect(screen, constants.WHITE, (0, 0, width, height), 5)

    # draw the defense areas
    pygame.draw.rect(screen, constants.WHITE, (0, int(height / 2) - 150, 150, 300), 5)
    pygame.draw.rect(screen, constants.WHITE, (width - 150, int(height / 2)- 150, 150, 300), 5)

    # draw the goals
    pygame.draw.rect(screen, constants.BLACK, (0, constants.GOAL_Y1, 5, constants.GOAL_WIDTH))
    pygame.draw.rect(screen, constants.BLACK, (width - 5, constants.GOAL_Y1, 5, constants.GOAL_WIDTH))

    # draw the field divider
    pygame.draw.rect(screen, constants.WHITE, (width / 2, 0, 3, height))

    # pause the game
    screen.blit(pause_image, (width / 2 - 32, height - 70))
