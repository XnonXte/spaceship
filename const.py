import pygame
import os

pygame.font.init()
pygame.mixer.init()

# Sounds.
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("assets", "Grenade+1.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("assets", "Gun+Silencer.mp3"))
MUSIC = pygame.mixer.Sound(os.path.join("assets", "music.mp3"))

# Fonts.
HEALTH_FONT = pygame.font.SysFont("arial", 20)
WINNER_FONT = pygame.font.SysFont("arial", 40)

# Essentials.
FPS = 75

# Width and height.
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
RED_X, RED_Y = 700, 300
YELLOW_X, YELLOW_Y = 100, 300
BULLET_WIDTH, BULLET_HEIGHT = 12, 6

# Colors.
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (255, 255, 0)

# Surfaces.
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
YELLOW_SHIP_IMG = pygame.image.load(os.path.join("assets", "spaceship_yellow.png"))
RED_SHIP_IMG = pygame.image.load(os.path.join("assets", "spaceship_red.png"))
YELLOW_SHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    90,
)
RED_SHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    270,
)
SPACE = pygame.transform.scale(
    (
        pygame.image.load(
            os.path.join("assets", "space.png"),
        )
    ),
    (WINDOW_WIDTH, WINDOW_HEIGHT),
)

# Logic.
VEL = 6
MAX_BULLETS = 3
BULLET_VEL = 12

# User events.
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2  # Incremented for each step up in custom event.

# Rectangles.
BORDER = pygame.Rect(WINDOW_WIDTH // 2 - 4, 0, 8, WINDOW_HEIGHT)
