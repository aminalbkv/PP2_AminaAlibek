
import pygame

pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
TOOLBAR = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)

colors = [
    BLACK,
    (255, 0, 0),
    (0, 180, 0),
    (0, 0, 255),
    (255, 220, 0),
    (150, 0, 200)
]

# Create drawing canvas
canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR))
canvas.fill(WHITE)

# Drawing tools
tools = ["Pencil", "Rectangle", "Circle", "Eraser"]

tool = "Pencil"
color = BLACK
drawing = False
start = None
last = None


# Draw rectangle or circle
def draw_shape(surface, start, end):

    if tool == "Rectangle":
        x = min(start[0], end[0])
        y = min(start[1], end[1])

        w = abs(end[0] - start[0])
        h = abs(end[1] - start[1])

        pygame.draw.rect(
            surface, color, (x, y, w, h), 3
        )

    elif tool == "Circle":
        radius = int(
            ((end[0] - start[0]) ** 2 +
             (end[1] - start[1]) ** 2) ** 0.5
        )

        pygame.draw.circle(
            surface, color, start, radius, 3
        )


# Main loop
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos

            # Select drawing tool
            if y < 45:
                for i, name in enumerate(tools):
                    button = pygame.Rect(
                        i * 140 + 10, 5, 130, 35
                    )

                    if button.collidepoint(x, y):
                        tool = name

            # Select color
            elif y < TOOLBAR:
                for i, c in enumerate(colors):
                    button = pygame.Rect(
                        i * 45 + 10, 55, 35, 35
                    )

                    if button.collidepoint(x, y):
                        color = c

            # Start drawing
            else:
                drawing = True
                start = (x, y - TOOLBAR)
                last = start

                if tool == "Pencil":
                    pygame.draw.circle(
                        canvas, color, start, 2
                    )

                elif tool == "Eraser":
                    pygame.draw.circle(
                        canvas, WHITE, start, 10
                    )

        # Mouse movement
        if event.type == pygame.MOUSEMOTION and drawing:
            x, y = event.pos
            current = (x, y - TOOLBAR)

            # Pencil
            if tool == "Pencil":
                pygame.draw.line(
                    canvas, color, last, current, 4
                )

            # Eraser
            elif tool == "Eraser":
                pygame.draw.line(
                    canvas, WHITE, last, current, 20
                )

                pygame.draw.circle(
                    canvas, WHITE, current, 10
                )

            last = current

        # Finish drawing
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

            if drawing:
                x, y = event.pos
                end = (x, y - TOOLBAR)

                if tool in ["Rectangle", "Circle"]:
                    draw_shape(canvas, start, end)

                drawing = False

    # Draw background
    screen.fill(GRAY)

    preview = canvas.copy()

    # Shape preview
    if drawing and tool in ["Rectangle", "Circle"]:
        x, y = pygame.mouse.get_pos()

        draw_shape(
            preview, start, (x, y - TOOLBAR)
        )

    screen.blit(preview, (0, TOOLBAR))

    # Draw tool buttons
    for i, name in enumerate(tools):

        button = pygame.Rect(
            i * 140 + 10, 5, 130, 35
        )

        button_color = (
            (180, 210, 255)
            if tool == name else WHITE
        )

        pygame.draw.rect(
            screen, button_color, button
        )

        text = font.render(name, True, BLACK)

        screen.blit(
            text, text.get_rect(center=button.center)
        )

    # Draw color buttons
    for i, c in enumerate(colors):

        button = pygame.Rect(
            i * 45 + 10, 55, 35, 35
        )

        pygame.draw.rect(screen, c, button)

        # Highlight selected color
        if c == color:
            pygame.draw.rect(
                screen, BLACK, button.inflate(6, 6), 2
            )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
