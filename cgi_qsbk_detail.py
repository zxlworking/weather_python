#!/usr/bin/env python
#coding=utf-8

import cgi
import re
import sys
import json

from com_zxl_common.QsbkUtil import *
from com_zxl_common.ParserUtil import *

SEX_MAN = 0
SEX_FEMALE = 1

reload(sys)
sys.setdefaultencoding("utf8")

result = {}

if __name__ == "__main__":

    mQsbkUtil = QsbkUtil()
    mParseUtil = ParserUtil()

    form = cgi.FieldStorage()
    author_id = form.getvalue("author_id")
    # author_id = "120535270"
    # author_id = "121327017"
    # author_id = "121308383"
    # author_id = "121311853"

    print "cgi_qsbk_detail--->%s" % author_id
    # fo = open("foo.txt", "a+")
    # fo.write(author_id)
    # fo.write("\n")
    # fo.close()

    if author_id is None:
        result["code"] = -1
        result["desc"] = "param error"
    else:
        mQsbkUtil.get_qsbk_detail(author_id, result)

    # fo = open("foo.txt", "a+")
    # fo.write(json.dumps(result, encoding="utf-8", ensure_ascii=False))
    # fo.write("\n")
    # fo.close()

    print "Content-type:text/html;charset=UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)
