#!C:\Python27\python.exe
#coding=utf-8


class QsbkCollectDB:
    DATABASE_NAME = 'weather_db'
    QSBK_COLLECT_TABLE = 'qsbk_collect'
    TABLES = {}
    TABLES[QSBK_COLLECT_TABLE] = (
        "CREATE TABLE IF NOT EXISTS qsbk_collect ("
        "  `_id` bigint(20) NOT NULL AUTO_INCREMENT,"
        "  `user_id` varchar(32),"
        "  `author_id` varchar(32),"
        "  `author_head_img` text,"
        "  `author_name` text,"
        "  `is_anonymity` text,"
        "  `author_sex` text,"
        "  `author_age` text,"
        "  `content` text,"
        "  `has_thumb` text,"
        "  `thumb` text,"
        "  `vote_number` text,"
        "  `comment_number` text,"
        "  PRIMARY KEY (`_id`)"
        ") ENGINE=InnoDB")


    INSERT_QSBK_COLLECT_SQL = ("INSERT INTO " + QSBK_COLLECT_TABLE + " " "(user_id, author_id, author_head_img, author_name, is_anonymity, author_sex, author_age, content, has_thumb, thumb, vote_number, comment_number) "
                                                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")


    QUERY_QSBK_COLLECT_BY_USER_ID_SQL = ("SELECT user_id, author_id, author_head_img, author_name, is_anonymity, author_sex, author_age, content, has_thumb, thumb, vote_number, comment_number "
                           " FROM " + QSBK_COLLECT_TABLE +
                           " WHERE user_id = '%s' ORDER BY _id DESC LIMIT %s,%s")

    QUERY_QSBK_COLLECT_BY_USER_ID_AUTHOR_ID_SQL = ("SELECT user_id, author_id, author_head_img, author_name, is_anonymity, author_sex, author_age, content, has_thumb, thumb, vote_number, comment_number "
                           " FROM " + QSBK_COLLECT_TABLE +
                           " WHERE user_id = '%s' AND author_id = '%s'")

    DELETE_QSBK_COLLECT_BY_USER_ID_AUTHOR_ID_SQL = ("DELETE"
                           " FROM " + QSBK_COLLECT_TABLE +
                           " WHERE user_id = '%s' AND author_id = '%s'")

    QUERY_QSBK_COLLECT_TOTAL_COUNT_SQL = ("SELECT COUNT(*)total_count FROM " + QSBK_COLLECT_TABLE)