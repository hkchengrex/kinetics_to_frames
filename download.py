import urllib.request
import shutil
import os

if __name__=="__main__":
    with open('k700_2020_train_path.txt') as f:
        vid_list = f.readlines()
    vid_list = [x.strip() for x in vid_list]
    for vid_name in vid_list:
        if os.path.exists(vid_name):
            continue
        url = vid_name
        file_name = os.path.join('output', os.path.basename(url))
        print(file_name)
        # the file from `url` and save it locally under `file_name`:
        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
