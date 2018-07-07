#!/usr/bin/evn python
#coding=utf-8
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

    def get_city_list(self):
        mCityCount = self.mDBUtil.query_to_city_total_count()
        if mCityCount > 0:
            return self.mDBUtil.query_to_city_by_city_name("")
        else:
            self.save_city_list()

    def save_city_list(self):
        mHttpCityList = self.mHttpUtil.get_city_list()

        mParserCityHandler = ParserCityHandler()
        xml.sax.parseString(mHttpCityList.encode("utf-8"), mParserCityHandler)

        for mCityBean in mParserCityHandler.mCityBeanList:
            print "zxl--->"+mCityBean.mCityName + "--->" + mCityBean.mCityPinYing
            self.mDBUtil.insert_to_city(mCityBean)
        print "zxl--->insert city finish"






if __name__ == "__main__":
    mCityUtil = CityUtil()
    mCityList = mCityUtil.get_city_list()

