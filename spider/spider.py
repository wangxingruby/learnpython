from urllib import request
from numpy import unicode
import re
import json
import time

# 使用原生爬虫爬取豆瓣图书 Top 250书籍信息， 
# 每一本书的信息都需要爬取，包括书名、作者、内容简介...等。 
# 参考地址：https://book.douban.com/top250
class Spider():
    base_url = 'https://book.douban.com/top250?start='
    inside_url_pattern = '<a class="nbg" href="([\s\S]*?)"\W*onclick='
    
    inside_name_pattern = '<span property="v:itemreviewed">([\s\S]*?)</span>'
    inside_value_pattern = '<div id="content">([\s\S]*?)<div id="footer">'

    img_pattern = '<a class="nbg" href="([\s\S]*?)" title="'
    author_pattern ='<span class="pl">作者:</span>&nbsp;[\s\S]*?<a href="[\s\S]*?>([\s\S]*?)</a>'
    page_pattern ='<table width="100%">([\s\S]*?)</table>'
    name_pattern ='<table width="100%">([\s\S]*?)</table>'
    abstract_pattern ='<table width="100%">([\s\S]*?)</table>'
    rating_nums_pattern ='<table width="100%">([\s\S]*?)</table>'
    

    def __create_url(self,i):
        #拼接外页的url
        r = Spider.base_url+str(i*25)
        return r

    def __fetch_content(self,url):
        htmls = ''
        # try:
        #     r = request.urlopen(url,data=None, timeout=3)
        #     htmls = r.read()
        #     htmls = str(htmls,encoding = 'utf-8')
        # except BaseException :
        #     pass
        print(url)
        r = request.urlopen(url,data=None, timeout=3)
        time.sleep(3)
        htmls = r.read()
        htmls = str(htmls,encoding = 'utf-8')
        return htmls

    def __achieveone(self,htmlin):
        #一本书一个book
        book = {}
        name = re.findall(Spider.inside_name_pattern,htmlin)
        book['bookname'] = name[0]
        insidevalue = re.findall(Spider.inside_value_pattern,htmlin)
        insidevalue = insidevalue[0]
        img = re.findall(Spider.img_pattern,insidevalue)
        if len(img) > 0:
            book['img'] = img[0]
        else:
            book['img'] = ''

        auther = re.findall(Spider.author_pattern,insidevalue)
        if len(auther) > 0:
            book['auther'] = auther[0]
        else:
            book['auther'] = ''

        return book



    def __achieveall(self,htmls):
        #一个外页有25本书
        booklist = []
        html_list = re.findall(Spider.page_pattern,htmls)

        for html in html_list:
            try:
                inside_url = re.findall(Spider.inside_url_pattern,html)
                inside_url = inside_url[0]
                htmlin = self.__fetch_content(inside_url)
                book = self.__achieveone(htmlin)
                book['inside_url'] = inside_url
                booklist.append(book)
            except BaseException :
                print('exception')
        return booklist



    def go(self):
        for i in range(0,1,1):
            url = self.__create_url(i)
            htmls = self.__fetch_content(url)
            booklist = self.__achieveall(htmls)
            #booklist = str(booklist,encoding = 'utf-8')
            filename = 'write_data.txt' 
            with open(filename,'w',encoding='utf-8') as f: 
                # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！ 
                res = json.dumps(booklist,ensure_ascii=False)
                f.write(res)



s = Spider()
s.go()
