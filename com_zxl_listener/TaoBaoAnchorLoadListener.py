#!/usb/bin/env python
#coding=utf-8

from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class TaoBaoAnchorLoadListener(AbstractEventListener):

    def __init__(self, r):
        self.result = r

    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)

    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)

        # chain = ActionChains(driver)
        # moveelment = driver.find_element_by_xpath('//div[@class="anchor-card-content"]/div[@class="anchor-card"][1]/div/a/div[@class="anchor-info-body"]/div/div[@class="v3-bond-icon-box"]')
        # chain.move_to_element(moveelment).perform()

    def before_navigate_back(self, driver):
        print("before_navigate_back")

    def after_navigate_back(self, driver):
        print("after_navigate_back")

    def before_navigate_forward(self, driver):
        print("before_navigate_forward")

    def after_navigate_forward(self, driver):
        print("after_navigate_forward")

    def before_find(self, by, value, driver):
        print("before_find")

    def after_find(self, by, value, driver):
        print("after_find")

    def before_click(self, element, driver):
        print("before_click")

    def after_click(self, element, driver):
        print("after_click")

    def before_change_value_of(self, element, driver):
        print("before_change_value_of")

    def after_change_value_of(self, element, driver):
        print("after_change_value_of")
        c = element.get_attribute("class")
        print c

    def before_execute_script(self, script, driver):
        print("before_execute_script")

    def after_execute_script(self, script, driver):
        print("after_execute_script")

    def before_close(self, driver):
        print("before_close")

    def after_close(self, driver):
        print("after_close")

    def before_quit(self, driver):
        print("before_quit")

    def after_quit(self, driver):
        print("after_quit")

    def on_exception(self, exception, driver):
        print("on_exception")
