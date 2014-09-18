# readability for python3


### 抓取页面标题和正文的小工具

- - -

from arc90labs-readability version 1.7.1

fork from https://github.com/kingwkb/readability



**update**

1 整体移植到python3, 改用beautifulsoup4, 修正原先不兼容的地方

2 使用requests请求，伪造request header的user-agent字段，防止网站屏蔽

3 对编码做出判断

4 增加少部分注释

- - -
用法：

```python
from py_read import py_read

if __name__ == '__main__':
    obj = py_read("http://www.chioka.in/differences-between-l1-and-l2-as-loss-function-and-regularization/");

    print(obj.title)
    print(obj.content)
```
目前content内容是HTML表示