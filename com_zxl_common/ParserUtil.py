#!C:\Python27\python.exe
#coding=utf-8
import re
from com_zxl_common.PrintUtil import *

class ParserUtil:
	# def __init__(self):
	# 	self.show("PrintUtil init...")

	def parse_city_weather(self, city_weather_content):
		pattern = re.compile(
			u"""<div class="left">.*?<span><b>(.*?)</b>(\d+).*?~.*?(\d+)℃</span>.*?</dd>.*?<dd class="shidu"><b>(.*?)%</b><b>(.*?)</b><b>(.*?)</b></dd>.*?<dd class="kongqi" ><h5.*?>(.*?)</h5><h6>PM.*?</div>""",
			re.S)
		parser_resutl = re.findall(pattern, city_weather_content)
		return parser_resutl

	def parse_wx_weather_request(self, wx_request):
		# mPrintUtil = PrintUtil()
		# mPrintUtil.print_to_file("parse_wx_weather_request::wx_request = ")
		# mPrintUtil.print_to_file(wx_request)
		pattern = re.compile(
			u"""([\u4E00-\u9FA5]+)天气""",
			re.S)
		parser_resutl = re.findall(pattern, wx_request)
		# mPrintUtil.print_to_file(str(len(parser_resutl)))
		return parser_resutl




