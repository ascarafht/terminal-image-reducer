#!/usr/bin/env python3

import os
from argparse import ArgumentParser
from PIL import Image


#arguments definition
parser = ArgumentParser(
        prog='rimg',
        description='Creates a reduced size copy of an image preserving aspect ratio.'
    )
parser.add_argument('source', help='Source file')
parser.add_argument('dest', help='Destination path')
parser.add_argument('--width', '-w', default=0, type=int, required=False, help='New width in pixels.')
parser.add_argument('--height', '-he', default=0, type=int, required=False, help='New height in pixels.')

#arguments asignation
args = parser.parse_args()
source_path = os.path.dirname(args.source)
source_name, source_suffix = os.path.splitext(os.path.basename(args.source))
dest_path = args.dest
new_width = args.width
new_height = args.height
new_img_path = f'{dest_path}/{source_name}_{source_suffix}'
try:
    if new_width == 0 and new_height == 0:
        raise ValueError('Required to define height or width with a value bigger than 0.')

    with Image.open(f'{source_path}/{source_name}{source_suffix}') as image:
        if new_width == 0:
            new_width = (new_height*image.size[0]//image.size[1])+1
        if new_height == 0:
            new_height = (new_width*image.size[1]//image.size[0])+1
        image.thumbnail((new_width, new_height))
        new_img_path = f'{dest_path}/{source_name}_{image.size[0]}x{image.size[1]}{source_suffix}'
        image.save(new_img_path, image.format)
        print(f'Created Image: {os.path.basename(new_img_path)}')
        print(f'Size: {image.size[0]}x{image.size[1]}')
except OSError:
    print(f'Error: cannot create image')
except ValueError as e:
    print('ValueError: ' + e)
except Exception as e:
    print(f'Unexpected error: {e}, {type(e)}')