#!/usb/bin/env python
#coding=utf-8

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class XPathParserUtil:

    def parse_today_weather_content(self, driver, result):
        # print driver.page_source.decode("utf-8")
        # today_weather_content = driver.find_element_by_xpath('//div[@class="con today clearfix"]')

        result["code"] = 0
        result["desc"] = "success"
        result["today_weather"] = {}

        today_weather_driver = driver.find_element_by_xpath('//div[@class="con today clearfix"]')

        today_weather_simple_content = today_weather_driver.find_element_by_xpath('//input[@id="hidden_title"]').get_attribute("value")
        result["today_weather"]["simple_content"] = today_weather_simple_content


        sk_content = today_weather_driver.find_element_by_xpath('//div[@class="sk"]').get_attribute("innerHTML")



        result["today_weather"]["now_time"] = today_weather_driver.find_element_by_xpath('//div[@class="sk"]/p[@class="time"]/span').text
        result["today_weather"]["temperature"] = today_weather_driver.find_element_by_xpath('//div[@class="sk"]/div[@class="tem"]/span').text

        if "zs h" in sk_content:
            result["today_weather"]["is_h"] = 1
            result["today_weather"]["humidity"] = today_weather_driver.find_element_by_xpath('//div[@class="sk"]/div[@class="zs h"]/em').text
        else:
            result["today_weather"]["is_h"] = 0
            result["today_weather"]["humidity"] = "暂无数据"

        if "zs w" in sk_content:
            result["today_weather"]["is_w"] = 1
            result["today_weather"]["wind_direction"] = today_weather_driver.find_element_by_xpath('//div[@class="sk"]/div[@class="zs w"]/span').text
            result["today_weather"]["wind_value"] = today_weather_driver.find_element_by_xpath('//div[@class="sk"]/div[@class="zs w"]/em').text
        else:
            result["today_weather"]["is_w"] = 0
            result["today_weather"]["wind_direction"] = "风向"
            result["today_weather"]["wind_value"] = "暂无数据"

        if "zs pol" in sk_content:
            result["today_weather"]["is_pol"] = 1
            result["today_weather"]["air_quality"] = today_weather_driver.find_element_by_xpath('//div[@class="sk"]/div[@class="zs pol"]/span/a').text
        else:
            result["today_weather"]["is_pol"] = 0
            result["today_weather"]["air_quality"] = "暂无数据"

        if "zs limit" in sk_content:
            result["today_weather"]["is_limit"] = 1
            limit_content = today_weather_driver.find_element_by_xpath('//div[@class="sk"]/div[@class="zs limit"]/span').text

            limit_class_content = today_weather_driver.find_element_by_xpath('//div[@class="sk"]/div[@class="zs limit"]').get_attribute("innerHTML")
            # print limit_class_content
            if "em" in limit_class_content:
                limit_content = limit_content + today_weather_driver.find_element_by_xpath('//div[@class="sk"]/div[@class="zs limit"]/em').text
            result["today_weather"]["limit_content"] = limit_content
        else:
            result["today_weather"]["is_limit"] = 0
        # today_weather_content = driver.find_element_by_xpath('//div[@class="sk"]/div[@class="therm"]')
        # print today_weather_content.value_of_css_property("therm")
        # today_weather_content = driver.find_element_by_xpath('//div[@class="sk"]/div[@class="therm"]/p/i[@class="t"]')
        # print today_weather_content
        # today_weather_content = driver.find_element_by_xpath('//div[@class="sk"]/div[@class="therm"]/p/i[@class="c"]')
        # print today_weather_content
        return today_weather_driver

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

    def parse_taobao_anchor(self, driver, result):
        try:
            # print driver.page_source.decode("utf-8")

            result["code"] = 0
            result["desc"] = "success"
            result["taobao_anchor_list"] = []




            if "anchor-card-content" not in driver.page_source:
                print "anchor-card-content load no ready"
                print time.asctime(time.localtime(time.time()))
                locator = (By.CLASS_NAME, 'anchor-card-content')
                WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
                print time.asctime(time.localtime(time.time()))

            anchor_card_list_element = driver.find_elements_by_xpath('//div[@class="anchor-card"]')
            print len(anchor_card_list_element)

            if len(anchor_card_list_element) > 0:
                for i in range(len(anchor_card_list_element)):
                    taobao_anchor_element = {}

                    i = i + 1
                    anchor_card_root_xpath = '//div[@class="anchor-card-content"]/div[@class="anchor-card"][%s]' % i

                    taobao_anchor_element["anchor_img"] = driver.find_element_by_xpath(anchor_card_root_xpath + '/div/a/div[@class="ice-img sharp anchor-avatar"]/img').get_attribute("src")

                    anchor_name_element = driver.find_element_by_xpath(anchor_card_root_xpath + '/div/a/div[@class="anchor-info-body"]/h3[@class="anchor-name"]')
                    taobao_anchor_element["anchor_name"] = anchor_name_element.text
                    if "anchor-vflag" in anchor_name_element.get_attribute("innerHTML"):
                        taobao_anchor_element["anchor_vflag"] = driver.find_element_by_xpath(anchor_card_root_xpath + '/div/a/div[@class="anchor-info-body"]/h3[@class="anchor-name"]/img[@class="anchor-vflag"]').get_attribute("src")
                    else:
                        taobao_anchor_element["anchor_vflag"] = ''
                    taobao_anchor_element["fans_count"] = driver.find_element_by_xpath(anchor_card_root_xpath + '/div/a/div[@class="anchor-info-body"]/div[@class="anchor-fans"]/span[@class="fans-count"]').text

                    result["taobao_anchor_list"].append(taobao_anchor_element)
            else:
                result["code"] = -4
                result["desc"] = "获取信息为空"
        except BaseException, e:
            print e
            result["code"] = -3
            result["desc"] = "获取信息异常"
            driver.close()
            driver.quit()
