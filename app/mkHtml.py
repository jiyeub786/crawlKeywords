import time

import crawler as cw
from module.logger import logger
import time

dateN = time.strftime('%Y-%m-%d', time.localtime(time.time()))

def getKeywordHtml():
    logger.info("----------getHtml()----------")
    daum = []
    naver = []
    youtube = []
    datas = []

    file_keyword = cw.base_dir + "result_" +dateN + ".txt"
    file_news = cw.base_dir + "result_news_" + dateN + ".txt"

    f = open(file_keyword, mode='r', encoding='UTF-8')
    filedata = f.readlines()

    for i, v in enumerate(filedata):
        datas.append(v.replace('\n', '').split('\t'))


    sets =[]

    for i, v in enumerate(datas):

        sets.append(v[2])
        if v[0] == '02':
            daum.append(v)
        if v[0] == '01':
            naver.append(v)
        if v[0] == '03':
            youtube.append(v)

    sets= set(sets)
    sets.remove('time')
    print(sets)

    datas = []


    for i0,v0 in enumerate(sets):
        create_dt = '2020-02-03 00:00'
        datas.append(v0)
        datas.append('다음, 네이버, 유튜브 검색 키워드(%s)' %(create_dt))
        datas.append('<h2 id= "style_title">%s 기준</br>검색 키워드 순위</h2>' %(create_dt))
        datas.append('</br>')
        datas.append('<p class ="outlink"><a href = "#style_daum" >다음 바로가기</a></p>')
        datas.append('<p class ="outlink"><a href = "#style_naver" >네이버 바로가기</a></p>')
        datas.append('<p class ="outlink"><a href = "#style_youtube" >유튜브 바로가기</a></p>')
        datas.append('<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle" style="display:block; text-align:center;" data-ad-layout="in-article" data-ad-format="fluid" data-ad-client="ca-pub-7985475884167551" data-ad-slot="3329701659"></ins><script> (adsbygoogle = window.adsbygoogle || []).push({});</script>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<h3 id= "style_daum" ><b>※ 다음 검색순위(1~10)</b></h3>')
        for i, v in enumerate(daum):
            if v0 == v[2] :
                datas.append('<a id="outlink_daum" href = "%s" > 검색순위%s "%s"</a>' %( v[5],v[3],v[4]))
        datas.append('<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle" style="display:block; text-align:center;" data-ad-layout="in-article" data-ad-format="fluid" data-ad-client="ca-pub-7985475884167551" data-ad-slot="3329701659"></ins><script> (adsbygoogle = window.adsbygoogle || []).push({});</script>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<h3 id= "style_naver" ><b>※ 네이버 검색순위(1~20)</b></h3>')
        #for#for
        for i, v in enumerate(naver):
            if v0 == v[2]:
                datas.append('<a id="outlink_naver" href = "%s" > 검색순위%s "%s"</a>' %( v[5],v[3],v[4]))
        datas.append('<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle" style="display:block; text-align:center;" data-ad-layout="in-article" data-ad-format="fluid" data-ad-client="ca-pub-7985475884167551" data-ad-slot="3329701659"></ins><script> (adsbygoogle = window.adsbygoogle || []).push({});</script>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        youtube_cnt =0
        for i, v in enumerate(youtube):
            if v0 == v[2]:
                youtube_cnt = youtube_cnt +1
        datas.append('<h3 id= "style_youtube" ><b>※ 유튜브 인기 검색순위(1~%s)</b></h3>' %(str(youtube_cnt)))
        #for#for
        for i, v in enumerate(youtube):
            if v0 == v[2]:
                datas.append('<a id="outlink_youtube" href = "%s" > 검색순위%s "%s"</a>' %( v[5],v[3],v[4]))
        datas.append('<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />')
        datas.append('<p class ="outlink"><a href = "#style_title" >맨 위로</a></p>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')

        return datas


for i,v in enumerate(getKeywordHtml()):
    print(v)