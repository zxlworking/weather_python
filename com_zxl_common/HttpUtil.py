#!/usr/bin/env python
# coding=utf-8
import json
import pickle
import urllib
import time
import urllib2
import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.common.exceptions import TimeoutException


# reload(sys)
# sys.setdefaultencoding("utf8")


class HttpUtil:

    def get_http_content(self, url, headers):
        try:
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            return response.read().decode("utf-8")
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print "e.code:"
                print e.code
            if hasattr(e, "reason"):
                print "e.reason:"
                print e.reason

    def get_qsbk_list_by_page(self, page):
        # https://www.qiushibaike.com/article/120535436
        url = "http://www.qiushibaike.com/hot/page/%s" % page
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent":user_agent}
        return self.get_http_content(url, headers)

    def get_qsbk_detail(self, author_id):
        # https://www.qiushibaike.com/article/120535436
        url = "http://www.qiushibaike.com/article/%s" % author_id
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent":user_agent}
        return self.get_http_content(url, headers)

    def get_city_list(self):
        url = "http://mobile.weather.com.cn/js/citylist.xml"
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        return self.get_http_content(url, headers)

    def get_weather_content_by_city_code(self, city_code):
        url = "http://www.weather.com.cn/data/cityinfo/" + city_code + ".html"
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        return self.get_http_content(url, headers)

    def get_weather_content_by_city_py(self, city_py):
        url = "https://www.tianqi.com/" + city_py
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        return self.get_http_content(url, headers)

    def get_wx_access_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx20280a1b4a149ecb&secret=0964fbba9b0a6fad952083adf33df782"
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        return self.get_http_content(url, headers)

    def get_wx_ip(self,token):
        url = "https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=%s" % token
        #11_FdsbNLE49EkEMctzX-KC8ssVb-aQxE7_S4ntAiu-5HBzVuyTCHeuf4LaoXvV3hJ1bf-aT5qoAvwmR-2FcMq7GPkyr-S140OLlV1awNBgUj82bPX9_4fjEw-YxOz4KcNxAb3IUcNnHfKdfnEhYPGdAIAFWN
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        return self.get_http_content(url, headers)

    def get_qsbk(self):
        url = "http://118.25.178.69/cgi_server/cgi_qsbk/cgi_qsbk.py?page=1&count=1"
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        return self.get_http_content(url, headers)

    def get_music_info(self, param):
        url = "http://tingapi.ting.baidu.com/v1/restserver/ting?%s" % param
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        return self.get_http_content(url, headers)
