
import pygame
import math
from collections import deque


def draw_shape(surface, tool, color, start, end, size):
    x1, y1 = start
    x2, y2 = end

    x = min(x1, x2)
    y = min(y1, y2)

    width = abs(x2 - x1)
    height = abs(y2 - y1)

    # Straight line
    if tool == "line":
        pygame.draw.line(
            surface, color, start, end, size
        )

    # Rectangle
    elif tool == "rectangle":
        pygame.draw.rect(
            surface, color,
            (x, y, width, height), size
        )

    # Circle
    elif tool == "circle":
        radius = int(math.hypot(x2 - x1, y2 - y1))

        pygame.draw.circle(
            surface, color, start, radius, size
        )

    # Square
    elif tool == "square":
        side = max(width, height)

        sx = x1 if x2 >= x1 else x1 - side
        sy = y1 if y2 >= y1 else y1 - side

        pygame.draw.rect(
            surface, color,
            (sx, sy, side, side), size
        )

    # Right triangle
    elif tool == "right_triangle":
        points = [
            (x1, y1),
            (x1, y2),
            (x2, y2)
        ]

        pygame.draw.polygon(
            surface, color, points, size
        )

    # Equilateral triangle
    elif tool == "equilateral_triangle":
        side = max(width, int(height * 2 / math.sqrt(3)))
        h = round(side * math.sqrt(3) / 2)

        direction_x = 1 if x2 >= x1 else -1
        direction_y = 1 if y2 >= y1 else -1

        points = [
            (x1 + direction_x * side // 2, y1),
            (x1, y1 + direction_y * h),
            (x1 + direction_x * side,
             y1 + direction_y * h)
        ]

        pygame.draw.polygon(
            surface, color, points, size
        )

    # Rhombus
    elif tool == "rhombus":
        points = [
            (x + width // 2, y),
            (x + width, y + height // 2),
            (x + width // 2, y + height),
            (x, y + height // 2)
        ]

        pygame.draw.polygon(
            surface, color, points, size
        )


# Flood Fill
def flood_fill(surface, position, new_color):
    width, height = surface.get_size()
    x, y = position

    if not (0 <= x < width and 0 <= y < height):
        return

    target_color = surface.get_at((x, y))
    new_color = pygame.Color(*new_color)

    if target_color == new_color:
        return

    queue = deque([(x, y)])

    surface.set_at((x, y), new_color)

    while queue:
        x, y = queue.popleft()

        neighbors = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]

        for nx, ny in neighbors:
            if 0 <= nx < width and 0 <= ny < height:
                if surface.get_at((nx, ny)) == target_color:
                    surface.set_at((nx, ny), new_color)
                    queue.append((nx, ny))
