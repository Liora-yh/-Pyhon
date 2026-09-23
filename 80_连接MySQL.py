from pymysql import Connection

conn = Connection(
    host = "localhost",     # 主机名（IP）
    port = 3306,            # 端口号
    user = "root",          # 账户
    password = "root"       # 密码
)

print(conn.get_server_info())

# 执行非查询性质SQL
cursor = conn.cursor()      # 获取游标对象
# conn.select_db("test")      # 选择数据库
# 执行sql语句
# cursor.execute("create table test_pymysql(id int)")

conn.select_db("world")
# 执行查询性质SQL
cursor.execute("select * from student")
# 获取查询结果
results: tuple = cursor.fetchall()
# print(results)
for r in results:
    print(r)

# 关闭连接
conn.close()