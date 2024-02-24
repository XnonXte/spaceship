import pygame
from pygame import key, Surface
from const import VEL, BORDER, WINDOW_WIDTH, WINDOW_HEIGHT


def handle_player_movement(
    keys_pressed: key.ScancodeWrapper, player: Surface, is_yellow: bool
) -> None:
    """Handling player movement 8-directional.

    Args:
        keys_pressed (ScancodeWrapper): pygame's keys object.
        player (Surface): The player's surface.
        is_yellow (bool): Is it the yellow player?
    """
    # Movement keys based on player colors.
    left_key = pygame.K_s if is_yellow else pygame.K_j
    right_key = pygame.K_f if is_yellow else pygame.K_l
    up_key = pygame.K_e if is_yellow else pygame.K_i
    down_key = pygame.K_d if is_yellow else pygame.K_k

    # Max boundaries for left and right.
    left_max_bound = (
        player.x - VEL > 0 if is_yellow else player.x - VEL > BORDER.x + BORDER.width
    )
    right_max_bound = (
        player.x + VEL + player.width < BORDER.x
        if is_yellow
        else player.x + VEL + player.width < WINDOW_WIDTH
    )

    # Max boundaries for top and down.
    up_max_bound = player.y - VEL > 0
    down_max_bound = player.y + VEL + player.height < WINDOW_HEIGHT

    # Movement based on the player colors.
    if keys_pressed[left_key] and left_max_bound:
        # Move left.
        player.x -= VEL
    if keys_pressed[right_key] and right_max_bound:
        # Move right.
        player.x += VEL
    if keys_pressed[up_key] and up_max_bound:
        # Move up.
        player.y -= VEL
    if keys_pressed[down_key] and down_max_bound:
        # Move down.
        player.y += VEL
