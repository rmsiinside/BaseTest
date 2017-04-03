#-*- coding:utf-8 -*-
import re
import requests
import os
UrlLists=[]
for index in range(57):
    url = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E7%8C%AB%E5%92%AA&pn="+str((index+1)*20)+"$gsm=0"
    UrlLists.append(url)
print(UrlLists)