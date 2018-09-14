#!C:\Python27\python.exe
#coding=utf-8
import mysql.connector

from mysql.connector import errorcode
from com_zxl_db.CityDB import *
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

    def insert_to_city(self, mCityBean):
        data_city = (mCityBean.mCityCode,
                          mCityBean.mCityName.encode("utf-8"),
                          mCityBean.mCityPinYing,
                          mCityBean.mCityPinYing[0].upper(),
                          mCityBean.mProvince.encode("utf-8"))
        cursor.execute(CityDB.INSERT_CITY_SQL, data_city)
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

    def close_db(self):
        cursor.close()
        cnx.close()
