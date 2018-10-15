#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi
import json
import sys

from com_zxl_common.QsbkCollectUtil import *
from com_zxl_data.QsbkParseElement import *

reload(sys)
sys.setdefaultencoding("utf-8")

result={}

if __name__ == "__main__":
    form = cgi.FieldStorage()
    collect_operator = form.getvalue("collect_operator")
    user_id = form.getvalue("user_id")

    # collect_operator = "2"
    # user_id = "a50895b8e0cb40e4a89b04d95617348b"

    print "test7.py===>collect_operator===>%s" % collect_operator
    print("test7.py--->user_id--->%s" % user_id)

    mQsbkCollectUtil = QsbkCollectUtil()

    if QsbkParseElement.QSBK_COLLECT_OPERATOR_COLLECT == collect_operator:
        try:


            qsbk_parse_element = form.getvalue("qsbk_parse_element")

            qsbk_parse_element_json = json.loads(qsbk_parse_element)

            mQsbkParseElement = QsbkParseElement()
            mQsbkParseElement.author_id = qsbk_parse_element_json["author_id"]
            mQsbkParseElement.author_head_img = qsbk_parse_element_json["author_head_img"]
            mQsbkParseElement.author_name = qsbk_parse_element_json["author_name"]
            mQsbkParseElement.is_anonymity = qsbk_parse_element_json["is_anonymity"]
            mQsbkParseElement.author_sex = qsbk_parse_element_json["author_sex"]
            mQsbkParseElement.author_age = qsbk_parse_element_json["author_age"]
            mQsbkParseElement.content = qsbk_parse_element_json["content"]
            mQsbkParseElement.has_thumb = qsbk_parse_element_json["has_thumb"]
            mQsbkParseElement.thumb = qsbk_parse_element_json["thumb"]
            mQsbkParseElement.vote_number = qsbk_parse_element_json["vote_number"]
            mQsbkParseElement.comment_number = qsbk_parse_element_json["comment_number"]

            print("test7.py--->user_id--->%s" % mQsbkParseElement.author_id)

            query_result = mQsbkCollectUtil.query_qsbk_collect_by_user_id_author_id(user_id, mQsbkParseElement.author_id)

            print query_result
            print len(query_result)

            if query_result is None or len(query_result) <= 0:
                mQsbkCollectUtil.insert_to_qsbk_collect(user_id, mQsbkParseElement)
                print("test7.py--->insert success")
            else:
                print("test7.py--->user_id=%s author_id=%s has exist" % (user_id, mQsbkParseElement.author_id))

            result["code"] = 0
            result["desc"] = "收藏成功"
        except BaseException, e:
            print e
            result["code"] = -1
            result["desc"] = "收藏失败"
    elif QsbkParseElement.QSBK_COLLECT_OPERATOR_CANCEL == collect_operator:
        try:
            user_id = form.getvalue("user_id")

            print("test7.py--->user_id--->%s" % user_id)

            qsbk_parse_element = form.getvalue("qsbk_parse_element")

            qsbk_parse_element_json = json.loads(qsbk_parse_element)

            mQsbkParseElement = QsbkParseElement()
            mQsbkParseElement.author_id = qsbk_parse_element_json["author_id"]
            mQsbkParseElement.author_head_img = qsbk_parse_element_json["author_head_img"]
            mQsbkParseElement.author_name = qsbk_parse_element_json["author_name"]
            mQsbkParseElement.is_anonymity = qsbk_parse_element_json["is_anonymity"]
            mQsbkParseElement.author_sex = qsbk_parse_element_json["author_sex"]
            mQsbkParseElement.author_age = qsbk_parse_element_json["author_age"]
            mQsbkParseElement.content = qsbk_parse_element_json["content"]
            mQsbkParseElement.has_thumb = qsbk_parse_element_json["has_thumb"]
            mQsbkParseElement.thumb = qsbk_parse_element_json["thumb"]
            mQsbkParseElement.vote_number = qsbk_parse_element_json["vote_number"]
            mQsbkParseElement.comment_number = qsbk_parse_element_json["comment_number"]

            print("test7.py--->user_id--->%s" % mQsbkParseElement.author_id)

            mQsbkCollectUtil.delete_qsbk_collect_by_user_id_author_id(user_id, mQsbkParseElement.author_id)

            print("test7.py--->delete success")

            result["code"] = 0
            result["desc"] = "取消收藏成功"
        except BaseException, e:
            print e
            result["code"] = -1
            result["desc"] = "取消收藏失败"
    elif QsbkParseElement.QSBK_COLLECT_OPERATOR_QUERY_ALL == collect_operator:
        page = form.getvalue("page")
        page_count = form.getvalue("page_count")

        # page = 0
        # page_count = 1

        print("test7.py--->page--->%s" % page)
        print("test7.py--->page_count--->%s" % page_count)

        total_count = mQsbkCollectUtil.query_qsbk_collect_total_count()
        query_result = mQsbkCollectUtil.query_qsbk_collect_by_user_id(page, page_count, user_id)

        print("test7.py--->total_count--->%s" % total_count)
        len = len(query_result)
        print "test7.py--->len--->%s" % len

        total_page = int(total_count) / int(page_count)
        if(int(total_count) % int(page_count)) != 0:
            total_page = total_page + 1

        result["code"] = 0
        result["desc"] = "success"
        result["current_page"] = page
        result["total_page"] = total_page
        result["result"] = query_result
    else:
        pass


    print "Content-type:text/html;charset=UTF-8"
    print "Accept:application/json"
    print "Accept-Charset:UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)