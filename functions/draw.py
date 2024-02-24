import pygame
from pygame import Surface
from const import (
    WINDOW,
    COLOR_WHITE,
    SPACE,
    COLOR_BLUE,
    BORDER,
    HEALTH_FONT,
    WINDOW_WIDTH,
    RED_SHIP,
    YELLOW_SHIP,
    COLOR_RED,
    COLOR_YELLOW,
)


def draw_window(
    red_player: Surface,
    yellow_player: Surface,
    red_bullets: Surface,
    yellow_bullets: Surface,
    red_health: int,
    yellow_health: int,
) -> None:
    """Drawing several surfaces onto the screen.

    Args:
        red_player (Surface): The red player's surface.
        yellow_player (Surface): The yellow player's surface.
        red_bullets (Surface): The red player bullet's surface.
        yellow_bullets (Surface): The yellow player bullet's surface.
        red_health (int): The red's player health.
        yellow_health (int): The yellow's player health.
    """
    WINDOW.fill(COLOR_WHITE)
    WINDOW.blit(SPACE, (0, 0))  # Background.

    pygame.draw.rect(WINDOW, COLOR_BLUE, BORDER)
    yellow_health_text = HEALTH_FONT.render(
        f"Health: {str(yellow_health)}", 1, COLOR_WHITE
    )
    red_health_text = HEALTH_FONT.render(f"Health: {str(red_health)}", 1, COLOR_WHITE)

    WINDOW.blit(
        red_health_text, ((WINDOW_WIDTH - red_health_text.get_width() - 10), 10)
    )
    WINDOW.blit(yellow_health_text, (10, 10))

    WINDOW.blit(RED_SHIP, (red_player.x, red_player.y))  # Player 1
    WINDOW.blit(YELLOW_SHIP, (yellow_player.x, yellow_player.y))  # Player 2

    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, COLOR_RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, COLOR_YELLOW, bullet)

    # Updating the display for every iteration.
    pygame.display.update()
