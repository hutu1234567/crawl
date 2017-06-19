#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2016-12-16 09:17:47
# Filename      : tianyancha.py
# Description   :
from __future__ import print_function, unicode_literals
import requests
import time
import re
import json

def getToken(index_url):
        session = requests.session()
        session.cookies.set("tnet", "218.108.215.127")

        #index_url = "http://www.tianyancha.com/company/150041670"
        tongji_url = "http://www.tianyancha.com/tongji/150041670.json?random=%s" % (int(time.time()) * 1000)
       # api_url = "http://www.tianyancha.com/company/150041670.json"

        public_headers = {
                "User-Agent": "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
                }

        api_headers = public_headers.copy()
        api_headers.update({
                "Tyc-From": "normal",
                "Accept": "application/json, text/plain, */*",
                "Referer": index_url,
                "CheckError": "check",
            })


        # 访问首页
        index_page = session.request("GET", index_url, headers = public_headers)

        #print(index_page.content)
        # 访问js取出_sgAtt
        js_url = re.findall(b"http\:\/\/static\.tianyancha.com/wap/resources/script.*js", index_page.content)[0]
        #print("js======",js_url)
        #js_url = re.findall(b"http\:\/\/static\.tianyancha.com/wap/resources/js/\w+\.js", index_page.content)[0]
        js_page = session.request("GET", js_url, headers = public_headers)
        #file=open("d:\\aa.txt","w")
        #file.write(str(js_page.content))
        #print("js_page.content",js_page.content)
        sgattrs = json.loads(re.findall(b"n\._sgArr=(.+?);", js_page.content)[0])

        # 取得token和fxckStr
        tongji_page = session.request("GET", tongji_url, headers = api_headers)
        js_code = "".join([ chr(int(code)) for code in tongji_page.json()["data"]["v"].split(",") ])
        token = re.findall(r"token=(\w+);", js_code)[0]
        #print("token:", token)

        fxck_chars = re.findall(r"\'([\d\,]+)\'", js_code)[0].split(",")
        sogou = sgattrs[9] # window.$SoGou$ = window._sgArr[9]
        utm = "".join([sogou[int(fxck)] for fxck in fxck_chars])    # if(window.wtf){var fxck = window.wtf().split(",");var fxckStr = "";for(var i=0;i<fxck.length;i++){fxckStr+=window.$SoGou$[fxck[i]];}document.cookie = "_utm="+fxckStr+";path=/;";window.wtf = null;}
        #print("utm:", utm)

        session.cookies.set("token", token)
        session.cookies.set("_utm", utm)
        # r = session.request("GET", "http://www.tianyancha.com/v2/company/2344338651.json",
        #          headers = api_headers)
        # print(str(r.content,"utf-8"))

        return session,api_headers


if __name__ == '__main__':
    getToken("http://www.tianyancha.com/")