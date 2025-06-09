import pymysql

class MySqlHelper:
    def __init__(self, host, user, password, database):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.Cursor
        )
        self.cursor = self.conn.cursor()

    def query(self, sql, params=()):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def execute(self, sql, params=(), commit=True):
        self.cursor.execute(sql, params)
        if commit:
            self.conn.commit()
        return self.cursor.rowcount

    def executemany(self, sql, params_list):
        self.cursor.executemany(sql, params_list)
        self.conn.commit()
        return self.cursor.rowcount

    def close(self):
        self.cursor.close()
        self.conn.close()

    def fetchall(self, sql, params=None):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, params or ())
                return cursor.fetchall()
        except Exception as e:
            print(f"❌ 查询失败：{e}")
            return []

