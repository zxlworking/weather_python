#!/usr/bin/python
# -*- coding: UTF-8 -*-

# print "Content-type:text/html"
# print                               # 空行，告诉服务器结束头部
# print '<html>'
# print '<head>'
# print '<meta charset="utf-8">'
# print '<title>Hello World - 我的第一个 CGI 程序！</title>'
# print '</head>'
# print '<body>'
# print '<h2>Hello World! 我是来自菜鸟教程的第一CGI程序</h2>'
# print '</body>'
# print '</html>'

import cgi
import json
import sys
import uuid

from com_zxl_data.UserBean import *
from com_zxl_common.UserUtil import *

from com_zxl_send_message import SendTemplateSMS

reload(sys)
sys.setdefaultencoding("utf-8")

result={}

if __name__ == "__main__":
    # SendTemplateSMS.sendTemplateSMS("15850687360", "zxl_test", )

    form = cgi.FieldStorage()
    user_operator = form.getvalue("user_operator")

    print "test5.py===>user_operator===>%s" % user_operator

    mUserUtil = UserUtil()

    if user_operator == UserBean.USER_OPERATOR_CREATE:
        try:
            user_info = form.getvalue("user_info").decode("utf-8")
            user_info_json = json.loads(user_info)

            user_name = user_info_json["user_name"]
            pass_word = user_info_json["pass_word"]
            phone_number = user_info_json["phone_number"]
            nick_name = user_info_json["nick_name"]
            sex = user_info_json["sex"]
            birthday = user_info_json["birthday"]


            query_user_result = mUserUtil.query_to_user_by_user_name(user_name)


            if len(query_user_result) == 0:

                mUserBean = UserBean()
                uuid = uuid.uuid5(uuid.NAMESPACE_DNS, 'weather')
                uuid = str(uuid)
                uuid = ''.join(uuid.split('-'))
                print uuid
                print len(uuid)
                mUserBean.mUserId = uuid
                mUserBean.mUserName = user_name
                mUserBean.mPassWord = pass_word
                mUserBean.mPhoneNumber = phone_number
                mUserBean.mNickName = nick_name
                if sex is not None:
                    mUserBean.mSex = sex
                else:
                    mUserBean.mSex = UserBean.USER_SEX_MAN
                if birthday is not None:
                    mUserBean.mBirthday = birthday
                else:
                    mUserBean.mBirthday = ""
                mUserBean.mState = UserBean.USER_STATE_INIT

                mUserUtil.insert_to_user(mUserBean)


                query_user_result = mUserUtil.query_to_user_by_user_name_pass_word(mUserBean.mUserName, mUserBean.mPassWord)


                if len(query_user_result) > 0:
                    result["code"] = 0
                    result["desc"] = "注册成功"
                    result["user_id"] = query_user_result[0]["user_id"]
                    result["user_name"] = query_user_result[0]["user_name"]
                    result["pass_word"] = query_user_result[0]["pass_word"]
                    result["phone_number"] = query_user_result[0]["phone_number"]
                    result["nick_name"] = query_user_result[0]["nick_name"]
                    result["sex"] = query_user_result[0]["sex"]
                    result["birthday"] = query_user_result[0]["birthday"]
                    result["state"] = query_user_result[0]["state"]
                else:
                    result["code"] = -3
                    result["desc"] = "注册失败"
                    mUserBean.create_empty_user_result(result)
            else:
                result["code"] = -2
                result["desc"] = "该用户已存在"
                mUserBean = UserBean()
                mUserBean.create_empty_user_result(result)
        except BaseException, e:
            print e
            result["code"] = -1
            result["desc"] = "注册异常"
            mUserBean = UserBean()
            mUserBean.create_empty_user_result(result)

    print "Content-type:text/html;charset=UTF-8"
    print "Accept:application/json"
    print "Accept-Charset:UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)