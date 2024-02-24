import pygame
from functions import bullets, draw, movement, winner
from const import (
    FPS,
    SPACESHIP_WIDTH,
    SPACESHIP_HEIGHT,
    RED_X,
    RED_Y,
    YELLOW_X,
    YELLOW_Y,
    BULLET_WIDTH,
    BULLET_HEIGHT,
    MAX_BULLETS,
    YELLOW_HIT,
    RED_HIT,
    BULLET_FIRE_SOUND,
    BULLET_HIT_SOUND,
    MUSIC,
)


pygame.init()
pygame.display.set_caption("Spaceship 2v2!")


def main() -> None:
    MUSIC.play(loops=-1)

    yellow_player = pygame.Rect(YELLOW_X, YELLOW_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red_player = pygame.Rect(RED_X, RED_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True

    yellow_bullets = []
    red_bullets = []

    red_health = 10
    yellow_health = 10

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            # Quit event handler.
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow_player.x + yellow_player.width,
                        yellow_player.y + yellow_player.height / 2 - BULLET_HEIGHT // 2,
                        BULLET_WIDTH,
                        BULLET_HEIGHT,
                    )
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_SEMICOLON and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red_player.x,
                        red_player.y + red_player.height / 2 - BULLET_HEIGHT // 2,
                        BULLET_WIDTH,
                        BULLET_HEIGHT,
                    )
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins! "

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            winner.draw_winner(winner_text)
            break

        # Handling bullets.
        bullets.handle_bullets(yellow_bullets, red_bullets, yellow_player, red_player)

        # Handling movement.
        keys_pressed = pygame.key.get_pressed()
        movement.handle_player_movement(keys_pressed, yellow_player, True)
        movement.handle_player_movement(keys_pressed, red_player, False)

        # Drawing objects onto the screen.
        draw.draw_window(
            red_player,
            yellow_player,
            red_bullets,
            yellow_bullets,
            red_health,
            yellow_health,
        )

    main()


if __name__ == "__main__":
    main()
