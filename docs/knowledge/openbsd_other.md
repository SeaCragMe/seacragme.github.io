OpenBSD　――　另类安装法

1月3号改进版 
在昨天的文档中, 我还有些地方不了解, 昨天晚上又操作了一次, 认识又新上一层. 在今天的文档中, 我们只需要要备份系统中的文件就可以重新克隆出一个新系统了.

我这装了好几台openbsd, 准备用来组局域网的, 所以操作起来很方便.

第一步, 记住自己在硬盘上分的各挂载点, 我的分区情况是: 
/dev/wd0a / 
/dev/wd0b swap 
/dev/wd0d /var 
/dev/wd0e /tmp 
/dev/wd0f /usr 
要一个硬盘上克隆一个新系统, 各挂载点要相同, 也就是说要和/etc/fstab上写的挂上号.

第二步, 备份文件: 
主要备份/dev/wd0a, /dev/wd0d, /dev/wd0f挂载点的文件. 我将这三个挂载点的文件分别存为root.tgz, var.tgz, usr.tgz., 放在/usr/back/目录下.

第三步, 挂上新硬盘wd1, 我们开始克隆系统: 
1, 为新硬盘分区: 
fdisk –i wd1 
disklabel –E wd1 
disklabel分的各挂载点同第一步说的一样, 各分区的大小可以自由变动. 
2, 格式化各分区 
newfs /dev/wd1a 
newfs /dev/wd1d 
newfs /dev/wd1e 
newfs /dev/wd1f 
3, 为新硬盘wd1设置mbr: 
fdisk –u –f /usr/mdec/mbr wd1 
4, 将备份的系统文件解到相应的wd1分区中: 
mount /dev/wd1a /mnt 
cd /mnt 
tar xvzfp /usr/back/root.tgz 
cd 
umount /mnt 
mount /dev/wd1d /mnt 
cd /mnt 
tar xzvfp /usr/back/var.tgz 
cd 
umount /mnt 
mount /dev/wd1f /mnt 
cd /mnt 
tar xvzfp /usr/back/usr.tgz 
cd 
umount /mnt 
在这里多谢谢三轮车夫提示, 在tar解压时加入p参数, 这样各文件所属就没有发生改变. 另外在挂载各区时最好先fsck修复检查一下. 
5, 设置pbr: 
fsck /dev/wd1a 
mount /dev/wd1a 
cp /usr/mdec/boot /mnt/boot 
/usr/mdec/installboot –v /mnt/boot /usr/mdec/biosboot wd1 
ok!到这里就操作完成了, wd1硬盘已装好了一个openbsd系统. 将wd1硬盘改为主启动盘, 你就有一个新系统了.

在第二步备份各分区文件时, 想到cnfug上的软盘系统, 在备份时你可以将一些自己认为不需要的文件删除, 对系统精减, 这样克隆出来的系统更小!

在第五步, 我又有一个想法, 就是关于与windows等多系统共存.等我有机会试验后再说!

/usr/mdec/目录下存放的是openbsd启动工具, 信息, 各位有兴趣的可以看看.

在我说的这个方法里, 你可以对一个系统进行多次备份, 主要就是三个区的文件备份, 我进行了几次备份, 第一次是最初安装的系统, 第二次是打上了locale patch补丁后的备份, 现在安装软件, 准备第三次备份. 自己想恢复哪时候系统都可以!

昨天晚上我只用的半个钟就让wd1克隆了一新系统. 所以操作还是很快的.

主要费时在备份解压文件上.

 

1月2号初版 
昨天晚上回来，　看着备份恢复mbr命令突然想到我可以将系统移到新硬盘上，　想到就动手操作，　从开始备份操作到新硬盘上的系统成功启动，　整个过程花了差不到２个小时．

需要: 一台已安装配置好的OpenBSD系统, 一块没安装系统的空硬盘．

我是在OpenBSD3.6下操作的．在操作之前，　我先简单的介绍ＯpenBSD的系统启动过程．

在i386平台上，　OpenBSD启动分两步，　系统开机进入启动时，　首先启动的是ＭＢＲ，　然后再启动PBR ( partition boot record) , mbr说明系统从哪启动，　pbr是载入/boot启动系统， 
这两步都可以自己操作．具体的损坏后安装操作可以参考OpenBSD FAQ 14节的How does OpenBSD/i386 boot?这一段．

下面我介绍如何将一个已安装配置好的OpenBSD系统移到一个新硬盘上，　然后我们就可以使用新硬盘上的OpenBSD了．

１，备份MBR, 当然如果你不备份也可以使用/usr/mdec/mbr这个也行（这个我还没操作过，　只在看man pages时上面都有说明） 
　　　dd if=/dev/wd0a of=boot.bin bs=512 count=1 
这一步总是提示硬盘忙, 所以我将这块硬盘挂到别的系统上备份mbr的: 
dd if=/dev/wd1a of=boot.bin bs=512 count=1

2, 备份系统文件，　除了/tmp下的文件不备份外，　/目录下的所有文件都备份． 
我的系统分区为wd0a /, wd0b swap, wd0d /var, wd0e /tmp, wd0f /usr: 
同备份mbr一样, 我将硬盘挂到别的系统上完成的: 
mount /dev/wd1a /mnt 
cd /mnt 
tar zcf ~/back/root.tar.gz . 
umount /mnt 
mount /dev/wd1d /mnt 
cd /mnt 
tar zcf ~/back/var.tar.gz . 
umount /mnt 
mount /dev/wd1f /mnt 
tar zcf ~/back/usr.tar.gz .

cd ~/back/ 
mv *.gz /mnt/ 
cd 
mv boot.bin /mnt 
halt -p

３，安装新硬盘． 
１， 分区： fdisk –i wd1 
２， disklabel –E wd1 (这里分的挂载点要和/etc/fstab的挂载点相同，　原来系统上分了几个挂载点，　现在这个硬盘就分几个挂载点)．

4, 为新硬盘配置mbr： 
　　　dd if = boot.bin of=wd1 
这里是FAQ上说的如何恢复mbr操作．我还没试过． 
　　　　fdisk –u –f /usr/mdec/mbr wd0 (wd0改为wd1，　现在我们为wd1设置mbr)

5, 为新硬盘配置pbr： 
　　　　操作步骤installboot (8); 
fsck /dev/wd1a 
mount /dev/wd1a /mnt 
cp /usr/mdec/boot /mnt/boot 
/usr/mdec/installboot –v /mnt/boot /usr/mdec/biosboot wd1

6, 将步骤２备份的系统文件解到新硬盘上． 
先前步骤2的root.tar.gz, var.tar.gz, usr.tar.gz文件是放在/usr目录下, 
将root.tar.gz解到 /dev/wd1a , var.tar.gz解到/dev/wd1d, usr.tar.gz解到/dev/wd1f．

好了，　现在可以将原来的系统关掉，　取下硬盘，　然后将从硬盘wd1改为挂主硬盘wd0，　开机启动新硬盘上的OpenBSD！基本上克隆主硬盘的OpenBSD系统到从硬盘上．现在发现主要是在启动gnome时报XKB错误，哪位兄弟能否详解一个XKB的各种信息；别的改变以的地方今晚回去再查查～～！

上面操作中有错误的地方请各位兄弟姐妹们指出！
