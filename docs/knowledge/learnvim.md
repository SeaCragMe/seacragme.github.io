
  ## 关于vim的设置 ##

1. 插件管理器

> 我下载的是pathogen.vim,

2. 插件使用

> 窗口管理插件：NERD_tree
  > 配色管理：

3. 窗口管理

> 窗口的大小调整和相互跳转等操作，都可以基于`ctrl+w`再添加相应操作 `+-=|`等这几个字符进行

> 关闭所有窗口：`:qa(ll)`


 ### 实际操作演示： ###

    :resize(res) 80            #窗口高度调整为80个字符
    :vertical resize 100    #窗口宽度调整为100
    :vs pathwin             #横向新建一个窗口
    :vertical resize 30     #设置宽度为30
    :split(sp) listwin             #纵向新建listwin窗口
    :f list1                #窗口改名
    :n                      #跳到下一个文件
    :Ex                     #当前窗口开启目录浏览,新开窗口浏览用：`:Sex`
    :q
    :shell                  #开启shell
    exit                    #关闭shell


4. 文件浏览，切换

    vim -p file1 file2 file3        #多标签打开多个文件，用`gt`和`gT`可以左右切换文件窗口

