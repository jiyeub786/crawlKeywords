import crawler as cw
from module.logger import logger

def getHtml():
    logger.info("----------getHtml()----------")
    daum = []
    naver = []
    youtube = []
    datas = []

    file_keyword = cw.base_dir + "result_" +cw.date + ".txt"
    file_news = cw.base_dir + "result_news_" + cw.date + ".txt"

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
    print(sets)


    for i0,v0 in enumerate(sets):
        create_dt = '2020-02-01 09:00'
        print(v0)

        # get html
        print('다음, 네이버, 유튜브 검색 키워드(%s)' %(create_dt))
        print('<h2 id= "style_title">%s 기준</br>검색 키워드 순위</h2>' %(create_dt))
        print('</br>')
        print('<p class ="outlink"><a href = "#style_daum" >다음 바로가기</a></p>')
        print('<p class ="outlink"><a href = "#style_naver" >네이버 바로가기</a></p>')
        print('<p class ="outlink"><a href = "#style_youtube" >유튜브 바로가기</a></p>')
        print('<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')

        print('<h3 id= "style_daum" ><b>※ 다음 검색순위(1~10)</b></h3>')
        #for
        for i, v in enumerate(daum):
            if v0 == v[2] :
                print('<a id="outlink_daum" href = "%s" > 검색순위%s : "%s"</a>' %( v[5],v[3],v[4]))


        print('<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')

        print('<h3 id= "style_naver" ><b>※ 네이버 검색순위(1~20)</b></h3>')
        #for#for
        for i, v in enumerate(naver):
            if v0 == v[2]:
                print('<a id="outlink_naver" href = "%s" > 검색순위%s : "%s"</a>' %( v[5],v[3],v[4]))

        print('<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')

        print('<h3 id= "style_youtube" ><b>※ 유튜브 인기 검색순위(1~%s)</b></h3>' %(str(len(youtube))))
        #for#for
        for i, v in enumerate(youtube):
            if v0 == v[2]:
                print('<a id="outlink_youtube" href = "%s" > 검색순위%s : "%s"</a>' %( v[5],v[3],v[4]))

        print('<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />')
        print('<p class ="outlink"><a href = "style_title" >맨 위로</a></p>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')
        print('</br>')


getHtml()