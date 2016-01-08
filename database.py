#2016. 1. 8 Made By GrooshBene

import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.ani24
ani_col = db.adi
video_col = db.video