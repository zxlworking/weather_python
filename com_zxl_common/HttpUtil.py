#!/usr/bin/env python
# coding=utf-8
import urllib
import time
import urllib2
import sys
from selenium import webdriver


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

    def get_today_weather_from_zh_tian_qi(self, city_code):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

        # 创建chrome参数对象
        opt = webdriver.ChromeOptions()

        # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
        opt.set_headless()
        prefs = {"profile.managed_default_content_settings.images": 2}
        opt.add_experimental_option("prefs", prefs)

        # 创建chrome无界面对象
        driver = webdriver.Chrome(executable_path=chromedriver, options=opt)

        driver.get('http://www.weather.com.cn/weather1d/%s.shtml#search' % city_code)

        # # < big class ="jpg80 d04" > < / big >
        # # link = driver.find_element_by_class_name("jpg80")
        # link = driver.find_element_by_css_selector("[class='jpg80 d04']")
        # print link.value_of_css_property("background-image")
        # print link.value_of_css_property("width")
        # print link.value_of_css_property("height")
        # print link.value_of_css_property("background-position-x")
        # print link.value_of_css_property("background-position-y")
        # print "\n"
        # link = driver.find_element_by_css_selector("[class='jpg80 n01']")
        # print link.value_of_css_property("background-image")
        # print link.value_of_css_property("width")
        # print link.value_of_css_property("height")
        # print link.value_of_css_property("background-position-x")
        # print link.value_of_css_property("background-position-y")
        # print "\n"
        # link = driver.find_element_by_css_selector("[class='con today clearfix']")
        # print link.text
        # print "\n"

        # 打印内容
        # return driver.page_source

        return driver

    def get_today_weather_temperature_icon_css(self,mParserUtil, driver, result):
        result["today_weather_temperature_icon_css"] = {}

        therm_css_selector = driver.find_element_by_css_selector("[class='therm']")
        result["today_weather_temperature_icon_css"]["img"] = mParserUtil.get_single_bracket_str(
            therm_css_selector.value_of_css_property("background-image"))
        t_css_selector = driver.find_element_by_css_selector('.today .t .sk .therm p .t')
        result["today_weather_temperature_icon_css"]["background_position_x1"] = mParserUtil.get_px_value(
            t_css_selector.value_of_css_property("background-position-x"))
        result["today_weather_temperature_icon_css"]["background_position_y1"] = mParserUtil.get_px_value(
            t_css_selector.value_of_css_property("background-position-y"))
        result["today_weather_temperature_icon_css"]["width1"] = mParserUtil.get_px_value(
            t_css_selector.value_of_css_property("width"))
        result["today_weather_temperature_icon_css"]["height1"] = mParserUtil.get_px_value(
            t_css_selector.value_of_css_property("height"))
        c_css_selector = driver.find_element_by_css_selector('.today .t .sk .therm p .c')
        result["today_weather_temperature_icon_css"]["background_position_x2"] = mParserUtil.get_px_value(
            c_css_selector.value_of_css_property("background-position-x"))
        result["today_weather_temperature_icon_css"]["background_position_y2"] = mParserUtil.get_px_value(
            c_css_selector.value_of_css_property("background-position-y"))
        result["today_weather_temperature_icon_css"]["width2"] = mParserUtil.get_px_value(
            c_css_selector.value_of_css_property("width"))
        result["today_weather_temperature_icon_css"]["height2"] = mParserUtil.get_px_value(
            c_css_selector.value_of_css_property("height"))

    def get_toaday_detail_weather_icon_css(self,mParserUtil, driver, toaday_detail_weather_element_result):
        big_css_selector = driver.find_element_by_css_selector(
            "[class='%s']" % toaday_detail_weather_element_result["weather_icon_css"])
        toaday_detail_weather_element_result["weather_icon_css"] = {}
        toaday_detail_weather_element_result["weather_icon_css"]["img"] = mParserUtil.get_single_bracket_str(
            big_css_selector.value_of_css_property("background-image"))
        toaday_detail_weather_element_result["weather_icon_css"]["background_position_x"] = mParserUtil.get_px_value(
            big_css_selector.value_of_css_property("background-position-x"))
        toaday_detail_weather_element_result["weather_icon_css"]["background_position_y"] = mParserUtil.get_px_value(
            big_css_selector.value_of_css_property("background-position-y"))
        toaday_detail_weather_element_result["weather_icon_css"]["width"] = mParserUtil.get_px_value(
            big_css_selector.value_of_css_property("width"))
        toaday_detail_weather_element_result["weather_icon_css"]["height"] = mParserUtil.get_px_value(
            big_css_selector.value_of_css_property("height"))

