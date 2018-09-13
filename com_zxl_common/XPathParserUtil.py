#!/usb/bin/env python
#coding=utf-8

from lxml import etree
from selenium import webdriver


class XPathParserUtil:

    def parse_today_weather_content(self, driver, result):
        # print driver.page_source.decode("utf-8")
        # today_weather_content = driver.find_element_by_xpath('//div[@class="con today clearfix"]')

        result["code"] = 0
        result["desc"] = "success"
        result["today_weather"] = {}

        result["today_weather"]["now_time"] = driver.find_element_by_xpath('//div[@class="sk"]/p[@class="time"]/span').text
        # result["today_weather"]["humidity"] = driver.find_element_by_xpath('//div[@class="sk"]/div[@class="zs h"]/span').text
        result["today_weather"]["humidity"] = driver.find_element_by_xpath('//div[@class="sk"]/div[@class="zs h"]/em').text
        result["today_weather"]["wind_direction"] = driver.find_element_by_xpath('//div[@class="sk"]/div[@class="zs w"]/span').text
        result["today_weather"]["wind_value"] = driver.find_element_by_xpath('//div[@class="sk"]/div[@class="zs w"]/em').text
        result["today_weather"]["temperature"] = driver.find_element_by_xpath('//div[@class="sk"]/div[@class="tem"]/span').text
        result["today_weather"]["air_quality"] = driver.find_element_by_xpath('//div[@class="sk"]/div[@class="zs pol"]/span/a').text
        # today_weather_content = driver.find_element_by_xpath('//div[@class="sk"]/div[@class="therm"]')
        # print today_weather_content.value_of_css_property("therm")
        # today_weather_content = driver.find_element_by_xpath('//div[@class="sk"]/div[@class="therm"]/p/i[@class="t"]')
        # print today_weather_content
        # today_weather_content = driver.find_element_by_xpath('//div[@class="sk"]/div[@class="therm"]/p/i[@class="c"]')
        # print today_weather_content

    def parse_today_detail_weather_content(self, driver, result):

        # x = driver.find_element_by_xpath('//ul[@class="clearfix"]').get_attribute("innerHTML")
        # print x

        is_first_sun_up = True
        try:
            #白天
            clearfix_li_1_content = driver.find_element_by_xpath('//ul[@class="clearfix"]/li[1]').get_attribute("innerHTML")
            is_first_sun_up = "sun sunUp" in clearfix_li_1_content
        except BaseException,e:
            print "parse_today_detail_weather_content exception"
            print e
            #夜晚
            is_first_sun_up = False

        toaday_detail_weather_list_result = []
        result["today_weather_detail"] = toaday_detail_weather_list_result

        print is_first_sun_up

        if is_first_sun_up:
            self.parse_day_detail_weather_content(True, driver, result)
            self.parse_night_detail_weather_content(False, driver, result)
        else:
            self.parse_night_detail_weather_content(True, driver, result)
            self.parse_day_detail_weather_content(False, driver, result)

    def parse_day_detail_weather_content(self, is_first_sun_up, driver, result):

        toaday_detail_weather_element = {}

        append_str = ""
        if is_first_sun_up:
            append_str = "[1]"
        else:
            append_str = "[2]"


        toaday_detail_weather_element["is_sun_up"] = 1
        toaday_detail_weather_element["title"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/h1' % append_str).text
        toaday_detail_weather_element["weather_icon_css"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/big' % append_str).get_attribute("class")
        toaday_detail_weather_element["weather"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/p[@class="wea"]' % append_str).text
        toaday_detail_weather_element["weather_desc"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/div[@class="sky"]/span' % append_str).get_attribute("innerHTML")
        toaday_detail_weather_element["temperature"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/p[@class="tem"]/span' % append_str).text
        toaday_detail_weather_element["wind_icon_css"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/p[@class="win"]/i' % append_str).get_attribute("class")
        toaday_detail_weather_element["wind_direction"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/p[@class="win"]/span' % append_str).get_attribute("title")
        toaday_detail_weather_element["wind_value"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/p[@class="win"]/span' % append_str).text
        toaday_detail_weather_element["sun_time"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/p[@class="sun sunUp"]' % append_str).text
        result["today_weather_detail"].append(toaday_detail_weather_element)

    def parse_night_detail_weather_content(self, is_first_sun_down, driver, result):

        toaday_detail_weather_element = {}

        append_str = ""
        if is_first_sun_down:
            append_str = "[1]"
        else:
            append_str = "[2]"

        toaday_detail_weather_element["is_sun_up"] = 0
        toaday_detail_weather_element["title"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/h1' % append_str).text
        toaday_detail_weather_element["weather_icon_css"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/big' % append_str).get_attribute("class")
        toaday_detail_weather_element["weather"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/p[@class="wea"]' % append_str).text
        toaday_detail_weather_element["temperature"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/p[@class="tem"]/span' % append_str).text
        toaday_detail_weather_element["wind_icon_css"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/p[@class="win"]/i' % append_str).get_attribute("class")
        toaday_detail_weather_element["wind_direction"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/p[@class="win"]/span' % append_str).get_attribute("title")
        toaday_detail_weather_element["wind_value"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/p[@class="win"]/span' % append_str).text
        toaday_detail_weather_element["sun_time"] = driver.find_element_by_xpath('//ul[@class="clearfix"]/li%s/p[@class="sun sunDown"]' % append_str).text
        result["today_weather_detail"].append(toaday_detail_weather_element)