from PIL import Image
import numpy as np
import configparser
import os

def monochrome(args):

    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config.read(config_path)

    colors = config['colors']

    with Image.open(args.file) as img:

        if args.size == None:
            width, height = img.size
        else:
            width, height = (args.size).split('x')
            width, height = int(width), int(height)

            img = img.resize((width, height), Image.Resampling.LANCZOS)

        img = img.convert('L')
        image = np.array(img)

        color_average = int(np.mean(image)) + args.sharpness
        color_average = min(255, max(0, color_average))

        height, width = image.shape
        new_image = np.zeros((height, width, 3), dtype=np.uint8)

        white = list(colors.get(args.white).split(', '))
        black = list(colors.get(args.black).split(', '))

        new_image[image >= color_average] = white
        new_image[image < color_average] = black

        result = Image.fromarray(new_image, 'RGB')
        result.show()
