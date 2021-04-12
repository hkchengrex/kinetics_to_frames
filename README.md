# Kinetics to frames

Convert kinetics datasets (or other video datasets) to frames. Support resizing and temporal sampling for space efficiency.

## Requirement

- OpenCV
- progressbar2

## Usage

`python convert.py --in_path [path_to_kinetics_root] --out_path [output_path] -n [number_of_processes] --min_size [Length of the minimum side, -1 to disable resizing] --sample_rate [temporal sampling rate]`
