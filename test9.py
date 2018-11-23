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

    muscic_method = form.getvalue("muscic_method")
    muscic_param_key = form.getvalue("muscic_param_key").decode("utf-8")
    music_param_value = form.getvalue("music_param_value").decode("utf-8")

    # muscic_method = 'baidu.ting.search.catalogSug'
    # muscic_param_key = 'query'
    # music_param_value = '一次就好'

    print "music============test9--->(%s::%s::%s)" % (muscic_method, muscic_param_key, music_param_value)

    mHttpUtil = HttpUtil()

    info = mHttpUtil.get_music_info(muscic_method, muscic_param_key, music_param_value)

    print info

    result["code"] = 0
    result["desc"] = "success"
    result["music_method"] = muscic_method
    result["result"] = json.loads(info, "utf-8")



    print "Content-type:text/html;charset=UTF-8"
    print "Accept:application/json"
    print "Accept-Charset:UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)