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