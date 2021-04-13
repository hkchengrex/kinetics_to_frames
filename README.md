# Kinetics to frames

Convert kinetics datasets (or other video datasets) to frames. Support resizing and temporal sampling for space efficiency.

## Requirement

- OpenCV
- progressbar2

## Usage

`python convert.py --in_path [path_to_kinetics_root] --out_path [output_path] -n [number_of_processes] --min_size [Length of the minimum side, -1 to disable resizing] --sample_rate [temporal sampling rate]`

Use `python weed.py --path [output_path] --remove` to remove empty folders.

## Note

Converting Kinetics 700 to frames with the default setting yields a dataset that is only slightly (10%?) larger than the original video format.

Good to know.

## Downloading

You can download the Kinetics 700 dataset here: https://github.com/cvdfoundation/kinetics-dataset. Oh my god I love them.

See also `download.py` (I copied it somewhere but I forgot where).