
## VIM 基本操作 ##


### 201903161639###

#### 1 记录和回放命令： ####

    qa
    ^
    i#include "<Esc>
    $
    a"<Esc>
    j
    q
这组命令完成了在当前行的起始位置添加'#include "'，
在结尾处加双引号的一组操作
用：@a调用，也可以前面加数字，增加重复次数

#### 2 Tab 命令####

    :tab new.txt
    gt

#### 3 单词统计命令 ####

    g+CTRL-G


#### 4 统计单词数 ####

    :%s/\i\+/&/gn

#### 5 挂起vim命令，以及返回 ####

    CTRL-Z

    fg

#### 6 保存当前开发环境 21.txt  ####

    :mksession! ~/.vim/20190316.vim
    :source ~/.vim/20190316.vim

或者：
    vim -S ~/.vim/20190316.vim

如果需要保存数据资料：
    
    wviminfo ~/.vim/20190316.viminfo

    rviminfo ~/.vim/20190316.viminfo



--------



  编辑文档时，你的手总要游走在键盘和鼠标之间吗？，有了这个神器，你的双手就再也不需要离开键盘了，下面先简单展示一下vim的魅力吧
  > 常用的删除操作：
  * 发现有个字符打错了?,删除它只需要按：`x`
  * 删除光标所在的这个单词：`dw`
  * 这一行都不想要了，好吧，按：`dd`
  * 删除当前行和下一行：`dj`
  * 现在我想删除11行以后的所有东西：`:11,$d`
  * 刚才我做了什么？，我后悔了：`u`

更多神奇功能，敬请浏览我为你精选的以下链接吧：

----
链接地址：



-   [vim 常用快捷键 二](http://www.cnblogs.com/wangkangluo1/archive/2012/04/12/2444952.html)
-   [Git时代的VIM不完全使用教程](http://beiyuu.com/git-vim-tutorial)
-   [如何组合使用 VIM 编辑器与 IPYthon](https://www.jianshu.com/p/539dbda310d5)
-   [Vim与Python真乃天作之合](https://segmentfault.com/a/1190000003962806)
-   [Vim 配置详解](http://www.cnblogs.com/witcxc/archive/2011/12/28/2304704.html)
-   专门学习vim博客[wim.ink](https://vim.ink/page/8/)
-	[像IDE一样使用 vim](https://github.com/yangyangwithgnu/use_vim_as_ide)
-	[Vim命令合集](http://www.cnblogs.com/softwaretesting/archive/2011/07/12/2104435.html)
-	[【vim环境配置】详细实录](http://www.cnblogs.com/xbf9xbf/p/4860484.html)
-	[让Vim更好用 for Mac OS X](http://hessian.cn/p/1026.html)
-   [mac自带vim7配置](http://www.cnblogs.com/liuqxFuture/archive/2012/11/20/2779560.html)
-   [vim中多标签和多窗口的使用](https://my.oschina.net/kutengshe/blog/464602)
-   [插件NERDTree的使用](http://www.cnblogs.com/feichexia/archive/2012/11/07/Vim_NerdTree.html)
-   [vim插件管理工具Vundle](https://www.cnblogs.com/schaepher/p/7533826.html)
-   [VIM选项配置说明](http://www.cnblogs.com/fengchi/p/6902965.html)
-   [vim 常用 NERDTree 快捷键](https://www.cnblogs.com/qiumingcheng/p/6275510.html)


-----
底线，底线
