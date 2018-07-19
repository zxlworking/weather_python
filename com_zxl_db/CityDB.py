#!C:\Python27\python.exe
#coding=utf-8


class CityDB:
    DATABASE_NAME = 'weather_db'
    CITY_TABLE = 'city'
    TABLES = {}
    TABLES[CITY_TABLE] = (
        "CREATE TABLE IF NOT EXISTS city ("
        "  `_id` bigint(20) NOT NULL AUTO_INCREMENT,"
        "  `city_code` varchar(16),"
        "  `city_name` text,"
        "  `city_py` text,"
        "  `province` text,"
        "  PRIMARY KEY (`_id`)"
        ") ENGINE=InnoDB")

    INSERT_CITY_SQL = ("INSERT INTO " + CITY_TABLE + " " "(city_code, city_name, city_py, province) "
                                                       "VALUES (%s, %s, %s, %s)")

    QUERY_CITY_BY_CITY_NAME_SQL = ("SELECT _id, city_code, city_name, city_py, province "
                           " FROM " + CITY_TABLE +
                           " WHERE locate(city_name,'%s') = 1")

    QUERY_CITY_TOTAL_COUNT_SQL = ("SELECT COUNT(*)total_count FROM " + CITY_TABLE)