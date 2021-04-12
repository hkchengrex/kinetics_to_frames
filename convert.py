from argparse import ArgumentParser
import os
from os import path

import cv2
from progressbar import progressbar
from multiprocessing import Pool

"""
Argument parsing
"""
parser = ArgumentParser()
parser.add_argument('--in_path', help='Path to a folder of folders of videos')
parser.add_argument('--out_path', help='Will maintain the same structure as the input')
parser.add_argument('-n', '--num_processes', default=8)
parser.add_argument('--new_min_size', help='Resize the min size to this. -1 to keep the original size.', default=224)
parser.add_argument('--sample_rate', help='Save every nth frame', default=5)

args = parser.parse_args()

def process_vid(class_vid_path):
    class_name, vid_name = class_vid_path.split('/')
    vid_in_path = path.join(args.in_path, class_name, vid_name)
    vid_out_path = path.join(args.out_path, class_name, vid_name[:-4])
    os.makedirs(vid_out_path, exist_ok=True)

    cap = cv2.VideoCapture(vid_in_path)

    idx = -1
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            cap.release()
            break
        idx += 1
        if (idx % args.sample_rate) != 0:
            continue

        if args.new_min_size > 0:
            h, w = frame.shape[:2]
            nh = h * args.new_min_size // min(h, w)
            nw = w * args.new_min_size // min(h, w)
            frame = cv2.resize(frame, (nw, nh), interpolation=cv2.INTER_LINEAR)

        cv2.imwrite(path.join(vid_out_path, '%05d.jpg' % idx), frame)


if __name__ == '__main__':

    all_classes = os.listdir(args.in_path)
    # This gives a flat list
    all_class_videos = [
        class_name+'/'+vid_name 
            for class_name in all_classes
                for vid_name in os.listdir(path.join(args.in_path, class_name))
    ]

    print('Total number of videos: ', len(all_class_videos))

    pool = Pool(processes=args.num_processes)
    for _ in progressbar(pool.imap_unordered(process_vid, all_class_videos), max_value=len(all_class_videos)):
        pass

    print('Done.')