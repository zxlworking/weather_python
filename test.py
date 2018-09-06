#!/usr/bin/env python
#coding=utf-8

import cgi
import os,sys,json
import re

from selenium import webdriver

from com_zxl_common.CityUtil import *
from com_zxl_common.HttpUtil import *
from com_zxl_common.ParserUtil import *

reload(sys)
sys.setdefaultencoding('utf-8')

result = {}

if __name__ == "__main__":

    form = cgi.FieldStorage()
    city_name = form.getvalue("city").decode("utf-8")


    # city_name = '南京'
    # city_name = '哈尔滨'

    print "city_name============%s" % city_name

    # fo = open("foo.txt", "a+")
    # fo.write(city_name)
    # fo.write("\n")
    # fo.close()

    # test = "<span>-33</span><em>"
    # pattern = re.compile("<span>(-?\d+\.?\d*)</span><em>")
    # print re.findall(pattern, test)

    if city_name is None:
        result["code"] = -1
        result["desc"] = "参数错误"
    else:

        result["city_name"] = city_name

        mHttpUtil = HttpUtil()
        mCityUtil = CityUtil()
        mParserUtil = ParserUtil()
        mCityUtil.init_city_list()
        mCityResult = mCityUtil.query_city_by_city_name(city_name)

        # print mCityResult

        if len(mCityResult) > 0:

            driver = mHttpUtil.get_today_weather_from_zh_tian_qi(mCityResult[0]["city_code"])

            try:
                weather_page_content = driver.page_source

                today_weather_page_content = mParserUtil.get_zh_tian_qi_today_weather(weather_page_content)
                # print "\ntoday_weather_page_content:\n"
                # print today_weather_page_content

                if len(today_weather_page_content) > 0:

                    mParserUtil.parse_zh_tian_qi_today_weather(today_weather_page_content[0], result)

                    if result["code"] == 0:

                        mHttpUtil.get_today_weather_temperature_icon_css(mParserUtil, driver, result)
                        mHttpUtil.get_today_humidity_icon_css(mParserUtil, driver, result)
                        mHttpUtil.get_today_wind_icon_css(mParserUtil, driver, result)
                        mHttpUtil.get_today_air_quality_icon_css(mParserUtil, driver, result)

                        toaday_detail_weather_page_content = mParserUtil.get_zh_tian_qi_today_detail_weather(today_weather_page_content[0])
                        if len(toaday_detail_weather_page_content) > 0:
                            toaday_detail_weather_list_result = mParserUtil.parse_zh_tian_qi_today_detail_weather(toaday_detail_weather_page_content[0])
                            if len(toaday_detail_weather_list_result) > 0:
                                for toaday_detail_weather_element_result in toaday_detail_weather_list_result:
                                    # print toaday_detail_weather_element_result
                                    # print toaday_detail_weather_element_result["weather_icon_css"]
                                    mHttpUtil.get_toaday_detail_weather_icon_css(mParserUtil, driver, toaday_detail_weather_element_result)
                                    mHttpUtil.get_toaday_detail_weather_wind_icon_css(mParserUtil, driver, toaday_detail_weather_element_result)
                                    if toaday_detail_weather_element_result["is_sun_up"] == 1:
                                        mHttpUtil.get_toaday_detail_weather_sun_up_icon_css(mParserUtil, driver, toaday_detail_weather_element_result)
                                    else:
                                        mHttpUtil.get_toaday_detail_weather_sun_down_icon_css(mParserUtil, driver, toaday_detail_weather_element_result)
                                result["today_weather_detail"] = toaday_detail_weather_list_result
                            else:
                                result["code"] = -6
                                result["desc"] = "天气详情解析出错"

                        else:
                            result["code"] = -5
                            result["desc"] = "天气详情获取出错"

                    else:
                        result["code"] = -4
                        result["desc"] = "城市数据解析出错"

                    # print "\n------------------------class element start------------------------\n"
                    #------------------------class element start------------------------
                    # < big class ="jpg80 d04" > < / big >
                    # link = driver.find_element_by_class_name("jpg80")

                    # link = driver.find_element_by_css_selector("[class='jpg80 n00']")
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
                    #------------------------class element end--------------------------
                    # print "\n------------------------class element end------------------------\n"
                else:
                    result["code"] = -3
                    result["desc"] = "获取城市数据失败"

                driver.close()
                driver.quit()
            except BaseException, e:
                print e.message
                driver.close()
                driver.quit()

        else:
            result["code"] = -2
            result["desc"] = "没有该城市数据"

    print "Content-type:text/html;charset=UTF-8"
    print "Accept:application/json"
    print "Accept-Charset:UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)
