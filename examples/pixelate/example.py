#!python3

from pixelate import pixelate
from utils_pixelate import open_image, save_image

import os
import sys

if __name__ == '__main__':
    originalImagePath = os.path.join(
        os.path.realpath(sys.path[0]), 'images', 'original')
    original_file_list = os.scandir(originalImagePath)

    pixelatedImagePath = os.path.join(
        os.path.realpath(sys.path[0]), 'images', 'pixelated')
    pixelated_file_list = os.scandir(pixelatedImagePath)

    num_files = len((next(os.walk(originalImagePath)))[2])
    print('Reading {} files...'.format(num_files))

    steps = {'shapeofwater': 70, 'marriage': 25, 'birdman': 110, 'jaws': 50,
             'dunkirk': 15, 'cmbyn': 55, '127': 5, 'fargo': 20, 'florida': 25, 'moonlight': 80}

    for filename in original_file_list:
        if not (filename.name.endswith('.jpg')):
            continue
        orig = open_image(os.path.join(originalImagePath, filename))

        filmName = os.path.basename(filename.name)
        filmName = ''.join(filmName.split('.')[:-1])

        print('Reading {}...'.format(filmName))
        pixelated = pixelate(orig, steps[filmName])
        save_image(pixelated, os.path.join(pixelatedImagePath, filmName + '.jpg'), 'jpeg')