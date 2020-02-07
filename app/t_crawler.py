import json
import requests
from bs4 import BeautifulSoup
from module.logger import logger
from module import functions  as fn
import os



def ttt():
    logger.info("----------getDaumNews()----------")
    source = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=').text
    soup = BeautifulSoup(source, 'html.parser')
    elem_list1 = soup.select("#daumWrap #daumContent #mAside #ratNewsCollDetail ")
    elem_list2 = soup.select("#daumWrap #daumContent #mAside #ratNewsCollDetail .keyword_rank .link_txt")
    elem_list3 = soup.select("#daumWrap #daumContent #mAside .g_comp_s")

    i1 = 0
    i2 = 0
    i3 = 0
    for i,v in enumerate(elem_list2):
        if i+1 <=10 and i+1 >0:
            i1 = i1 + 1
            print('종합'+str(i1).zfill(2) +v.get_text())
        if i+1 <=20 and i+1 >10:
            i2 = i2 + 1
            print('연예'+str(i2).zfill(2) +v.get_text())
        if i+1 <=30 and i+1 >20:
            i3 = i3 + 1
            print('스포츠'+str(i3).zfill(2) +v.get_text())

def ttt2():
       logger.info("----------getDaumNews()----------")
       source = requests.get('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=').text
       soup = BeautifulSoup(source, 'html.parser')
       elem_list1 = soup.select("#daumWrap #daumContent #mAside #ratNewsCollDetail ")
       elem_list2 = soup.select(".realtime_srch .lst_realtime_srch li .tit")
       elem_list3 = soup.select("#daumWrap #daumContent #mAside .g_comp_s")

       print(elem_list2)
       for i,v in enumerate(elem_list2):
           if i < 20 :
               print(str(i).zfill(2) + ' '+ v.get_text())





ttt2()