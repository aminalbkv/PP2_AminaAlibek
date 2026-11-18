
import pygame
from player import (
    play_music, stop_music, next_track,
    previous_track, get_track_name,
    get_progress, get_duration_seconds
)

pygame.init()

WIDTH, HEIGHT = 650, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Music Player")

BACKGROUND = (255, 235, 245)
PINK = (220, 65, 130)
LIGHT_PINK = (245, 185, 210)
BLACK = (55, 45, 55)

title_font = pygame.font.SysFont("Arial", 38, bold=True)
text_font = pygame.font.SysFont("Arial", 25)
small_font = pygame.font.SysFont("Arial", 19)

clock = pygame.time.Clock()
running = True


def format_time(seconds):
    seconds = int(seconds)
    return f"{seconds // 60}:{seconds % 60:02d}"


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                previous_track()
            elif event.key == pygame.K_q:
                running = False

    screen.fill(BACKGROUND)

    title = title_font.render("My Music Player", True, PINK)
    screen.blit(title, title.get_rect(center=(325, 65)))

    # Decorative music icon
    pygame.draw.circle(screen, LIGHT_PINK, (325, 170), 65)
    note = title_font.render("♫", True, PINK)
    screen.blit(note, note.get_rect(center=(325, 170)))

    track = text_font.render(get_track_name(), True, BLACK)
    screen.blit(track, track.get_rect(center=(325, 270)))

    # Playback progress
    progress = get_progress()
    duration = get_duration_seconds()
    ratio = min(progress / duration, 1) if duration > 0 else 0

    pygame.draw.rect(
        screen, LIGHT_PINK, (100, 320, 450, 12),
        border_radius=6
    )
    pygame.draw.rect(
        screen, PINK, (100, 320, int(450 * ratio), 12),
        border_radius=6
    )

    current_text = small_font.render(format_time(progress), True, BLACK)
    total_text = small_font.render(format_time(duration), True, BLACK)

    screen.blit(current_text, (100, 345))
    screen.blit(total_text, (500, 345))

    controls = [
        "P - Play    S - Stop",
        "N - Next    B - Previous",
        "Q - Quit"
    ]

    for i, control in enumerate(controls):
        text = small_font.render(control, True, BLACK)
        screen.blit(text, text.get_rect(center=(325, 405 + i * 25)))

    pygame.display.flip()
    clock.tick(60)

pygame.mixer.music.stop()
pygame.quit()
