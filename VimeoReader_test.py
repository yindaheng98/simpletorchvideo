import random
import logging
from torchvideo.vimeo import VimeoReader
from torchvideo import VideoDataset

logging.basicConfig(level=logging.DEBUG)
inc = [
    '00001/0001',
    '00001/0003',
    '00001/0005',
    '00002/0002',
    '00002/0004',

]
reader = VimeoReader("D:\\Documents\\MyPrograms\\vimeo_septuplet", include_list=inc)
dataset = VideoDataset(reader)
for _ in range(3):
    data = dataset[random.randint(0, len(dataset))]
    print(data, len(data), data[0].shape, data[-1].shape)
data = dataset[0]
print(len(data), data[0].shape, data[-1].shape)
data = dataset[len(dataset) - 1]
print(len(data), data[0].shape, data[-1].shape)
reader = VimeoReader("D:\\Documents\\MyPrograms\\视频数据\\vimeo_septuplet.zip", include_list=inc)
dataset = VideoDataset(reader, num_frames=3)
for _ in range(3):
    data = dataset[random.randint(0, len(dataset))]
    print(data, len(data), data[0].shape, data[-1].shape)
data = dataset[0]
print(len(data), data[0].shape, data[-1].shape)
data = dataset[len(dataset) - 1]
print(len(data), data[0].shape, data[-1].shape)
