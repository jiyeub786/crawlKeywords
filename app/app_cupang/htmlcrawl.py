from urllib import parse
import sys
import json
import requests
from bs4 import BeautifulSoup
import os
import time
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.logger import logger
from common import functions  as fn

globalDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
globalTime = time.strftime('%H:%M:%S', time.localtime(time.time()))
createTime = globalDate+'\t'+globalTime

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

target_code = { 'keyword_naver1': '01-1'                }

target_url = { "keyword_cpn" : "https://www.coupang.com/vp/products/104722?isAddedCart="
               ,"keyword_cpn2" : "https://www.coupang.com/vp/product/reviews/positive-critical?productId=104722&viRoleCode=3"
               ,"cpn3": "https://www.coupang.com/vp/product/reviews?productId=104722&size=20&sortBy=ORDER_SCORE_ASC"}



def getDaumKeyword() :
    logger.info("----------getDaumKeyword()----------")
    logger.debug("get Source Datas")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    source1 = requests.get(target_url['keyword_cpn'],headers=headers).text
    source2 = requests.get(target_url['keyword_cpn2'],headers=headers).text
    source3 = requests.get(target_url['cpn3'],headers=headers).text
    #source1 = requests.get("https://www.naver.com").text
    soup1 = BeautifulSoup(source1, 'html.parser')
    soup2 = BeautifulSoup(source2, 'html.parser')
    soup3 = BeautifulSoup(source3, 'html.parser')

    #print(source1)
    #print(source2)
    #print(soup3)
    elem_list1 = soup1.select(".subType-IMAGE")
    elem_list_good = soup2.select(".sdp-review__highlight__positive__article__content")
    elem_list_bad = soup2.select(".sdp-review__highlight__critical__article__content")
    elem_list_review = soup3.select(".sdp-review__article__list__review__content")

    for i,v in enumerate(elem_list_review):
        print(str(i) + v.get_text())
    #print(elem_list_review)



    #print(elem_list_bad)

    #print(elem_list_good)
    datas =[]

    return datas

getDaumKeyword()