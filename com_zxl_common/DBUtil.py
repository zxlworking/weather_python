#!C:\Python27\python.exe
#coding=utf-8
import mysql.connector

from mysql.connector import errorcode

from com_zxl_db.QsbkCollectDB import *
from com_zxl_db.CityDB import *
from com_zxl_db.UserDB import *
from com_zxl_common.PrintUtil import *


class DBUtil():
    # host = '118.25.178.69'
    host = 'localhost'
    urser_name = "root"
    pass_word = "root"
    mPrintUtil = PrintUtil()

    def __init__(self):
        global cnx
        global cursor
        try:
            cnx = mysql.connector.connect(user=self.urser_name, password=self.pass_word, host=self.host, database=CityDB.DATABASE_NAME)
            cursor = cnx.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.mPrintUtil.show("Something is wrong with your user name or password")
                exit(1)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.mPrintUtil.show("Database does not exist")
                cnx = mysql.connector.connect(user=self.urser_name, password=self.pass_word, host=self.host)
                cursor = cnx.cursor()
                self.__create_database()
                self.__create_table()
            else:
                self.mPrintUtil.show(err)
                exit(1)
        else:
            self.__create_table()
            self.mPrintUtil.show("DBUtil init finish")

    def __create_database(self):
        try:
            cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(CityDB.DATABASE_NAME))
            cnx.database = CityDB.DATABASE_NAME
            self.mPrintUtil.show("Create database finish")
        except mysql.connector.Error as err:
            self.mPrintUtil.show("Failed creating database: {}".format(err))
            exit(1)

    def __create_table(self):
        for name, ddl in CityDB.TABLES.iteritems():
            try:
                self.mPrintUtil.show("Creating table {}: ".format(name),)
                cursor.execute(ddl)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    self.mPrintUtil.show("already exists.")
                else:
                    self.mPrintUtil.show(err.msg)
                    exit(1)
            else:
                self.mPrintUtil.show("OK")
        for name, ddl in UserDB.TABLES.iteritems():
            try:
                self.mPrintUtil.show("Creating table {}: ".format(name),)
                cursor.execute(ddl)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    self.mPrintUtil.show("already exists.")
                else:
                    self.mPrintUtil.show(err.msg)
                    exit(1)
            else:
                self.mPrintUtil.show("OK")
        for name, ddl in QsbkCollectDB.TABLES.iteritems():
            try:
                self.mPrintUtil.show("Creating table {}: ".format(name), )
                cursor.execute(ddl)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    self.mPrintUtil.show("already exists.")
                else:
                    self.mPrintUtil.show(err.msg)
                    exit(1)
            else:
                self.mPrintUtil.show("OK")

    def insert_to_city(self, mCityBean):
        data_city = (mCityBean.mCityCode,
                          mCityBean.mCityName.encode("utf-8"),
                          mCityBean.mCityPinYing,
                          mCityBean.mCityPinYing[0].upper(),
                          mCityBean.mProvince.encode("utf-8"))
        cursor.execute(CityDB.INSERT_CITY_SQL, data_city)
        cnx.commit()

    def insert_to_user(self, mUserBean):
        data_user = (mUserBean.mUserId,
                     mUserBean.mUserName,
                     mUserBean.mPassWord,
                     mUserBean.mPhoneNumber,
                     mUserBean.mNickName.encode("utf-8"),
                     mUserBean.mSex,
                     mUserBean.mBirthday,
                     mUserBean.mState)
        cursor.execute(UserDB.INSERT_USER_SQL, data_user)
        cnx.commit()

    def insert_to_qsbk_collect(self, mUserId, mQsbkParseElement):
        data_qsbk_collect = (mUserId,
                     mQsbkParseElement.author_id,
                     mQsbkParseElement.author_head_img,
                     mQsbkParseElement.author_name.encode("utf-8"),
                     mQsbkParseElement.is_anonymity,
                     mQsbkParseElement.author_sex,
                     mQsbkParseElement.author_age,
                     mQsbkParseElement.content.encode("utf-8"),
                     mQsbkParseElement.has_thumb,
                     mQsbkParseElement.thumb,
                     mQsbkParseElement.vote_number,
                     mQsbkParseElement.comment_number)
        cursor.execute(QsbkCollectDB.INSERT_QSBK_COLLECT_SQL, data_qsbk_collect)
        cnx.commit()

    def query_to_city_by_city_name(self, cityName):
        #self.mPrintUtil.print_to_file(CityDB.QUERY_CITY_BY_CITY_NAME_SQL % cityName)
        cursor.execute(CityDB.QUERY_CITY_BY_CITY_NAME_SQL % cityName)
        result_element_list = []
        for (_id, city_code, city_name, city_py, province) in cursor:
            result_element = {"_id": _id, "city_code": city_code, "city_name": city_name,
                              "city_py": city_py,
                              "province": province}
            result_element_list.append(result_element)
        return result_element_list

    def query_all_city(self):
        cursor.execute(CityDB.QUERY_ALL_CITY_SQL)
        result_element_list = []
        for (_id, city_code, city_name, city_py, city_head, province) in cursor:
            result_element = {"_id": _id, "city_code": city_code, "city_name": city_name,
                              "city_py": city_py, "city_head": city_head, "province": province}
            result_element_list.append(result_element)
        return result_element_list

    def query_to_city_total_count(self):
        cursor.execute(CityDB.QUERY_CITY_TOTAL_COUNT_SQL)
        for(total_count, ) in cursor:
            return total_count

    def query_to_user_by_user_name(self, userName):
        cursor.execute(UserDB.QUERY_USER_BY_USER_NAME_SQL % userName)
        result_element_list = []
        for (user_id, user_name, pass_word, phone_number, nick_name, sex, birthday, state) in cursor:
            result_element = {"user_id": user_id, "user_name": user_name, "pass_word": pass_word,
                              "phone_number": phone_number, "nick_name": nick_name, "sex": sex,
                              "birthday": birthday, "state": state}
            result_element_list.append(result_element)
        print "xxx"
        print result_element_list
        print "yyy===>%d" % len(result_element_list)
        return result_element_list

    def query_to_user_by_user_name_pass_word(self, userName, passWord):
        cursor.execute(UserDB.QUERY_USER_BY_USER_NAME_PASS_WORD_SQL % (userName, passWord))
        result_element_list = []
        for (user_id, user_name, pass_word, phone_number, nick_name, sex, birthday, state) in cursor:
            result_element = {"user_id": user_id, "user_name": user_name, "pass_word": pass_word,
                              "phone_number": phone_number, "nick_name": nick_name, "sex": sex,
                              "birthday": birthday, "state": state}
            result_element_list.append(result_element)
        return result_element_list

    def query_to_user_by_phone_number(self, phoneNumber):
        cursor.execute(UserDB.QUERY_USER_BY_PHONE_NUMBER_SQL % phoneNumber)
        result_element_list = []
        for (user_id, user_name, pass_word, phone_number, nick_name, sex, birthday, state) in cursor:
            result_element = {"user_id": user_id, "user_name": user_name, "pass_word": pass_word,
                              "phone_number": phone_number, "nick_name": nick_name, "sex": sex,
                              "birthday": birthday, "state": state}
            result_element_list.append(result_element)
        return result_element_list

    def query_qsbk_collect_by_user_id_author_id(self, user_id, author_id):
        cursor.execute(QsbkCollectDB.QUERY_QSBK_COLLECT_BY_USER_ID_AUTHOR_ID_SQL % (user_id, author_id))
        result_element_list = []
        for (user_id, author_id, author_head_img, author_name, is_anonymity, author_sex, author_age, content, has_thumb, thumb, vote_number, comment_number) in cursor:
            result_element = {"user_id": user_id, "author_id": author_id, "author_head_img": author_head_img,
                              "author_name": author_name, "is_anonymity": is_anonymity, "author_sex": author_sex,
                              "author_age": author_age, "content": content, "has_thumb": has_thumb,
                              "thumb": thumb, "vote_number": vote_number, "comment_number": comment_number}
            result_element_list.append(result_element)
            break
        return result_element_list

    def query_qsbk_collect_by_user_id(self, page, page_count, user_id):
        page_value = int(page)
        page_count_value = int(page_count)
        start_index = page_value * page_count_value
        cursor.execute(QsbkCollectDB.QUERY_QSBK_COLLECT_BY_USER_ID_SQL % (user_id, start_index, page_count))
        result_element_list = []
        for (user_id, author_id, author_head_img, author_name, is_anonymity, author_sex, author_age, content, has_thumb, thumb, vote_number, comment_number) in cursor:
            result_element = {"user_id": user_id, "author_id": author_id, "author_head_img": author_head_img,
                              "author_name": author_name, "is_anonymity": is_anonymity, "author_sex": author_sex,
                              "author_age": author_age, "content": content, "has_thumb": has_thumb,
                              "thumb": thumb, "vote_number": vote_number, "comment_number": comment_number,
                              "is_collect": True}
            result_element_list.append(result_element)
        return result_element_list

    def query_qsbk_collect_total_count(self):
        cursor.execute(QsbkCollectDB.QUERY_QSBK_COLLECT_TOTAL_COUNT_SQL)
        for(total_count, ) in cursor:
            return total_count

    def update_user_state(self, state, userID):
        cursor.execute(UserDB.UPDATE_USER_STATE_SQL % (state, userID))

    def delete_qsbk_collect_by_user_id_author_id(self, user_id, author_id):
        cursor.execute(QsbkCollectDB.DELETE_QSBK_COLLECT_BY_USER_ID_AUTHOR_ID_SQL % (user_id, author_id))
        cnx.commit()

    def close_db(self):
        cursor.close()
        cnx.close()
