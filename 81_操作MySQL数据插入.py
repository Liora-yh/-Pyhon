from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    autocommit=True     # 设置自动提交
)

cursor = conn.cursor()
conn.select_db("world")

cursor.execute("insert into student values(10021, '落雨花', 21, '女')")

# 通过commit确认
# conn.commit()   # 只有确认了上面的修改才会提交上去

conn.close()