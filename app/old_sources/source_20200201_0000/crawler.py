import json
import time
import requests
from bs4 import BeautifulSoup
from module.logger import logger
from module import functions  as fn
import os

date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
time = time.strftime('%H:%M:%S', time.localtime(time.time()))

base_dir = os.path.dirname( os.path.abspath( __file__ ) ) +"/files/"

file_keyword = base_dir+"result_"+date +".txt"
file_news = base_dir+"result_news_"+date +".txt"

header = "target\tdate\ttime\trank\tkeyword\turls\n"
header_news = "target\tdate\ttime\trank\ttitle\tcontents\turls\n"


#files = [ base_dir+"naver_"+date +".txt"
#          , base_dir+"daum_"+date +".txt"
#          , base_dir+"youtube_"+date +".txt" ]

#headers = ["target\tdate\ttime\trank\tkeyword\turls\n"
#           ,"target\tdate\ttime\trank\tkeyword\turls\n"
#           ,"target\tdate\ttime\trank\tkeyword\turls\n" ]

target_code = [ '01' #naver realtime keyword
               ,'02' #daum realtime keyword
               ,'03' #youtube
               ,'04' #daum rank news
              ]

urls = [ "https://www.naver.com/srchrank?frm=main&ag=all&gr=1&ma=-2&si=0&en=0&sp=0" #naver_url
         , "https://www.daum.net" #daum_url
         , "https://www.youtube.com/feed/trending" #youtube
         , "https://media.daum.net/ranking/popular/" #daum rank news
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


def setKeywordHeader():
    logger.info("----------setKeywordHeader()----------")
    if os.path.exists(file_keyword):
        logger.info("Header Already set ")

    else:
        logger.info("Header Setting")
        f = open(file_keyword, mode='wt', encoding='UTF-8')
        f.write(header)
        f.close()

def setNewsHeader():
    logger.info("----------setNewsHeader()----------")
    if os.path.exists(file_news):
        logger.info("Header Already set ")

    else:
        logger.info("Header Setting")
        f = open(file_news, mode='wt', encoding='UTF-8')
        f.write(header_news)
        f.close()




def getNaverKeyword() :
    logger.info("----------getNaverKeyword()----------")
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


def getDaumKeyword() :
    logger.info("----------getDaumKeyword()----------")
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

def getYoutubeKeyword():
    logger.info("----------getYoutubeKeyword()----------")

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




def getResultKeywordFile():
    logger.info("----------getResultKeywordFile()----------")
    getDatas = [getDaumKeyword(), getNaverKeyword(), getYoutubeKeyword()]
    setKeywordHeader()

    logger.info("make file - file path : "+file_keyword)
    f = open(file_keyword, mode='a', encoding='UTF-8')
    for i,v in enumerate(getDatas):
        logger.info('write data - write num : '   +  str(i))
        f.writelines(v)
    logger.info('succ make file')
    f.close()

def getResultNewsFile():
    logger.info("----------getResultNewsFile()----------")
    getDatas = [getDaumNews()]
    setKeywordHeader()
    setNewsHeader()


    logger.info("make file - file path : "+file_news)

    f = open(file_news, mode='a', encoding='UTF-8')
    for i,v in enumerate(getDatas):
        logger.info('write data - write num : '   +  str(i))
        f.writelines(v)
    logger.info('succ make file')
    f.close()


def getDaumNews():
    logger.info("----------getDaumNews()----------")
    source = requests.get(urls[3]).text
    soup = BeautifulSoup(source, 'html.parser')
    elem_list_title = soup.select("div.cont_thumb .tit_thumb a")
    elem_list_desc = soup.select("div.cont_thumb .desc_thumb span")

    titles = []
    descs = []
    datas = []
    for i, v in enumerate(elem_list_title):
        titles.append(v.text + '\t' + v.attrs['href'])
        # print(v.text+'\t'+v.attrs['href'])

    for i, v in enumerate(elem_list_desc):
        descs.append(v.text.strip())

    fn.aryLenSync(titles, descs)

    for i, v in enumerate(titles):
        datas.append('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(target_code[3], date, time, str(i + 1).zfill(2), titles[i].split('\t')[0], descs[i], titles[i].split('\t')[1]))
        logger.debug('%s\t%s\t%s\t%s\t%s\t%s\t%s' %( target_code[3], date, time, str(i + 1).zfill(2), titles[i].split('\t')[0] , descs[i], titles[i].split('\t')[1]))

    return datas