import os
import argparse

import cv2
import numpy as np
from glob import glob


parser = argparse.ArgumentParser(description="tracking demo")
parser.add_argument('--video_name', default='data/video/test', type=str,
                    help='videos or image files')
args = parser.parse_args()
root=args.video_name

print(root)

def get_frames(video_name):
    images = glob(os.path.join(video_name, '*.png*'))
    images = sorted(images, key=lambda x: x.split('/')[-1].split('.')[0])
        # key=lambda x: int(x.split('/')[-1].split('.')[0]))
    for img in images:
        frame = cv2.imread(img)
        yield frame

def main():
    name = root.split('/')[-1].split('.')[0]
    for fram in get_frames(root):
        cv2.imshow(name, fram)
        cv2.waitKey(40)

if __name__=="__main__":
    main()