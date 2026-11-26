
import pygame
import random

pygame.init()

# Window settings
WIDTH, HEIGHT = 600, 400
CELL = 20
TOP = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

# Colors
WHITE = (255, 255, 255)
GREEN = (40, 170, 60)
RED = (220, 40, 40)
BLACK = (0, 0, 0)

# Initial snake position
snake = [(200, 200), (180, 200), (160, 200)]
direction = (CELL, 0)

score = 0
level = 1
speed = 8


# Generate food outside the snake
def generate_food():
    positions = [
        (x, y)
        for x in range(0, WIDTH, CELL)
        for y in range(TOP, HEIGHT, CELL)
        if (x, y) not in snake
    ]

    return random.choice(positions) if positions else None


food = generate_food()

running = True
game_over = False
won = False

# Main game loop
while running:
    next_direction = direction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change snake direction
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != (0, CELL):
                next_direction = (0, -CELL)

            elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                next_direction = (0, CELL)

            elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                next_direction = (-CELL, 0)

            elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                next_direction = (CELL, 0)

    direction = next_direction

    if not game_over:

        # Calculate new head position
        x = snake[0][0] + direction[0]
        y = snake[0][1] + direction[1]
        head = (x, y)

        eating = head == food
        body = snake if eating else snake[:-1]

        # Check wall collision
        if x < 0 or x >= WIDTH or y < TOP or y >= HEIGHT:
            game_over = True

        # Check body collision
        elif head in body:
            game_over = True

        else:
            snake.insert(0, head)

            # Collect food
            if eating:
                score += 1

                # New level every 4 foods
                level = score // 4 + 1

                # Increase speed
                speed = 8 + (level - 1) * 2

                food = generate_food()

                if food is None:
                    won = True
                    game_over = True

            else:
                snake.pop()

    # Draw background
    screen.fill(WHITE)

    # Draw snake
    for x, y in snake:
        pygame.draw.rect(
            screen, GREEN,
            (x, y, CELL - 1, CELL - 1)
        )

    # Draw food
    if food is not None:
        pygame.draw.rect(
            screen, RED,
            (food[0], food[1], CELL, CELL)
        )

    # Draw score panel
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, TOP))

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(score_text, (10, 5))
    screen.blit(level_text, (WIDTH - 110, 5))

    # Game over message
    if game_over:
        message = "YOU WIN!" if won else "GAME OVER"
        text = font.render(message, True, RED)
        screen.blit(text, text.get_rect(center=(300, 220)))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
