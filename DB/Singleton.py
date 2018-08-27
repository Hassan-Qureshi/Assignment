import pymysql


class DbConnection:
    host = 'localhost'
    user = 'root'
    password = 'root'
    db = 'assignment'
    _connection = None

    def __init__(self):
        pass

    @classmethod
    def get_connection(self):
        if self._connection is None:
            self._connection = pymysql.connect(self.host, self.user, self.password, self.db, charset='utf8mb4',
                                               cursorclass=pymysql.cursors.DictCursor)
        return self._connection
