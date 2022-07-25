import random
from pprint import pprint
from simpletorchvideo.reader import DirectoryImageReader

reader = DirectoryImageReader("~/dataset/vimeo_septuplet")
l = reader.list_images("")
pprint(l)
print(reader.read_image(l[-1]))
print(reader.read_image(l[random.randint(0, len(l))]))
print(reader.read_image(l[0]))
