import pandas as pd

import requests
from bs4 import BeautifulSoup
from urllib import parse

source = requests.get('https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day').text
soup = BeautifulSoup(source, 'html.parser')
elem_list = soup.select(".ranking_section ol li dl a")
info = pd.DataFrame(columns=['num','type','content','url'])
type =''
num = ''
datas = []
for i ,v in enumerate(elem_list):
    content =  v.attrs['title']
    if i +1 <=5 :
        type ='정치'
        num = i + 1
    if i + 1 <= 10 and i + 1 > 5:
        type = '경제'
        num = i + 1 -5
    if i + 1 <= 15 and i + 1 > 10:
        type = '사회'
        num = i + 1 -10
    if i + 1 <= 20 and i + 1 > 15:
        type = '생활/문화'
        num = i + 1 - 15
    if i + 1 <= 25 and i + 1 > 20:
        type = '세계'
        num = i + 1 -20
    if i + 1 <= 30 and i + 1 > 25:
        type = 'IT/과학'
        num = i + 1 - 25

        #data = '%s\t(%s)%s\t%s' % ( fn.getStrNo(num), type,fn.getConvData(content),'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+fn.getEncodeUrl(content))
        #atas.append((data))
    info = info.append({'num':  num
                            , 'type' :  type
                            , 'content': content
                            ,'url': 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=' +  content
                            } ,ignore_index=True)



info





