import pymysql

class DbConnection:

    _connection = None
    def __init__(self):
        pass
    def get_connection(self):
        global _connection
        if _connection is None:
            _connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='root',
                                     db='test',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return _connection