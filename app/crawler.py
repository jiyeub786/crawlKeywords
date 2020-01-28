import json
import time
import requests
from bs4 import BeautifulSoup
from module.logger import logger
import os

date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
time = time.strftime('%H:%M:%S', time.localtime(time.time()))

base_dir = os.path.dirname( os.path.abspath( __file__ ) ) +"/files/"

file = base_dir+"result_"+date +".txt"
header = "target\tdate\ttime\trank\tkeyword\turls\n"

#files = [ base_dir+"naver_"+date +".txt"
#          , base_dir+"daum_"+date +".txt"
#          , base_dir+"youtube_"+date +".txt" ]

#headers = ["target\tdate\ttime\trank\tkeyword\turls\n"
#           ,"target\tdate\ttime\trank\tkeyword\turls\n"
#           ,"target\tdate\ttime\trank\tkeyword\turls\n" ]

target_code = [ '01' #naver realtime keyword
               ,'02' #daum realtime keyword
               ,'03' #youtube
              ]

urls = [ "https://www.naver.com/srchrank?frm=main&ag=all&gr=1&ma=-2&si=0&en=0&sp=0" #naver_url
         , "https://www.daum.net" #daum_url
         , "https://www.youtube.com/feed/trending" #youtube
     ]

#def setHeaders():
#    logger.info("setHeader")
#    for i, f in enumerate(files):
#        if os.path.exists(f):
#            i
#        else:
#            logger.info("setHeader-files"+files[i])
#            logger.info("setHeader-files"+headers[i])
#            #f = open(files[i], mode='wt')
#            f = open(files[i], mode='wt', encoding='UTF-8')
#            f.write(headers[i])
#            f.close()


def setHeader():
    logger.info("----------setHeader()----------")
    if os.path.exists(file):
        logger.info("Header Already set ")

    else:
        logger.info("Header Setting")
        f = open(file, mode='wt', encoding='UTF-8')
        f.write(header)
        f.close()




def getNaver() :
    logger.info("----------getNaver()----------")
    logger.info("get Source Datas")
    source = requests.get(urls[0]).text
    jsonObject = json.loads(str(source));
    data = jsonObject['data']

    logger.info("parsing Datas")
    datas =[]
    for i,v in enumerate(data):

        datas.append("%s\t%s\t%s\t%s\t%s\t%s\n" % (target_code[0], date, time, str(i+1).zfill(2), v['keyword'] ,'https://search.naver.com/search.naver?where=nexearch&query=' +v['keyword'] ))
        logger.debug("%s\t%s\t%s\t%s\t%s\t%s" % (target_code[0],date,time, str(i+1).zfill(2) , v['keyword'],'https://search.naver.com/search.naver?where=nexearch&query=' +v['keyword'] ))
    logger.info('succ pasrsing')
    return datas


def getDaum() :
    logger.info("----------getDaum()----------")
    logger.info("get Source Datas")
    source = requests.get(urls[1]).text
    soup = BeautifulSoup(source, 'html.parser')
    elem_list = soup.select(".list_mini .rank_cont .link_issue")
    searchword_list = []
    for elem in elem_list:
        searchword_list.append(elem.get_text())

    logger.info("parsing Datas")
    datas =[]
    for i,v in enumerate(searchword_list):
        datas.append("%s\t%s\t%s\t%s\t%s\t%s\n"  % (target_code[1],date, time, str(i+1).zfill(2), v ,'https://search.daum.net/search?w=tot&q='+v))
        logger.debug("%s\t%s\t%s\t%s\t%s\t%s"  % (target_code[1],date, time, str(i+1).zfill(2), v,'https://search.daum.net/search?w=tot&q='+v))
    logger.info('succ pasrsing')
    return datas

def getYoutube():
    logger.info("----------getYoutube()----------")

    logger.info("get Source Datas")
    source = requests.get(urls[2]).text
    soup = BeautifulSoup(source, 'html.parser')
    elem_list = soup.select("h3.yt-lockup-title > a ")

    logger.info("parsing Datas")
    datas = []
    for i, v in enumerate(elem_list):
        if 'title' in v.attrs:
            datas.append("%s\t%s\t%s\t%s\t%s\t%s\n" % (target_code[2],date,time,str(i+1).zfill(2), v.attrs['title'], "https://www.youtube.com" + v.attrs['href']))
            logger.debug("%s\t%s\t%s\t%s\t%s\t%s" % (target_code[2],date,time,str(i+1).zfill(2), v.attrs['title'], "https://www.youtube.com" + v.attrs['href']))
    logger.info('succ pasrsing')
    return datas




def getResultFile():
    logger.info("----------getResultFile()----------")
    getDatas = [getDaum(), getNaver(), getYoutube()]
    setHeader()

    logger.info("make file - file path : "+file)
    f = open(file, mode='a', encoding='UTF-8')
    for i,v in enumerate(getDatas):
        logger.info('write data - write num : '   +  str(i))
        f.writelines(v)
    logger.info('succ make file')
    f.close()
