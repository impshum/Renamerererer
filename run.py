import os
from random import shuffle

script_dir = os.path.dirname(__file__)
dir1_path = 'test1/'
dir2_path = 'test2/'
new_filenames_path = 'new_filenames.txt'
new_filenames = os.path.join(script_dir, new_filenames_path)
dir1 = os.path.join(script_dir, dir1_path)
dir2 = os.path.join(script_dir, dir2_path)
ext = '.PAC'

with open(new_filenames) as f:
    fnames = f.readlines()


def rename(re1, re2):
    file_list = os.listdir(re1)
    files = []

    for file in file_list:
        files.append(file)

    shuffle(files)
    shuffle(fnames)

    for x, y in zip(files, fnames):
        a = re1 + x
        b = re2 + y + ext
        os.rename(a, b)

    print(str(len(fnames)) + '/' + str(len(files)))


rename(dir1, dir2)
rename(dir2, dir1)
