#-*- coding:utf-8 -*-
import re
import requests
import os
UrlLists=[]
for index in range(57):
    urlor = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E7%8C%AB%E5%92%AA&pn="+str((index+2)*20)
    UrlLists.append(urlor)
print(UrlLists)
j = 1
for url in UrlLists :
    html = requests.get(url).text
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 0
    for each in pic_url:
        print(each)
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue
        string = 'D:\\Cat\\Cat'+str(j)+"\\" + str(i) + '.jpg'
        fp = open(string, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
    j+=1
