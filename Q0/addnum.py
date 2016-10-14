# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os


def add_num(image, num, size=5):
    """

    :param image: PIL.Image object for add number
    :param num: number to add
    :param size: division of num_image_size divide image_size, default set to 5
                 which means num_image size is 20% of image size
    :return: composed image object
    """
    img = Image.open(image)
    length, height = img.size
    num_img = create_num(num, (length/size, height/size))
    return compose_two_image(img, num_img, (length/size * (size-1), 0, length, height/size))


def create_num(num, size):
    """
    create a image with the specified number and size
    :param num: number on the image
    :param size: a tuple contains size of the return image
    :return: image object
    """
    img = Image.new("RGB", size, (255,255,255))
    dr = ImageDraw.Draw(img)
    font = ImageFont.truetype(font=os.path.join('Fonts', 'Futura.ttc'), size=size[0] /10 * 8 )
    dr.text((0, 0), str(num), font=font, fill='#FF0000')
    return img


def compose_two_image(base, upper, pos):
    """

    :param base: base image
    :param upper: image to be added
    :param pos: position of the upper image on the base image, a four-element tuple
                (x, y, z, w) represents the top left position (x, y), bottom right
                position (z, w) respectively
    :return: composed image
    """
    base.paste(upper, pos)
    return base


if __name__ == '__main__':
    add_num('test.jpeg', 12).show()
