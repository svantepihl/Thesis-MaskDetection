from struct import unpack
import os
from tqdm import tqdm

marker_mapping = {
    0xffd8: "Start of Image",
    0xffe0: "Application Default Header",
    0xffdb: "Quantization Table",
    0xffc0: "Start of Frame",
    0xffc4: "Define Huffman Table",
    0xffda: "Start of Scan",
    0xffd9: "End of Image"
}


class JPEG:
    def __init__(self, image_file):
        with open(image_file, 'rb') as f:
            self.img_data = f.read()

    def decode(self):
        data = self.img_data
        while(True):
            marker, = unpack(">H", data[0:2])
            # print(marker_mapping.get(marker))
            if marker == 0xffd8:
                data = data[2:]
            elif marker == 0xffd9:
                return
            elif marker == 0xffda:
                data = data[-2:]
            else:
                lenchunk, = unpack(">H", data[2:4])
                data = data[2+lenchunk:]
            if len(data) == 0:
                break


bads = []

root_img = "/Users/svantepihl/Google Drive/MaskedFace/MaskImages"

images = []

for fold in os.listdir(root_img,):
    if not fold.startswith('.'):
        for filename in os.listdir(f'{root_img}/{fold}'):
            images.append(f'{fold}/{filename}')


for img in tqdm(images):
    image = os.path.join(root_img, img)
    image = JPEG(image)
    try:
        image.decode()
    except:
        bads.append(img)
        print(img)

print(len(images))
print(bads)
# for name in bads:
#    os.remove(osp.join(root_img, name))
