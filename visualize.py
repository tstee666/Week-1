import pymysql
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv
from mysql_helper import MySqlHelper

# 建立数据库连接
db = MySqlHelper(
    host="localhost",
    user="root",
    password="Tst050303.",
    database="baidu_hot"
)

# 查询最新时间戳的前10条热搜
sql = """
SELECT title, hot, timestamp FROM hot_search
WHERE timestamp = (SELECT MAX(timestamp) FROM hot_search)
ORDER BY hot DESC
LIMIT 10
"""
results = db.query(sql)
db.close()

# 提取数据
titles = [row[0] for row in results]
hots = [int(row[1]) for row in results]
timestamp = results[0][2]

# 图表设置
plt.figure(figsize=(10, 6))
bars = plt.barh(titles, hots, color='#6495ED')  # 颜色改为温和的亮蓝色
plt.xlabel("热度")
plt.title(f"百度热搜 Top10（{timestamp}）")
plt.gca().invert_yaxis()

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.tight_layout()

# 美化 X 轴数值：千分位显示
ax = plt.gca()
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

# 显示柱子右侧的数字标签
for bar in bars:
    width = bar.get_width()
    plt.text(width + max(hots) * 0.01, bar.get_y() + bar.get_height() / 2,
             f'{int(width):,}', va='center', fontsize=9)

# 保存图表
plt.savefig("baidu_hot_top10.png", dpi=300)
plt.show()

# 保存 CSV
with open("baidu_hot_top10.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["标题", "热度", "抓取时间"])
    writer.writerows(results)

print("✅ 图表和 CSV 已更新！")

