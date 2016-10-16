from PIL import Image
import os
import fnmatch


def resize(image_name, size=(1136, 640)):
    """
    resize image to no larger than size, its scale stays unchange
    :param image_name: full path of image file
    :param size: tuple contains maximum length and height for the image
    :return: PIL Image object
    """
    image = Image.open(image_name)
    length, height = image.size
    resize_length, resize_height = size
    length_scale = (length + 0.0) / resize_length
    height_scale = (height + 0.0) / resize_height
    if length_scale > height_scale:
        if length_scale > 1:
            length = 1136
            height = int(height / length_scale)
    else:
        if height_scale > 1:
            length = int(length / height_scale)
            height = 640
    image.thumbnail((length, height))
    image.save(image_name, 'JPEG')


def match_file(path, pattern='*'):
    """
    Find the matching file in specified directory, return
    as an iterator
    :param path: directory path to search
    :param pattern: regex pattern string for matching
    :return: matched filename
    """
    files = os.listdir(path)
    for file in files:
        if fnmatch.fnmatch(file, pattern):
            yield file


if __name__ == '__main__':
    dir_ = '.'
    for file_ in match_file(dir, '*.jpg'):
        resize('{}/{}'.format(dir, file_))
