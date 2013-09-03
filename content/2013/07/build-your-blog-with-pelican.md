Title: 用pelican搭建博客
Date: 2013-07-11 16:57
Category: Python
Tags: pelican,publishing,python 
Slug: build-your-blog-with-pelican
Author: Tony Zhou
Summary: 使用wordpress搭建博客网站是一种常规的做法，但也是一种浪费资源的做法。下面介绍如何使用静态博客生成器pelican搭建个人博客。

使用wordpress搭建博客网站是一种常规的做法，但也是一种浪费资源的做法。下面介绍如何使用静态博客生成器pelican搭建个人博客。

如果使用wordpress，你往往需要做很多事情：

* 购买一个免费的PHP+MYSQL托管主机
* 购买一个域名
* 将wordpress的代码传到主机空间
* 配置数据库，配置主题

wordpress的最大问题在于性能，在没有经过优化的情况下，每次访问一篇博客文章都要走HTTP
server，并运行一段PHP代码，读几次数据库. 换个角度来看，对更新并不频繁的博客站点来说，根本不需要如此复杂的过程，静态页面就能满足博客网站的需求。博客网站还是存在一部分“动态”的内容：评论，幸运的是我们有disqus评论系统来实现这一需求。

静态博客生成器，在不同语言/平台有不同的实现。最常见的莫过于octopress，但它是用ruby语言开发的。作为对Python比较感兴趣的开发者，我选择用python写的pelican。

博客网站的托管，这里有成本低效果好的方案——github pages，github官方也支持将github pages用作个人博客，对在博客上写技术文章的人来说，不必顾忌是否在滥用github。

##pelican安装##

Pelican的官方站点有关于快速启动的[介绍](http://docs.getpelican.com/en/latest/getting_started.html#installing-pelican)，这里有两种安装方式：全局安装和在virtualenv下的安装，推荐使用后者。安装过程中需要用到[virtualenv](http://pypi.python.org/pypi/virtualenv)和[pip](http://pypi.python.org/pypi/pip)。

``` bash
$ virtualenv ~/virtualenvs/pelican
$ cd ~/virtualenvs/pelican
$ . bin/activate

$ pip install -e git://github.com/getpelican/pelican#egg=pelican

$ pip install Markdown
```

##使用Pelican-quickstart产生示例网站##

使用pelican-quickstart快速产生一个示例网站

``` bash
$ pelican-quickstart
```

命令运行过程中会提示你输入网站的参数，比如站点名称，是否支持ssh上传网站内容等；运行结束，当前目录下会产生如下的目录结构：

	yourproject/
	├── content
	│   └── (pages)
	├── output
	├── develop_server.sh
	├── Makefile
	├── pelicanconf.py       # Main settings file
	└── publishconf.py       # Settings to use when ready to publish

content目录用于存放博客文章的markdown文档，一般根据"YEAR/MONTH"的目录结构存放（content/2013/07)；output目录存放pelican的生成结果；develop_server.sh是一个bash脚本,用于控制本地测试web服务器的启动和自动监视进程；pelicanconf.py是网站的配置文件，另外还有一个配置文件publishconf.py，前者一般用于本地测试，后者一般用于网站发布。

Makefile中包含了接下来Pelican支持的操作，里面包含了手动和自动生成站点页面的几个命令：

``` bash
$ make html         #生成整个网站的内容

$ make regenerate   #对上次生成后Modified部分生成（增量）

$ make serve        #启动一个Web服务器，可在本机测试生成的站点

$ make devserver    #生成一个Web服务器，并且自动监视修改，增量生成

$ make rsync_upload #将网站内容上传到服务器
```

##使用Markdown撰写博客文章##

Markdown是一种轻量级的标记语言，“易读易写”是它的特点，相比较于HTML，Markdown的标记更加简洁，输入更方便，对阅读的影响更小。Markdown是基于文本格式的，可以用任何文字编辑器打开。学习曲线也非常平缓，是一种让作者把注意力集中在写作上的语言。这里推荐使用[Mou](http://mouapp.com)编写markdown文档。

Pelican要求博客文章的Markdown文件必须有metadata，格式如下：

	Title: build your blog with pelican 
	Date: 2013-07-07 10:20
	Category: Python
	Tags: pelican, publishing
	Slug: build-your-blog-with-pelican
	Author: Tony Zhou
	Summary: summary of my blog

##博客定制##

* 换一个不错的主题

Responsive theme是一种比较友好的主题，它能产生对设备自适应的版式，用移动设备访问网站同样有完美的阅读效果。我发现有个台湾女程序员开发的fresh主题不错，也是一个responsive theme，因此决定采用这个主题。

更换主题，只需要在配置文件中添加：

``` python
THEME = " #the path of the theme directory# "
```

* 定制博客的menu

pelican默认的网站navigation bar（以下称之为menu）的items是文章的Categories， 这可能不是我们想要的，一般情况下，我们需要这么几个navigation items: blog(博客主页的链接)、Archives（博客文章的列表）、About（作者的自我介绍）... 因此我们需要在配置文件中作如下几个配置：

``` python
USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False
HIDE_CATEGORIES_FROM_MENU = True
MENUITEMS = [('Blog', '#YOUR_SITE_URL#'),('Archives', '#YOUR_SITE_URL#/archives.html'), ('About', '#YOUR_SITE_URL#/about.html')]
```

* 定制博客的URL

博客的URL，需要特别定制，我希望博客文章采用以下的URL：

``` python
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
```
这里面用到了slug，每篇博客文章都有自己的meta data，slug在meta data中配置。

* 加上评论功能

disqus是一个在线评论系统，可以为网站提供评论托管服务，集成disqus非常简单：只要在静态页面上放disqus的js源代码。 pelican的主题已经内置了对disqus的支持，我们只要在配置文件中添加：

``` python
DISQUS_SITENAME = "YOUR_DISQUS_SITENAME"
```

##更多参考##

* [pelican](http://docs.getpelican.com)官方网站

* [virtualenv](https://pypi.python.org/pypi/virtualenv) in pypi

* [jsliang](http://jsliang.com/blog/2013/02/moving-to-pelican-hosting-on-github-pages.html)'s blog about pelican

