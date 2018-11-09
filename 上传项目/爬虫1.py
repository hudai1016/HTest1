import requests
import re
import time
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
f=open("C:/Users/Asus/Desktop/doupo.txt",'a+')
def get_info(url):
    data=requests.get(url,headers=headers)
    if data.status_code==200:
        contents=re.findall('<p>(.*?)<p>',data.content.decode('utf-8'),re.S)
        for content in contents:
            f.write(content+'\n')
        else:
            pass

if __name__=='__main__':
    urls=['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2,1665)]
    for url in urls:
        get_info(url)
        time.sleep(1)
f.close()



