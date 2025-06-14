import pygame
import sys

pygame.init()

font = pygame.font.Font(None, 35)
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

def draw_game(paddle1, paddle2, ball):
    WIN.fill((0, 0, 0))
    pygame.draw.rect(WIN, (0, 0, 255), paddle1)
    pygame.draw.rect(WIN, (255, 0, 0), paddle2)
    pygame.draw.ellipse(WIN, (51, 255, 0), ball)

def show_loss_message(player):
    message = font.render(f"Player {player} Loses - Press R to Restart", True, (180, 0, 0))
    WIN.blit(message, (WIDTH // 2 - 200, HEIGHT // 2))

def main():
    paddle_width, paddle_height = 10, 100
    paddle_speed = 5
    ball_speed_x, ball_speed_y = 4, 4

    paddle1 = pygame.Rect(20, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
    paddle2 = pygame.Rect(WIDTH - 30, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
    ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20)

    clock = pygame.time.Clock()
    finish = False
    loser = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if not finish:
            if keys[pygame.K_w] and paddle1.top > 0:
                paddle1.y -= paddle_speed
            if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
                paddle1.y += paddle_speed
            if keys[pygame.K_i] and paddle2.top > 0:
                paddle2.y -= paddle_speed
            if keys[pygame.K_k] and paddle2.bottom < HEIGHT:
                paddle2.y += paddle_speed

            ball.x += ball_speed_x
            ball.y += ball_speed_y

            if ball.top <= 0 or ball.bottom >= HEIGHT:
                ball_speed_y *= -1

            if ball.colliderect(paddle1) or ball.colliderect(paddle2):
                ball_speed_x *= -1

            if ball.left <= 0:
                finish = True
                lose = 1
            elif ball.right >= WIDTH:
                finish = True
                lose = 2

            draw_game(paddle1, paddle2, ball)

        else:
            draw_game(paddle1, paddle2, ball)
            if keys[pygame.K_r]:
                main()  

        pygame.display.flip()
        clock.tick(60)

main()

