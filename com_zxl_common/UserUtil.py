#!/usr/bin/evn python
# coding=utf-8
from com_zxl_common.DBUtil import *

class UserUtil:
    mDBUtil = DBUtil()

    def insert_to_user(self, mUserBean):
        self.mDBUtil.insert_to_user(mUserBean)

    def query_to_user_by_user_name(self, userName):
        return self.mDBUtil.query_to_user_by_user_name(userName)

    def query_to_user_by_user_name_pass_word(self, userName, passWord):
        return self.mDBUtil.query_to_user_by_user_name_pass_word(userName, passWord)

    def query_to_user_by_phone_number(self, phoneNumber):
        return self.mDBUtil.query_to_user_by_phone_number(phoneNumber)

    def update_user_state(self, state, userID):
        self.mDBUtil.update_user_state(state, userID)
