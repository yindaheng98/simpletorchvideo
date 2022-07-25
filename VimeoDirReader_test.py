from pprint import pprint

from torchvideo.vimeo.VimeoDirReader import VimeoDirReader

inc = [
    '00001/0001',
    '00001/0003',
    '00001/0005',
    '00002/0002',
    '00002/0004',

]
reader = VimeoDirReader("D:\\Documents\\MyPrograms\\vimeo_septuplet", include_list=inc)
l = reader.list_videos()
pprint(l)
print(reader.read_images(l[0][0:3]))
print(reader.read_images(l[0][-3:]))
print(reader.read_images(l[-1][0:3]))
print(reader.read_images(l[-1][-3:]))
