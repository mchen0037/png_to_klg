#!/usr/bin/python

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

print("Example: '/home/mesa/mighty/png_to_klg/Datasets/Stanford/apt0/'")
mypath = input("Please enter file path: ")

os.makedirs(mypath + "image/")
os.makedirs(mypath + "depth/")
os.makedirs(mypath + "text/")

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
filesList = []
for x in sorted_nicely(files):
    filesList.append(x)

for i in range(0, len(filesList)):
    s = list(filesList[i])
    if s[len(filesList[i]) - 3] == 'p':
        string = mypath + str(filesList[i])
        #print(string)
        os.rename(mypath + str(filesList[i]), mypath + "depth/" + str(filesList[i]))
    elif s[len(filesList[i]) - 3] == 'j':
        string = mypath + str(filesList[i])
        print(string)
        os.rename(mypath + str(filesList[i]), mypath + "image/" + str(filesList[i]))
    elif s[len(filesList[i]) - 3] == 't':
        string = mypath + str(filesList[i])
        print(string)
        os.rename(mypath + str(filesList[i]), mypath + "text/" + str(filesList[i]))
    
        
#################################################################################

path = mypath

mypath = mypath + "depth"
#"/home/mesa/mighty/png_to_klg/Datasets/mit_76_studyroom/76-1studyroom2/depth"

depthfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

f = open(path + "depth.txt", 'w')
num = ''
depthList = []
print(">>>>>>>>>>" + mypath)

for x in sorted_nicely(depthfiles):
    depthList.append(x)




for i in range (0, len(depthList)):
    f.write(str(i) + " ./depth/" + depthList[i] + '\n')
f.close()

mypath = path + "image"
print(" >>>>>>>>>>>>>>>" + mypath)
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
    f.write(str(i) + " ./rgb/" + rgbfiles[i] + '\n')
f.close()
