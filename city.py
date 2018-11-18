import urllib.request
import re
import time
import datetime

while 1:
    f = open('log.txt','a')
    url = 'http://panshi.qq.com/v2/vote/23212312?source=1&_=1542523645175&callback=Zepto1542523645036' 
    req = urllib.request.urlopen(url)
    html = req.read()
    html = html.decode('utf-8')
    pattern = '"selected":(.*?)}'
    score = re.findall(pattern,html)
    time_stamp = datetime.datetime.now()
    result = time_stamp.strftime('%Y.%m.%d-%H:%M:%S')+'\n'
    for i in range(20):
    	result = result + score[i] + '\n'
    print(result)
    f.write(result)
    f.close()
    time.sleep(10)