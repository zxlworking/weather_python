#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import Cookie
import cgi
import json
import os
import sys

from com_zxl_common.HttpUtil import *


reload(sys)
sys.setdefaultencoding("utf-8")

result = {}

if __name__ == "__main__":
    form = cgi.FieldStorage()

    param = form.getvalue("param").decode("utf-8")

    # param = "method=baidu.ting.billboard.billList&type=1&size=20&offset=0"

    print "music============test9--->%s" % param

    fo = open("foo.txt", "a+")
    fo.write("music============test9--->%s" % param)
    fo.write("\n")
    fo.close()

    mHttpUtil = HttpUtil()

    info = mHttpUtil.get_music_info(param)

    print info

    result["code"] = 0
    result["desc"] = "success"
    result["param"] = param
    result["result"] = json.loads(info, "utf-8")

    # fo = open("foo.txt", "a+")
    # fo.write(json.dumps(result, encoding="utf-8", ensure_ascii=False))
    # fo.write("\n")
    # fo.close()



    print "Content-type:text/html;charset=UTF-8"
    print "Accept:application/json"
    print "Accept-Charset:UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)