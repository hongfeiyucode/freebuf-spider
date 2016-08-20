# freebuf-spider

一个抓取freebuf所有栏目的文章的爬虫，以离线网页形式展现，上传了一些爬取好的结果

## 程序运行方式
```
  python freebuf.py
```
![程序运行方式](https://github.com/hongfeiyucode/freebuf-spider/blob/master/pic/how2run.png)

- 输入文件名：输入要生成的html文件的文件名
- 输入栏目网址：freebuf文章分成了很多栏目，在分类阅读里面可以获取每个栏目的网址
  ![](https://github.com/hongfeiyucode/freebuf-spider/blob/master/pic/article.png)
- 该栏目总共有多少页：在栏目网址后面加上   /page/页数

```
http://www.freebuf.com/sectool    -->
http://www.freebuf.com/sectool/page/100
```

  如果返回是![](https://github.com/hongfeiyucode/freebuf-spider/blob/master/pic/404.png)
  说明这个栏目没有这么多页，写程序的二分法不用我教吧，用这个方法可以快速得出总页数，然后填上即可

## 需要模块
```
  import requests
  import re
  import urllib
```  
## 输出结果

暂时爬取了三个栏目放在这里，大家可以看下效果，自己可以动手爬其他的

### 终端安全

可以看到freebuf终端安全的文章从建站到现在全部在这里了

![](https://github.com/hongfeiyucode/freebuf-spider/blob/master/pic/product.png)


### 安全工具合集
![](https://github.com/hongfeiyucode/freebuf-spider/blob/master/pic/product2.png)
