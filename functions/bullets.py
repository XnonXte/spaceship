import pygame
from pygame import Surface
from const import BULLET_VEL, RED_HIT, WINDOW_WIDTH, YELLOW_HIT


def handle_bullets(
    yellow_bullets: Surface,
    red_bullets: Surface,
    yellow_player: Surface,
    red_player: Surface,
) -> None:
    """Handling bullets collision, post an event when a collision is triggered, remove a bullet when it's off screen.

    Args:
        yellow_bullets (Surface): The yellow player bullet's surface.
        red_bullets (Surface): The red player bullet's surface.
        yellow_player (Surface): The yellow player's surface.
        red_player (Surface): The red player's surface.
    """
    # Handling bullet for yellow player.
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red_player.colliderect(bullet):
            event = pygame.event.Event(RED_HIT)
            pygame.event.post(event)
            yellow_bullets.remove(bullet)
        elif bullet.x > WINDOW_WIDTH:
            yellow_bullets.remove(bullet)

    # Handling bullet for red player.
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow_player.colliderect(bullet):
            event = pygame.event.Event(YELLOW_HIT)
            pygame.event.post(event)
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
