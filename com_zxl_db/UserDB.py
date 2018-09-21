#!C:\Python27\python.exe
#coding=utf-8


class UserDB:
    DATABASE_NAME = 'weather_db'
    USER_TABLE = 'user'
    TABLES = {}
    TABLES[USER_TABLE] = (
        "CREATE TABLE IF NOT EXISTS user ("
        "  `_id` bigint(20) NOT NULL AUTO_INCREMENT,"
        "  `user_id` varchar(32),"
        "  `user_name` text,"
        "  `pass_word` text,"
        "  `phone_number` text,"
        "  `nick_name` text,"
        "  `sex` text,"
        "  `birthday` text,"
        "  `state` text,"
        "  PRIMARY KEY (`_id`)"
        ") ENGINE=InnoDB")


    INSERT_USER_SQL = ("INSERT INTO " + USER_TABLE + " " "(user_id, user_name, pass_word, phone_number, nick_name, sex, birthday, state) "
                                                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")


    QUERY_USER_BY_USER_NAME_SQL = ("SELECT user_id, user_name, pass_word, phone_number, nick_name, sex, birthday, state "
                           " FROM " + USER_TABLE +
                           " WHERE user_name = '%s'")

    QUERY_USER_BY_USER_NAME_PASS_WORD_SQL = ("SELECT user_id, user_name, pass_word, phone_number, nick_name, sex, birthday, state "
                           " FROM " + USER_TABLE +
                           " WHERE user_name = '%s' and pass_word = '%s'")

    QUERY_USER_BY_PHONE_NUMBER_SQL = ("SELECT user_id, user_name, pass_word, phone_number, nick_name, sex, birthday, state "
                           " FROM " + USER_TABLE +
                           " WHERE phone_number = '%s'")

    UPDATE_USER_STATE_SQL = ("UPDATE " + USER_TABLE +
                            "SET state = '%s'" +
                           " WHERE user_id = '%s'")
