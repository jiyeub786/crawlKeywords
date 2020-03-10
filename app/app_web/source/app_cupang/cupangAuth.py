# coding: utf-8

import hmac
import hashlib
import os
import time
import requests
import json
import urllib.request 
from urllib.parse import urlencode

__author__ = "Jaejin Jang<jaejin_me@naver.com>"

from bs4 import BeautifulSoup


class cupangMgr:
    DOMAIN = "https://api-gateway.coupang.com"

    def generateHmac(self, method, url, secretKey, accessKey):
        path, *query = url.split("?")
        os.environ["TZ"] = "GMT+0"
        datetime = time.strftime('%y%m%d') + 'T' + time.strftime('%H%M%S') + 'Z'
        message = datetime + method + path + (query[0] if query else "")
        signature = hmac.new(bytes(secretKey, "utf-8"), message.encode("utf-8"), hashlib.sha256).hexdigest()

        return "CEA algorithm=HmacSHA256, access-key={}, signed-date={}, signature={}".format(accessKey, datetime,
                                                                                              signature)

    def get_productsdata(self, request_method, authorization, keyword, limit):
        URL = "/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword=" + urllib.parse.quote(
            keyword) + "&limit=" + str(limit)
        url = "{}{}".format(self.DOMAIN, URL)

        response = requests.request(method=request_method, url=url, headers={"Authorization": authorization,
                                                                             "Content-Type": "application/json;charset=UTF-8"})
        retdata = json.dumps(response.json(), indent=4).encode('utf-8')
        jsondata = json.loads(retdata)
        data = jsondata['data']
        productdata = data['productData']

        return productdata

    def getProductDescription(productId):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
        # source1 = requests.get(target_url['keyword_cpn'],headers=headers).text
        # source2 = requests.get(target_url['keyword_cpn2'],headers=headers).text
        source3 = requests.get("https://www.coupang.com/vp/products/" + productId

                               , headers=headers).text
        # source1 = requests.get("https://www.naver.com").text
        # soup1 = BeautifulSoup(source1, 'html.parser')
        # soup2 = BeautifulSoup(source2, 'html.parser')
        soup3 = BeautifulSoup(source3, 'html.parser')

        print(soup3)

        # print(source1)
        # print(source2)
        # print(soup3)
        # elem_list1 = soup1.select(".subType-IMAGE")
        # elem_list_good = soup2.select(".sdp-review__highlight__positive__article__content")
        # elem_list_bad = soup2.select(".sdp-review__highlight__critical__article__content")
        elem_list_review = soup3.select(".prod-description ul li")

        for i, v in enumerate(elem_list_review):
            print(v.get_text())
        datas = []
        return datas

    def getProductReview(productId):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
        # source1 = requests.get(target_url['keyword_cpn'],headers=headers).text
        # source2 = requests.get(target_url['keyword_cpn2'],headers=headers).text
        source3 = requests.get(
            "https://www.coupang.com/vp/product/reviews?productId=" + productId + "&size=20&sortBy=ORDER_SCORE_ASC"

            , headers=headers).text
        # source1 = requests.get("https://www.naver.com").text
        # soup1 = BeautifulSoup(source1, 'html.parser')
        # soup2 = BeautifulSoup(source2, 'html.parser')
        soup3 = BeautifulSoup(source3, 'html.parser')

        # print(source1)
        # print(source2)
        # print(soup3)
        # elem_list1 = soup1.select(".subType-IMAGE")
        # elem_list_good = soup2.select(".sdp-review__highlight__positive__article__content")
        # elem_list_bad = soup2.select(".sdp-review__highlight__critical__article__content")
        elem_list_review = soup3.select(".sdp-review__article__list__review__content")

        datas = []
        for i, v in enumerate(elem_list_review):
            datas.append({"productId": str(productId), "review": str(v.get_text()).strip()})

        return datas




if __name__ == '__main__':
    method = 'GET'  # 정보를 얻는것이기 때문에 GET
    keyword = '천연펄프100% 무형광 3겹'  # 검색할 키워드, 쿠팡에서 검색하는거랑 결과가 동일합니다.
    limit = 100  # 몇개의 정보를 가져올지 설정. 상위부터 가져옵니다.

    access_key = "d07c048a-7fc9-4882-804b-37562f4887f3"
    secret_key = "899744dab9e9406bf8f361f91685e6b74d3edac0"

    URL = "/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword=" + urllib.parse.quote(
        keyword) + "&limit=" + str(limit)

    test = cupangMgr()
    authorization = test.generateHmac(method, URL, secret_key, access_key)  # HMAC 생성
    productdata = test.get_productsdata(method, authorization, keyword, limit)  # API 호출
    print(productdata)  # 결과 확인