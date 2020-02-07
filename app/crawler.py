
from urllib import parse
import json
import requests
from bs4 import BeautifulSoup
from module.logger import logger
from module import functions  as fn
import os
import time

globalDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
globalTime = time.strftime('%H:%M:%S', time.localtime(time.time()))

def setTime():
    global globalTime
    global globalDate
    globalDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    globalTime = time.strftime('%H:%M:%S', time.localtime(time.time()))

base_dir = os.path.dirname( os.path.abspath( __file__ ) ) +"/files/"

file_keyword = base_dir+"result_"+ globalDate +".txt"
file_news = base_dir+"result_news_"+globalDate +".txt"

header_keyword = "target\tdate\ttime\trank\tkeyword\turls\n"
header_news = "target\tdate\ttime\trank\ttitle\tcontents\turls\n"

target_code = { 'keyword_naver1': '01-1'
                ,'keyword_naver2': '01-2'
                ,'keyword_naver3': '01-3'
                ,'keyword_daum1' : '02-1'
                ,'keyword_daum2' : '02-2'
                ,'keyword_daum3' : '02-3'
                ,'keyword_daum4' : '02-4'
                ,'keyword_youtube' : '03'
                ,'news_daum' : '04'
                }

target_url = { "keyword_naver1" : "https://www.naver.com/srchrank?frm=main&ag=all&gr=1&ma=-2&si=0&en=0&sp=0" #naver_url1
              ,"keyword_naver2" : "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=" #naver url2
              ,"keyword_daum1" : "https://www.daum.net" #daum_url1
              ,"keyword_daum2" : "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=" #daum_url2
              ,"keyword_youtube" : "https://www.youtube.com/feed/trending" #youtube
              ,"news_daum" : "https://media.daum.net/ranking/popular/" #daum rank news
               }

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
    source1 = requests.get(target_url['keyword_naver1']).text
    jsonObject = json.loads(str(source1));
    data = jsonObject['data']

    source2 = requests.get(target_url['keyword_naver2']).text
    soup2 = BeautifulSoup(source2, 'html.parser')
    elem_list2 = soup2.select(".realtime_srch .lst_realtime_srch li .tit")

    searchword_list = []
    for i,v in enumerate(data):
        searchword_list.append( fn.getConvData(v['keyword']))
    for i,v in enumerate(elem_list2):
        if i <40 :
            searchword_list.append( fn.getConvData(v.get_text()))

    logger.debug("parsing Datas")
    datas =[]
    for i, v in enumerate(searchword_list):
        if i +1 <=20 and i + 1 >0 :
            datas.append("%s\t%s\t%s\t%s\t%s\t%s\n" % (target_code['keyword_naver1'], globalDate, globalTime, str(i + 1).zfill(2), v,'https://search.naver.com/search.naver?where=nexearch&query=' + fn.getEncodeUrl(v)))
            logger.debug("%s\t%s\t%s\t%s\t%s\t%s" % (target_code['keyword_naver1'], globalDate, globalTime, str(i + 1).zfill(2), v,'https://search.naver.com/search.naver?where=nexearch&query=' + fn.getEncodeUrl(v)))
        if i +1 <=30 and i + 1 >20:
            datas.append("%s\t%s\t%s\t%s\t%s\t%s\n" % (target_code['keyword_naver2'], globalDate, globalTime, str(i + 1 - 20).zfill(2), v,'https://search.naver.com/search.naver?where=nexearch&query=' + fn.getEncodeUrl(v)))
            logger.debug("%s\t%s\t%s\t%s\t%s\t%s" % (target_code['keyword_naver2'], globalDate, globalTime, str(i + 1 - 20).zfill(2), v,'https://search.naver.com/search.naver?where=nexearch&query=' + fn.getEncodeUrl(v)))
        if i +1 <=40 and i + 1 >30:
            datas.append("%s\t%s\t%s\t%s\t%s\t%s\n" % (target_code['keyword_naver3'], globalDate, globalTime, str(i + 1 -30).zfill(2), v,'https://search.naver.com/search.naver?where=nexearch&query=' + fn.getEncodeUrl(v)))
            logger.debug("%s\t%s\t%s\t%s\t%s\t%s" % (target_code['keyword_naver3'], globalDate, globalTime, str(i + 1 -30).zfill(2), v,'https://search.naver.com/search.naver?where=nexearch&query=' + fn.getEncodeUrl(v)))

    logger.debug('succ pasrsing')
    return datas

def getDaumKeyword() :

    logger.info("----------getDaumKeyword()----------")
    logger.debug("get Source Datas")
    source1 = requests.get(target_url['keyword_daum1']).text
    source2 = requests.get(target_url['keyword_daum2']).text
    soup1 = BeautifulSoup(source1, 'html.parser')
    soup2 = BeautifulSoup(source2, 'html.parser')
    elem_list1 = soup1.select(".list_mini .rank_cont .link_issue")
    elem_list2 = soup2.select("#daumWrap #daumContent #mAside #ratNewsCollDetail .keyword_rank .link_txt")

    searchword_list = []
    for i,v in enumerate(elem_list1):
        searchword_list.append(fn.getConvData(v.get_text()))
    for i,v in enumerate(elem_list2):
        searchword_list.append(fn.getConvData(v.get_text()))

    logger.debug("parsing Datas")
    datas =[]
    for i,v in enumerate(searchword_list):
        if i + 1 <= 10 and i + 1 > 0:
            datas.append("%s\t%s\t%s\t%s\t%s\t%s\n" % (target_code['keyword_daum1'], globalDate, globalTime, str(i + 1).zfill(2), v,'https://search.daum.net/search?w=tot&q=' + fn.getEncodeUrl(v)))
            logger.debug("%s\t%s\t%s\t%s\t%s\t%s" % (target_code['keyword_daum1'], globalDate, globalTime, str(i + 1).zfill(2), v,'https://search.daum.net/search?w=tot&q=' + fn.getEncodeUrl(v)))
        if i + 1 <= 20 and i + 1 > 10:
            datas.append("%s\t%s\t%s\t%s\t%s\t%s\n" % (target_code['keyword_daum2'], globalDate, globalTime, str(i + 1 -10).zfill(2), v,'https://search.daum.net/search?w=tot&q=' + fn.getEncodeUrl(v)))
            logger.debug("%s\t%s\t%s\t%s\t%s\t%s" % (target_code['keyword_daum2'], globalDate, globalTime, str(i + 1 -10).zfill(2), v,'https://search.daum.net/search?w=tot&q=' + fn.getEncodeUrl(v)))
        if i + 1 <= 30 and i + 1 > 20:
            datas.append("%s\t%s\t%s\t%s\t%s\t%s\n" % (target_code['keyword_daum3'], globalDate, globalTime, str(i + 1 -20).zfill(2), v,'https://search.daum.net/search?w=tot&q=' + fn.getEncodeUrl(v)))
            logger.debug("%s\t%s\t%s\t%s\t%s\t%s" % (target_code['keyword_daum3'], globalDate, globalTime, str(i + 1 -20).zfill(2), v,'https://search.daum.net/search?w=tot&q=' + fn.getEncodeUrl(v)))
        if i + 1 <= 40 and i + 1 > 30:
            datas.append("%s\t%s\t%s\t%s\t%s\t%s\n" % (target_code['keyword_daum4'], globalDate, globalTime, str(i + 1 -30).zfill(2), v,'https://search.daum.net/search?w=tot&q=' + fn.getEncodeUrl(v)))
            logger.debug("%s\t%s\t%s\t%s\t%s\t%s" % (target_code['keyword_daum4'], globalDate, globalTime, str(i + 1 -30).zfill(2), v,'https://search.daum.net/search?w=tot&q=' + fn.getEncodeUrl(v)))

    logger.debug('succ pasrsing')
    return datas

def getYoutubeKeyword():
    logger.info("----------getYoutubeKeyword()----------")

    logger.debug("get Source Datas")
    source = requests.get(target_url['keyword_youtube']).text
    soup = BeautifulSoup(source, 'html.parser')
    elem_list = soup.select("h3.yt-lockup-title > a ")

    logger.debug("parsing Datas")
    datas = []
    for i, v in enumerate(elem_list):
        if 'title' in v.attrs:
            datas.append("%s\t%s\t%s\t%s\t%s\t%s\n" % (target_code['keyword_youtube'],globalDate,globalTime,str(i+1).zfill(2), fn.getConvData(v.attrs['title']), "https://www.youtube.com" + v.attrs['href']))
            logger.debug("%s\t%s\t%s\t%s\t%s\t%s" % (target_code['keyword_youtube'],globalDate,globalTime,str(i+1).zfill(2), fn.getConvData(v.attrs['title']), "https://www.youtube.com" + v.attrs['href']))
    logger.debug('succ pasrsing')
    return datas

def getDaumNews():
    logger.info("----------getDaumNews()----------")
    source = requests.get(target_url['news_daum']).text
    soup = BeautifulSoup(source, 'html.parser')
    elem_list_title = soup.select("div.cont_thumb .tit_thumb a")
    elem_list_desc = soup.select("div.cont_thumb .desc_thumb span")

    titles = []
    descs = []
    datas = []
    for i, v in enumerate(elem_list_title):
        titles.append(v.text + '\t' + v.attrs['href'])

    for i, v in enumerate(elem_list_desc):
        descs.append(v.text.strip())
    fn.aryLenSync(titles, descs)
    for i, v in enumerate(titles):
        datas.append('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(target_code['news_daum'], globalDate, globalTime, str(i + 1).zfill(2), fn.getConvData(titles[i].split('\t')[0]), fn.getConvData(descs[i]), titles[i].split('\t')[1]))
        logger.debug('%s\t%s\t%s\t%s\t%s\t%s\t%s' %( target_code['news_daum'], globalDate, globalTime, str(i + 1).zfill(2), fn.getConvData(titles[i].split('\t')[0]) , fn.getConvData(descs[i]), titles[i].split('\t')[1]))

    return datas

def getResultKeywordFile():
    logger.info("----------getResultKeywordFile()----------")
    setTime()

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

    setTime()
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
