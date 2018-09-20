#!/usr/bin/env python
# coding=utf-8
import urllib
import time
import urllib2
import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
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

    def get_today_weather_temperature_icon_css(self, mParserUtil, driver, result):
        # print "get_today_weather_temperature_icon_css---start"

        result["today_weather"]["temperature_icon_css"] = {}

        therm_css_selector = driver.find_element_by_css_selector("[class='therm']")
        result["today_weather"]["temperature_icon_css"]["img"] = mParserUtil.get_single_bracket_str(
            therm_css_selector.value_of_css_property("background-image"))
        t_css_selector = driver.find_element_by_css_selector('.today .t .sk .therm p .t')
        result["today_weather"]["temperature_icon_css"]["background_position_x1"] = mParserUtil.get_px_value(
            t_css_selector.value_of_css_property("background-position-x"))
        result["today_weather"]["temperature_icon_css"]["background_position_y1"] = mParserUtil.get_px_value(
            t_css_selector.value_of_css_property("background-position-y"))
        result["today_weather"]["temperature_icon_css"]["width1"] = mParserUtil.get_px_value(
            t_css_selector.value_of_css_property("width"))
        result["today_weather"]["temperature_icon_css"]["height1"] = mParserUtil.get_px_value(
            t_css_selector.value_of_css_property("height"))
        c_css_selector = driver.find_element_by_css_selector('.today .t .sk .therm p .c')
        result["today_weather"]["temperature_icon_css"]["background_position_x2"] = mParserUtil.get_px_value(
            c_css_selector.value_of_css_property("background-position-x"))
        result["today_weather"]["temperature_icon_css"]["background_position_y2"] = mParserUtil.get_px_value(
            c_css_selector.value_of_css_property("background-position-y"))
        result["today_weather"]["temperature_icon_css"]["width2"] = mParserUtil.get_px_value(
            c_css_selector.value_of_css_property("width"))
        result["today_weather"]["temperature_icon_css"]["height2"] = mParserUtil.get_px_value(
            c_css_selector.value_of_css_property("height"))
        # print "get_today_weather_temperature_icon_css---end"

    def get_today_humidity_icon_css(self, mParserUtil, driver, result):
        # print "get_today_humidity_icon_css---start"

        result["today_weather"]["humidity_icon_css"] = {}

        therm_css_selector = driver.find_element_by_css_selector(".con .left i, .today .sk .therm")
        result["today_weather"]["humidity_icon_css"]["img"] = mParserUtil.get_single_bracket_str(therm_css_selector.value_of_css_property("background-image"))
        h_css_selector = driver.find_element_by_css_selector(".today .t .sk .h i")
        result["today_weather"]["humidity_icon_css"]["background_position_x"] = mParserUtil.get_px_value(h_css_selector.value_of_css_property("background-position-x"))
        result["today_weather"]["humidity_icon_css"]["background_position_y"] = mParserUtil.get_px_value(h_css_selector.value_of_css_property("background-position-y"))

        zs_css_selector = driver.find_element_by_css_selector(".today .t .sk .zs i")
        result["today_weather"]["humidity_icon_css"]["width"] = mParserUtil.get_px_value(zs_css_selector.value_of_css_property("width"))
        result["today_weather"]["humidity_icon_css"]["height"] = mParserUtil.get_px_value(zs_css_selector.value_of_css_property("height"))

        # print "get_today_humidity_icon_css---end"

    def get_today_wind_icon_css(self, mParserUtil, driver, result):
        # print "get_today_wind_icon_css---start"

        result["today_weather"]["wind_icon_css"] = {}

        therm_css_selector = driver.find_element_by_css_selector(".con .left i, .today .sk .therm")
        result["today_weather"]["wind_icon_css"]["img"] = mParserUtil.get_single_bracket_str(therm_css_selector.value_of_css_property("background-image"))
        w_css_selector = driver.find_element_by_css_selector(".today .t .sk .w i")
        result["today_weather"]["wind_icon_css"]["background_position_x"] = mParserUtil.get_px_value(w_css_selector.value_of_css_property("background-position-x"))
        result["today_weather"]["wind_icon_css"]["background_position_y"] = mParserUtil.get_px_value(w_css_selector.value_of_css_property("background-position-y"))

        zs_css_selector = driver.find_element_by_css_selector(".today .t .sk .zs i")
        result["today_weather"]["wind_icon_css"]["width"] = mParserUtil.get_px_value(zs_css_selector.value_of_css_property("width"))
        result["today_weather"]["wind_icon_css"]["height"] = mParserUtil.get_px_value(zs_css_selector.value_of_css_property("height"))

        # print "get_today_wind_icon_css---end"

    def get_today_air_quality_icon_css(self, mParserUtil, driver, result):
        # print "get_today_air_quality_icon_css---start"

        result["today_weather"]["air_quality_icon_css"] = {}

        therm_css_selector = driver.find_element_by_css_selector(".con .left i, .today .sk .therm")
        result["today_weather"]["air_quality_icon_css"]["img"] = mParserUtil.get_single_bracket_str(therm_css_selector.value_of_css_property("background-image"))
        pol_css_selector = driver.find_element_by_css_selector(".today .t .sk .pol i")
        result["today_weather"]["air_quality_icon_css"]["background_position_x"] = mParserUtil.get_px_value(pol_css_selector.value_of_css_property("background-position-x"))
        result["today_weather"]["air_quality_icon_css"]["background_position_y"] = mParserUtil.get_px_value(pol_css_selector.value_of_css_property("background-position-y"))

        zs_css_selector = driver.find_element_by_css_selector(".today .t .sk .zs i")
        result["today_weather"]["air_quality_icon_css"]["width"] = mParserUtil.get_px_value(zs_css_selector.value_of_css_property("width"))
        result["today_weather"]["air_quality_icon_css"]["height"] = mParserUtil.get_px_value(zs_css_selector.value_of_css_property("height"))

        # print "get_today_air_quality_icon_css---end"

    def get_today_limit_icon_css(self, mParserUtil, driver, result):
        # print "get_today_limit_icon_css---start"

        result["today_weather"]["limit_icon_css"] = {}

        therm_css_selector = driver.find_element_by_css_selector(".con .left i, .today .sk .therm")
        result["today_weather"]["limit_icon_css"]["img"] = mParserUtil.get_single_bracket_str(therm_css_selector.value_of_css_property("background-image"))
        limit_css_selector = driver.find_element_by_css_selector(".today .t .sk .limit i")
        result["today_weather"]["limit_icon_css"]["background_position_x"] = mParserUtil.get_px_value(limit_css_selector.value_of_css_property("background-position-x"))
        result["today_weather"]["limit_icon_css"]["background_position_y"] = mParserUtil.get_px_value(limit_css_selector.value_of_css_property("background-position-y"))

        zs_css_selector = driver.find_element_by_css_selector(".today .t .sk .zs i")
        result["today_weather"]["limit_icon_css"]["width"] = mParserUtil.get_px_value(zs_css_selector.value_of_css_property("width"))
        result["today_weather"]["limit_icon_css"]["height"] = mParserUtil.get_px_value(zs_css_selector.value_of_css_property("height"))

        # print "get_today_limit_icon_css---end"

    def get_toaday_detail_weather_icon_css(self, mParserUtil, driver, toaday_detail_weather_element_result):
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

    def get_toaday_detail_weather_wind_icon_css(self, mParserUtil, driver, toaday_detail_weather_element_result):
        # print "get_toaday_detail_weather_wind_icon_css---start"

        wind_icon_css = toaday_detail_weather_element_result["wind_icon_css"]

        wind_css_selector = driver.find_element_by_css_selector(
            "[class='%s']" % wind_icon_css)
        toaday_detail_weather_element_result["wind_icon_css"] = {}
        toaday_detail_weather_element_result["wind_icon_css"]["img"] = mParserUtil.get_single_bracket_str(
            wind_css_selector.value_of_css_property("background-image"))

        wind_direction_css_selector = driver.find_element_by_css_selector(".today .t ul li .win i.%s" % wind_icon_css)
        toaday_detail_weather_element_result["wind_icon_css"]["background_position_x"] = mParserUtil.get_px_value(
            wind_direction_css_selector.value_of_css_property("background-position-x"))
        toaday_detail_weather_element_result["wind_icon_css"]["background_position_y"] = mParserUtil.get_px_value(
            wind_direction_css_selector.value_of_css_property("background-position-y"))

        wind_i_css_selector = driver.find_element_by_css_selector(".today .t ul li .win i")
        toaday_detail_weather_element_result["wind_icon_css"]["width"] = mParserUtil.get_px_value(
            wind_i_css_selector.value_of_css_property("width"))
        toaday_detail_weather_element_result["wind_icon_css"]["height"] = mParserUtil.get_px_value(
            wind_i_css_selector.value_of_css_property("height"))

        # print "get_toaday_detail_weather_wind_icon_css---start"

    def get_toaday_detail_weather_sun_up_icon_css(self, mParserUtil, driver, toaday_detail_weather_element_result):
        # print "get_toaday_detail_weather_sun_up_icon_css---start"

        toaday_detail_weather_element_result["sun_icon_css"] = {}

        therm_css_selector = driver.find_element_by_css_selector(".con .left i, .today .sk .therm")
        toaday_detail_weather_element_result["sun_icon_css"]["img"] = mParserUtil.get_single_bracket_str(therm_css_selector.value_of_css_property("background-image"))
        sun_up_css_selector = driver.find_element_by_css_selector(".today .t ul li .sunUp i")
        toaday_detail_weather_element_result["sun_icon_css"]["background_position_x"] = mParserUtil.get_px_value(sun_up_css_selector.value_of_css_property("background-position-x"))
        toaday_detail_weather_element_result["sun_icon_css"]["background_position_y"] = mParserUtil.get_px_value(sun_up_css_selector.value_of_css_property("background-position-y"))

        sun_css_selector = driver.find_element_by_css_selector(".today .t ul li .sun i")
        toaday_detail_weather_element_result["sun_icon_css"]["width"] = mParserUtil.get_px_value(sun_css_selector.value_of_css_property("width"))
        toaday_detail_weather_element_result["sun_icon_css"]["height"] = mParserUtil.get_px_value(sun_css_selector.value_of_css_property("height"))

        # print "get_toaday_detail_weather_sun_up_icon_css---end"

    def get_toaday_detail_weather_sun_down_icon_css(self, mParserUtil, driver, toaday_detail_weather_element_result):
        # print "get_toaday_detail_weather_sun_down_icon_css---start"

        toaday_detail_weather_element_result["sun_icon_css"] = {}

        therm_css_selector = driver.find_element_by_css_selector(".con .left i, .today .sk .therm")
        toaday_detail_weather_element_result["sun_icon_css"]["img"] = mParserUtil.get_single_bracket_str(therm_css_selector.value_of_css_property("background-image"))
        sun_down_css_selector = driver.find_element_by_css_selector(".today .t ul li .sunDown i")
        toaday_detail_weather_element_result["sun_icon_css"]["background_position_x"] = mParserUtil.get_px_value(sun_down_css_selector.value_of_css_property("background-position-x"))
        toaday_detail_weather_element_result["sun_icon_css"]["background_position_y"] = mParserUtil.get_px_value(sun_down_css_selector.value_of_css_property("background-position-y"))

        sun_css_selector = driver.find_element_by_css_selector(".today .t ul li .sun i")
        toaday_detail_weather_element_result["sun_icon_css"]["width"] = mParserUtil.get_px_value(sun_css_selector.value_of_css_property("width"))
        toaday_detail_weather_element_result["sun_icon_css"]["height"] = mParserUtil.get_px_value(sun_css_selector.value_of_css_property("height"))

        # print "get_toaday_detail_weather_sun_down_icon_css---end"

    def query_city_by_location(self, l, type):
        # http: // gc.ditu.aliyun.com / regeocoding?l = 31.949393, 118.808820 & type = 100
        url = "http://gc.ditu.aliyun.com/regeocoding?l=%s&type=%s" % (l, type)
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        return self.get_http_content(url, headers)

    def get_taobao_anchor(self, page, taobao_anchor_load_listener):
        url = "http://mm.taobao.com/json/request_top_list.htm?page=%s" % page

        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

        # 创建chrome参数对象
        opt = webdriver.ChromeOptions()

        # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
        opt.set_headless()
        prefs = {"profile.managed_default_content_settings.images": 2}
        opt.add_experimental_option("prefs", prefs)

        # 创建chrome无界面对象
        driver = webdriver.Chrome(executable_path=chromedriver, options=opt)

        # driver = EventFiringWebDriver(driver, taobao_anchor_load_listener)

        driver.get(url)

        # time.sleep(5)

        # chain = ActionChains(driver)
        # moveelment = driver.find_element_by_xpath('//div[@class="anchor-card-content"]/div[@class="anchor-card"][1]/div/a/div[@class="anchor-info-body"]/div/div[@class="v3-bond-icon-box"]')
        # chain.move_to_element(moveelment).perform()

        return driver
