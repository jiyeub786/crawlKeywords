import time

import crawler as cw
from module.logger import logger
import time

dateN = time.strftime('%Y-%m-%d', time.localtime(time.time()))

def getKeywordHtml():
    logger.info("----------getHtml()----------")
    daum = []
    News_daum = []
    naver = []
    News_naver = []
    youtube = []
    datas = []


    file_keyword = cw.base_dir + "result_" +dateN + ".txt"
    file_news = cw.base_dir + "result_news_" + dateN + ".txt"

    f = open(file_keyword, mode='r', encoding='UTF-8')
    filedata = f.readlines()
    f.close()


    for i, v in enumerate(filedata):
        datas.append(v.replace('\n', '').split('\t'))


    sets =[]

    for i, v in enumerate(datas):

        sets.append(v[2])
        if v[0] in ('02-1','02-2','02-3','02-4'):
            daum.append(v)
        if v[0] in ('01-1','01-2','01-3'):
            naver.append(v)
        if v[0] == '03':
            youtube.append(v)
        if v[0] == '04':
            News_daum.append(v)
        if v[0] == '05':
            News_naver.append(v)
    sets= set(sets)
    sets.remove('time')
    print(sets)

    datas = []


    for i0,v0 in enumerate(sets):
        create_dt = dateN
        datas.append(v0)
        datas.append('다음, 네이버, 유튜브 검색 키워드(%s)' %(create_dt))
        datas.append('<h2 id= "style_title">%s 기준</br>검색 키워드 순위</h2>' %(create_dt))
        datas.append('</br>')
        datas.append('<p class ="outlink"><a href = "#keyword_daum" >다음 바로가기</a></p>')
        datas.append('<p class ="outlink"><a href = "#keyword_naver" >네이버 바로가기</a></p>')
        datas.append('<p class ="outlink"><a href = "#keyword_youtube" >유튜브 바로가기</a></p>')
        datas.append('<p class ="outlink"><a href = "#news_daum" >다음 뉴스 바로가기</a></p>')
        datas.append('<p class ="outlink"><a href = "#news_naver" >네이버 뉴스 바로가기</a></p>')
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
        datas.append('<h3 id= "keyword_daum" ></h3>')
        datas.append('<h3 id= "style_daum" ><b>※ 다음 검색 키워드</b></h3>')
        datas.append('<p id= "style_daum" data-ke-size="size14"><b> @ 실시간 이슈(1~10)</b></p>')
        for i, v in enumerate(daum):
            if v0 == v[2] and v[0] == '02-1':
                datas.append('<a id="outlink_daum" href = "%s" > 검색순위%s "%s"</a>' % (v[5], v[3], v[4]))
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<p id= "style_daum" data-ke-size="size14"><b> @ 실시간 뉴스(1~10)</b></p>')
        for i, v in enumerate(daum):
            if v0 == v[2] and v[0] == '02-2':
                datas.append('<a id="outlink_daum" href = "%s" > 검색순위%s "%s"</a>' % (v[5], v[3], v[4]))
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<p id= "style_daum" data-ke-size="size14"><b> @ 실시간 연예(1~10)</b></p>')
        for i, v in enumerate(daum):
            if v0 == v[2] and v[0] == '02-3':
                datas.append('<a id="outlink_daum" href = "%s" > 검색순위%s "%s"</a>' % (v[5], v[3], v[4]))
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<p id= "style_daum" data-ke-size="size14"><b> @ 실시간 스포츠(1~10)</b></p>')
        for i, v in enumerate(daum):
            if v0 == v[2] and v[0] == '02-4':
                datas.append('<a id="outlink_daum" href = "%s" > 검색순위%s "%s"</a>' % (v[5], v[3], v[4]))
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
        datas.append('<h3 id= "keyword_naver" ></h3>')
        datas.append('<h3 id= "style_naver" ><b>※ 네이버 검색 키워드</b></h3>')
        datas.append('<p id= "style_naver" data-ke-size="size14"><b> @ 실시간 이슈(1~20)</b></p>')
        for i, v in enumerate(naver):
            if v0 == v[2] and v[0] == '01-1':
                datas.append('<a id="outlink_naver" href = "%s" > 검색순위%s "%s"</a>' % (v[5], v[3], v[4]))
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<p id= "style_naver" data-ke-size="size14"><b> @ 실시간 뉴스(1~10)</b></p>')
        for i, v in enumerate(naver):
            if v0 == v[2] and v[0] == '01-2':
                datas.append('<a id="outlink_naver" href = "%s" > 검색순위%s "%s"</a>' % (v[5], v[3], v[4]))
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<p id= "style_naver" data-ke-size="size14"><b> @ 실시간 연예,스포츠(1~10)</b></p>')

        #for#for
        for i, v in enumerate(naver):
            if v0 == v[2] and v[0] == '01-3':
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


        # for i, v in enumerate(youtube):
        #     if v0 == v[2]:
        #         youtube_cnt = youtube_cnt +1
        datas.append('<h3 id= "keyword_youtube" ></h3>')
        datas.append('<h3 id= "style_youtube" ><b>※ 유튜브 인기 검색순위(1~20)</b></h3>' )
        youtube_cnt = 0
        for i00, v in enumerate(youtube):
            if v0 == v[2] and youtube_cnt < 20 :
                youtube_cnt = youtube_cnt + 1
                datas.append('<a id="outlink_youtube" href = "%s" > 검색순위 %s "%s"</a>' %( v[5],v[3],v[4]))

        datas.append('<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />')
        datas.append('<p class ="outlink"><a href = "#style_title" >맨 위로</a></p>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle" style="display:block; text-align:center;" data-ad-layout="in-article" data-ad-format="fluid" data-ad-client="ca-pub-7985475884167551" data-ad-slot="3329701659"></ins><script> (adsbygoogle = window.adsbygoogle || []).push({});</script>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<h3 id= "news_daum" ></h3>')
        datas.append('<h3 id= "style_daum" ><b>※ 다음 랭킹뉴스 목록</b></h3>')
        datas.append('<p id= "style_daum" data-ke-size="size14"><b> @ 다음 랭킹뉴스</b></p>')
        for i, v in enumerate(News_daum):
            if v0 == v[2] :
                datas.append('<a id="outlink_daum" href = "%s" >랭킹%s "%s"</a>' % (v[5],v[3], v[4]))
        datas.append('<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />')
        datas.append('<p class ="outlink"><a href = "#style_title" >맨 위로</a></p>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle" style="display:block; text-align:center;" data-ad-layout="in-article" data-ad-format="fluid" data-ad-client="ca-pub-7985475884167551" data-ad-slot="3329701659"></ins><script> (adsbygoogle = window.adsbygoogle || []).push({});</script>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('<h3 id= "news_naver" ></h3>')
        datas.append('<h3 id= "style_naver" ><b>※ 네이버 랭킹뉴스 목록</b></h3>')
        datas.append('<p id= "style_naver" data-ke-size="size14"><b> @ 네이버 랭킹뉴스</b></p>')
        #for#for
        for i, v in enumerate(News_naver):
            if v0 == v[2] :
                datas.append('<a id="outlink_naver" href = "%s" >랭킹%s"%s"</a>' %( v[5],v[3],v[4]))

        datas.append('<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />')
        datas.append('<p class ="outlink"><a href = "#style_title" >맨 위로</a></p>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')
        datas.append('</br>')

    return datas






for i,v in enumerate(getKeywordHtml()):
    print(v)