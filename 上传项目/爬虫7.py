import requests
from lxml import etree
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
url='http://www.qiushibaike.com/text/'
res=requests.get(url,headers=headers)
selector=etree.HTML(res.text)
content=selector.xpath('//*[@id="qiushi_tag_121120420"]/a[1]/text()')
print(content)
