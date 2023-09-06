from PIL import Image, ImageDraw
from happy_color import HAPPY_COLOR_RANGE
from random import choice


def create_badge(width, height):
    # Create a new image with transparent background
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Create a draw object
    draw = ImageDraw.Draw(image, "RGBA")

    # Define the color for the circle

    # Draw the circle in the center of the image
    for x in range(width):
       
        for y in range(height):
            color = choice(HAPPY_COLOR_RANGE)
            color = (color[0], color[1], color[2], 255)
            if in_circle(x, y, width, height):
                draw.point((x, y), fill=color)

    # Save the image
    image.save("happy_badge.png")


def in_circle(x, y, width, height):
    center_x = width / 2 - 0.5
    center_y = height / 2 - 0.5
    radius = int(min(width, height) / 3)
    return (x - center_x) ** 2 + (y - center_y) ** 2 < radius**2


create_badge(512, 512)
