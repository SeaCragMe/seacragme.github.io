一、OpenBSD.Apache.MySQL.PHP软件环境的安装
 
OpenBSD内核中已经集成了Apache，而且内置了对PHP的支持，所以安装MySQL、PHP环境非常的简单。
 
需要注意的是，在系统安装分区的时候，请按下面的示例进行分区（80G硬盘）：
 
/             200M
(swap)        1G
/tmp          200M
/usr          500M
/usr/local    200M
/var          100M
/var/mysql    10G
/var/mail     100M
/var/log      5G~10G
/home         200M
/var/www      剩余空间
 
在安装程序询问要安装的组件时，最好不要选择comp44.tgz这个包，系统安装到最后询问是否默认启动服务时，一律回答“No”。
 
halt重启后执行下面的命令安装必须的软件，以OpenBSD4.4为例进行讲解，root权限。
 
export PKG_PATH=ftp://ftp.openbsd.org/pub/OpenBSD/4.4/packages/i386/
pkg_add wget mysql-server php5-gd-5.2.6-no_x11 phpMyAdmin pecl-APC
 
等所需的软件都安装完成后，按提示作链接并创建PHP临时目录：
 
ln -s /var/www/conf/modules.sample/php5.conf /var/www/conf/modules
ln -fs /var/www/conf/php5.sample/apc.ini /var/www/conf/php5/apc.ini
ln -fs /var/www/conf/php5.sample/gd.ini /var/www/conf/php5/gd.ini
ln -fs /var/www/conf/php5.sample/mbstring.ini /var/www/conf/php5/mbstring.ini
ln -fs /var/www/conf/php5.sample/mcrypt.ini /var/www/conf/php5/mcrypt.ini
ln -fs /var/www/conf/php5.sample/mysql.ini /var/www/conf/php5/mysql.ini
mkdir /var/www/tmp
chmod 0777 /var/www/tmp
 
二、使MySQL适应chroot环境
 
由于OpenBSD中的Apache默认工作于chroot环境下，无法直接与MySQL通信，所以需要修改下MySQL的配置文件，使之适应chroot环境。
 
执行下面的命令：
 
mkdir -p /var/www/var/run/mysql
chown _mysql:_mysql /var/www/var/run/mysql
 
等到上面的命令都执行完成后，还需要修改MySQL的配置文件。
 
vi /etc/my.cnf
 
将[client]段的socket修改成：
 
socket          = /var/www/var/run/mysql/mysql.sock
 
将[mysqld]段的socket修改成：
 
socket          = /var/www/var/run/mysql/mysql.sock
 
在[mysqld]段增加：
 
skip-networking
 
其他的请酌情修改。
 
改完后保存退出。
 
三、phpMyAdmin的配置
 
在上面pkg_add phpMyAdmin以后，提示ln做个连接就可以用phpMyAdmin了。不过偶试了，是不行的，404错误。所以，我们需要把phpMyAdmin拷贝到/var/www/htdocs目录下面使用。
 
mkdir /var/www/htdocs/pma
cp -rf /var/www/phpMyAdmin/* /var/www/htdocs/pma/
 
同样需要修改pma目录下的config.inc.php文件，加个字母即可。
 
其他关于PHP的强化、SSH强化、PF防火墙以及系统其他部分的安全强化，可以参照O.N.M.P.手册的第二版，这里就不罗嗦了。
 
另外，由于Apache已经是chroot，所以PHP的强化设置会略有不同，如下：
 
# 禁止动态加载模块
enable_dl = Off
 
# 隐藏PHP信息
expose_php = Off
 
# 限定可访问目录
# 注意此时的根目录实际是/var/www目录
open_basedir = /
 
# 设定PHP上传文件的临时目录
# 同理，此时的/tmp目录实际是/var/www/tmp目录
upload_tmp_dir=/tmp
 
# 禁用危险函数（注意下面的内容应该是一行，编排的原因分成了多行）
disable_functions = phpinfo,com,shell,exec,system,passthru,error_log,
stream_socket_server,putenv,ini_alter,ini_restore,ini_set,dl,openlog,
syslog,readlink,symlink,link,leak,fsockopen,pfsockopen,proc_open,
popepassthru,escapeshellcmd,escapeshellarg,chroot,scandir,
chgrp,chown,shell_exec,proc_get_status,popen,shmop_close,
shmop_delete,shmop_open,shmop_read,shmop_size,shmop_write
 
# 启用PHP的安全模式
# PHP在安全模式下运行是用性能换安全。据简单测试，性能下降到30%左右，各位请酌情使用
safe_mode = On
 
# pecl-APC只使用16M的共享内存用以加速PHP程序的运行
apc.shm_size=16M
 
四、O.A.M.P.的启动
 
对于Apache来说，系统虽然提供了自动启动的方法，但是因为考虑到MySQL需要先启动，因此仍然在/etc/rc.local文件中解决。
 
vi /etc/rc.local
 
跳到最后，加入：
 
rdate -n 210.72.145.44
# Start MySQL
if [ -x /usr/local/bin/mysqld_safe ] ; then
   echo -n 'Starting MySQL...'
   su -c mysql root -c '/usr/local/bin/mysqld_safe >/dev/null 2>&1 &'
   echo "DONE"
fi
# Start Apache
apachectl start
 
五、提高O.A.M.P.环境的安全性
 
在O.A.M.P.环境下，除了可以和O.N.M.P.环境下一样设置提高安全性以外，在Apache环境下，还可以安装mod_security这个模块来提高web程序的安全性。
 
export PKG_PATH=ftp://ftp.openbsd.org/pub/OpenBSD/4.4/packages/i386/
pkg_add modsecurity-apache
 
安装完成后使用下面的命令启用mod_security：
 
/usr/local/sbin/mod_security-enable
 
mod_security可以用来抵御XSS和SQL注入等攻击，我们需要把一些“防御”指令加到mod_security的配置文件中：
 
vi /var/www/conf/modules/modsecurity.conf
 
输入下面的内容：
 
# 启用mod_security过滤
SecFilterEngine On
 
# 分析URL请求
SecFilterCheckURLEncoding On
 
# 检查字节长度以避免栈溢出攻击（数字请酌情修改）
SecFilterForceByteRange 32 126
 
# 有效记录日志信息
SecAuditEngine RelevantOnly
 
# 定义日志文件
SecAuditLog logs/audit_log
 
# 定义DEBUG文件
SecFilterDebugLog logs/modsec_debug_log
SecFilterDebugLevel 0
 
# 检查POST请求（某些POST请求可能会和这个冲突）
# 使用phpMyAdmin管理数据库时，某些操作会被这个拦截（例如新建数据库和用户时）
# 遇此情况，则把此行注释掉，重启Apache
# 操作完后记得恢复，以提高数据库的安全性
SecFilterScanPOST On
 
# 阻止返回406错误
SecFilterDefaultAction "deny,log,status:406"
 
# 阻止返回500错误
SecFilterDefaultAction "deny,log,status:500"
 
# 当攻击者使用chmod,chgrp,wget等命令的時候,重定向到特殊的页面（请自行酌情增减）
SecFilter chmod redirect:http://www.google.com
SecFilter chgrp redirect:http://www.google.com
SecFilter wget redirect:http://www.google.com
 
# 防止操作系统关键词攻击
SecFilter /bin
SecFilter /sbin
SecFilter /etc
SecFilter /bsd
SecFilter /usr
SecFilter /var
 
# 只接受知道如何处理的请求
# GET请求是个例外，是因为某些客户端把text/html当做请求内容的一部分
SecFilterSelective REQUEST_METHOD "!^(GET|HEAD){1}quot; chain
SecFilterSelective HTTP_Content-Type "!(^application/x-www-form-urlencoded$|^multipart/form-data;)"
 
# 不接受仅有GET和HEAD头的请求
SecFilterSelective REQUEST_METHOD "^(GET|HEAD){1}quot; chain
SecFilterSelective HTTP_Content-Length "!^{1}quot;
 
# 要求每个POST请求提供长度
SecFilterSelective REQUEST_METHOD "^POST{1}quot; chain
SecFilterSelective HTTP_Content-Length "^{1}quot;
 
# 不接受无法处理的转换
SecFilterSelective HTTP_Transfer-Encoding "!^{1}quot;
 
# 防止目录遍历攻击
SecFilter "\.\./"
 
# 防止跨站(XSS)攻击(HTML/Javascript注入)
SecFilter "<( |\n)*script"
SecFilter "<(.|\n)+>"
 
# 防止SQL注入攻击（简单示例，请自行完善）
SecFilter "delete[[:space:]]+from"
SecFilter "insert[[:space:]]+into"
SecFilter "select.+from"
SecFilter "union[[:space:]]+from"  
SecFilter "drop[[:space:]]"
 
# 需要HTTP头确认
SecFilterSelective "HTTP_USER_AGENT|HTTP_HOST" "^{1}quot;
 
# 呵呵~~~把服务器伪装成M$机器
ServerTokens Full
SecServerSignature "Microsoft-IIS/6.0"
 
# 限制upload.php文件只能用来上传jpeg,bmp和gif的文件（仅为示例，请酌情修改）
#<Location /upload.php>
#SecFilterInheritance Off
#SecFilterSelective POST_PAYLOAD "!image/(jpeg|bmp|gif)"
#</Location>
 
在/usr/local/share/doc/mod_security目录下有pdf版本的使用手册，可以用PSFTP down下来仔细看。自带的配置示例：
/usr/local/share/examples/mod_security/httpd.conf.example-minimal。
 
记住把mod_security的配置文件保存在/var/www/conf/modules目录，例如上面的：/var/www/conf/modules/modsecurity.conf
 
mod_security的配置按需修改好后，保存退出，重启Apache即可！
 
注意：上面的配置仅为示例，未必适合你的环境，请结合环境情况酌情修改！个别参数调整不当可能造成无法访问的后果！


