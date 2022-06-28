`import sys
import glob

import numpy as np

url1 = sys.argv[1]
url2 = sys.argv[2]

frame_file_list1 = glob.glob(url1)
frame_file_list2 = glob.glob(url2)

for i in range(len(frame_file_list1)):
    frame_file1 = open(frame_file_list1[i], "r")
    frame_file2 = open(frame_file_list2[i], "r")

    vectors1 = frame_file1.split("|")[1]
    vectors2 = frame_file2.split("|")[1]

    frame_file1.close()
    frame_file2.close()

    for j in range(len(vectors1)):
        vec1 = vectors1[j].split(",")
        vec2 = vectors2[j].split(",")