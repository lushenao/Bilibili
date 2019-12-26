#__auth__:"Sky lu"
# -*- coding:utf-8 -*-
# coding=utf-8
import requests,os,re
import os,sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Bilibili(object):
    def __init__(self,search_name,pages):
        self.search_name = search_name
        self.pages = pages

    def download(self):
        video_path = BASE_DIR  # 视频保存在程序存放路径
        for page in range(0,int(self.pages)):#翻页循环
            url = ('https://search.bilibili.com/all?keyword='+self.search_name+'&single_column=0&page='+str(page+1)) #翻页循环设定
            r = requests.get(url)#GET请求访问网页
            content = r.text#解析网页源码
            links = re.findall(r'www.bilibili.com/video/av\d+',content)#使用正则表达式从源码中找到所有视频地址
            for link in links:#循环下载所有链接
                print(link)
                os.system('you-get -o %s %s' % (video_path,link))#调用you-get方法挨个下载该次循环的所有视频

if __name__ == '__main__':
    search_name = input('\033[32;1m您想要爬取的视频关键字是？\n\033[37;1m(输入完毕请按回车)：\033[0m')
    pages = input('\033[32;1m您想要爬取总页数？\n\033[37;1m(输入完毕请按回车)：\033[0m')
    Bilibili(search_name,pages).download()


