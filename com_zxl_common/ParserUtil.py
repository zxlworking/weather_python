#!C:\Python27\python.exe
#coding=utf-8
import re
from com_zxl_common.PrintUtil import *


class ParserUtil:

    # def __init__(self):
    # self.show("PrintUtil init...")


    def parse_city_weather(self, city_weather_content):
        pattern = re.compile(u"""<div class="left">.*?<span><b>(.*?)</b>(\d+).*?~.*?(\d+)℃</span>.*?</dd>.*?<dd class="shidu"><b>(.*?)%</b><b>(.*?)</b><b>(.*?)</b></dd>.*?<dd class="kongqi" ><h5.*?>(.*?)</h5><h6>PM.*?</div>""",re.S)
        parser_resutl = re.findall(pattern, city_weather_content)
        return parser_resutl

    def parse_wx_weather_request(self, wx_request):
        # mPrintUtil = PrintUtil()
        # mPrintUtil.print_to_file("parse_wx_weather_request::wx_request = ")
        # mPrintUtil.print_to_file(wx_request)
        pattern = re.compile(u""".*?([\u4E00-\u9FA5]+)天气.*?""", re.S)
        parser_resutl = re.findall(pattern, wx_request)
        # mPrintUtil.print_to_file(str(len(parser_resutl)))
        return parser_resutl

    def parse_wx_qsbk_request(self, wx_request):
        # mPrintUtil = Print_to_file(wx_request)Util()
        # mPrintUtil.print_to_file("parse_wx_weather_request::wx_request = ")
        # mPrintUtil.print
        pattern = re.compile(u""".*?(笑话).*?""",re.S)
        parser_resutl = re.findall(pattern, wx_request)
        # mPrintUtil.print_to_file(str(len(parser_resutl)))
        return parser_resutl

    def get_zh_tian_qi_today_weather(self, weather_page_content):
        print "get_zh_tian_qi_today_weather---start"
        pattern = re.compile(u"""<div class="con today clearfix">(.*?)<div class="tq_zx" id="tq_zx">""", re.S)
        today_weather_page_content = re.findall(pattern, weather_page_content)
        print "get_zh_tian_qi_today_weather---end"
        return today_weather_page_content

    def get_zh_tian_qi_today_detail_weather(self, today_weather_page_content):
        print "get_zh_tian_qi_today_detail_weather---start"

        pattern = re.compile(u""".*?<ul class="clearfix">(.*?)<input type=".*?" id=".*?" value=".*?" />.*?""", re.S)
        toaday_detail_weather_page_content = re.findall(pattern, today_weather_page_content)

        print "get_zh_tian_qi_today_detail_weather---end"
        return toaday_detail_weather_page_content

    def parse_zh_tian_qi_today_weather(self, today_weather_page_content, result):
        print "parse_zh_tian_qi_today_weather---start"
        # print today_weather_page_content.decode("utf-8")
        # 实况==湿度==风向==风级==温度==空气质量
        # (^(\-|\+)?\d+(\.\d+)?)
        pattern = re.compile(u""".*?<div class="sk">.*?<p class="time"><span>(.*?)</span></p><div class="zs h"><i></i><span>.*?</span><em>(.*?)</em></div><div class="zs w"><i></i><span>(.*?)</span><em>(.*?)级</em></div><div class="tem"><span>(-?\d+\.?\d*)</span><em>℃</em></div><p></p><div class="therm"><p><i class="t"></i><i class="c" style="height:.*?"></i></p></div><div class="zs pol"><i></i><span><a.*?>(.*?)</a></span></div></div>.*?<ul class="clearfix">.*?""",re.S)
        today_weather_page_parse_result = re.findall(pattern, today_weather_page_content)

        if len(today_weather_page_parse_result) > 0:
            result["code"] = 0
            result["desc"] = "success"
            result["today_weather"] = {}
            result["today_weather"]["now_time"] = today_weather_page_parse_result[0][0].decode("utf-8")
            result["today_weather"]["humidity"] = today_weather_page_parse_result[0][1].decode("utf-8")
            result["today_weather"]["wind_direction"] = today_weather_page_parse_result[0][2].decode("utf-8")
            result["today_weather"]["wind_value"] = today_weather_page_parse_result[0][3].decode("utf-8")
            result["today_weather"]["temperature"] = today_weather_page_parse_result[0][4].decode("utf-8")
            result["today_weather"]["air_quality"] = today_weather_page_parse_result[0][5].decode("utf-8")
        else:
            result["code"] = -4

        print "parse_zh_tian_qi_today_weather---end"
        # return today_weather_page_parse_result

    def parse_zh_tian_qi_today_detail_weather(self, toaday_detail_weather_page_content):
        print "parse_zh_tian_qi_today_detail_weather---start"
        # print toaday_detail_weather_page_content.decode("utf-8")
        # print "\n"

        pattern = re.compile(u"""(.*?)<div class="slid">(.*?)</ul>
</div>.*?""", re.S)
        toaday_detail_weather_list_content = re.findall(pattern, toaday_detail_weather_page_content)

        # print "toaday_detail_weather_list_content===>length\n"
        # print len(toaday_detail_weather_list_content)
        # print "\n"
        # print toaday_detail_weather_list_content

        toaday_detail_weather_list_result = []
        i = 0
        for toaday_detail_weather_element_content in toaday_detail_weather_list_content[0]:
            pattern = re.compile(u""".*?(<p class="sun sunUp">).*?""", re.S)
            is_sun_up = re.findall(pattern, toaday_detail_weather_element_content)

            # print toaday_detail_weather_element_content.decode("utf-8")
            # print is_daytime
            # print "\n"

            if len(is_sun_up) > 0:
                toaday_detail_weather_element = {}
                #标题==天气图标样式==天气==天气描述==气温==风向图标样式==风向==风级==日出时间
                pattern = re.compile(u""".*?<li>.*?<h1>(.*?)</h1>.*?<big class="(.*?)"></big>.*?<p class="wea" title=".*?">(.*?)</p>.*?<div class="sky">.*?<span class=".*?">(.*?)</span>.*?<i class="icon"></i>.*?<div class="skypop">.*?</div>.*?</div>.*?<p class="tem">.*?<span>(.*?)</span><em>°C</em>.*?</p>.*?<p class="win">.*?<i class="(.*?)"></i>.*?<span class="" title="(.*?)">(.*?)</span>.*?</p>.*?<p class="sun sunUp"><i></i>.*?<span>(.*?)</span>.*?</p>.*?""", re.S)
                toaday_detail_weather_element_result = re.findall(pattern, toaday_detail_weather_element_content)

                # print "toaday_detail_weather_element_result\n"
                # print toaday_detail_weather_element_result

                if len(toaday_detail_weather_element_result) > 0:
                    toaday_detail_weather_element["title"] = toaday_detail_weather_element_result[0][0].decode("utf-8")
                    toaday_detail_weather_element["weather_icon_css"] = toaday_detail_weather_element_result[0][1].decode("utf-8")
                    toaday_detail_weather_element["weather"] = toaday_detail_weather_element_result[0][2].decode("utf-8")
                    toaday_detail_weather_element["weather_desc"] = toaday_detail_weather_element_result[0][3].decode("utf-8")
                    toaday_detail_weather_element["temperature"] = toaday_detail_weather_element_result[0][4].decode("utf-8")
                    toaday_detail_weather_element["wind_icon_css"] = toaday_detail_weather_element_result[0][5].decode("utf-8")
                    toaday_detail_weather_element["wind_direction"] = toaday_detail_weather_element_result[0][6].decode("utf-8")
                    toaday_detail_weather_element["wind_value"] = toaday_detail_weather_element_result[0][7].decode("utf-8")
                    toaday_detail_weather_element["sun_time"] = toaday_detail_weather_element_result[0][8].decode("utf-8")
                    toaday_detail_weather_element["is_sun_up"] = 1
                    toaday_detail_weather_list_result.append(toaday_detail_weather_element)
            else:
                toaday_detail_weather_element = {}
                # 标题==天气图标样式==天气==气温==风向图标样式==风向==风级==日落时间
                pattern = re.compile(
                    u""".*?<li>.*?<h1>(.*?)</h1>.*?<big class="(.*?)"></big>.*?<p class="wea" title=".*?">(.*?)</p>.*?<div class="sky">.*?</div>.*?<p class="tem">.*?<span>(.*?)</span><em>°C</em>.*?</p>.*?<p class="win">.*?<i class="(.*?)"></i>.*?<span class="" title="(.*?)">(.*?)</span>.*?</p>.*?<p class="sun sunDown"><i></i>.*?<span>(.*?)</span>.*?</p>.*?""",
                    re.S)
                toaday_detail_weather_element_result = re.findall(pattern, toaday_detail_weather_element_content)

                # print "toaday_detail_weather_element_result\n"
                # print toaday_detail_weather_element_result

                if len(toaday_detail_weather_element_result) > 0:
                    toaday_detail_weather_element["title"] = toaday_detail_weather_element_result[0][0].decode("utf-8")
                    toaday_detail_weather_element["weather_icon_css"] = toaday_detail_weather_element_result[0][1].decode("utf-8")
                    toaday_detail_weather_element["weather"] = toaday_detail_weather_element_result[0][2].decode("utf-8")
                    toaday_detail_weather_element["temperature"] = toaday_detail_weather_element_result[0][3].decode("utf-8")
                    toaday_detail_weather_element["wind_icon_css"] = toaday_detail_weather_element_result[0][4].decode("utf-8")
                    toaday_detail_weather_element["wind_direction"] = toaday_detail_weather_element_result[0][5].decode("utf-8")
                    toaday_detail_weather_element["wind_value"] = toaday_detail_weather_element_result[0][6].decode("utf-8")
                    toaday_detail_weather_element["sun_time"] = toaday_detail_weather_element_result[0][7].decode("utf-8")
                    toaday_detail_weather_element["is_sun_up"] = 0
                    toaday_detail_weather_list_result.append(toaday_detail_weather_element)

        print "parse_zh_tian_qi_today_detail_weather---end"
        return toaday_detail_weather_list_result

    def get_single_bracket_str(self, content):
        pattern = re.compile(u""".*?[(]"(.*?)"[)].*?""", re.S)
        result = re.findall(pattern, content)
        if len(result) > 0:
            return result[0]
        else:
            return ''

    def get_px_value(self, content):
        pattern = re.compile(u"""(.*?)px.*?""", re.S)
        result = re.findall(pattern, content)
        if len(result) > 0:
            return result[0]
        else:
            return 0

    def parse_city_info(self, adm_name):
        name_array = adm_name.split(",")
        for name in name_array:
            if "市" in name:
                return name
