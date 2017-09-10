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
import re

def sorted_nicely( l ): 
    """ Sort the given iterable in the way that humans expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)


s = set(['booklet', '4 sheets', '48 sheets', '12 sheets'])
for x in sorted_nicely(s):
    print(x)


mypath = "/home/mesa/data/sun3d/harvard_c11/hv_c11_2/depth"

depthfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print (onlyfiles)

f = open("/home/mesa/data/sun3d/harvard_c11/hv_c11_2/depth.txt", 'w')
num = ''
depthList = []

for x in sorted_nicely(depthfiles):
    depthList.append(x)




for i in range (0, len(depthList)):
    f.write("." + str(i) + " ./depth/" + depthList[i] + '\n')
f.close()

mypath = "/home/mesa/data/sun3d/harvard_c11/hv_c11_2/image"
rgbfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
rgbList = []
for x in sorted_nicely(rgbfiles):
    rgbList.append(x)

for i in range(0, len(rgbList)):
     im = Image.open(mypath + '/' + rgbList[i])
     s = list(rgbList[i])
     s[len(rgbList[i]) - 3] = 'p'
     s[len(rgbList[i]) - 2] = 'n'
     s[len(rgbList[i]) - 1] = 'g'
     rgbfiles[i] = "".join(s)
     im.save("/home/mesa/data/sun3d/harvard_c11/hv_c11_2/rgb/" + rgbList[i])
     im.close()


f = open("/home/mesa/data/sun3d/harvard_c11/hv_c11_2/rgb.txt", 'w')
for i in range (0, len(rgbList)):
    f.write("." + str(i) + " ./rgb/" + rgbList[i] + '\n')
f.close()

