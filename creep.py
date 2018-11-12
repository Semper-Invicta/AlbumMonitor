import urllib.request
import re
import time
import datetime


while 1:
    f = open('log.txt','a')
    url = 'https://mall.video.qq.com/x/bu/rocketgirl101/album?ptag=from:weco;hd:293' 
    req = urllib.request.urlopen(url)
    html = req.read()
    html = html.decode('utf-8')
    pattern = '<span class="num">(.*?)</span><!---->'
    score = re.findall(pattern,html)
    time_stamp = datetime.datetime.now()
    result = score[0]+'\n'+time_stamp.strftime('%Y.%m.%d-%H:%M:%S')+'\n'
    print(result)
    f.write(result)
    f.close()
    time.sleep(10)
