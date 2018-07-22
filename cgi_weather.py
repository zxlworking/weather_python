#!/usr/bin/env python
# coding=utf-8

import cgi
import re
import os, sys, json
from com_zxl_common.CityUtil import *
from com_zxl_common.ParserUtil import *

reload(sys)
sys.setdefaultencoding('utf-8')

result = {}

form = cgi.FieldStorage()
fo = open("foo.txt", "a+")
fo.write(form.value)
fo.write("\n")
fo.close()
json_str = json.loads(form.value)
# json_dict = JSONDecoder().decode(json_str)

weather_content = "你好"

version = json_str["version"]
shouldEndSession = True

output = {}
response = {}
response["output"] = {}

intent = {}
context = {}
directives = {}

if json_str["request"]["type"] == "IntentRequest":
    shouldEndSession = True
    weather_content = "暂无天气数据"
    intent = json_str["request"]["intent"]
    card = {}
    response["card"] = {}

    directives["directives"] = []
    directive = {}
    directive["intent"] = intent
    directive["slotName"] = "city"
    directive["type"] = "Dialog.ConfirmSlot"
    directives["directives"].append(directive)
    result["directives"] = directives["directives"]

    result["intent"] = "weather"

    city_name = json_str["request"]["intent"]["slots"]["city"]["value"];
    fo = open("foo.txt", "a+")
    fo.write(city_name)
    fo.write("\n")
    fo.close()

    context["city_name"] = city_name

    # http://www.weather.com.cn/data/cityinfo/101010100.html
    mHttpUtil = HttpUtil()
    mCityUtil = CityUtil()
    mParserUtil = ParserUtil()
    mCityUtil.init_city_list()
    mCityResult = mCityUtil.query_city_by_city_name(city_name)

    if len(mCityResult) > 0:
        context["city_code"] = mCityResult[0]["city_code"]

        weather_py_response = mHttpUtil.get_weather_content_by_city_py(mCityResult[0]["city_py"])

        parser_resutl = mParserUtil.parse_city_weather(weather_py_response)

        # print parser_resutl[0][0].decode("utf-8")
        # print parser_resutl[0][1].decode("utf-8")
        # print parser_resutl[0][2].decode("utf-8")
        # print parser_resutl[0][3].decode("utf-8")
        # print parser_resutl[0][4].decode("utf-8")
        # print parser_resutl[0][5].decode("utf-8")
        # print parser_resutl[0][6].decode("utf-8")

        if len(parser_resutl) > 0:

            weather_content = city_name + \
                              "今天" + parser_resutl[0][0].decode("utf-8") + "," + \
                              "最低温度" + parser_resutl[0][1].decode("utf-8") + "," + \
                              "最高温度" + parser_resutl[0][2].decode("utf-8") + "," + \
                              parser_resutl[0][3].decode("utf-8") + "," + \
                              parser_resutl[0][4].decode("utf-8") + "," + \
                              parser_resutl[0][5].decode("utf-8") + "," + \
                              parser_resutl[0][6].decode("utf-8")

            fo = open("foo.txt", "a+")
            # fo.write(weather_content)
            fo.close()
        else:
            fo = open("foo.txt", "a+")
            # fo.write("***************************")
            fo.close()

        # weather_response = mHttpUtil.get_weather_content_by_city_code(mCityResult[0]["city_code"])
        # weather_response_json_str = json.loads(weather_response)
        # weather_content = weather_response_json_str["weatherinfo"]["city"] + "今天" + weather_response_json_str["weatherinfo"]["weather"] + "最低温度" + weather_response_json_str["weatherinfo"]["temp1"] + "最高温度" + weather_response_json_str["weatherinfo"]["temp2"]

        ########################################
elif json_str["request"]["type"] == "LaunchRequest":
    shouldEndSession = False

    directives["directives"] = []
    directive = {}
    directive["intent"] = {}
    directive["intent"]["confirmResult"] = "NONE"
    directive["intent"]["name"] = "weather"
    directive["intent"]["slots"] = {}
    directive["intent"]["slots"]["category"] = {}
    directive["intent"]["slots"]["category"]["name"] = "city"
    directive["slotName"] = "city"
    directive["type"] = "Dialog.ElicitSlot"
    directives["directives"].append(directive)
    result["directives"] = directives["directives"]

    weather_content = "你想知道哪里的天气?"

########################################

response["output"]["type"] = "PlainText"
response["output"]["text"] = weather_content
response["reprompt"] = {}
response["reprompt"]["type"] = "PlainText"
response["reprompt"]["text"] = weather_content

result["version"] = version
result["contexts"] = context

result["shouldEndSession"] = shouldEndSession
result["response"] = response

resultStr = json.dumps(result, encoding="utf-8", ensure_ascii=False);

fo = open("foo.txt", "a+")
fo.write(resultStr)
fo.write("\n")
fo.close()

print "Content-Type:application/json;charset=UTF-8"
print "Accept:application/json"
print "Accept-Charset:UTF-8"
print ""

# print "{}"
print resultStr




