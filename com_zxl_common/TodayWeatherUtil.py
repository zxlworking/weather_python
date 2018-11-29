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


class TodayWeatherUtil:

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
