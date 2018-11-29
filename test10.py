#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi
import json
import os
import sys

from com_zxl_common.WyMusicUtil import *
from com_zxl_common.XPathParserUtil import *

reload(sys)
sys.setdefaultencoding("utf-8")

MUSIC_OPERATOR_SEARCH_MUSIC = "1"

result = {}

if __name__ == "__main__":

    form = cgi.FieldStorage()

    music_operator = form.getvalue("music_operator")

    music_operator = "1"


    # music_operator = 1::search_music_name = 一次就好::search_music_offset = 0::search_music_page_count = 20
    print "music============test10--->music_operator--->%s" % music_operator

    mWyMusicUtil = WyMusicUtil()

    if music_operator == MUSIC_OPERATOR_SEARCH_MUSIC:
        search_music_name = form.getvalue("search_music_name")
        search_music_offset = form.getvalue("search_music_offset")
        search_music_page_count = form.getvalue("search_music_page_count")

        # search_music_name = "一次就好"
        # search_music_offset = "0"
        # search_music_page_count = "20"

        print "music============test10===>%s===>%s===>%s" % (search_music_name, search_music_offset, search_music_page_count)

        fo = open("foo.txt", "a+")
        fo.write("music============test10--->%s===>%s===>%s===>%s" % (music_operator, search_music_name, search_music_offset, search_music_page_count))
        fo.write("\n")
        fo.close()

        search_result = mWyMusicUtil.search_music(search_music_name, search_music_offset, search_music_page_count)

        print "search_result================"
        print search_result

        result["code"] = 0
        result["desc"] = "success"
        result["music_operator"] = music_operator
        result["result"] = json.loads(search_result, "utf-8")
    else:
        mWyMusicUtil.get_music_lrc("440207429")
        mWyMusicUtil.get_music_comment("440207429")
        mWyMusicUtil.get_music_play_url("440207429")


    print "Content-type:text/html;charset=UTF-8"
    print "Accept:application/json"
    print "Accept-Charset:UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)

# https://music.163.com/#/search/m/?s=%E4%B8%80%E6%AC%A1%E5%B0%B1%E5%A5%BD&type=1