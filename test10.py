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

result = {}

if __name__ == "__main__":
    mWyMusicUtil = WyMusicUtil()

    mWyMusicUtil.search_music_by_name("一次就好")
    mWyMusicUtil.get_music_lrc("440207429")
    mWyMusicUtil.get_music_comment("440207429")
    mWyMusicUtil.get_music_play_url("440207429")




# https://music.163.com/#/search/m/?s=%E4%B8%80%E6%AC%A1%E5%B0%B1%E5%A5%BD&type=1