import random
from pprint import pprint
from torchvideo.reader import ZipImageReader

reader = ZipImageReader("~/dataset/Vid4.zip")
l = reader.list_images("GT")
pprint(l)
print(reader.read_image(l[-1]))
print(reader.read_image(l[random.randint(0, len(l))]))
print(reader.read_image(l[0]))
info = reader.getinfo("GT/city/")
print(info)
