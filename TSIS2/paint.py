
import pygame
from datetime import datetime
from pathlib import Path

from tools import draw_shape, flood_fill


pygame.init()

# Window settings
WIDTH = 1200
HEIGHT = 800
TOOLBAR_HEIGHT = 110
CANVAS_HEIGHT = HEIGHT - TOOLBAR_HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS2 Paint")

clock = pygame.time.Clock()

toolbar_font = pygame.font.SysFont("Arial", 15)
text_font = pygame.font.SysFont("Arial", 26)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (235, 235, 235)
DARK_GRAY = (80, 80, 80)
SELECTED_BLUE = (190, 220, 255)

# Drawing canvas
canvas = pygame.Surface((WIDTH, CANVAS_HEIGHT))
canvas.fill(WHITE)

# Available tools
tools = [
    ("pencil", "Pencil"),
    ("line", "Line"),
    ("rectangle", "Rectangle"),
    ("circle", "Circle"),
    ("square", "Square"),
    ("right_triangle", "Right Tri"),
    ("equilateral_triangle", "Equal Tri"),
    ("rhombus", "Rhombus"),
    ("eraser", "Eraser"),
    ("fill", "Fill"),
    ("text", "Text"),
    ("picker", "Picker")
]

# Color palette
colors = [
    BLACK,
    WHITE,
    (255, 0, 0),
    (0, 180, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (255, 105, 180),
    (128, 0, 128),
    (0, 200, 200),
    (150, 75, 0),
    (128, 128, 128)
]

# Default settings
active_tool = "pencil"
active_color = BLACK
brush_size = 2

drawing = False
start_pos = None
last_pos = None

# Text tool settings
text_active = False
text_position = None
text_value = ""

pygame.key.stop_text_input()

# Tool buttons
tool_buttons = []

for i, (tool, label) in enumerate(tools):
    rect = pygame.Rect(
        10 + i * 98, 10, 92, 35
    )

    tool_buttons.append((rect, tool, label))

# Color buttons
color_buttons = []

for i, color in enumerate(colors):
    rect = pygame.Rect(
        10 + i * 32, 55, 27, 27
    )

    color_buttons.append((rect, color))

# Brush size buttons
size_buttons = []

for i, size in enumerate([2, 5, 10]):
    rect = pygame.Rect(
        410 + i * 65, 53, 60, 30
    )

    size_buttons.append((rect, size))

# Save and Clear buttons
save_button = pygame.Rect(620, 53, 80, 30)
clear_button = pygame.Rect(710, 53, 80, 30)

status_message = "Ready"


# Draw a button
def draw_button(rect, label, selected=False):
    color = SELECTED_BLUE if selected else WHITE

    pygame.draw.rect(
        screen, color, rect, border_radius=4
    )

    pygame.draw.rect(
        screen, DARK_GRAY, rect, 1,
        border_radius=4
    )

    text = toolbar_font.render(
        label, True, BLACK
    )

    screen.blit(
        text, text.get_rect(center=rect.center)
    )


# Draw the toolbar
def draw_toolbar():
    pygame.draw.rect(
        screen,
        LIGHT_GRAY,
        (0, 0, WIDTH, TOOLBAR_HEIGHT)
    )

    # Tool buttons
    for rect, tool, label in tool_buttons:
        draw_button(
            rect, label, active_tool == tool
        )

    # Color palette
    for rect, color in color_buttons:
        pygame.draw.rect(screen, color, rect)

        border = 3 if color == active_color else 1

        pygame.draw.rect(
            screen, DARK_GRAY, rect, border
        )

    # Brush sizes
    for rect, size in size_buttons:
        draw_button(
            rect,
            str(size) + " px",
            brush_size == size
        )

    draw_button(save_button, "Save")
    draw_button(clear_button, "Clear")

    # Current selected color
    pygame.draw.rect(
        screen, active_color,
        (810, 55, 28, 28)
    )

    pygame.draw.rect(
        screen, BLACK,
        (810, 55, 28, 28), 1
    )

    info = toolbar_font.render(
        "1 / 2 / 3: Size | Ctrl/Cmd + S: Save",
        True, BLACK
    )

    screen.blit(info, (850, 62))

    status = toolbar_font.render(
        status_message, True, DARK_GRAY
    )

    screen.blit(status, (10, 88))

    pygame.draw.line(
        screen, DARK_GRAY,
        (0, TOOLBAR_HEIGHT - 1),
        (WIDTH, TOOLBAR_HEIGHT - 1)
    )


# Convert screen position to canvas position
def canvas_position(position):
    x, y = position
    return x, y - TOOLBAR_HEIGHT


# Keep coordinates inside the canvas
def clamp_position(position):
    x, y = canvas_position(position)

    x = max(0, min(WIDTH - 1, x))
    y = max(0, min(CANVAS_HEIGHT - 1, y))

    return x, y


# Save canvas as PNG
def save_canvas():
    global status_message

    folder = Path(__file__).parent / "saved_drawings"
    folder.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S_%f"
    )

    filename = folder / f"drawing_{timestamp}.png"

    pygame.image.save(canvas, str(filename))

    status_message = "Saved: " + filename.name

    print("Saved:", filename)


# Cancel text input
def cancel_text():
    global text_active, text_value, text_position

    text_active = False
    text_value = ""
    text_position = None

    pygame.key.stop_text_input()


# Handle toolbar clicks
def handle_toolbar(position):
    global active_tool, active_color
    global brush_size, status_message

    for rect, tool, label in tool_buttons:
        if rect.collidepoint(position):
            cancel_text()

            active_tool = tool
            status_message = "Tool: " + label
            return

    for rect, color in color_buttons:
        if rect.collidepoint(position):
            active_color = color
            return

    for rect, size in size_buttons:
        if rect.collidepoint(position):
            brush_size = size
            return

    if save_button.collidepoint(position):
        save_canvas()

    elif clear_button.collidepoint(position):
        cancel_text()
        canvas.fill(WHITE)
        status_message = "Canvas cleared"


# Pencil and eraser
def draw_brush(start, end):
    if active_tool == "eraser":
        color = WHITE
        size = brush_size * 4
    else:
        color = active_color
        size = brush_size

    pygame.draw.line(
        canvas, color, start, end, size
    )

    pygame.draw.circle(
        canvas, color, end, size // 2
    )


# Main game loop
running = True

while running:

    for event in pygame.event.get():

        # Close the application
        if event.type == pygame.QUIT:
            running = False

        # Keyboard input
        elif event.type == pygame.KEYDOWN:

            # Save using Ctrl+S or Command+S
            if (
                event.key == pygame.K_s
                and event.mod & (
                    pygame.KMOD_CTRL | pygame.KMOD_META
                )
            ):
                save_canvas()

            # Text input mode
            elif text_active:

                if event.key == pygame.K_RETURN:
                    rendered_text = text_font.render(
                        text_value, True, active_color
                    )

                    canvas.blit(
                        rendered_text, text_position
                    )

                    cancel_text()

                    status_message = "Text added"

                elif event.key == pygame.K_ESCAPE:
                    cancel_text()
                    status_message = "Text cancelled"

                elif event.key == pygame.K_BACKSPACE:
                    text_value = text_value[:-1]

            # Brush size shortcuts
            else:
                if event.key == pygame.K_1:
                    brush_size = 2

                elif event.key == pygame.K_2:
                    brush_size = 5

                elif event.key == pygame.K_3:
                    brush_size = 10

        # Typed characters
        elif event.type == pygame.TEXTINPUT:
            if text_active:
                text_value += event.text

        # Mouse button pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                # Click on toolbar
                if event.pos[1] < TOOLBAR_HEIGHT:
                    handle_toolbar(event.pos)

                # Click on canvas
                else:
                    position = canvas_position(
                        event.pos
                    )

                    # Fill tool
                    if active_tool == "fill":
                        flood_fill(
                            canvas,
                            position,
                            active_color
                        )

                        status_message = "Area filled"

                    # Color picker
                    elif active_tool == "picker":
                        picked = canvas.get_at(position)

                        active_color = (
                            picked.r,
                            picked.g,
                            picked.b
                        )

                        status_message = "Color picked"

                    # Text tool
                    elif active_tool == "text":
                        text_active = True
                        text_position = position
                        text_value = ""

                        pygame.key.start_text_input()

                        status_message = (
                            "Type text | Enter: Confirm "
                            "| Esc: Cancel"
                        )

                    # Pencil, eraser and shapes
                    else:
                        drawing = True
                        start_pos = position
                        last_pos = position

                        if active_tool in [
                            "pencil", "eraser"
                        ]:
                            draw_brush(
                                position, position
                            )

        # Mouse movement
        elif event.type == pygame.MOUSEMOTION:

            if drawing:
                position = clamp_position(event.pos)

                if active_tool in [
                    "pencil", "eraser"
                ]:
                    draw_brush(last_pos, position)

                    last_pos = position

        # Mouse button released
        elif event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1 and drawing:

                position = clamp_position(event.pos)

                if active_tool in [
                    "pencil", "eraser"
                ]:
                    draw_brush(last_pos, position)

                else:
                    draw_shape(
                        canvas,
                        active_tool,
                        active_color,
                        start_pos,
                        position,
                        brush_size
                    )

                drawing = False
                start_pos = None
                last_pos = None

    # Create a temporary canvas for previews
    preview = canvas.copy()

    # Live preview of shapes
    if drawing and active_tool not in [
        "pencil", "eraser"
    ]:
        mouse_pos = clamp_position(
            pygame.mouse.get_pos()
        )

        draw_shape(
            preview,
            active_tool,
            active_color,
            start_pos,
            mouse_pos,
            brush_size
        )

    # Live text preview
    if text_active:
        rendered_text = text_font.render(
            text_value, True, active_color
        )

        preview.blit(
            rendered_text, text_position
        )

        cursor_x = (
            text_position[0]
            + rendered_text.get_width()
        )

        cursor_y = text_position[1]

        # Blinking text cursor
        if pygame.time.get_ticks() // 500 % 2 == 0:
            pygame.draw.line(
                preview,
                active_color,
                (cursor_x, cursor_y),
                (cursor_x, cursor_y + 26),
                2
            )

    # Display canvas and toolbar
    screen.blit(preview, (0, TOOLBAR_HEIGHT))

    draw_toolbar()

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
