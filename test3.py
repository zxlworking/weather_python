#!/usr/bin/env python
#coding=utf-8

import cgi
import os,sys,json
import time
from com_zxl_common.CityUtil import *
from com_zxl_common.TodayWeatherUtil import *
from com_zxl_common.ParserUtil import *
from com_zxl_common.XPathParserUtil import *

reload(sys)
sys.setdefaultencoding('utf-8')

result = {}

if __name__ == "__main__":

    form = cgi.FieldStorage()
    addr = form.getvalue("addr")
    if addr is not None:
        addr = addr.decode("utf-8")
    city_name = form.getvalue("city").decode("utf-8")
    # l = form.getvalue("l").decode("utf-8")

    # city_name = '南京市'
    # city_name = '北京'
    # city_name = '泗阳'
    print "city_name============test3--->%s" % city_name
    # l = "31.949393,118.808820"
    # l = "39.9775,116.308781"
    # print "city_name============test2--->%s" % l
    fo = open("foo.txt", "a+")
    if addr is not None:
        fo.write(addr+"--->")
    fo.write(city_name)
    fo.write("\n")
    fo.close()

    if city_name is None:
        result["code"] = -1
        result["desc"] = "参数错误"
    else:
        mTodayWeatherUtil = TodayWeatherUtil()
        mCityUtil = CityUtil()
        mParserUtil = ParserUtil()
        mXPathParserUtil = XPathParserUtil()

        try:

            result["address_info"] = addr
            result["city_name"] = city_name

            mCityUtil.init_city_list()
            mCityResult = mCityUtil.query_city_by_city_name(city_name)

            # print mCityResult

            if len(mCityResult) > 0:

                test_time = time.asctime(time.localtime(time.time()))
                print test_time
                print time.time()
                driver = mTodayWeatherUtil.get_today_weather_from_zh_tian_qi(mCityResult[0]["city_code"])

                test_time = time.asctime(time.localtime(time.time()))
                print test_time
                print time.time()

                try:
                    today_weather_driver = mXPathParserUtil.parse_today_weather_content(driver, result)

                    mParserUtil.parse_today_weather_simple_content(result)

                    mTodayWeatherUtil.get_today_weather_temperature_icon_css(mParserUtil, driver, result)

                    if result["today_weather"]["is_limit"] == 1:
                        mTodayWeatherUtil.get_today_limit_icon_css(mParserUtil, driver, result)

                    if result["today_weather"]["is_h"] == 1:
                        mTodayWeatherUtil.get_today_humidity_icon_css(mParserUtil, driver, result)

                    if result["today_weather"]["is_w"] == 1:
                        mTodayWeatherUtil.get_today_wind_icon_css(mParserUtil, driver, result)

                    if result["today_weather"]["is_pol"] == 1:
                        mTodayWeatherUtil.get_today_air_quality_icon_css(mParserUtil, driver, result)

                    mXPathParserUtil.parse_today_detail_weather_content(today_weather_driver, result)

                    for toaday_detail_weather_element_result in result["today_weather_detail"]:
                        # print toaday_detail_weather_element_result
                        # print toaday_detail_weather_element_result["weather_icon_css"]
                        mTodayWeatherUtil.get_toaday_detail_weather_icon_css(mParserUtil, driver,
                                                                     toaday_detail_weather_element_result)
                        mTodayWeatherUtil.get_toaday_detail_weather_wind_icon_css(mParserUtil, driver,
                                                                          toaday_detail_weather_element_result)
                        if toaday_detail_weather_element_result["is_sun_up"] == 1:
                            mTodayWeatherUtil.get_toaday_detail_weather_sun_up_icon_css(mParserUtil, driver,
                                                                                toaday_detail_weather_element_result)
                        else:
                            mTodayWeatherUtil.get_toaday_detail_weather_sun_down_icon_css(mParserUtil, driver,
                                                                                  toaday_detail_weather_element_result)

                    driver.close()
                    driver.quit()
                except BaseException, e:
                    print e
                    result["code"] = -4
                    result["desc"] = "数据解析异常"
                    driver.close()
                    driver.quit()
                    fo = open("foo.txt", "a+")
                    fo.write("3")
                    fo.write("\n")
                    fo.close()

            else:
                result["code"] = -3
                result["desc"] = "没有该城市数据"
                fo = open("foo.txt", "a+")
                fo.write("2")
                fo.write("\n")
                fo.close()

        except BaseException,e:
            print e
            result["code"] = -2
            result["desc"] = "获取城市信息失败"
            fo = open("foo.txt", "a+")
            fo.write("1")
            fo.write("\n")
            fo.close()


    test_time = time.asctime(time.localtime(time.time()))
    print test_time
    print time.time()

    fo = open("foo.txt", "a+")
    fo.write(json.dumps(result, encoding="utf-8", ensure_ascii=False))
    fo.write("\n")
    fo.close()

    print "Content-type:text/html;charset=UTF-8"
    print "Accept:application/json"
    print "Accept-Charset:UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)