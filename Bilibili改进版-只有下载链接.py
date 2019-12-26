#__auth__:"Sky lu"
# -*- coding:utf-8 -*-

#__auth__:"Sky lu"
# -*- coding:utf-8 -*-
# coding=utf-8
import requests,re
import os,sys,json


class Bilibili(object):
    def __init__(self,search_name,pages):
        self.search_name = search_name
        self.pages = pages

    def download(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # 视频保存在程序存放路径
        for page in range(0,int(self.pages)):#翻页循环
            url = ('https://search.bilibili.com/all?keyword=' + search_name + '&single_column=0&page=' + str(1))
            r = requests.get(url)  # GET请求访问网页
            content = r.text  # 解析网页源码
            content = content.replace(' ', '').replace('\n', '')  # 去除html的空格和换行
            # print(content)
            video_list = str(content).split('video-itemmatrix')  # 以video的项目模型为分界分割html文本
            #print(video_list)

            for i in video_list:
                video_dict = {
                    '标题': 0,
                    '链接': 0,
                    '播放量': 0,
                    '弹幕数': 0,
                    '上传时间': 0

                }  # 初始化video字典
                try:
                    links = re.search(r'www.bilibili.com/video/av\d+', i).group()
                    title = re.findall(r'</span><atitle="(.*?)"href=', i)
                    title = " ".join(str(i) for i in title)
                    view_counts = re.findall(r'<iclass="icon-playtime"></i>(.*?)</span>', i)
                    view_counts = " ".join(str(i) for i in view_counts)
                    bullet_screen_counts = re.findall(r'<iclass="icon-subtitle"></i>(.*?)</span>', i)
                    bullet_screen_counts = " ".join(str(i) for i in bullet_screen_counts)
                    uptime = re.findall(r'<iclass="icon-date"></i>(.*?)</span>', i)
                    uptime = " ".join(str(i) for i in uptime)
                except:
                    continue
                if not os.path.isfile(BASE_DIR + str(title)):
                    f = open(BASE_DIR + '/'+search_name+'.json', 'a')
                    video_dict['标题'] = str(title)
                    video_dict['链接'] = str(links)
                    video_dict['播放量'] = str(view_counts)
                    video_dict['弹幕数'] = str(bullet_screen_counts)
                    video_dict['上传时间'] = str(uptime)
                    f.writelines(json.dumps(video_dict, ensure_ascii=False) + '\n')
                    f.close()
                else:
                    continue
            print('\033[32;1m第%s页%s视频信息爬取完成...\033[0m' % (page,search_name))
        print('\033[32;1m所有%s视频爬取完成,文件保存在\n%s\n目录下\033[0m' %(search_name,BASE_DIR))


if __name__ == '__main__':
    search_name = input('\033[32;1m您想要爬取的视频关键字是？\n\033[37;1m(输入完毕请按回车)：\033[0m')
    pages = input('\033[32;1m您想要爬取总页数？\n\033[37;1m(输入完毕请按回车)：\033[0m')
    Bilibili(search_name,pages).download()


