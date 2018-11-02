
## 记忆的长河，青春的流水账 ##


  #### 20181028 ####
  - 设置VIM的Vundle插件管理器：
    > 在配置文件里添加：
        >filetype off
         set rtp+=~/.vim/bundle/Vundle.vim
         call vundle#begin()

         Plugin 'VundleVim/Vundle.vim'
         Plugin 'altercation/vim-colors-solarized'
         Plugin 'Lokaltog/vim-powerline'

         " 记得安装完插件后要输入这2个：
         call vundle#end()
         filetype plugin indent on

        > 也可以输入查找命令进行选择性的安装：
          :PluginSearch         #在命令中按i健可以直接安装好
        > 删除插件，除了关闭Plugin命令还要输入: ':PluginClean'
        > 升级插件检查，输入： ':PluginUpdate'



  20181027
  _ 安装了一个OSX软件安装管理的HOMEBREW,
    命令是：'/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'
    [链接在这](https://brew.sh/index_zh-cn)

  20181026
  - 进入到了python 操作 SQLite3
  - 发现了两个好的模块：

    pip3 install "ipython[notebook]"
    pip3 install pandas

  20181024
  - 下载了MacVim，用`sudo vi /etc/paths`命令添加gvim 命令行的启动路径`/Applications.MacVim.app/Contents/bin`，这样就可以随时调用图形版的vim了
  - OSX系统默认安装的python2.7,竟然没有默认安装pip，原来还要手动安装
  > `sudo easy_install pip`   # easy_install是python默认安装的包



  20180123 纠结了一天多，总是登陆Github有问题，后来竟然把Mac的登陆密码也搞丢了，昨晚看群组消息，才知道是网站出问题了，神奇的一天。
