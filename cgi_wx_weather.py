#!/usr/bin/env python
#coding=utf-8

import cgi
import os,sys,json
import re
import time
from com_zxl_common.CityUtil import *
from com_zxl_common.HttpUtil import *
from com_zxl_common.PrintUtil import *
from com_zxl_common.ParserUtil import *

reload(sys)
sys.setdefaultencoding('utf-8')

class ParserWxHandler(xml.sax.ContentHandler):
    tag = ""
    wx_msg = {}

    def startElement(self, tag, attributes):
        self.tag = tag
        # mPrintUtil.print_to_file("characters-----------start")
        # mPrintUtil.print_to_file(self.tag)

    def characters(self, content):

        # mPrintUtil.print_to_file(content)

        if self.tag == "ToUserName":
            self.wx_msg["ToUserName"] = content
        elif self.tag == "FromUserName":
            self.wx_msg["FromUserName"] = content
        elif self.tag == "CreateTime":
            self.wx_msg["CreateTime"] = content
        elif self.tag == "MsgType":
            self.wx_msg["MsgType"] = content
        elif self.tag == "Content":
            self.wx_msg["Content"] = content
        elif self.tag == "MsgId":
            self.wx_msg["MsgId"] = content

    def endElement(self, tag):
        self.tag = ""
        # mPrintUtil.print_to_file("characters-----------end")

result = {}
mPrintUtil = PrintUtil()
mParserUtil = ParserUtil()

if __name__ == "__main__":


    form = cgi.FieldStorage()

    if form.list is None:
        mPrintUtil.print_to_file("form.list is none")
    else:
        echostr = form.getvalue("echostr")
        if echostr is None:
            mPrintUtil.print_to_file("echostr is none")
        else:
            mPrintUtil.print_to_file(echostr)
            print "Content-type:text/html;charset=UTF-8"
            print ""

            print echostr

    mPrintUtil.print_to_file("form.value-----------start")
    mPrintUtil.print_to_file(form.value)
    mPrintUtil.print_to_file("form.value-----------end")

    mParserWxHandler = ParserWxHandler()
    xml.sax.parseString(form.value, mParserWxHandler)

    mPrintUtil.print_to_file(mParserWxHandler.wx_msg["FromUserName"])
    mPrintUtil.print_to_file(mParserWxHandler.wx_msg["ToUserName"])
    mPrintUtil.print_to_file(mParserWxHandler.wx_msg["CreateTime"])
    mPrintUtil.print_to_file(mParserWxHandler.wx_msg["MsgType"])
    mPrintUtil.print_to_file(mParserWxHandler.wx_msg["Content"])
    mPrintUtil.print_to_file(mParserWxHandler.wx_msg["MsgId"])

    wx_request_msg = mParserWxHandler.wx_msg["Content"]
    wx_parse_result = mParserUtil.parse_wx_weather_request(wx_request_msg.decode("utf-8"))
    wx_response_txt = "没有该城市的天气"
    if len(wx_parse_result) > 0:
        mPrintUtil.print_to_file(str(len(wx_parse_result[0])))
        city_name = wx_parse_result[0].decode("utf-8")
        if city_name is None:
            wx_response_txt = "没有找到该城市"
        else:
            mHttpUtil = HttpUtil()
            mCityUtil = CityUtil()
            mCityUtil.init_city_list()
            mCityBeanResult = mCityUtil.query_city_by_city_name(city_name)

            if len(mCityBeanResult) > 0:
                city_weather_response = mHttpUtil.get_weather_content_by_city_py(mCityBeanResult[0]["city_py"])
                parser_resutl = mParserUtil.parse_city_weather(city_weather_response)

                if len(parser_resutl) > 0:
                    wx_response_txt = mCityBeanResult[0]["city_name"] + \
                                      "今天" + parser_resutl[0][0].decode("utf-8") + "," + \
                                      "最低温度" + parser_resutl[0][1].decode("utf-8") + "," + \
                                      "最高温度" + parser_resutl[0][2].decode("utf-8") + "," + \
                                      parser_resutl[0][3].decode("utf-8") + "," + \
                                      parser_resutl[0][4].decode("utf-8") + "," + \
                                      parser_resutl[0][5].decode("utf-8") + "," + \
                                      parser_resutl[0][6].decode("utf-8")
                else:
                    wx_response_txt = "没有该城市的天气"
            else:
                wx_response_txt = "没有找到该城市"
    else:
        wx_response_txt = "格式错误"

    wx_response_msg = "<xml>" \
                      "<ToUserName><![CDATA[" + mParserWxHandler.wx_msg["FromUserName"] +"]]></ToUserName>" \
                      "<FromUserName><![CDATA[" + mParserWxHandler.wx_msg["ToUserName"] + "]]></FromUserName>" \
                      "<CreateTime>" + str(int(time.time())) + "</CreateTime>" \
                      "<MsgType><![CDATA[text]]></MsgType>" \
                      "<Content><![CDATA[" + wx_response_txt + "]]></Content>" \
                      "</xml>"
    mPrintUtil.print_to_file(wx_response_msg)

    print "Content-type:text/html;charset=UTF-8"
    print ""

    print wx_response_msg

    # mHttpUtil = HttpUtil()
    # token_result = json.loads(mHttpUtil.get_wx_access_token())
    # mPrintUtil.print_to_file(token_result["access_token"])
    # wx_ip = mHttpUtil.get_wx_ip(token_result["access_token"])
    # mPrintUtil.print_to_file(wx_ip)


    #https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx20280a1b4a149ecb&secret=0964fbba9b0a6fad952083adf33df782
    #%e4%b8%8a%e6%b5%b7
    # form = cgi.FieldStorage()
    # city_name = form.getvalue("city").decode("utf-8")
    #
    #
    # weather_content = ""
    # #http://www.weather.com.cn/data/cityinfo/101010100.html
    # if city_name is None:
    #     result["code"] = -1
    #     result["desc"] = "参数错误"
    # else:
    #     mHttpUtil = HttpUtil()
    #     mCityUtil = CityUtil()
    #     mCityUtil.init_city_list()
    #     mCityResult = mCityUtil.query_city_by_city_name(city_name)
    #
    #     if len(mCityResult) > 0:
    #         weather_py_response = mHttpUtil.get_weather_content_by_city_py(mCityResult[0]["city_py"])
    #         pattern = re.compile(
    #             u"""<div class="left">.*?<span><b>(.*?)</b>(\d+).*?~.*?(\d+)℃</span>.*?</dd>.*?<dd class="shidu"><b>(.*?)%</b><b>(.*?)</b><b>(.*?)</b></dd>.*?<dd class="kongqi" ><h5.*?>(.*?)</h5><h6>PM.*?</div>""",
    #             re.S)
    #         parser_resutl = re.findall(pattern, weather_py_response)
    #         if len(parser_resutl) > 0:
    #
    #             weather_content = city_name + \
    #                               "今天" + parser_resutl[0][0].decode("utf-8") + "," + \
    #                               "最低温度" + parser_resutl[0][1].decode("utf-8") + "," + \
    #                               "最高温度" + parser_resutl[0][2].decode("utf-8") + "," + \
    #                               parser_resutl[0][3].decode("utf-8") + "," + \
    #                               parser_resutl[0][4].decode("utf-8") + "," + \
    #                               parser_resutl[0][5].decode("utf-8") + "," + \
    #                               parser_resutl[0][6].decode("utf-8")
    #             result["code"] = 0
    #             result["weather_content"] = weather_content
    #             result["desc"] = "success"
    #         else:
    #             result["code"] = -2
    #             result["desc"] = "没有该城市数据"
    #     else:
    #         result["code"] = -2
    #         result["desc"] = "没有该城市数据"

    # mHttpUtil = HttpUtil()
    # wx_access_token = mHttpUtil.get_wx_access_token()
    # wx_access_token_json = json.loads(wx_access_token)

    # form = cgi.FieldStorage()
    # keys = form.keys()
    # for key in keys:
    #     if key == "echostr":
    #         result["echostr"] = form.getvalue(key)
    #
    # # print "Content-Type:application/json;charset=UTF-8"
    # # print "Accept:application/json"
    # # print "Accept-Charset:UTF-8"
    # # print ""
    # #
    # # print json.dumps(result, encoding="utf-8", ensure_ascii=False)
    #
    # print "Content-type:text/html;charset=UTF-8"
    # print ""
    #
    # print result["echostr"]



