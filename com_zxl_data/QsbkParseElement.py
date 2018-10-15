#!/usr/bin/env python
#coding=utf-8


class QsbkParseElement:
    SEX_MAN = 0
    SEX_FEMALE = 1

    QSBK_COLLECT_OPERATOR_COLLECT = "0"
    QSBK_COLLECT_OPERATOR_CANCEL = "1"
    QSBK_COLLECT_OPERATOR_QUERY_ALL = "2"

    author_id = ""
    author_head_img = ""
    author_name = ""
    is_anonymity = False
    author_sex = SEX_MAN
    author_age = 0
    content = ""
    has_thumb = False
    thumb = ""
    vote_number = 0
    comment_number = 0
