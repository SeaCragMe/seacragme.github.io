
## Python 操作 sqlite3 ##


### 20181106 ###



#### 首先当然是连接数据库了 ####

    import sqlite3
    conn = sqlite3.connect('example.db')            #在内存建立一个临时的数据库：sqlite3.connect(":memory:")
    c = conn.cursor()                               #创建一个游标

#### 执行你需要操作的SQL命令 ####

    c.execute('SELECT * FROM stocks ORDER BY price')
    print(c.fetchone())

#### 需要的话进行数据保存 ####
    conn.commit()                                   #事物提交，回滚是：rollback()

#### 关闭数据库 ####
    conn.close()




## SQLite3 的常用SQL命令 ##

### 创建表格catalog,包含id,pid,name,nickname等4个列,id是主键,name不可重复,nickname初始为NULL， ###
    '''CREATE TABLE catalog(id int primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)'''

### 插入数据 ###
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")    #直接添加一条记录

    t = ('RHAT',)
    c.execute('SELECT * FROM stocks WHERE symbol=?',t)           #添加数据记录
    purchases = [('2006-03-28','BUY','IBM',1000,45.00),('2006-04-05','BUY','MSFT',1000,72.00),('2006-04-06','SELL','IBM',53.00),]
    c.executemany('INSERT INTO stocks VALUSE (?,?,?,?,?)',purchases)    #添加一组数据

### 查询数据 ###
    for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

### 修改 ###

### 删除 ###


### 20181106 ###

[SQLite - Python](http://www.runoob.com/sqlite/sqlite-python.html)
[SQLite Python](https://www.yiibai.com/sqlite/sqlite_python.html)
[python开发_sqlite3](https://www.cnblogs.com/hongten/p/hongten_python_sqlite3.html)


-------


