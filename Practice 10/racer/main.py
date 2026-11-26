
import pygame
import random

pygame.init()

# Window settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

# Colors
WHITE = (255, 255, 255)
GRAY = (65, 65, 65)
GREEN = (40, 130, 60)
BLUE = (30, 120, 255)
RED = (220, 40, 40)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)

# Player and enemy
player = pygame.Rect(180, 500, 40, 70)
enemy = pygame.Rect(random.randint(65, 295), -70, 40, 70)

# Random coin
coin = pygame.Rect(random.randint(65, 310), -30, 24, 24)

coins = 0
speed = 5
road_offset = 0
running = True
game_over = False


# Draw a car
def draw_car(car, color):
    pygame.draw.rect(screen, color, car, border_radius=8)

    # Car windows
    pygame.draw.rect(
        screen, WHITE,
        (car.x + 7, car.y + 12, 26, 15)
    )

    pygame.draw.rect(
        screen, BLACK,
        (car.x + 7, car.y + 45, 26, 12)
    )

    # Wheels
    for y in [car.y + 10, car.y + 48]:
        pygame.draw.rect(screen, BLACK, (car.x - 4, y, 6, 15))
        pygame.draw.rect(screen, BLACK, (car.right - 2, y, 6, 15))


# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:

        # Player movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x = max(60, player.x - 5)

        if keys[pygame.K_RIGHT]:
            player.x = min(300, player.x + 5)

        # Moving road markings
        road_offset = (road_offset + speed) % 100

        # Enemy movement
        enemy.y += speed

        if enemy.top > HEIGHT:
            enemy.y = -70
            enemy.x = random.randint(65, 295)

        # Coin movement
        coin.y += speed

        if coin.top > HEIGHT:
            coin.y = -random.randint(30, 200)
            coin.x = random.randint(65, 310)

        # Collect coins
        if player.colliderect(coin):
            coins += 1
            coin.y = -random.randint(30, 200)
            coin.x = random.randint(65, 310)

        # Collision with enemy
        if player.colliderect(enemy):
            game_over = True

    # Draw background and road
    screen.fill(GREEN)
    pygame.draw.rect(screen, GRAY, (50, 0, 300, HEIGHT))

    # Road borders
    pygame.draw.line(screen, WHITE, (55, 0), (55, HEIGHT), 4)
    pygame.draw.line(screen, WHITE, (345, 0), (345, HEIGHT), 4)

    # Road markings
    for y in range(-100, HEIGHT, 100):
        pygame.draw.rect(
            screen, WHITE,
            (197, y + road_offset, 6, 50)
        )

    # Draw cars
    draw_car(player, BLUE)
    draw_car(enemy, RED)

    # Draw coin
    pygame.draw.circle(screen, GOLD, coin.center, 12)
    pygame.draw.circle(screen, (200, 150, 0), coin.center, 12, 2)

    # Coin counter in the top right corner
    score_text = font.render(f"Coins: {coins}", True, WHITE)

    screen.blit(
        score_text,
        (WIDTH - score_text.get_width() - 10, 10)
    )

    # Game over message
    if game_over:
        text = font.render("GAME OVER", True, RED)
        screen.blit(text, text.get_rect(center=(200, 300)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
