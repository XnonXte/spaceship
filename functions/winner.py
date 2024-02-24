import pygame
from const import WINNER_FONT, COLOR_WHITE, WINDOW, WINDOW_WIDTH


def draw_winner(text: str) -> None:
    """Displaying winner text on the middle of the screen.

    Args:
        text (str): The winner text.
    """
    draw_text = WINNER_FONT.render(text, 1, COLOR_WHITE)
    WINDOW.blit(
        draw_text,
        (
            WINDOW_WIDTH / 2 - draw_text.get_width() / 2,
            WINDOW_WIDTH / 2 - draw_text.get_width() / 2,
        ),
    )
    pygame.display.update()
    pygame.time.delay(5000)
