#!usr/bin/python
# MIT data doesn't provide the list of depth/rgb files to create the associates
# folder
# This script will convert the jpg files to png in the 'image' folder' and then
# create the depth.txt and rgb.txt

from __future__ import print_function
import os
from os import listdir
from os.path import isfile, join
import Image

mypath = "/home/mesa/data/sun3d/harvard_c11/hv_c11_2/depth"

depthfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print (onlyfiles)

f = open("/home/mesa/data/sun3d/harvard_c11/hv_c11_2/depth.txt", 'w')
for i in range (0, len(depthfiles)):
    f.write("." + str(i) + " ./depth/" + depthfiles[i] + '\n')
f.close()

mypath = "/home/mesa/data/sun3d/harvard_c11/hv_c11_2/image"
rgbfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for i in range(0, len(rgbfiles)):
     im = Image.open(mypath + '/' + rgbfiles[i])
     s = list(rgbfiles[i])
     s[len(rgbfiles[i]) - 3] = 'p'
     s[len(rgbfiles[i]) - 2] = 'n'
     s[len(rgbfiles[i]) - 1] = 'g'
     rgbfiles[i] = "".join(s)
     im.save("/home/mesa/data/sun3d/harvard_c11/hv_c11_2/rgb/" + rgbfiles[i])
     im.close()



f = open("/home/mesa/data/sun3d/harvard_c11/hv_c11_2/rgb.txt", 'w')
for i in range (0, len(rgbfiles)):
    f.write("." + str(i) + " ./rgb/" + rgbfiles[i] + '\n')
f.close()
