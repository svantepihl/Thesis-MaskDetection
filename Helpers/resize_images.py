import PIL
import os
import os.path
import tensorflow as tf
from PIL import Image
from tqdm import tqdm


root_img = "/Users/svantepihl/Downloads/facemask-detection-thesis-images-jpeg"

TARGET_SIZE = (224, 244)
images = []

for fold in os.listdir(root_img):
    if not fold.startswith('.'):
        for filename in os.listdir(f'{root_img}/{fold}'):
            if not fold.startswith('.'):
                images.append(f'{fold}/{filename}')


def resize_image_tensorflow(image):
    image = tf.image.resize(
        image,
        TARGET_SIZE,
        method=tf.image.ResizeMethod.AREA,
        preserve_aspect_ratio=False,
        antialias=True)
    return image


for image in tqdm(images):
    img_path = os.path.join(root_img, image)
    img = Image.open(img_path)
    img = img.resize(TARGET_SIZE)
    img.save(img_path)
