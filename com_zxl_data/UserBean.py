#!/usr/bin/env python
#coding=utf-8


class UserBean:

    USER_SEX_MAN = "0"
    USER_SEX_FEMALE = "1"

    USER_OPERATOR_CREATE = "0"
    USER_OPERATOR_LOGIN = "1"
    USER_OPERATOR_LOGOUT = "2"

    USER_STATE_NONE = "-1"
    USER_STATE_INIT = "0"
    USER_STATE_LOGIN = "1"
    USER_STATE_LOGOUT = "2"

    mUserId = ""
    mUserName = ""
    mPassWord = ""
    mPhoneNumber = ""
    mNickName = ""
    mSex = ""
    mBirthday = ""
    mState = ""

    def create_empty_user_result(self, result):
        result["user_id"] = ""
        result["user_name"] = ""
        result["pass_word"] = ""
        result["phone_number"] = ""
        result["nick_name"] = ""
        result["sex"] = ""
        result["birthday"] = ""
        result["state"] = ""
