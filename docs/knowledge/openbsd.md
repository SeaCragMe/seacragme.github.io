
## 关于OpenBSD系统的知识 ##

### 系统安装 ###

安装
设置在线程序下载服务器地址（镜像）
    vi /.profile
    export PKG_PATH=https://mirror.aarnet.edu.au/Pub/OpenBSD/6.3/packages/amd64/

(另一个速度比较快的镜像：ftp.jaist.ac.jp/Pub......)

安装无线fireware的licenes:
    fw-update -P http://fireware.openbsd.org/fireware/6.3/


无线设置
    ifconfig			#查看网络连接方式
    vi /etc/hostname.iwn0
>    nwid sea
     wpakey RHai
     dhcp

    chmod o-r /etc/hostname.iwn0	#设置权限


常用应用程序的安装
    pkg_add vim zh-wqy-zenhei-ttf firefox tor-browser


挂载U盘
软件在线升级命令：
    pkg_add -u

用tar做系统备份及恢复

    tar cvpzf backup.tgz / --exclude=/Proc --exclude=/Lost+found --exclude=/home --exclude=/mnt --exclude=/SYS

恢复：

    tar cvpzf backup.tgz -C /
    mkdir Proc Lost+found home mnt SYS

### 常用指令进阶操作：###

挂载外部磁盘:
    mount /dev/sda8 /temp
    mkfs -t ext3 -b 4096 /dev/dsa8
    cp -a /usr/. /temp

下载整站至本地：
    wget -r -k -np seacragme.github.io/

解决目录空间不足问题：（软连接，硬连接）
    mv /var/www /home		#将www移动到home
    ln -s /home/www /var	#指向新位置，加-s软连接不占用磁盘空间，硬连接是copy

安装：Ports
    pkg_add -r wget
    cd /usr/obj
    wget https://ftp.jaist.ac.jp/pub/OpenBSD/6.3/ports.tar.gz
    tar zxf ports.tar.gz
    ln -S /usr/local/ports /usr/ports

进入要安装的目录
    make install clean

