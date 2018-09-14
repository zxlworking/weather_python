#!/usr/bin/env python
#coding=utf-8

import cgi
import os,sys,json
import time
from com_zxl_common.CityUtil import *
from com_zxl_common.HttpUtil import *
from com_zxl_common.ParserUtil import *
from com_zxl_common.XPathParserUtil import *

reload(sys)
sys.setdefaultencoding('utf-8')

result = {}

if __name__ == "__main__":

    mHttpUtil = HttpUtil()
    mCityUtil = CityUtil()
    mParserUtil = ParserUtil()
    mXPathParserUtil = XPathParserUtil()

    try:

        mCityUtil.init_city_list()
        mCityListResult = mCityUtil.query_all_city()

        result["code"] = 0
        result["desc"] = "success"
        result["city_list"] = mCityListResult

    except BaseException, e:
        print e
        result["code"] = -1
        result["desc"] = "获取数据失败"


    print "Content-type:text/html;charset=UTF-8"
    print "Accept:application/json"
    print "Accept-Charset:UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)