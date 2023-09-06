import sys
from PIL import Image, ImageDraw

from happy_color import is_happy_color, generate_happy_color


def verify_badge(image):
    width, height = image.size

    if width != 512 or height != 512:
        return False

    middle_height = height / 2
    radius = -1
    # We search the first pixel that's not transparent
    for x in range(width):
        r, g, b, a = image.getpixel((x, middle_height))
        if a != 0:
            radius = (width - 2 * x) / 2
            break

    # We didn't find any pixel that's not transparent
    if radius == -1:
        return False

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if in_circle(x, y, width, height, radius):
                if not is_happy_color(pixel):
                    # There is a pixel inside the circle that is not "happy"
                    return False
            else:
                if pixel[3] != 0:
                    # There is a non-transparent pixel outside the circle
                    return False

    return True


def in_circle(x, y, width, height, radius):
    center_x = width / 2 - 0.5
    center_y = height / 2 - 0.5
    return (x - center_x) ** 2 + (y - center_y) ** 2 < radius**2


def convert_to_badge(image):
    image = image.resize((512, 512))

    for x in range(512):
        r, g, b, a = image.getpixel((x, 256))
        if a != 0:
            radius = (512 - 2 * x) / 2
            break

    draw = ImageDraw.Draw(image, "RGBA")

    # We associate each sad color we find to a happy color
    associated_colors = {}
    for x in range(512):
        for y in range(512):
            pixel = image.getpixel((x, y))
            color = (pixel[0], pixel[1], pixel[2])
            if in_circle(x, y, 512, 512, radius):
                if not is_happy_color(color):
                    # If it's in the circle and the color is not happy we keep the opacity but change the color to a happy one
                    associated_colors, happy_color = associate_with_happy_color(
                        color, associated_colors
                    )
                    c = happy_color + (pixel[3],)
                    draw.point((x, y), fill=c)
            # Outside the circle everything is transparent
            else:
                draw.point((x, y), fill=(0, 0, 0, 0))

    return image


def associate_with_happy_color(color, associated_colors):
    if color in associated_colors:
        return associated_colors, associated_colors[color]
    else:
        happy_color = generate_happy_color()
        while happy_color in associated_colors.values():
            happy_color = generate_happy_color()
        associated_colors[color] = happy_color
        return associated_colors, happy_color


image_path = sys.argv[1]
try:
    image = Image.open(image_path)
    if verify_badge(image):
        print("The badge meets the requirements.")
    else:
        print("The badge doesn't meet the requirements. We will try to convert it.")
        new_image = convert_to_badge(image)
        new_image.save(image_path[: image_path.rfind(".png")] + "_converted.png")
except FileNotFoundError:
    print("There is no such file.")
