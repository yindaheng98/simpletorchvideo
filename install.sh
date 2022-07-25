#!/bin/sh
rm -rf venv
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu116 -i https://pypi.tuna.tsinghua.edu.cn/simple

wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
tar -C venv/bin -xvf ffmpeg-release-amd64-static.tar.xz --strip-components=1
