#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

package_dir = {
    'simpltorchvideo': 'simpltorchvideo',
    'simpltorchvideo.reader': 'simpltorchvideo/reader',
    'simpltorchvideo.ffmpeg': 'simpltorchvideo/ffmpeg',
    'simpltorchvideo.reds': 'simpltorchvideo/reds',
    'simpltorchvideo.vimeo': 'simpltorchvideo/vimeo',
}

setup(
    name='simpltorchvideo',
    version='0.0.1',
    author='yindaheng98',
    author_email='yindaheng98@163.com',
    url='https://github.com/yindaheng98/simpltorchvideo',
    description=u'Some useful video dataset in pytorch',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir=package_dir,
    packages=[key for key in package_dir],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
