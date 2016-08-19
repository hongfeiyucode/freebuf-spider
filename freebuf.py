#coding:utf-8
import requests
import re
import urllib

filename = raw_input(u"输入文件名: \n")
#filename= unicode(filename , "utf8")
f=open(filename+".html",'a')
home = raw_input(u"输入栏目网址: \n")
start = 1
end = input(u"该栏目总共有多少页:\n")
for i in range(start,end+1):
    print u"正在解析第"+str(i)+u"页..."
    html = requests.get(home+'/page/'+str(i))
    if i==start:
        site = re.findall('([\s\S]*)      </div>\n      <div class="news-more" id="pagination">',html.text,re.S)
    else:
        site = re.findall('<div id="timeline" class="news-detial">([\s\S]*?)      </div>\n      <div class="news-more" id="pagination">',html.text,re.S)
    for each in site:
        f.write(urllib.unquote(each.encode('utf-8')))
f.close()