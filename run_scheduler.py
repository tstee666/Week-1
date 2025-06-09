from datetime import datetime
import schedule
import time
from crawler import run_crawler
from export_csv import export_to_csv

def job():
    try:
        print(f"🕒 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始执行定时任务：抓取百度热搜 + 存入数据库...")
        run_crawler()
        export_to_csv()
        with open("scheduler.log", "a", encoding="utf-8") as log_file:
            log_file.write(f"[{datetime.now()}] ✅ 成功执行任务：已抓取并导出数据。\n")
        print("✅ 抓取并导出完成。")
    except Exception as e:
        with open("scheduler_error.log", "a", encoding="utf-8") as err_file:
            err_file.write(f"[{datetime.now()}] ❌ 执行失败：{str(e)}\n")
        print(f"❌ 执行失败：{e}")

# 每小时执行一次
schedule.every().hour.do(job)

print("✅ 调度器已启动，每小时自动抓取百度热搜并导出为 CSV。按 Ctrl+C 可退出。")
job()  # 启动时先执行一次

while True:
    schedule.run_pending()
    time.sleep(1)

