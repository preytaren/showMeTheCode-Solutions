import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageColor


def random_text(length):
    """
    Generate a random string contains length elements
    :param length:
    :return:
    """
    result = []
    for idx in range(length):
        result.append(random.choice(string.letters))
    return result


def random_color():
    table = ['0', '1', '2', '3',
             '4', '5', '6', '7',
             '8', '9', 'a', 'b',
             'c', 'd', 'e', 'f',]
    result = []
    for i in range(6):
        result.append(random.choice(table))
    return '#' + ''.join(result)


def draw_letters(base, letters):
    width, height = base.size
    padding = 5
    number = len(letters)
    draw = ImageDraw.Draw(base)
    font = ImageFont.truetype('Futura.ttc', 25 )
    font_width, font_height = font.getsize(''.join(letters))
    per_width = (width - 2 * padding) / number
    per_height = (height - font_height) / number
    for idx, letter in enumerate(letters):
        color = random_color()
        draw.text((padding + per_width * idx, per_height * (idx+1)), letter,
              font=font, fill=color)
    # base = base.transform((width+20,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)
    base = base.filter(ImageFilter.SMOOTH)
    return base


def bg_image():
    return Image.new('RGBA', (100, 30), color='#ffffff')
    """
    image = Image.open('test/q10.jpg')
    image = image.filter(ImageFilter.SMOOTH_MORE)
    return image
    """


def generate_code():
    image = bg_image()
    text = random_text(4)
    output = draw_letters(image, text)
    output.show()


if __name__ == '__main__':
    generate_code()
