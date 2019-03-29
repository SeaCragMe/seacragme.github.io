
## OpenBSD DOC ##


官方[FAQ](https://www.openbsd.org/faq/index.html)
类似系统[FreeBSD](https://www.freebsd.org/doc/zh_CN/books/handbook/index.html)的中文手册

----
链接地址：

* 简介： [深度探索 OpenBSD](https://www.ibm.com/developerworks/cn/aix/library/au-openbsd.html)
* 文档： [OpenBSD 4.8 FAQ 中文版](http://llww.me/index.html)
* 有趣   [fun](http://openbsdjumpstart.org/#/1)
* 栗子： [如何使用 OpenBSD 3.2 作 ADSL 路由](http://www.kuqin.com/article/05bsd/23827.html)
* 安全： [扔掉 OpenSSL，拥抱 LibreSSL——远离心脏出血与溺亡漏洞](https://hltj.me/security/2017/05/26/libressl-instead-openssl.html)
* 自习：[20181021](/docs/knowledge/openbsd.md)
* 邮件： [配置mail使用SMTP发送邮件](https://tlanyan.me/config-mail-use-smtp/)
* 建站： [OpenBSD.Apache.MySQL.PHP软件环境的安装](https://blog.csdn.net/oyzl68/article/details/6910025)
* 双系统:[Windows XP + FreeBSD 双系统](https://wiki.freebsdchina.org/doc/d/dualsystem)
* 安装:  [关于fdisk的一些介绍](http://bbs.chinaunix.net/thread-1122505-1-1.html)
* 网络服务：    [openbsd+openvpn搭建网络联机游戏平台](http://biancheng.dnbcw.net/bsd/258371.html)


______


20181105
### 安装OpenBSD 6.4 ###

1.  进入fdisk之后用(E)dit方式修改硬盘分区记录
    Ending .C(3631)

2.  设置分区：

    >e 1            #选择1号分区进行编辑
    [0F]:A6         #设置为OpenBSD分区格式
    CHS mode:Y
    start cylinder [0-xxx]:3632
    

    Ending cylinder [3632 - 7782]:[3632] 7782


3.  >f 1            #将1分区设置为启动分区
    p m             #显示当前设置状态

4.  >w              #保存
    >q              #退出

5.  >[a]tuo         #回车，自动分配分区内的各区大小

6.  Directory does not contain SHA256 sig[no]:yes       #确认执行操作

7.  系统备份

    cd /home
    tar cvpzf backup.tgz / --exclude=/home --exclude=/dev --exclude=/mnt --exclude=/sys

    恢复压缩： 
    tar xvpfz backup.tgz -C /
    mkdir home mnt dev sys
    (如果想只解压缩某个目录：tar -xvpfz backup.tgz ./usr/local/ )


-----

### 系统安装结束后的软件安装 ###

1.  添加pkg包安装源

    vi ~/.profile
    exprot PKG_PATH=https://xxxx.xxxx.xxx/pub/OpenBSD/6.4/packages/amd64/

    国外的源：
    mirror.aarnet.deu.au
    mirror.vdms.io
    ftp.jaist.ac.jp
    国内的源：
    mirror.tuna.tsinghua.edu.cn     #这个清华大学的源速度很不错

2.  我一般安装的常用包：

    vim
    python 
    wget
    git
    firefox 
    zh-wqy-zenhei-ttf 
    qemu
    ipython
    pandas

3.  [virtualenv](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000)


4.  下载网络上的某个目录下所有文件：

    wget -c -r -np -k -L -p gamelay.usami.com/~netboy/w30/
    tar zcf download.tar.gz gamelay.usami.com








------
底线*底线
