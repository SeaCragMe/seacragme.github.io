import sqlite3
conn = sqlite3.connect('example.db')            #在内存建立一个临时的数据库：sqlite3.connect(":memory:")
c = conn.cursor()                               #创建一个游标

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)




### 退出程序时记得要关闭数据库 ###
conn.close()

