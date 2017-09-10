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

def sorted_nicely( l ):   #code from https://stackoverflow.com/questions/2669059/how-to-sort-alpha-numeric-set-in-python
    """ Sort the given iterable in the way that humans expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

print("Example: /home/mesa/mighty/png_to_klg/Datasets/mit_76_studyroom/76-1studyroom2/")
path = input("Please enter file path: ")

mypath = path + "/depth"
#"/home/mesa/mighty/png_to_klg/Datasets/mit_76_studyroom/76-1studyroom2/depth"

depthfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print (onlyfiles)

f = open(path + "/depth.txt", 'w')
num = ''
depthList = []

for x in sorted_nicely(depthfiles):
    depthList.append(x)




for i in range (0, len(depthList)):
    f.write("." + str(i) + " ./depth/" + depthList[i] + '\n')
f.close()

mypath = path + "image"
rgbfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
rgbList = []
for x in sorted_nicely(rgbfiles):
    rgbList.append(x)

os.makedirs(path + "rgb/")      #credit: https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
for i in range(0, len(rgbList)):
     im = Image.open(mypath + '/' + rgbList[i])
     s = list(rgbList[i])
     s[len(rgbList[i]) - 3] = 'p'
     s[len(rgbList[i]) - 2] = 'n'
     s[len(rgbList[i]) - 1] = 'g'
     rgbfiles[i] = "".join(s)
     #print(s)
     
     print(str(i + 1))
     im.save(path + "/rgb/" + rgbfiles[i])
     im.close()

f = open(path + "/rgb.txt", 'w')
for i in range (0, len(rgbList)):
    f.write("." + str(i) + " ./rgb/" + rgbfiles[i] + '\n')
f.close()

