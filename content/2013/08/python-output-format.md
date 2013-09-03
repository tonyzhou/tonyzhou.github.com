Title: Python格式化输出
Date: 2013-08-01 16:57
Category: Python
Tags: publishing
Slug: python-output-format
Author: Tony Zhou
Summary: 从2.6版本开始，Python引入了一种新的格式化输出字符串的方式：string.format，这种格式化方式和老的%tuple方式有所不同。 有了这个string.format，我们能更灵活的输出格式化字符串。

从2.6版本开始，Python引入了一种新的格式化输出字符串的方式：string.format，这种格式化方式和老的%tuple方式有所不同。 有了这个string.format，我们能更灵活的输出格式化字符串。

##string.format使用方式

``` python
	>>>print '{0} and {1}'.format('spam', 'eggs')
	spam and eggs
```

{0}和{1}在这里被称作replacement_field，replacement_field在输出时候会被替换成指定的参数，除了{number}，replacement_field还支持更加复杂的用法，它的详细语法格式如下：

	replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
	field_name        ::=  <arg_name ("." attribute_name | "[" element_index "]")*
	arg_name          ::=  [identifier | integer]
	attribute_name    ::=  identifier
	element_index     ::=  integer | index_string
	index_string      ::=  <any source character except "]"> +
	conversion        ::=  "r" | "s" | "a"
	format_spec       ::=  <described in the next section>

* replacement_field必须被包围在"{}"中，任何在"{}"之外的字符串都会被直接输出，如果要输出"{", 必须使用转义“{{”。

* field_name表示格式化参数的参数名，它可以是字典的key（当参数是一个dictionary），也可以是一个数字。

* conversion以!开头，表示格式化之前是否需要对参数进行强制转换，它支持三种形式的转换：!s-对参数调用str(), !r-对参数调用repr(),!a对参数调用ascii()

* format_spec以:开头，表示参数的输出格式，详细定义如下：

	format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
	fill        ::=  &lt;a character other than '{' or '}'\>
	align       ::=  "<" | ">" | "=" | "^"
	sign        ::=  "+" | "-" | " "
	width       ::=  integer
	precision   ::=  integer
	type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

详细的格式化输出例子，请见：http://docs.python.org/3/library/string.html#format-examples

特别留意datetime的输出格式：

``` python
>>> import datetime
>>> d = datetime.datetime(2010, 7, 4, 12, 15, 58)
>>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
'2010-07-04 12:15:58'
```

## string.format对比%tuple

Python官方文档将string.format称为fancier output formatting, 毫无疑问string.format比%tuple花哨很多， 比如：

string.format支持argment的reuse：

``` python
tu =(12,45,22222,103,6)
print'{0} {2} {1} {2} {3} {2} {4} {2}'.format(*tu)
```

string.format是一个函数，可以在用作其它函数的参数，从而有更加灵活的用法：

``` python
from datetime import datetime,timedelta

once_upon_a_time = datetime(2010,7,1,12,0,0)
delta = timedelta(days=13, hours=8,  minutes=20)

gen =(once_upon_a_time +x*delta for x in xrange(20))
print'\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen))
```

以上例子均取自: http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format

Python官方文档建议用string.format替换%tuple方式进行格式化输出，除非你要编写Python2.5及以下版本兼容的代码。