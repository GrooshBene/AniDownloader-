#2016. 1. 8 Made By GrooshBene

import pymongo
import sys
from pymongo import MongoClient
import glob
import os
from os import path
import time


client = MongoClient("mongodb://localhost")
db = client.ani24
ani = db.ani
video = db.video
id = 0
aniid = 0

tree = glob.glob('*')
for i in tree:
    dirtree = glob.glob(os.path.abspath(i) + '/*.txt')
    for j in dirtree:
        a = os.path.basename(j.decode('utf-8')).split('-')
        date = time.time()
        aniDoc = {'_id' : aniid, 'title' : a[0]}
        videoDoc = {'_id' : id , 'aniid' : aniid ,'subtitle' : a[-1], 'time' : int(date)}
        id += 1
        try:
            ani.insert(aniDoc)
        except:
            print "Ani Insert Error", sys.exc_info()[0]
        try:
            video.insert(videoDoc)
        except:
            print "Video Insert Error", sys.exc_info()[0]
    aniid += 1