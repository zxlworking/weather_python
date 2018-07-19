#!/usr/bin/evn python
# coding=utf-8
import xml.sax
import sys
from com_zxl_common.HttpUtil import *
from com_zxl_data.CityBean import *
from com_zxl_common.DBUtil import *


# default_encoding = 'utf-8'
# if sys.getdefaultencoding() != default_encoding:
#     reload(sys)
#     sys.setdefaultencoding(default_encoding)


class ParserCityHandler(xml.sax.ContentHandler):
    mCityBeanList = []
    mCityBean = CityBean()
    contentData = ""

    def startElement(self, tag, attributes):
        self.mCityBean = CityBean()
        self.contentData = tag
        if tag == "d":
            d1 = attributes["d1"]
            self.mCityBean.mCityCode = d1
            d2 = attributes["d2"]
            self.mCityBean.mCityName = d2
            d3 = attributes["d3"]
            self.mCityBean.mCityPinYing = d3
            d4 = attributes["d4"]
            self.mCityBean.mProvince = d4

    def endElement(self, tag):
        self.contentData = ""
        self.mCityBeanList.append(self.mCityBean)


class CityUtil:
    mDBUtil = DBUtil()
    mHttpUtil = HttpUtil()

    def init_city_list(self):
        mCityCount = self.mDBUtil.query_to_city_total_count()
        print mCityCount
        if mCityCount <= 0:
            self.save_city_list()

    def save_city_list(self):
        mHttpCityList = self.mHttpUtil.get_city_list()

        mParserCityHandler = ParserCityHandler()
        xml.sax.parseString(mHttpCityList.encode("utf-8"), mParserCityHandler)

        for mCityBean in mParserCityHandler.mCityBeanList:
            print "zxl--->" + mCityBean.mCityName + "--->" + mCityBean.mCityPinYing
            self.mDBUtil.insert_to_city(mCityBean)
        print "zxl--->insert city finish"

    def query_city_by_city_name(self, city_name):
        return self.mDBUtil.query_to_city_by_city_name(city_name)


if __name__ == "__main__":
    mCityUtil = CityUtil()
    mCityUtil.init_city_list()
    mCityResult = mCityUtil.query_city_by_city_name("南京市")
    print len(mCityResult)
    if len(mCityResult) > 0:
        print "zxl--->" + mCityResult[0]["city_code"] + "--->" + mCityResult[0]["city_py"] + "--->" + mCityResult[0][
            "city_name"]


