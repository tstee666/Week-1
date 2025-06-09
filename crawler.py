import requests
from bs4 import BeautifulSoup
from datetime import datetime
from mysql_helper import MySqlHelper
import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_baidu_hot():
    url = "https://top.baidu.com/board?tab=realtime"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        hot_list = []
        cards = soup.find_all('div', class_='category-wrap_iQLoo')[:10]

        for card in cards:
            title = card.find('div', class_='c-single-text-ellipsis').text.strip()
            hot = card.find('div', class_='hot-index_1Bl1a').text.strip()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            hot_list.append((title, hot, timestamp))

        logging.info("✅ 成功抓取百度热搜 Top 10.")
        return hot_list

    except Exception as e:
        logging.error(f"❌ 抓取百度热搜失败: {e}")
        return []

def run_crawler():
    hot_list = get_baidu_hot()

    try:
        db = MySqlHelper(
            host="localhost",
            user="root",
            password="Tst050303.",
            database="baidu_hot"
        )
        sql = "INSERT INTO hot_search (title, hot, timestamp) VALUES (%s, %s, %s)"
        db.executemany(sql, hot_list)
        db.close()

        print(f"✅ 已成功写入 {len(hot_list)} 条热搜数据。")
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now()}] 成功写入 {len(hot_list)} 条热搜数据。\n")

    except Exception as e:
        print(f"❌ 数据写入错误: {e}")
        with open("error.log", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now()}] 插入错误: {str(e)}\n")

if __name__ == "__main__":
    run_crawler()

