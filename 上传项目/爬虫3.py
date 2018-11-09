import requests
import re
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

lists=[]
def judgement_sex(sex):
    if sex=='manIcon':
        return '男'
    else:
        return '女'
def get_info(url):
    data=requests.get(url,headers=headers)
    ids=re.findall('<h2>(.*?)</h2>',data.text,re.S)
    levels=re.findall('<div class="articleGender \D+Icon">(.*?)</div>',data.text,re.S)
    sexs=re.findall('<div class="articleGender (.*?)Icon">',data.text,re.S)
    contents=re.findall('<div class="content">.*?<span>(.*?)</span>',data.text,re.S)
    for id,level,sex,content in zip(ids,levels,sexs,contents):
        datas={
            'id':id,
            'level':level,
            'sex':judgement_sex(sex),
            'content':content
        }
        lists.append(datas)



if __name__=='__mian__':
    urls=['http://www.qiushibaike.com/text/pade/{}/'.format(str(i)) for i in range(1,36)]
    for url in urls:
        get_info(url)
    for list in lists:
        f = open('C:/Users/Asus/Desktop/0.text', 'a+')
        try:
            f.write(list['id']+'\n')
            f.write(list['level'] + '\n')
            f.write(list['sex'] + '\n')
            f.write(list['content'] + '\n\n')
            f.close()
        except UnicodeEncodeError:
            pass



