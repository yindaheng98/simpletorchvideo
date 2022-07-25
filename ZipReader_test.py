import random
from pprint import pprint
from torchvideo.ZipReader import ZipReader

reader = ZipReader("~/dataset/Vid4.zip")
l = reader.list_file("GT")
pprint(l)
print(reader.read_file(l[0]))
print(reader.read_file(l[-1]))
print(reader.read_file(l[random.randint(0, len(l))]))
