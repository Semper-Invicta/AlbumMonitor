#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']

f = open('log.txt','r')
x=[]
y=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
cnt = 0
iteration = 0
title = ''
for line in f:
	line = line.strip('\n')
	if ((cnt % 21) != 0):
		y[cnt % 21 - 1].append(line)
	else:
		iteration += 1
		x.append(iteration)
		last = line
		if (iteration == 1):
			title += line + ' — '
	cnt+=1
title += last
#color = ['#FF0000','#00FF00','#0000FF','#FFFF00','#FF00FF','#00FFFF','#7F0000','#007F00','#00007F','#FF7F00','#FF007F','#00FF7F','#7FFF00','#007FFF','#7F00FF','#7F7F00','#007F7F','#7F007F','#000000','#7F7F7F']
color = ['#F32938','#003E73','#8ED400','#F5AA00','#407631','#8CDEE4','#E81B75','#00C58E','#006956','#AB1455','#B080D0','#E3ABD7','#003847','#FF5A00','#FD94AB','#810262','#E51A9B','#EF8200','#FED900','#682D86']
cites = ['广州','南京','杭州','郑州','济南','青岛','长沙','厦门','福州','武汉','沈阳','大连','合肥','石家庄','南昌','重庆','南宁','西安','太原','哈尔滨']

plt.figure(dpi=300)
plt.title(title)
for i in range(20):
	a = np.array(y[i]).astype(np.float)
	plt.plot(x, a, color=color[i], label=cites[i])
plt.legend(loc=2, bbox_to_anchor=(0.94,1.0),ncol=1)
plt.savefig('plot.png')


