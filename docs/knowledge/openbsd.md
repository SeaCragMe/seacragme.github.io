
## 关于OpenBSD系统的知识 ##

### 系统安装 ###



#### U盘启动制作 ####
20181102

installxx.fs 是 u 盘镜像文件，直接刻录在 u 盘上即可，在 linux 下或者 BSD 系统下，使用 dd 命令即可。


下面给出我的操作步骤和说明，OpenBSD 系统为例：

1，插入 u 盘，这时系统内核认出 u 盘，给出磁盘名称，这个很重要。如果当前是在第一个 console 字符界面下，屏幕或许有提示，很多行，最常见的就是：...umass0...sd0...serial...
如果没有看到这些，你可以在命令中输入“ dmesg | tail ” 查看内核消息的最近部分，里面有磁盘名称。例子中的磁盘名称就是 sd0

2，命令中输入“ disklabel sd0” 查看 u 盘分区和分区的文件格式，确认是否正确，有用的数据请备份。

3，知道了磁盘名称，就可以开始制作 u 盘安装盘了。如果 u 盘上分区已经挂载，请用 mount 命令看看，然后用 umount 命令卸载它们。最后输入以下命令：
dd if=/path/to/installxx.fs of=/dev/rsd0c bs=1m
这里解释一下。/path/to/installxx.fs 就是 install55.fs 的文件路径，/dev/rsd0c 指的是 u 盘这个硬件，根据情况将“sd0”替换为第1步得到的u盘磁盘名称。

--------- 安装过程与光盘安装相同，最后安装软件包的时候安装介质选择“disk”




------



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

在线升级：
    pkg_add -u

查看已经安装的软件：
    pkg_info

    pkg_add virsion  #查看已安装的软件版本号
删除软件：
    pkg_delete

进入要安装的目录
    make install clean


挂载U盘：
    
    显示当前所有磁盘的名称：
        sysctl hw.disknames
    
    查看sd0i的磁盘分区等信息：
        disklabel sd0i
    挂载：
        mount /dev/sd0i /mnt/usb
    U盘sd0制作install64.fs的启动盘：
        dd if=install64.fs of=/dev/sd0c
    
    在OSX下需要加上sudo,否则会报错dd: /dev/disk1: Permission denied
        
        sudo dd if=install64.iso of=/dev/disk1
        这里的disk1是由以下命令找到的：
            diskutil list






20181102


由于光驱损坏，就想着做一个u盘安装盘。刚制作成功，步骤如下：

0，处理openbsd镜像文件 install51.iso，步骤
  1）mkdir /mnt2
  2) vnconfig vnd0 /home/install51.iso
  3) mount -t cd9660 /dev/vnd0c /mnt2

1，fdisk -i sd0
重写 mbr

2，disklabel -Aw sd0
自动方法分区 sd0
结果是少量空间分配 swap，其余给 a 区，将是安装盘的启动分区

3，newfs /dev/rsd0a
格式化 u 盘第一个分区

4，mount /dev/sd0a /mnt
挂接 u 盘第一个分区

5，cp /usr/mdec/boot /mnt/boot
拷贝 boot 程序，放在 u 盘启动分区中，引导 bsd 内核需要的程序

6，/usr/mdec/installboot –v /mnt/boot /usr/mdec/biosboot sd0
安装启动第一阶段代码 /usr/mdec/biosboot，目的是启动 boot 程序

7，cp -r /mnt2/5.1 /mnt/
把启动所需文件从安装镜像文件中拷贝至 u 盘，所有所需文件在u盘上的路径为 /5.1/i386

----------- 使用方法 ----------- ----------- ----------- ----------- ----------- -----------
u盘启动后，进入 boot> ，按任意键等待

1，machine diskinfo
查看可以识别的硬盘

2，set
查看 boot 的引导参数

3，ls
查看当前目录下的文件，可以执行“ ls 5.1/i386 ”找到启动内核

3，boot 5.1/i386/bsd.rd
启动 bsd.rd 内核，进入安装程序

4，一路安装，直到安装程序时，询问 SETS 所在的介质和路径

5，！
暂时暂停安装，退出 install 程序

6，mount /dev/sd0a /mnt2
挂载 u 盘a分区

7，return
返回，继续 install 安装程序，停留在安装介质的选择上

8，继续时，安装介质选择 disk，已经挂载，路径写 /mnt2/5.1/i386


