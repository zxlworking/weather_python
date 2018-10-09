#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import os
import sys
from subprocess import Popen, PIPE

from com_zxl_common.ParserUtil import *


reload(sys)
sys.setdefaultencoding("utf-8")

result = {}

if __name__ == "__main__":

    try:
        p = Popen("aapt d badging %s" % "C:\\zxl\programe\\apache-tomcat-8.5.31\\webapps\\cgi_server\\test.apk", shell=True, stdout=PIPE, stderr=PIPE)
        # fo = open("foo.txt", "a+")
        # fo.write("--->test6.py--->success--->%s" % p.stdout.read().decode("utf-8"))
        # fo.write("\n")
        # fo.close()
        package_content = p.stdout.read().decode("utf-8")

        # package_content = os.popen("aapt d badging %s" % "C:\\zxl\programe\\apache-tomcat-8.5.31\\webapps\\cgi_server\\test.apk").read().decode("utf-8")
        # print package_content
        mParserUtil = ParserUtil()
        mParserUtil.parse_today_apk_package_info(package_content, result)

    except BaseException, e:
        print e
        result["code"] = -1
        result["desc"] = "获取版本信息失败"

        fo = open("foo.txt", "a+")
        fo.write("--->test6.py--->fail")
        fo.write("\n")
        fo.close()


    print "Content-type:text/html;charset=UTF-8"
    print "Accept:application/json"
    print "Accept-Charset:UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)
