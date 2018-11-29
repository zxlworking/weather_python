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


class TaoBaoAnchorUtil:

    def get_taobao_anchor(self, page, taobao_anchor_load_listener):
        url = "http://mm.taobao.com/json/request_top_list.htm?page=%s" % page

        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

        # 创建chrome参数对象
        opt = webdriver.ChromeOptions()

        # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
        opt.set_headless()
        prefs = {"profile.managed_default_content_settings.images": 2}
        opt.add_experimental_option("prefs", prefs)
        # opt.add_argument('Referer="http://mm.taobao.com"')

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

        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
        cookies = pickle.load(open("cookies.pkl", "rb"))
        if cookies is None or len(cookies) == 0:
            pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)


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
