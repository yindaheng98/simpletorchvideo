import random

from simpletorchvideo import VideoDataset
from simpletorchvideo.reader import VideoReaderList
from simpletorchvideo.reds.REDSZipReader import REDSZipReader

lr_reader = REDSZipReader("~/dataset/val_sharp_bicubic.zip", "val/val_sharp_bicubic/X4")
hr_reader = REDSZipReader("~/dataset/val_sharp.zip", "val/val_sharp")
reader = VideoReaderList(lr_reader, hr_reader)
dataset = VideoDataset(reader)
for _ in range(3):
    data = dataset[random.randint(0, len(dataset))]
    print(data, len(data), data[0][0].shape, data[-1][0].shape)
data = dataset[0]
print(len(data), data[0][0].shape, data[-1][0].shape)
data = dataset[len(dataset) - 1]
print(len(data), data[0][0].shape, data[-1][0].shape)
