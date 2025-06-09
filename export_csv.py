import csv
import pymysql
from mysql_helper import MySqlHelper

def export_to_csv():
    # 初始化数据库连接
    db = MySqlHelper(
        host="localhost",
        user="root",
        password="Tst050303.",
        database="baidu_hot"
    )

    # 查询全部数据
    sql = "SELECT title, hot, timestamp FROM hot_search"
    results = db.fetchall(sql)
    db.close()

    # 写入 CSV 文件
    with open("baidu_hot.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["热搜标题", "热度", "时间戳"])  # 表头
        writer.writerows(results)

    print("✅ 已成功导出为 baidu_hot.csv")

if __name__ == "__main__":
    export_to_csv()

