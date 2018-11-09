import requests
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
lists=[]
def get_info(url):
    data=requests.get(url,headers=headers)
    soup=BeautifulSoup(data.text,'lxml')
    addresses=soup.select('body > div.content > div.leftContent > ul > li > div.info.clear > div.address > div > a')
    prices=soup.select('body > div.content > div.leftContent > ul > li > div.info.clear > div.priceInfo > div.totalPrice > span')
    for address,price in zip(addresses,prices):
        datas={
            'address':address.get_text().strip(),
            'price':price.get_text()
        }
        lists.append(datas)

if __name__=='__main__':
    urls=['http://sy.lianjia.com/ershoufang/pg{}'.format(str(i)) for i in range(1,24) ]
    for url in urls:
        get_info(url)
    for list in lists:
        f=open('C:/Users/Asus/Desktop/fangjia.text','a+')
        try:
            f.write(list['address']+'')
            f.write(list['price'] + '\n')
            f.close()
        except UnicodeEncodeError:
            pass
