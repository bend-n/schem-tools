#!/bin/python
from PIL import Image, ImageStat
from argparse import ArgumentParser

parser = ArgumentParser("yes")
parser.add_argument("image", help="image to convert")


def median(image):
    img = Image.open(image)

    return tuple(ImageStat.Stat(img).median[:3])  # :3 :3


print(median(parser.parse_args().image))
