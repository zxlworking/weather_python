#!/usr/bin/env python
#coding=utf-8

import cgi
import re
import sys
import json

from com_zxl_common.HttpUtil import *
from com_zxl_common import ParserUtil

SEX_MAN = 0
SEX_FEMALE = 1

reload(sys)
sys.setdefaultencoding("utf8")

result = {}

if __name__ == "__main__":

    mHttpUtil = HttpUtil()
    mParseUtil = ParserUtil()

    form = cgi.FieldStorage()
    author_id = form.getvalue("author_id")
    # author_id = "120535270"
    if author_id is None:
        result["code"] = -1
        result["desc"] = "param error"
    else:
        qsbk_detail = mHttpUtil.get_qsbk_detail(author_id)
        # print "qsbk_detail--->" + qsbk_detail

        if qsbk_detail:

            qsbk_detail_parse_result = mParseUtil.parse_qsbk_detal(qsbk_detail)

            qsbk_detail_content = qsbk_detail_parse_result[0][0]
            qsbk_detail_content = qsbk_detail_content.strip("\n")
            qsbk_detail_content = re.sub("<br/>", "\n", qsbk_detail_content)

            qsbk_detail_comment_list = qsbk_detail_parse_result[0][1]
            parse_qsbk_detail_comment_list = mParseUtil.parse_qsbk_detail_comment_list(qsbk_detail_comment_list)

            user_comment_list = []
            for parse_qsbk_detail_comment_element in parse_qsbk_detail_comment_list:
                user_comment_element = {}
                user_comment_element["user_id"] = parse_qsbk_detail_comment_element[0]
                user_comment_element["user_head_img"] = "http:" + parse_qsbk_detail_comment_element[1]
                user_comment_element["user_name"] = parse_qsbk_detail_comment_element[2]
                if "manIcon" in parse_qsbk_detail_comment_element[3]:
                    user_comment_element["user_sex"] = SEX_MAN
                else:
                    user_comment_element["user_sex"] = SEX_FEMALE
                user_comment_element["user_age"] = int(parse_qsbk_detail_comment_element[4])
                user_comment_element["comment_content"] = parse_qsbk_detail_comment_element[5]
                user_comment_element["comment_report"] = int(parse_qsbk_detail_comment_element[6])

                user_comment_list.append(user_comment_element)

            result["code"] = 0
            result["desc"] = "success"
            result["qsbk_detail_content"] = qsbk_detail_content
            result["user_comment_list"] = user_comment_list
        else:
            result["code"] = -2
            result["desc"] = "no data"

    print "Content-type:text/html;charset=UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)
