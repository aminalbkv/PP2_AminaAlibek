
import pygame
from ball import draw_ball, move_ball

pygame.init()

WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")

clock = pygame.time.Clock()

x = WIDTH // 2
y = HEIGHT // 2

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            x, y = move_ball(
                x, y, event.key, WIDTH, HEIGHT
            )

    screen.fill(WHITE)
    draw_ball(screen, x, y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
