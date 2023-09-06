import random

HAPPY_COLOR_RANGE = [
    (255, 255, 0),    # Yellow
    (255, 165, 0),    # Orange
    (255, 192, 203),  # Pink
    (255, 0, 0),      # Red
    (255, 218, 185),  # Peach
    (255, 182, 193),  # Light Pink
    (200, 162, 200),  # Lilac
]

HAPPY_COLOR_SENSITIVITY = 50


def is_happy_color(pixel):
    # Check if the pixel color is within the happy color range
    for color in HAPPY_COLOR_RANGE:
        if all(abs(pixel[i] - color[i]) < HAPPY_COLOR_SENSITIVITY for i in range(3)):
            return True

    return False

def generate_happy_color():
    happy_color = []
    color = random.choice(HAPPY_COLOR_RANGE)
    for i in range(3):
        sensitivity  = random.randrange(0, HAPPY_COLOR_SENSITIVITY)
        happy_color.append(color[i] + sensitivity)
    return tuple(happy_color)