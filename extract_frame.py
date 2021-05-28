import os
import cv2
import glob
import argparse

parser = argparse.ArgumentParser(description="video_name")
parser.add_argument('--video_name', default='video', type=str,
                    help='videos or image files')
parser.add_argument('--frame', default=6, type=int,
                    help='fpn')
args = parser.parse_args()
dir=args.video_name + '/'

frame=args.frame

video_files = glob.glob(dir + "*.mp4")

print(video_files)

if not os.path.isdir('/data'):
    os.makedirs('/data')

for video in video_files:
    file_name = video.split('/')[-1]
    save_dir = 'data/' + file_name.split('.')[0]  # data/PoseVideos\2
    video_name = save_dir.split('\\')[-1]
    print(save_dir)
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    vidcap = cv2.VideoCapture(video)

    count = 0
    while vidcap.isOpened():
        ret, image = vidcap.read()
        if not ret:
            break
        if int(vidcap.get(1)) % frame == 0:
            print('Saved from number: ' + str(int(vidcap.get(1))))
            name = save_dir + '/' +video_name + '_{0:05d}.png'.format(count)
            cv2.imwrite(name, image)
            count += 1
    vidcap.release()
