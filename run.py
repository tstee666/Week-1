import schedule
import time
from crawler import get_baidu_hot
from mysql_helper import MySqlHelper

def job():
    print("正在抓取百度热搜并写入数据库...")
    hot_list = get_baidu_hot()

    db = MySqlHelper(
        host="localhost",
        user="root",
        password="Tst050303.",
        database="baidu_hot"
    )

    sql = "INSERT INTO hot_search (title, hot, timestamp) VALUES (%s, %s, %s)"
    db.executemany(sql, hot_list)
    db.close()
    print("✅ 抓取完成，数据已更新！")

# 每小时运行一次
schedule.every(1).hours.do(job)

# 立即运行一次
job()

# 循环执行计划任务
while True:
    schedule.run_pending()
    time.sleep(1)

