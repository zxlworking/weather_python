#!/usr/bin/env python
# coding=utf-8
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

        # opt.add_argument(
        # 'authority="v.taobao.com"' + "\n"
        #     'method="GET"' + "\n"
        #     'path="/v/content/live?catetype=704&from=taonvlang & page = 2"' + "\n"
        #     'scheme="https"' + "\n"
        #     'accept="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"' + "\n"
        #     'accept-encoding="gzip,deflate,br"' + "\n"
        #     'accept-language="zh - CN,zh;q = 0.9"' + "\n"
        #     'cookie="_tb_token_=undefined;cna=GC5mEj/alUECAd3it6rWpcD2;thw=cn;miid=774333864791300153;enc=tU0%2BrzUbyATyb3sYiaZUhXgeHDCyGxFh%2BfDMe5Q1dHi8j5gW4hrH%2FOZVLUaC%2F0dmwVDxjxFi9%2B1n9VnPcTnkHw%3D%3D;hng=CN%7Czh-CN%7CCNY%7C156;t=281e4c04bcc183892f168906f4f51774;JSESSIONID=F480C8AE7839E0E68C4F87BF1D28F678;v=0;cookie2=10747f1c5f5d3b4f9ab83a1b52b8fcbd;_tb_token_=eb09e84ed3f30;uc1=cookie14=UoTfLJFAE5UaQw%3D%3D;isg=BL6-x1ndac0H8r1AjvCx1BmOD9QKJYV1WsBGBWjHKoH8C17l0I_SieTph5diM3qR"' + "\n"
        #     'upgrade-insecure-requests="1"' + "\n"
        #     'user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"')
        # opt.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"')

        # opt.add_argument("--proxy-server=http://180.118.134.76:9000")

        # 创建chrome无界面对象
        driver = webdriver.Chrome(executable_path=chromedriver, options=opt)

        # driver = EventFiringWebDriver(driver, taobao_anchor_load_listener)

        driver.get(url)


        # if page != "1":
        if "next-input next-input-single next-input-medium" not in driver.page_source:
            print "next-input load no ready"
            print time.asctime(time.localtime(time.time()))
            locator = (By.CLASS_NAME, 'next-input next-input-single next-input-medium')
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
            print time.asctime(time.localtime(time.time()))
        next_input_element = driver.find_element_by_xpath(
            '//span[@class="next-input next-input-single next-input-medium"]/input')
        next_input_element.clear()
        next_input_element.send_keys(page)
        next_btn_element = driver.find_element_by_xpath(
            '//button[@class="next-btn next-btn-normal next-btn-medium next-pagination-go"]')
        next_btn_element.click()

        # time.sleep(5)

        # chain = ActionChains(driver)
        # moveelment = driver.find_element_by_xpath('//div[@class="anchor-card-content"]/div[@class="anchor-card"][1]/div/a/div[@class="anchor-info-body"]/div/div[@class="v3-bond-icon-box"]')
        # chain.move_to_element(moveelment).perform()

        return driver
