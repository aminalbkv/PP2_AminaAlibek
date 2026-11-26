
import pygame
import random

pygame.init()

# Window settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer - Practice 11")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22)
coin_font = pygame.font.SysFont("Arial", 16, bold=True)

# Colors
WHITE = (255, 255, 255)
GRAY = (65, 65, 65)
GREEN = (40, 130, 60)
BLUE = (30, 120, 255)
RED = (220, 40, 40)
BLACK = (0, 0, 0)

BRONZE = (184, 115, 51)
SILVER = (192, 192, 192)
GOLD = (255, 215, 0)

# Coin colors and weights
coin_colors = {
    1: BRONZE,
    2: SILVER,
    3: GOLD
}

# Player and enemy
player = pygame.Rect(180, 500, 40, 70)
enemy = pygame.Rect(
    random.randint(65, 295), -70, 40, 70
)

# Generate a random coin with a random weight
def generate_coin():
    rect = pygame.Rect(
        random.randint(65, 310),
        -random.randint(30, 200),
        24, 24
    )

    weight = random.choice([1, 2, 3])

    return rect, weight


coin, coin_weight = generate_coin()

coins = 0
score = 0
enemy_speed = 5
road_speed = 5
road_offset = 0

# Increase enemy speed every N collected coins
N = 5

running = True
game_over = False


# Draw a car
def draw_car(car, color):

    pygame.draw.rect(
        screen, color, car, border_radius=8
    )

    # Car windows
    pygame.draw.rect(
        screen, WHITE,
        (car.x + 7, car.y + 12, 26, 15)
    )

    pygame.draw.rect(
        screen, BLACK,
        (car.x + 7, car.y + 45, 26, 12)
    )

    # Car wheels
    for y in [car.y + 10, car.y + 48]:

        pygame.draw.rect(
            screen, BLACK,
            (car.x - 4, y, 6, 15)
        )

        pygame.draw.rect(
            screen, BLACK,
            (car.right - 2, y, 6, 15)
        )


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

        # Move road markings
        road_offset = (
            road_offset + road_speed
        ) % 100

        # Enemy movement
        enemy.y += enemy_speed

        if enemy.top > HEIGHT:
            enemy.y = -70
            enemy.x = random.randint(65, 295)

        # Coin movement
        coin.y += road_speed

        # Generate a new coin
        if coin.top > HEIGHT:
            coin, coin_weight = generate_coin()

        # Collect coin
        if player.colliderect(coin):

            coins += 1
            score += coin_weight

            # Increase enemy speed every 5 coins
            if coins % N == 0:
                enemy_speed += 1

            coin, coin_weight = generate_coin()

        # Check collision with enemy
        if player.colliderect(enemy):
            game_over = True

    # Draw background
    screen.fill(GREEN)

    pygame.draw.rect(
        screen, GRAY, (50, 0, 300, HEIGHT)
    )

    # Road borders
    pygame.draw.line(
        screen, WHITE, (55, 0), (55, HEIGHT), 4
    )

    pygame.draw.line(
        screen, WHITE, (345, 0), (345, HEIGHT), 4
    )

    # Road markings
    for y in range(-100, HEIGHT, 100):

        pygame.draw.rect(
            screen, WHITE,
            (197, y + road_offset, 6, 50)
        )

    # Draw cars
    draw_car(player, BLUE)
    draw_car(enemy, RED)

    # Draw coin according to its weight
    pygame.draw.circle(
        screen,
        coin_colors[coin_weight],
        coin.center,
        12
    )

    # Display coin weight
    coin_text = coin_font.render(
        str(coin_weight), True, BLACK
    )

    screen.blit(
        coin_text,
        coin_text.get_rect(center=coin.center)
    )

    # Display score, coins and enemy speed
    score_text = font.render(
        f"Score: {score}", True, WHITE
    )

    coins_text = font.render(
        f"Coins: {coins}", True, WHITE
    )

    speed_text = font.render(
        f"Speed: {enemy_speed}", True, WHITE
    )

    screen.blit(score_text, (10, 10))

    screen.blit(
        coins_text,
        (WIDTH - coins_text.get_width() - 10, 10)
    )

    screen.blit(speed_text, (10, 40))

    # Game over message
    if game_over:

        text = font.render(
            "GAME OVER", True, RED
        )

        screen.blit(
            text,
            text.get_rect(center=(200, 300))
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
