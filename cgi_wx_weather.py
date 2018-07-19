#!/usr/bin/env python
#coding=utf-8

import cgi
import os,sys,json
import re
from com_zxl_common.CityUtil import *
from com_zxl_common.HttpUtil import *

reload(sys)
sys.setdefaultencoding('utf-8')

result = {}

# print "Content-type:text/html;charset=UTF-8"
# print ""
#
# print "__name__ = " + __name__
# print "</br>"

if __name__ == "__main__":
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

    form = cgi.FieldStorage()
    keys = form.keys()
    for key in keys:
        if key == "echostr":
            result["echostr"] = form.getvalue(key)

    # print "Content-Type:application/json;charset=UTF-8"
    # print "Accept:application/json"
    # print "Accept-Charset:UTF-8"
    # print ""
    #
    # print json.dumps(result, encoding="utf-8", ensure_ascii=False)

    print "Content-type:text/html;charset=UTF-8"
    print ""

    print result["echostr"]



