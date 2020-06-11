import sys
""" All sizes in pixels and speeds in pixels per second """
FPS = 60
TIME_DELTA = 0.016

# Screen size
HEIGHT = 600
WIDTH = 1200

# Paddle
PADDLE_SIZE = 40
PADDLE_SPEED = 400

# Paddle 1 start position.
PADDLE_LEFT_X = 60
PADDLE_LEFT_Y = HEIGHT / 2
PADDLE_LEFT_COLOR = (0, 0, 150)

# Paddle 2 start position.
PADDLE_RIGHT_X = WIDTH - 60
PADDLE_RIGHT_Y = HEIGHT / 2
PADDLE_RIGHT_COLOR = (220, 220, 0)

# Puck
PUCK_SIZE = 30
PUCK_SPEED = 650
PUCK_COLOR = (150, 0, 0)

# Tolerance for collision

EPSILON = PADDLE_SIZE/4

# Goal Position
GOAL_WIDTH = 180
GOAL_Y_LEFT = HEIGHT / 2 - GOAL_WIDTH / 2
GOAL_Y_RIGHT = HEIGHT / 2 + GOAL_WIDTH / 2

# Speed levels
EASY = 450
MEDIUM = 650
HARD = 850

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 120, 0)
# Scoring
#SCORE_LIMIT = 5
SCORE_LIMIT = 5
ROUND_LIMIT = 2

# Environment
FRICTION = 0.998
MAX_SPEED = 1500

# mute button
MUTE_BUTTON_RADIUS = 32

# pause button
PAUSE_BUTTON_RADIUS = 32

# info button
INFO_BUTTON_RADIUS = 32

# Raio do botão de quit
buttonRadius = 60

# sides
LEFT = 0
RIGHT = 1

# strings
PADDLE_RIGHT = "paddle_right"
PADDLE_LEFT = "paddle_left"
PUCK = "puck"
PLACAR = "placar"
ROUND= "round"

# vetor de cores
COLORS = [[(46, 120, 50), (66, 152, 60)], [(200, 72, 72), (255, 92, 92)],
          [(0, 158, 239), (100, 189, 219)], [(221, 229, 2), (252, 255, 59)],
          [(232, 114, 46), (244, 133, 51)]]