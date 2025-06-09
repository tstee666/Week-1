import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter, PercentFormatter
from mysql_helper import MySqlHelper
from matplotlib import rcParams

# ---------- 中文字体 ----------
rcParams['font.sans-serif'] = ['PingFang', 'Microsoft YaHei', 'SimHei']
rcParams['axes.unicode_minus'] = False

# ---------- 读取 ----------
def fetch_data():
    db = MySqlHelper(host="localhost",
                     user="root",
                     password="Tst050303.",
                     database="baidu_hot")
    rows = db.fetchall("SELECT title, hot, timestamp FROM hot_search")
    db.close()
    df = pd.DataFrame(rows, columns=["title", "hot", "timestamp"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hot"] = pd.to_numeric(df["hot"], errors="coerce")
    return df.dropna()

# ---------- 选出波动最大的 n 条 ----------
def pick_most_volatile(df, n=5):
    vol = (
        df.groupby("title")["hot"]
          .agg(lambda s: s.max() - s.min())
          .sort_values(ascending=False)
          .head(n)
          .index
    )
    return df[df["title"].isin(vol)].copy()

# ---------- 绘图 ----------
def plot_relative(df):
    df.sort_values("timestamp", inplace=True)
    # 计算相对涨幅（当前值 / 最小值 -1）
    df["rel"] = (
        df.groupby("title")["hot"]
          .transform(lambda s: (s / s.min()) - 1)
    )

    fig, ax = plt.subplots(figsize=(12, 6))
    colors = plt.get_cmap("tab10")

    for i, title in enumerate(df["title"].unique()):
        sub = df[df["title"] == title]
        ax.plot(sub["timestamp"], sub["rel"],
                marker="o", label=title,
                color=colors(i))

    # x 轴
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    fig.autofmt_xdate()

    # y 轴：百分比
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=1.0, decimals=1))

    ax.set_title("百度热搜波动最大的 Top5 词条——相对涨幅", fontsize=16)
    ax.set_xlabel("时间")
    ax.set_ylabel("涨幅（%）")
    ax.grid(ls="--", alpha=.3)
    ax.legend(fontsize=9)
    plt.tight_layout()
    plt.show()

# ---------- main ----------
if __name__ == "__main__":
    df      = fetch_data()
    top_var = pick_most_volatile(df, n=5)
    plot_relative(top_var)

