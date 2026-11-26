
import pygame
import random

pygame.init()

# Window settings
WIDTH, HEIGHT = 600, 400
CELL = 20
TOP = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake - Practice 11")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22)
food_font = pygame.font.SysFont("Arial", 15, bold=True)

# Colors
WHITE = (255, 255, 255)
GREEN = (40, 170, 60)
RED = (220, 40, 40)
BLACK = (0, 0, 0)
BLUE = (30, 120, 255)
GOLD = (255, 190, 0)

# Food colors and weights
food_colors = {
    1: RED,
    2: BLUE,
    3: GOLD
}

# Initial snake position
snake = [(200, 200), (180, 200), (160, 200)]
direction = (CELL, 0)

score = 0
level = 1
speed = 8

# Food lifetime: 5 seconds
FOOD_TIME = 5000


# Generate food with random position and weight
def generate_food():

    positions = [
        (x, y)
        for x in range(0, WIDTH, CELL)
        for y in range(TOP, HEIGHT, CELL)
        if (x, y) not in snake
    ]

    position = random.choice(positions) if positions else None

    weight = random.choice([1, 2, 3])

    # Save food creation time
    created = pygame.time.get_ticks()

    return position, weight, created


food, food_weight, food_created = generate_food()

running = True
game_over = False
won = False

time_left = 5

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

        # Check food lifetime
        current_time = pygame.time.get_ticks()

        elapsed = current_time - food_created

        # Replace food after 5 seconds
        if elapsed >= FOOD_TIME:

            food, food_weight, food_created = generate_food()

        # Calculate remaining time
        time_left = max(
            0,
            (FOOD_TIME - (pygame.time.get_ticks() - food_created)) / 1000
        )

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

                # Add points according to food weight
                score += food_weight

                # Increase level and speed
                level = score // 4 + 1
                speed = 8 + (level - 1) * 2

                # Generate new food and reset timer
                food, food_weight, food_created = generate_food()

                time_left = 5

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

    # Draw food according to its weight
    if food is not None:

        food_rect = pygame.Rect(
            food[0], food[1], CELL, CELL
        )

        pygame.draw.rect(
            screen,
            food_colors[food_weight],
            food_rect
        )

        # Display food weight
        food_text = food_font.render(
            str(food_weight), True, WHITE
        )

        screen.blit(
            food_text,
            food_text.get_rect(center=food_rect.center)
        )

    # Draw score panel
    pygame.draw.rect(
        screen, BLACK, (0, 0, WIDTH, TOP)
    )

    score_text = font.render(
        f"Score: {score}", True, WHITE
    )

    level_text = font.render(
        f"Level: {level}", True, WHITE
    )

    timer_text = font.render(
        f"Time: {time_left:.1f}", True, WHITE
    )

    screen.blit(score_text, (10, 7))
    screen.blit(timer_text, (245, 7))
    screen.blit(level_text, (WIDTH - 110, 7))

    # Game over message
    if game_over:

        message = "YOU WIN!" if won else "GAME OVER"

        text = font.render(message, True, RED)

        screen.blit(
            text,
            text.get_rect(center=(300, 220))
        )

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
