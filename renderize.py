import sys
import pygame
import const_values


def function render_field (background, screen, game, currentPlayerId)
    """
    this function renders some aspects of the field
    """
    # simplify variable names
    width, height = const_values.WIDTH, const_values.HEIGHT

    # fill the context with the background color
    screen.fill (background.color)

    # print the look of the opponent's disc
    const player = game.state.player2
    screen.fill (background.player2)

    # draw the center of circle
    pygame.draw.circle(screen, const_values.WHITE, (int(width / 2), int(height / 2)), 70, 5)

    # draw the rectangle of field
    pygame.draw.rect(screen, const_values.WHITE, (0, 0, width, height), 5)

    # draw the defense areas
    pygame.draw.rect(screen, const_values.WHITE, (0, int(height / 2) - 150, 150, 300), 5)
    pygame.draw.rect(screen, const_values.WHITE, (width - 150, int(height / 2)- 150, 150, 300), 5)

    # draw the goals
    pygame.draw.rect(screen, const_values.BLACK, (0, const.GOAL_Y1, 5, const_values.GOAL_WIDTH))
    pygame.draw.rect(screen, const_values.BLACK, (width - 5, const.GOAL_Y1, 5, const_values.GOAL_WIDTH))

    # draw the field divider
    pygame.draw.rect(screen, const_values.WHITE, (width / 2, 0, 3, height))

    # print the look of the current player disc
    const current_player = game.state.player1
    screen.fill (background.player1)
