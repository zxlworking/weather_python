#!/usr/bin/env python
#coding=utf-8

import cgi
import sys
import json

from com_zxl_common.HttpUtil import *
from com_zxl_common.ParserUtil import *
from com_zxl_common.QsbkCollectUtil import QsbkCollectUtil

SEX_MAN = 0
SEX_FEMALE = 1

reload(sys)
sys.setdefaultencoding("utf8")

result = {}

if __name__ == "__main__":

    mHttpUtil = HttpUtil()
    mParseUtil = ParserUtil()
    mQsbkCollectUtil = QsbkCollectUtil()

    form = cgi.FieldStorage()
    page = form.getvalue("page")
    user_id = form.getvalue("user_id")


    # page = "1"
    # user_id = "a50895b8e0cb40e4a89b04d95617348b"
    print "cgi_qsbk.py--->page--->%s" % page
    print "cgi_qsbk.py--->user_id--->%s" % user_id

    if page is None:
        result["code"] = -1
        result["desc"] = "param error"
    else:
        qsbk_list = mHttpUtil.get_qsbk_list_by_page(page)
        # print "qsbk_list--->" + qsbk_list

        if qsbk_list:
            qsbk_element_list = mParseUtil.parse_qsbk_list(qsbk_list)
            mQsbkParseEleements = []

            for qsbk_element in qsbk_element_list:

                mQsbkParseElement = {}


                mQsbkParseElement["author_id"] = re.findall("\d+", qsbk_element[0])[0]
                mQsbkParseElement["author_head_img"] = "http:" + qsbk_element[1]
                mQsbkParseElement["author_name"] = qsbk_element[2]

                qsbk_anonymity = mParseUtil.parse_qsbk_anonymity(qsbk_element[3])
                if qsbk_anonymity:
                    mQsbkParseElement["is_anonymity"] = 1
                    mQsbkParseElement["author_sex"] = SEX_MAN
                    mQsbkParseElement["author_age"] = 0
                else:
                    mQsbkParseElement["is_anonymity"] = 0
                    author_sex_age = mParseUtil.parse_qsbk_author_sex_age(qsbk_element[3])
                    if author_sex_age[0][0] == "articleGender manIcon":
                        mQsbkParseElement["author_sex"] = SEX_MAN
                    else:
                        mQsbkParseElement["author_sex"] = SEX_FEMALE
                    mQsbkParseElement["author_age"] = int(author_sex_age[0][1])

                qsbk_content = qsbk_element[4].strip("\n")
                qsbk_content = re.sub("<br/>", "\n", qsbk_content)
                mQsbkParseElement["content"] = qsbk_content

                # print qsbk_element[4]
                qsbk_thumb = mParseUtil.parse_qsbk_thumb(qsbk_element[5])
                if qsbk_thumb:
                    mQsbkParseElement["has_thumb"] = 1
                    mQsbkParseElement["thumb"] = "http:" + qsbk_thumb[0]
                else:
                    mQsbkParseElement["has_thumb"] = 0
                    mQsbkParseElement["thumb"] = ""

                qsbk_vote_comment = mParseUtil.parse_qsbk_vote_comment(qsbk_element[6])
                mQsbkParseElement["vote_number"] = int(qsbk_vote_comment[0][0])
                mQsbkParseElement["comment_number"] = int(qsbk_vote_comment[0][1])

                if user_id is not None:
                    query_result = mQsbkCollectUtil.query_qsbk_collect_by_user_id_author_id(user_id, mQsbkParseElement["author_id"])

                    if query_result is None or len(query_result) <= 0:
                        mQsbkParseElement["is_collect"] = False
                    else:
                        mQsbkParseElement["is_collect"] = True

                mQsbkParseEleements.append(mQsbkParseElement)


            result["code"] = 0
            result["desc"] = "success"
            result["current_page"] = page
            result["result"] = mQsbkParseEleements
        else:
            result["code"] = -2
            result["desc"] = "no data"

    print "Content-type:text/html;charset=UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)
