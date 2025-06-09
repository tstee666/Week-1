from mysql_helper import MySqlHelper
from crawler import get_baidu_hot

# 建立数据库连接
db = MySqlHelper(
    host="localhost",
    user="root",
    password="Tst050303.",
    database="baidu_hot"
)

# 获取百度热搜前10
hot_list = get_baidu_hot()

# 插入数据库
sql = "INSERT INTO hot_search (title, hot) VALUES (%s, %s)"
db.executemany(sql, hot_list)

# 关闭连接
db.close()

print("✅ 百度热搜 Top 10 已成功插入数据库！")

