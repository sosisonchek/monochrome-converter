import argparse
from init import monochrome

def parsing_args():
    parser = argparse.ArgumentParser(description="Converts image to monochrome, with colors provided in config.ini")

    parser.add_argument('file', help='File destination', default='None')
    parser.add_argument('--size', type=str, help="Output's image resolution", default=None)
    parser.add_argument('--white', type=str, help='Color for lighter pixels', default='white')
    parser.add_argument('--dark', type=str, help='Color for darker pixels', default='black')
    parser.add_argument('--sharpness', type=int, help='Changes sharpness (0-255)', default=0)

    return parser.parse_args()
def main():
    monochrome(parsing_args())