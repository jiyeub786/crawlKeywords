import os
import time

dateN = time.strftime('%Y-%m-%d', time.localtime(time.time()))
hourN = time.strftime('%H:%M:%S', time.localtime(time.time()))
dir =os.path.dirname( os.path.abspath( __file__ ) ) +"/static/files/result_2020-03-06.txt"
base_dir = os.path.dirname( os.path.abspath( __file__ ) ) +"/files/"
file_keyword = base_dir + "result_" +dateN + ".txt"
file_news = base_dir + "result_news_" + dateN + ".txt"


def getFile () :
    f = open(dir, mode='r', encoding='UTF-8')
    filedata = f.readlines()
    f.close()

    datas =[]
    for i, v in enumerate(filedata):
        datas.append(v.replace('\n', '').split('\t'))

    return datas


