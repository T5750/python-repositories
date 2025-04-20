import oracledb

# 连接到数据库
connection = oracledb.connect(dsn="用户名称/密码@主机地址:端口号1521/实例")
# 创建游标
cursor = connection.cursor()
# 执行查询
cursor.execute("SELECT COUNT(*) FROM DEPT")
# 获取结果
for row in cursor:
    print(row)
# 关闭游标和连接
cursor.close()
connection.close()
