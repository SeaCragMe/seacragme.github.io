
## Python 操作 sqlite3 ##


### 首先当然是连接数据库了 ###

    import sqlite3
    conn = sqlite3.connect('example.db')            #在内存建立一个临时的数据库：sqlite3.connect(":memory:")
    c = conn.cursor()                               #创建一个游标

### 执行你需要操作的SQL命令 ###

    c.execute('SELECT * FROM book WHERE book.category = 1')
    print(c.fetchone())

### 需要的话进行数据保存 ###
    conn.commit()                                   #事物提交，回滚是：rollback()
### 关闭数据库 ###
    conn.close()




## SQLite3 的常用SQL命令 ##

### 创建包含id,pid,name,text这4个列的表格叫catalog,name不可重复,nickname默认为NULL，其中id是主键是 ###
    '''CREATE TABLE catalog(id int primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)'''

### 插入数据 ###
    "INSERT INTO category VALUES (1,1,kitchen')"                #直接插入一条数据
    "INSERT INTO category BALUES (?,?,?),[(2,2,'computer')]"    #插入一条数据的另一种方法
    books = [(1,1,'Cook Recipe',3.12,1),(2,3,'Python Intro',17.5,2),(3,2,'OS Intro',13.6,2),]
    'INSERT INTO category VALUES (?,?,?,?,?)',books             #插入几组数据的方法

### 查询数据 ###
    'SELECT * FROM catalog'                                     #返回一条记录
    print(c.fetchone())                                         #可以从c.fetchone()提取
    'SELECT * FROM book WHERE book.category=1'                  #查询book列表里的所有category=1的记录

### 修改 ###

### 删除 ###

