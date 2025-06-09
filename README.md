
# MySqlHelper

A lightweight Python class that simplifies interaction with MySQL using PyMySQL.

## 📦 Features

- ✅ Automatic connection and cleanup
- ✅ Supports parameterized queries (prevents SQL injection)
- ✅ Easy-to-use methods for SELECT, INSERT, UPDATE, DELETE

## 🚀 Installation

Install dependency:

```bash
pip install pymysql

## 🔧 Usage
1. Import and Initialize
from mysql_helper import MySqlHelper

db = MySqlHelper(
    host="localhost",
    user="root",
    password="your_password",
    database="student_db"
)
2. Run Queries
🔍 SELECT

students = db.query("SELECT * FROM student")
for s in students:
    print(s)

➕ INSERT
db.execute(
    "INSERT INTO student (name, height) VALUES (%s, %s)",
    ("Alice", 1.65)
)

📦 INSERT MANY
db.executemany(
    "INSERT INTO student (name, height) VALUES (%s, %s)",
    [("Bob", 1.78), ("Charlie", 1.80)]
)

✏️ UPDTE
db.execute(
    "UPDATE student SET height = %s WHERE name = %s",
    (1.75, "Alice")
)

🗑️ DELETE
db.execute(
    "DELETE FROM student WHERE name = %s",
    ("Charlie",)
)

3. Close the Connection
db.close()

🧠 Why use MySqlHelper?
Keeps your code clean and Pythonic

Eliminates repetitive connection logic

Protects against SQL injection by default

Makes SQL operations intuitive and less error-prone

📁 File Structure
mysql_project/
├── mysql_helper.py           #  封装好的 MySqlHelper 类
├── example.py                #  使用示例代码（连接、增删查改）
├── requirements.txt          #  所需依赖列表（如 pymysql）
├── .gitignore                #  忽略缓存文件和中间文件（如 __pycache__）
└── README.md                 #  项目说明文件（当前这个文档）

# Week-2
