#!/usr/bin/evn python
# coding=utf-8
from com_zxl_common.DBUtil import *


class QsbkCollectUtil:

    mDBUtil = DBUtil()

    def insert_to_qsbk_collect(self, mUserId, mQsbkParseElement):
        self.mDBUtil.insert_to_qsbk_collect(mUserId, mQsbkParseElement)

    def query_qsbk_collect_by_user_id_author_id(self, user_id, author_id):
        return self.mDBUtil.query_qsbk_collect_by_user_id_author_id(user_id, author_id)

    def delete_qsbk_collect_by_user_id_author_id(self, user_id, author_id):
        self.mDBUtil.delete_qsbk_collect_by_user_id_author_id(user_id, author_id)

    def query_qsbk_collect_by_user_id(self, page, page_count, user_id):
        return self.mDBUtil.query_qsbk_collect_by_user_id(page, page_count, user_id)

    def query_qsbk_collect_total_count(self):
        return self.mDBUtil.query_qsbk_collect_total_count()