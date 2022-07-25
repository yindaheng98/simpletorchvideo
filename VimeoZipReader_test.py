from pprint import pprint

from simpletorchvideo.vimeo.VimeoZipReader import VimeoZipReader

inc = [
    '00001/0266',
    '00001/0268',
    '00001/0275',
    '00001/0278',
    '00001/0285',
    '00001/0287',
    '00002/0209',
    '00002/0235',
    '00002/0236',
    '00002/0238',
    '00002/0241',
    '00002/0243'

]
reader = VimeoZipReader("~/dataset/vimeo_septuplet.zip", include_list=inc)
l = reader.list_videos()
pprint(l)
print(reader.read_images(l[0][0:3]))
print(reader.read_images(l[0][-3:]))
print(reader.read_images(l[-1][0:3]))
print(reader.read_images(l[-1][-3:]))
