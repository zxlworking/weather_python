#!/usr/bin/env python
#coding=utf-8

import cgi
import os,sys,json
import re
from com_zxl_common.HttpUtil import *

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    mHttpUtil = HttpUtil()

    weather_page_content_1 = mHttpUtil.get_weather_content_from_zh_tian_qi()

    print "weather_page_content_1::\n"
    print weather_page_content_1

    weather_page_content_2 = mHttpUtil.get_weather_content_detail_from_zh_tian_qi()


    fo = open("foo.txt", "a+")
    fo.write(weather_page_content_2)
    fo.write("\n")
    fo.close()

    print "weather_page_content_2::\n"
    print weather_page_content_2.encode("utf-8")