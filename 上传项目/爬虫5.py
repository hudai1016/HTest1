from lxml import etree
import requests
import csv
f=open('C://Users/Asus/Desktop/doubanbook.csv','wt',newline='',encoding='utf-8')
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
urls=["https://book.douban.com/top250?start={}".format(str(i)) for i in range(0,250,25)]
writer=csv.writer(f)
writer.writerow(('name','author','publisher','date','price','rate','comment'))
for url in urls:
    data=requests.get(url,headers=headers)
    selector=etree.HTML(data.text)
    infos=selector.xpath('//tr[@class="item"]')
    for info in infos:
        name=info.xpath('td/div/a/@title')[0]
        book_infos=info.xpath('td/p/text()')[0]
        author=book_infos.split('/')[0]
        publisher=book_infos.split('/')[-3]
        data=book_infos.split('/')[-2]
        price=book_infos.split('/')[-1]
        rate=info.xpath('td/div/span[2]/text()')[0]
        comments=info.xpath('td/p/span/text()')
        comment=comments[0] if len(comments)!=0 else '空'
        writer.writerow(('name','author','publisher','date','price','rate','comment'))
f.close()
