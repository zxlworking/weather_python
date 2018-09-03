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
        print "get_zh_tian_qi_today_detail_weather---start\n"
        #big class==温度==风向==风级==日出时间
        pattern = re.compile(u""".*?<ul class="clearfix">(.*?)<input type=".*?" id=".*?" value=".*?" />.*?""", re.S)
        toaday_detail_weather_page_content = re.findall(pattern, today_weather_page_content)

        pattern = re.compile(u""".*?<li>(.*?)</li>.*?<li>(.*?)</li>.*?""", re.S)
        toaday_detail_weather_page_content = re.findall(pattern, toaday_detail_weather_page_content[0])


        pattern = re.compile(u""".*?<p class="sun sunUp">.*?""", re.S)
        is_daytime = re.findall(pattern, toaday_detail_weather_page_content[0][0])
        if len(is_daytime) > 0:


        print "get_zh_tian_qi_today_detail_weather---end"
        return toaday_detail_weather_page_content

    def parse_zh_tian_qi_today_weather(self, today_weather_page_content):
        print "parse_zh_tian_qi_today_weather---start"
        # 湿度==风向==风级==温度==空气质量
        # (^(\-|\+)?\d+(\.\d+)?)
        pattern = re.compile(u""".*?<div class="sk">.*?<p class="time"><span>.*?</span></p><div class="zs h"><i></i><span>.*?</span><em>(\d+)%</em></div><div class="zs w"><i></i><span>(.*?)</span><em>(.*?)级</em></div><div class="tem"><span>(-?\d+\.?\d*)</span><em>℃</em></div><p></p><div class="therm"><p><i class="t"></i><i class="c" style="height:.*?"></i></p></div><div class="zs pol"><i></i><span><a.*?>(.*?)</a></span></div></div>.*?<ul class="clearfix">.*?""",re.S)
        today_weather_page_parse_result = re.findall(pattern, today_weather_page_content)
        print "parse_zh_tian_qi_today_weather---end"
        return today_weather_page_parse_result



