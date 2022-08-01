from pprint import pprint
import cv2
from simpletorchvideo.vimeo.VimeoZipReader import VimeoZipReader

inc = [
    '00001/0266',
    '00001/0268',
    '00001/0275',
    '00001/0278',
    '00001/0285',
    '00001/0287',
    '00002/0209',
    '00002/0235',
    '00002/0236',
    '00002/0238',
    '00002/0241',
    '00002/0243'

]
reader = VimeoZipReader("~/dataset/vimeo_septuplet.zip", include_list=inc)
l = reader.list_videos()
pprint(l)
print(reader.read_images(l[0][0:3]))
print(reader.read_images(l[0][-3:]))
print(reader.read_images(l[-1][0:3]))
print(reader.read_images(l[-1][-3:]))
cv2.imwrite("dataset/default.png", reader.read_images(l[-1][-3:])[0])
cv2.imwrite("dataset/flag_color.png", reader.read_images(l[-1][-3:], flag='color')[0])  # 正常
cv2.imwrite("dataset/channel_order_rgb.png", reader.read_images(l[-1][-3:], channel_order='rgb')[0])  # 正常
cv2.imwrite("dataset/flag_color_channel_order_rgb.png",
            reader.read_images(l[-1][-3:], flag='color', channel_order='rgb')[0])  # 不正常
