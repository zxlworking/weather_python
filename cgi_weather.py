#!/usr/bin/env python
#coding=utf-8

import cgi
import os,sys,json
import re
from com_zxl_common.CityUtil import *

reload(sys)
sys.setdefaultencoding('utf-8')

result = {}

form = cgi.FieldStorage()
#json_str = json.loads(form.value)
#json_dict = JSONDecoder().decode(json_str)


# test_str = """
# {
# "contexts": "{"city_name": "南京市"}",
# "version": "1.0",
# "directives": [
# 	{
# 		"type": "Dialog.ConfirmSlot",
# 		"intent": {
# 			"slots": {
# 				"city": {
# 					"value": "南京市", "name": "city", "confirmResult": "NONE", "matched": true
# 				}
# 			},
# 			"name": "weather",
# 			"confirmResult": "NONE"
# 		},
# 		"slotName": "city"
# 	}
# ],
# "intent": "weather",
# "shouldEndSession": false,
# "response": "{
# 	"output": {
# 		"text": "南京的天气晴天", "type": "PlainText"
# 	},
# 	"reprompt": {
# 		"text": "南京的天气晴天", "type": "PlainText"
# 	},
# 	"card": {
# 	}
# }"
# }
# """
# json_str = json.loads(test_str)


# city_name = json_str["request"]["intent"]["slots"]["city"]["value"];
city_name = "南京市";
fo = open("foo.txt", "a+")
fo.write(city_name)
fo.close()

context = {}
context["city_name"] = city_name


#http://www.weather.com.cn/data/cityinfo/101010100.html
mHttpUtil = HttpUtil()
mCityUtil = CityUtil()
mCityUtil.init_city_list()
mCityResult = mCityUtil.query_city_by_city_name(city_name)
weather_content = "暂无天气数据"
if len(mCityResult) > 0:
    context["city_code"] = mCityResult[0]["city_code"]

    weather_py_response = mHttpUtil.get_weather_content_by_city_py(mCityResult[0]["city_py"])
    pattern = re.compile(
        u"""<div class="left">.*?<span><b>(.*?)</b>(\d+).*?~.*?(\d+)℃</span>.*?</dd>.*?<dd class="shidu"><b>(.*?)%</b><b>(.*?)</b><b>(.*?)</b></dd>.*?<dd class="kongqi" ><h5.*?>(.*?)</h5><h6>PM.*?</div>""",
        re.S)
    parser_resutl = re.findall(pattern, weather_py_response)

    #print parser_resutl[0][0].decode("utf-8")
    #print parser_resutl[0][1].decode("utf-8")
    #print parser_resutl[0][2].decode("utf-8")
    #print parser_resutl[0][3].decode("utf-8")
    #print parser_resutl[0][4].decode("utf-8")
    #print parser_resutl[0][5].decode("utf-8")
    #print parser_resutl[0][6].decode("utf-8")
    
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
        #fo.write(weather_content)
        fo.close()
    else:
        fo = open("foo.txt", "a+")
        #fo.write("***************************")
        fo.close()
    
    #weather_response = mHttpUtil.get_weather_content_by_city_code(mCityResult[0]["city_code"])
    #weather_response_json_str = json.loads(weather_response)
    #weather_content = weather_response_json_str["weatherinfo"]["city"] + "今天" + weather_response_json_str["weatherinfo"]["weather"] + "最低温度" + weather_response_json_str["weatherinfo"]["temp1"] + "最高温度" + weather_response_json_str["weatherinfo"]["temp2"]

    


########################################
# version = json_str["version"]
version = "1.0"

# intent = json_str["request"]["intent"]
intent = ""




output = {}
response = {}
response["output"] = {}
response["output"]["type"] = "PlainText"
response["output"]["text"] = weather_content
response["reprompt"] = {}
response["reprompt"]["type"] = "PlainText"
response["reprompt"]["text"] = weather_content


card = {}
response["card"] = {}

directives = {}
directives["directives"] = []
directive = {}
directive["intent"] = intent
directive["slotName"] = "city"
directive["type"] = "Dialog.ConfirmSlot"
directives["directives"].append(directive)

shouldEndSession = True
########################################

# 打开一个文件
#fo = open("foo.txt", "a+")
#fo.write(json_str["version"])
#fo.write(city_name)


#print len(mCityResult)
#if len(mCityResult) > 0:
#    fo.write("zxl--->"+mCityResult[0]["city_code"] + "--->" + mCityResult[0]["city_py"] + "--->" + mCityResult[0]["city_name"])

#fo.close()



result["version"] = version
result["intent"] = "weather"

result["contexts"] = context
result["directives"] = directives["directives"]
result["shouldEndSession"] = shouldEndSession
result["response"] = response

resultStr = json.dumps(result, encoding="utf-8", ensure_ascii=False);

fo = open("foo.txt", "a+")
#fo.write(resultStr)
fo.close()

print "Content-Type:application/json;charset=UTF-8"
print "Accept:application/json"
print "Accept-Charset:UTF-8"
print ""

#print "{}"
print resultStr


