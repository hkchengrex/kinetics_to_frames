from argparse import ArgumentParser
import os
from os import path

import shutil

"""
Argument parsing
"""
parser = ArgumentParser()
parser.add_argument('--path', help='Path to a folder of folders of videos')
parser.add_argument('--threshold', help='Find folders with <= [threshold] frames', default=3, type=int)
parser.add_argument('--remove', help='Remove the found folders', action='store_true')

args = parser.parse_args()

if __name__ == '__main__':

    total_weeded = 0
    all_classes = os.listdir(args.path)

    for class_name in all_classes:
        all_videos = os.listdir(path.join(args.path, class_name))
        for video_name in all_videos:
            vid_path = path.join(args.path, class_name, video_name)
            num_frames = len(os.listdir(vid_path))
            if num_frames <= args.threshold:
                if args.remove:
                    shutil.rmtree(vid_path)
                total_weeded += 1
                
    print('Done.')
    print('Total weeded: ', total_weeded)