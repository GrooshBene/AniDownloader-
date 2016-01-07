#!/usr/bin/python

import MySQLdb

fileUrl = "/Volumes/Seagate Backup Plus Drive/Projects/AniDownloader-/test"

fileFormat = ".txt"
val = input("Plz Input the Value : ")

db = MySQLdb.connect("localhost", "root", "wltn6705", "pythontest")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE FILES (
         id INT,
         subtitle   CHAR(100),
         date   INT
)"""

cursor.execute(sql)
for i in range(0,val):
    record = "INSERT INTO FILES(id,subtitle, date) VALUES ('%d', '%s', '%d')" % (i, fileUrl + (i+1) + fileFormat, new Date());
    try:
        cursor.execute(record)
        db.commit()
    except:
        db.rollback()
db.close()