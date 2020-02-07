import requests
from bs4 import BeautifulSoup
from module.logger import logger
from urllib import parse



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


def ttt3():
       logger.info("----------getDaumNews()----------")

       keywords = ['서울','부산','대구','인천','광주','대전','울산','세종','경기','강원','충북','전북','전남','경북','경남','제주'
                    '한국','일본','중국','동남아','러시아','미국','유럽','호주','캐나다']
       for i, v in enumerate(keywords):
           print(v)
           url1="https://search.daum.net/search?nil_suggest=btn&w=news&DA=SBC&cluster=y&q="
           url2="https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
           source1 = requests.get(url1 + v).text
           source2 = requests.get(url2 + v).text
           soup1 = BeautifulSoup(source1, 'html.parser')
           soup2 = BeautifulSoup(source2, 'html.parser')
           elem_list1 = soup1.select("li .wrap_tit a")
           elem_list2 = soup2.select(".type01 li dt a")

           for ii, vv in enumerate(elem_list1):
               data= vv.get_text()
               print(v+'\t'+'daum'+'\t'+str(i).zfill(2) +'\t'+  data + '\t' + url1+parse.quote(data) )

           for ii, vv in enumerate(elem_list2):
               data= vv.get_text()
               print(v+'\t'+'naver'+'\t'+str(i).zfill(2) +'\t'+  vv.get_text() + '\t' + url2+ parse.quote(data))




ttt3()