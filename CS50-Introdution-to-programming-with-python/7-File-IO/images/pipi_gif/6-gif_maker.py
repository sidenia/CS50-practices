#pillow.readthedocs.io

import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    img = Image.open(arg)
    images.append(img)

images[0].save(
    "cat_gif.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)