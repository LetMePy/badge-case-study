

# Installation

You must have Python installed on your machine. If not, please do so.

Then run this command.

```bash
pip install -r requirements.txt
```

# How to use it ?

To use the script, simply run the following command and enter the path to the image.

```bash
python3 badge.py data/happy_badge.png
```

# Comments

## The "happy" thing

Since interpreting the notion of "happy" is rather subjective, I turned to my friend google and here's the definition that convinced me the most.

> Happy colors are usually thought to be bright, warm shades, like yellow, orange, pink and red, or pastels, like peach, light pink and lilac. The brighter and lighter the color, the happier and more optimistic it can make you feel. Combining lots of colors together can feel joyful and exuberant, like the Holi festival, or maybe a little chaotic and overwhelming, like an overcrowded city street.
>
> -- <cite>[99designs][1]</cite>

[1]: https://99designs.com/blog/tips/how-color-impacts-emotions-and-behaviors/

## The create_avatar.py script

 I created this script to generate images that comply with the conditions (sometimes they don't) since I've found it difficult to find images to work on on the Internet.

Feel free to tweak it and use it.

## The conversion function

The conversion function presents several challenges:
1. When the image does not respect the specified size, it is resized.
2. When the badge and avatar format is not respected, we can consider a circle inside the image and set the opacity to 0 outside the circle.
3. There's now the feeling of happiness that the image should give off, which is rather difficult to achieve. I therefore chose to associate each color judged as "unhappy" with a color that is "happy", making sure of course that no two colors have the same association (a bijection in algebra).
