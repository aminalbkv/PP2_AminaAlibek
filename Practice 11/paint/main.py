
import pygame
import math

pygame.init()

# Window settings
WIDTH, HEIGHT = 1000, 650
TOOLBAR = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint - Practice 11")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 17)

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
tools = [
    "Pencil",
    "Rectangle",
    "Circle",
    "Eraser",
    "Square",
    "Right Triangle",
    "Equilateral",
    "Rhombus"
]

shapes = [
    "Rectangle",
    "Circle",
    "Square",
    "Right Triangle",
    "Equilateral",
    "Rhombus"
]

tool = "Pencil"
color = BLACK
drawing = False
start = None
last = None


# Draw selected geometric shape
def draw_shape(surface, start, end):

    x1, y1 = start
    x2, y2 = end

    x = min(x1, x2)
    y = min(y1, y2)

    w = abs(x2 - x1)
    h = abs(y2 - y1)

    # Rectangle
    if tool == "Rectangle":

        pygame.draw.rect(
            surface, color,
            (x, y, w, h), 3
        )

    # Circle
    elif tool == "Circle":

        radius = int(
            math.hypot(x2 - x1, y2 - y1)
        )

        pygame.draw.circle(
            surface, color,
            start, radius, 3
        )

    # Square
    elif tool == "Square":

        side = max(w, h)

        sx = x1 if x2 >= x1 else x1 - side
        sy = y1 if y2 >= y1 else y1 - side

        pygame.draw.rect(
            surface, color,
            (sx, sy, side, side), 3
        )

    # Right triangle
    elif tool == "Right Triangle":

        points = [
            (x1, y1),
            (x1, y2),
            (x2, y2)
        ]

        pygame.draw.polygon(
            surface, color, points, 3
        )

    # Equilateral triangle
    elif tool == "Equilateral":

        side = max(w, h)
        triangle_height = side * math.sqrt(3) / 2

        points = [
            (x1, y1),
            (x1 - side / 2, y1 + triangle_height),
            (x1 + side / 2, y1 + triangle_height)
        ]

        pygame.draw.polygon(
            surface, color, points, 3
        )

    # Rhombus
    elif tool == "Rhombus":

        points = [
            (x + w / 2, y),
            (x + w, y + h / 2),
            (x + w / 2, y + h),
            (x, y + h / 2)
        ]

        pygame.draw.polygon(
            surface, color, points, 3
        )


# Main program loop
running = True

while running:

    for event in pygame.event.get():

        # Close application
        if event.type == pygame.QUIT:
            running = False

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            x, y = event.pos

            # Select drawing tool
            if y < 45:

                for i, name in enumerate(tools):

                    button = pygame.Rect(
                        i * 123 + 5, 5, 118, 35
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

            # Pencil drawing
            if tool == "Pencil":

                pygame.draw.line(
                    canvas, color,
                    last, current, 4
                )

            # Eraser
            elif tool == "Eraser":

                pygame.draw.line(
                    canvas, WHITE,
                    last, current, 20
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

                if tool in shapes:

                    draw_shape(
                        canvas, start, end
                    )

                drawing = False

    # Draw background
    screen.fill(GRAY)

    preview = canvas.copy()

    # Preview shape before releasing mouse
    if drawing and tool in shapes:

        x, y = pygame.mouse.get_pos()

        draw_shape(
            preview, start,
            (x, y - TOOLBAR)
        )

    screen.blit(preview, (0, TOOLBAR))

    # Draw tool buttons
    for i, name in enumerate(tools):

        button = pygame.Rect(
            i * 123 + 5, 5, 118, 35
        )

        button_color = (
            (180, 210, 255)
            if tool == name else WHITE
        )

        pygame.draw.rect(
            screen, button_color, button
        )

        text = font.render(
            name, True, BLACK
        )

        screen.blit(
            text,
            text.get_rect(center=button.center)
        )

    # Draw color buttons
    for i, c in enumerate(colors):

        button = pygame.Rect(
            i * 45 + 10, 55, 35, 35
        )

        pygame.draw.rect(
            screen, c, button
        )

        # Highlight selected color
        if c == color:

            pygame.draw.rect(
                screen, BLACK,
                button.inflate(6, 6), 2
            )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
