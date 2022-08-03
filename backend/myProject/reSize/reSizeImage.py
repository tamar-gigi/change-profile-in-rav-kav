from PIL import Image


def resizeWithWhiteBackground(path_ori, path_dest, size):
    img = Image.open(f'{path_ori}')

    # resize and keep the aspect ratio
    img.thumbnail((size, size), Image.ANTIALIAS)

    # add the white background
    img_w, img_h = img.size
    background = Image.new('RGB', (size, size), (255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    background.save(f'{path_dest}')




