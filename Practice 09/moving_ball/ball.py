
import pygame

RED = (255, 0, 0)
RADIUS = 25
STEP = 20


def draw_ball(screen, x, y):
    pygame.draw.circle(screen, RED, (x, y), RADIUS)


def move_ball(x, y, key, width, height):
    new_x, new_y = x, y

    if key == pygame.K_LEFT:
        new_x -= STEP
    elif key == pygame.K_RIGHT:
        new_x += STEP
    elif key == pygame.K_UP:
        new_y -= STEP
    elif key == pygame.K_DOWN:
        new_y += STEP

    if RADIUS <= new_x <= width - RADIUS and RADIUS <= new_y <= height - RADIUS:
        return new_x, new_y

    return x, y
