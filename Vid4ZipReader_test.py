import random
import cv2
from pprint import pprint

from simpletorchvideo.vid4.Vid4ZipReader import Vid4ZipBDx4Reader
from simpletorchvideo import VideoDataset

reader = Vid4ZipBDx4Reader("~/dataset/Vid4.zip")
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
dataset = VideoDataset(reader, num_frames=None)
for _ in range(3):
    data = dataset[random.randint(0, len(dataset) - 1)]
    print(data, len(data), data[0].shape, data[-1].shape)
data = dataset[0]
print(len(data), data[0].shape, data[-1].shape)
data = dataset[len(dataset) - 1]
print(len(data), data[0].shape, data[-1].shape)
