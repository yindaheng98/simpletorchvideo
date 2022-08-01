import random
from pprint import pprint
import cv2
from simpletorchvideo.reader import ZipImageReader

reader = ZipImageReader("~/dataset/Vid4.zip")
l = reader.list_images("GT")
pprint(l)
print(reader.read_image(l[-1]))
print(reader.read_image(l[random.randint(0, len(l))]))
print(reader.read_image(l[0]))
print(reader.read_image(l[0]).shape)
for i in range(3):
    cv2.imwrite("dataset/%d.png" % i, reader.read_image(l[random.randint(0, len(l))]))
cv2.imwrite("dataset/flag_color.png", reader.read_image(l[random.randint(0, len(l))], flag='color'))  # 正常
cv2.imwrite("dataset/channel_order_rgb.png", reader.read_image(l[random.randint(0, len(l))], channel_order='rgb'))  # 正常
cv2.imwrite("dataset/flag_color_channel_order_rgb.png",
            reader.read_image(l[random.randint(0, len(l))], flag='color', channel_order='rgb'))  # 不正常
info = reader.getinfo("GT/city/")
print(info)
