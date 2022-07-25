import random
from pprint import pprint

from simpletorchvideo.reds.REDSZipReader import REDSZipReader
from simpletorchvideo import VideoDataset

reader = REDSZipReader("~/dataset/test_sharp_bicubic.zip", "test/test_sharp_bicubic/X4")
l = reader.list_videos()
pprint(l)
print(reader.read_images(l[0][0:3]))
print(reader.read_images(l[0][-3:]))
print(reader.read_images(l[-1][0:3]))
print(reader.read_images(l[-1][-3:]))
dataset = VideoDataset(reader)
for _ in range(3):
    data = dataset[random.randint(0, len(dataset))]
    print(data, len(data), data[0].shape, data[-1].shape)
data = dataset[0]
print(len(data), data[0].shape, data[-1].shape)
data = dataset[len(dataset) - 1]
print(len(data), data[0].shape, data[-1].shape)
