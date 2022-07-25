import random
from pprint import pprint
from simpletorchvideo.ffmpeg import FFmpegReader
from simpletorchvideo.VideoDataset import VideoDataset

reader = FFmpegReader(["~/Videos/4K-small.mkv", "~/Videos/720p-small.mkv"])
pprint(reader.list_videos())
for frames in reader.list_videos():
    f0 = reader.read_images(frames[0:3])
    f1 = reader.read_images(frames[-3:])
    i = random.randint(0, len(frames))
    fr = reader.read_images(frames[i:i + 3])
    print(f0)
    print(f1)
    print(fr)
    print(f0[0].shape)
    print(f1[0].shape)
    print(fr[0].shape)

dataset = VideoDataset(reader)
for _ in range(3):
    data = dataset[random.randint(0, len(dataset))]
    print(data, len(data), data[0].shape, data[-1].shape)
data = dataset[0]
print(len(data), data[0].shape, data[-1].shape)
data = dataset[len(dataset) - 1]
print(len(data), data[0].shape, data[-1].shape)
