import requests
from bs4 import BeautifulSoup
import time
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
def judgment_sex(class_name):
    if class_name==['member_icol']:
        return '女'
    else:
        return '男'
def get_links(url):
    data=requests.get(url,headers=headers)
    soup=BeautifulSoup(data.text,'lxml')
    links=soup.select('#page_list > ul > li > a')
    for line in links:
        href=line.get("href")
        get_info(href)

def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    tittles=soup.select('div.pho_info > h4')
    addresses=soup.selct('span.pr5')
    prices=soup.select('#pricePart > div.day_l > span')
    images=soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    names=soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs=soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    for tittle,address,price,image,name,sex in zip(tittles,addresses,prices,images,names,sexs):
        data={
            'tittle':tittle.get_text().strip(),
            'address':address.get_text().strip(),
            'price':price.get_text(),
            'image': image.get("src"),
            'name': name.get_text(),
            'sex': judgment_sex(sex.get("class"))
        }
        print(data)

    if __name__=='__main__':
        urls=['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,14)]
        for single_url in urls:
            get_links(single_url)
            time.sleep(2)


