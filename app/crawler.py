import json
import requests
from bs4 import BeautifulSoup
from module.logger import logger
from module import functions  as fn
import os
import main as m


base_dir = os.path.dirname( os.path.abspath( __file__ ) ) +"/files/"

file_keyword = base_dir+"result_"+ m.globalDate +".txt"
file_news = base_dir+"result_news_"+m.globalDate +".txt"

header_keyword = "target\tdate\ttime\trank\tkeyword\turls\n"
header_news = "target\tdate\ttime\trank\ttitle\tcontents\turls\n"

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

def setKeywordHeader():
    logger.info("----------setKeywordHeader()----------")
    if os.path.exists(file_keyword):
        logger.debug("Header Already set ")

    else:
        logger.debug("Header Setting")
        f = open(file_keyword, mode='wt', encoding='UTF-8')
        f.write(header_keyword)
        f.close()

def setNewsHeader():
    logger.info("----------setNewsHeader()----------")
    if os.path.exists(file_news):
        logger.debug("Header Already set ")

    else:
        logger.debug("Header Setting")
        f = open(file_news, mode='wt', encoding='UTF-8')
        f.write(header_news)
        f.close()

def getNaverKeyword() :
    logger.info("----------getNaverKeyword()----------")
    logger.debug("get Source Datas")
    source = requests.get(urls[0]).text
    jsonObject = json.loads(str(source));
    data = jsonObject['data']

    logger.debug("parsing Datas")
    datas =[]

    for i,v in enumerate(data):

        datas.append("%s\t%s\t%s\t%s\t%s\t%s\n" % (target_code[0], m.globalDate, m.globalTime, str(i+1).zfill(2), v['keyword'] ,'https://search.naver.com/search.naver?where=nexearch&query=' +v['keyword'] ))
        logger.debug("%s\t%s\t%s\t%s\t%s\t%s" % (target_code[0],m.globalDate,m.globalTime, str(i+1).zfill(2) , v['keyword'],'https://search.naver.com/search.naver?where=nexearch&query=' +v['keyword'] ))
    logger.debug('succ pasrsing')
    return datas

def getDaumKeyword() :
    logger.info("----------getDaumKeyword()----------")
    logger.debug("get Source Datas")
    source = requests.get(urls[1]).text
    soup = BeautifulSoup(source, 'html.parser')
    elem_list = soup.select(".list_mini .rank_cont .link_issue")
    searchword_list = []
    for elem in elem_list:
        searchword_list.append(elem.get_text())

    logger.debug("parsing Datas")
    datas =[]
    for i,v in enumerate(searchword_list):
        datas.append("%s\t%s\t%s\t%s\t%s\t%s\n"  % (target_code[1],m.globalDate, m.globalTime, str(i+1).zfill(2), v ,'https://search.daum.net/search?w=tot&q='+v))
        logger.debug("%s\t%s\t%s\t%s\t%s\t%s"  % (target_code[1],m.globalDate, m.globalTime, str(i+1).zfill(2), v,'https://search.daum.net/search?w=tot&q='+v))
    logger.debug('succ pasrsing')
    return datas

def getYoutubeKeyword():
    logger.info("----------getYoutubeKeyword()----------")

    logger.debug("get Source Datas")
    source = requests.get(urls[2]).text
    soup = BeautifulSoup(source, 'html.parser')
    elem_list = soup.select("h3.yt-lockup-title > a ")

    logger.debug("parsing Datas")
    datas = []
    for i, v in enumerate(elem_list):
        if 'title' in v.attrs:
            datas.append("%s\t%s\t%s\t%s\t%s\t%s\n" % (target_code[2],m.globalDate,m.globalTime,str(i+1).zfill(2), v.attrs['title'], "https://www.youtube.com" + v.attrs['href']))
            logger.debug("%s\t%s\t%s\t%s\t%s\t%s" % (target_code[2],m.globalDate,m.globalTime,str(i+1).zfill(2), v.attrs['title'], "https://www.youtube.com" + v.attrs['href']))
    logger.debug('succ pasrsing')
    return datas

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
        datas.append('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(target_code[3], m.globalDate, m.globalTime, str(i + 1).zfill(2), titles[i].split('\t')[0], descs[i], titles[i].split('\t')[1]))
        logger.debug('%s\t%s\t%s\t%s\t%s\t%s\t%s' %( target_code[3], m.globalDate, m.globalTime, str(i + 1).zfill(2), titles[i].split('\t')[0] , descs[i], titles[i].split('\t')[1]))

    return datas

def getResultKeywordFile():
    logger.info("----------getResultKeywordFile()----------")
    m.setTime()

    getDatas = [getDaumKeyword(), getNaverKeyword(), getYoutubeKeyword()]
    setKeywordHeader()

    logger.debug("make file - file path : "+file_keyword)
    f = open(file_keyword, mode='a', encoding='UTF-8')
    for i,v in enumerate(getDatas):
        logger.debug('write data - write num : '   +  str(i))
        f.writelines(v)
    logger.debug('succ make file')
    f.close()

def getResultNewsFile():
    logger.info("----------getResultNewsFile()----------")

    m.setTime()
    getDatas = [getDaumNews()]
    setKeywordHeader()
    setNewsHeader()


    logger.debug("make file - file path : "+file_news)

    f = open(file_news, mode='a', encoding='UTF-8')
    for i,v in enumerate(getDatas):
        logger.debug('write data - write num : '   +  str(i))
        f.writelines(v)
    logger.debug('succ make file')
    f.close()
