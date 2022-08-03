from PIL import Image
# import os


def resizeWithWhiteBackground(path_ori, path_des, size):
    img = Image.open(f'../{path_ori}')

    # resize and keep the aspect ratio
    img.thumbnail((size, size), Image.ANTIALIAS)

    # add the white background
    img_w, img_h = img.size
    background = Image.new('RGB', (size, size), (255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    background.save(f'../{path_des}')


# for dir in os.listdir(r'../images/imageDB/imegeFont/dicLattersSave'):
#     for image in os.listdir(fr'images/imageDB/imegeFont/dicLattersSave/{dir}'):
#         if image.endswith('.PNG') or image.endswith('.png'):
#             path = fr'images/imageDB/imegeFont/dicLattersSave/{dir}/{image}'
#             pathNew = fr'images/imageDB/imegeFont/reSaize/{dir}/{image}'
#             resize_with_white_background(path, pathNew)


