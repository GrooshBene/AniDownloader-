#-*- coding: utf-8 -*-
import urllib2
import urllib

#nichijou
#
#front
#http://cdn9.ani24.moe/Nichijou/%5B%ED%95%9C%EC%83%9B-Raws%5D%20Nichijou%20-%20
#
#back
#%20%28TVA%201280x720%20x264%20AAC%29.mp4

#val = "26"
#front = "http://cdn9.ani24.moe/Nichijou/%5B%ED%95%9C%EC%83%9B-Raws%5D%20Nichijou%20-%20"
#back = "%20%28TVA%201280x720%20x264%20AAC%29.mp4"



val = input("Please input the value: ")
front = raw_input("Front : ")
back = raw_input("Back : ")

for i in range(1, val+1):
    if i<10:
        num = "0" + str(i)
        url = ""+front+num+back
    elif i>=10:
        url = ""+front+i+back
    else:
        print "fucking error"
    url = urllib.unquote(url)
    file_name = url.split('/')[-1].decode('utf-8')
    print url
    u = urllib2.urlopen(url)
    f = open(file_name,'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes : %s" %(file_name, file_size)
    
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
            
        file_size_dl += len(buffer)
        f.write(buffer)
        status = "%10d [%3.2f%%]" %(file_size_dl,file_size_dl*100./file_size)
        status = status +chr(8)*(len(status)+1)
        print status,
f.close()