import pygame
import math
from pathlib import Path
from datetime import datetime
from clock import get_clock_angles

pygame.init()

WIDTH, HEIGHT = 700, 750
CENTER = (350, 400)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")

clock = pygame.time.Clock()

# Colors
BACKGROUND = (255, 240, 245)
BLACK = (15, 15, 15)
WHITE = (255, 255, 255)
RED = (230, 40, 65)

font = pygame.font.SysFont("Arial", 28, bold=True)
time_font = pygame.font.SysFont("Arial", 45, bold=True)

# Load Mickey hand image
hand_path = (
    Path(__file__).parent
    / "images"
    / "mickey_hand.png"
)

hand = pygame.image.load(
    str(hand_path)
).convert_alpha()

hand.set_colorkey((0, 0, 0))

hand = pygame.transform.smoothscale(
    hand, (100, 180)
)


# Draw Mickey Mouse silhouette
def draw_mickey_head():
    # Left ear
    pygame.draw.circle(
        screen, BLACK, (185, 175), 95
    )

    # Right ear
    pygame.draw.circle(
        screen, BLACK, (515, 175), 95
    )

    # Head
    pygame.draw.circle(
        screen, BLACK, CENTER, 240
    )


# Draw clock numbers
def draw_clock_numbers():
    radius = 205

    for number in range(1, 13):
        angle = math.radians(number * 30 - 90)

        x = CENTER[0] + radius * math.cos(angle)
        y = CENTER[1] + radius * math.sin(angle)

        text = font.render(
            str(number), True, WHITE
        )

        rect = text.get_rect(
            center=(int(x), int(y))
        )

        screen.blit(text, rect)


# Rotate Mickey's hands
def draw_hand(image, angle, flip=False):
    if flip:
        image = pygame.transform.flip(
            image, True, False
        )

    surface = pygame.Surface(
        (500, 500), pygame.SRCALPHA
    )

    rect = image.get_rect()
    rect.midbottom = (250, 250)
    surface.blit(image, rect)

    rotated = pygame.transform.rotate(
        surface, -angle
    )

    rotated_rect = rotated.get_rect(
        center=CENTER
    )

    screen.blit(rotated, rotated_rect)


# Main application loop
running = True
last_second = None

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current system time
    now = datetime.now()

    current_time = (
        now.hour,
        now.minute,
        now.second
    )

    # Update every second
    if current_time != last_second:
        last_second = current_time

        # Calculate rotation angles
        minute_angle, second_angle = get_clock_angles(now)

        # Background
        screen.fill(BACKGROUND)

        # Mickey Mouse silhouette
        draw_mickey_head()

        # Clock numbers
        draw_clock_numbers()

        # Right hand = minutes
        draw_hand(hand, minute_angle)

        # Left hand = seconds
        draw_hand(hand, second_angle, flip=True)

        # Center point
        pygame.draw.circle(
            screen, RED, CENTER, 12
        )

        # Digital time (MM:SS)
        time_text = now.strftime("%M:%S")

        text = time_font.render(
            time_text, True, BLACK
        )

        text_rect = text.get_rect(
            center=(350, 700)
        )

        screen.blit(text, text_rect)

        # Update display
        pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

pygame.quit()