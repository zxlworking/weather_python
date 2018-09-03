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

    # form = cgi.FieldStorage()
    # city_name = form.getvalue("city").decode("utf-8")

    city_name = '南京'
    # city_name = '哈尔滨'

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
        mHttpUtil = HttpUtil()
        mCityUtil = CityUtil()
        mParserUtil = ParserUtil()
        mCityUtil.init_city_list()
        mCityResult = mCityUtil.query_city_by_city_name(city_name)

        print mCityResult

        if len(mCityResult) > 0:

            driver = mHttpUtil.get_today_weather_from_zh_tian_qi(mCityResult[0]["city_code"])
            weather_page_content = driver.page_source

            today_weather_page_content = mParserUtil.get_zh_tian_qi_today_weather(weather_page_content)
            print "\ntoday_weather_page_content:\n"
            print today_weather_page_content

            if len(today_weather_page_content) > 0:

                today_weather_page_parse_result = mParserUtil.parse_zh_tian_qi_today_weather(today_weather_page_content[0])
                print "\ntoday_weather_page_parse_result:\n"
                print today_weather_page_parse_result

                if len(today_weather_page_parse_result) > 0:
                    result["code"] = 0
                    result["desc"] = "success"
                    result["city_name"] = city_name
                    result["today_weather"] = {}
                    result["today_weather"]["humidity"] = today_weather_page_parse_result[0][0].decode("utf-8")
                    result["today_weather"]["wind_direction"] = today_weather_page_parse_result[0][1].decode("utf-8")
                    result["today_weather"]["wind_value"] = today_weather_page_parse_result[0][2].decode("utf-8")
                    result["today_weather"]["temperature"] = today_weather_page_parse_result[0][3].decode("utf-8")
                    result["today_weather"]["air_quality"] = today_weather_page_parse_result[0][4].decode("utf-8")

                    toaday_detail_weather_page_content = mParserUtil.get_zh_tian_qi_today_detail_weather(today_weather_page_content[0])
                    print "\ntoaday_detail_weather_page_content:\n"
                    print len(toaday_detail_weather_page_content[0])
                    print toaday_detail_weather_page_content

                else:
                    result["code"] = -4
                    result["desc"] = "城市数据解析出错"

                print "\n------------------------class element start------------------------\n"
                #------------------------class element start------------------------
                # < big class ="jpg80 d04" > < / big >
                # link = driver.find_element_by_class_name("jpg80")

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
                #------------------------class element end--------------------------
                print "\n------------------------class element end------------------------\n"


                # weather_content = city_name + \
                #                   "今天" + parser_resutl[0][0].decode("utf-8") + "," + \
                #                   "最低温度" + parser_resutl[0][1].decode("utf-8") + "," + \
                #                   "最高温度" + parser_resutl[0][2].decode("utf-8") + "," + \
                #                   parser_resutl[0][3].decode("utf-8") + "," + \
                #                   parser_resutl[0][4].decode("utf-8") + "," + \
                #                   parser_resutl[0][5].decode("utf-8") + "," + \
                #                   parser_resutl[0][6].decode("utf-8")
                # result["code"] = 0
                # result["weather_content"] = weather_content
                # result["desc"] = "success"
            else:
                result["code"] = -3
                result["desc"] = "获取城市数据失败"

            driver.close()
            driver.quit()

        else:
            result["code"] = -2
            result["desc"] = "没有该城市数据"

    print "Content-type:text/html;charset=UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)
