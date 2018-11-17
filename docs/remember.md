
## 记忆的长河，青春的流水账 ##


#### 20181117 ####

vim:

    :colorscheme <CTRL>D            #显示可用配色选项



#### 20181116 ####

1.   python:

    dir(os)         #列出模块的所有方法

2.  vimrc

    winpos 8 22
    set lines=76 columns=190

    set termencoding=utf-8
    set fileencoding=ucs-bom,utf-8,cp936,gb18030,big5,euc-jp,euc-kr
    set encoding=urf-8
    set gfn=Monaco:j10:cANSI
    set gfw=NSimsun:h12

    set number
    set nowrap
    set gcr=a:block-blinkon0
    set cursorline
    set magic
    set guioptions-=l
    set guioptions-=L
    set guioptions-=m
    set guioptions-=M
    set guioptions-=t
    set guioptions-=T
    set laststatus=2
    set foldcolumn=0
    set foldmethod=indent
    set foldlevel=3
    set foldenable

    set cindent
    set tabstop=4
    set softtabstop=4
    set shiftwidth=4
    set smarttab

    set ignorecase
    set hlsearch
    set incsearch
    set gdefault

    set wildmenu

    :usr_05.txt

    set noexpandtab
    set nocompatible
    set backspace=indent,eol,start
    set autoindent

    set ruler
    set showcmd
    set showmode
    vnoremap _9 y:exe "grep /" . escape(@", '\\/') . "/ *.c *.h"CR>

    set listchars=tab:>-,trail:-
    
    
    set expandtab
    set background=dark
    colorscheme darkblue


3.  vim 常用功能
3.1 #### usr_22.txt ####
    :edit .         #打开文件路径，其中o键打开文件，i键切换显示路径的方式，u键选择是否显示路径，v键纵向打开文件

3.2 #### usr_21.txt ####

    <CTRL>Z         #返回到终端命令行
    fg<CR>          #返回到vim

3.3 #### usr_20.txt ####

    :tab             #子窗口操作
    :tab + <CTRL>D  #自动补齐功能，显示可以使用的选项
    :tabedit newfile
    :tabfirst
    :tabnext
    :tabs
    :tabonly
    :tabmove

3.4 #### window size ####

    10<CTRL>W+      #当前窗口扩展10行



_______



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
