import pandas as pd
import numpy as np

data = pd.read_excel('C:\\Users\\Asus\\Desktop\\traintest.xlsx')


# print(data)

def reformat_data(row):
    activity = []
    activitys = []
    for t in row[-1].strip().split('#'):
        # print(t)
        activity = [j for j in t.strip().split(':')]

        activitys.append(activity)
    # print(activitys)
    # row[-1]=activitys
    return activitys


data.iloc[:, -1] = data.apply(reformat_data, axis=1)
##print(data.iloc[:,-1])
# 用户个数
user_num = len(set(data['user_id']))

#3print(user_num)

merchandise = []#商品种类
click_counts = 0  # 总点击数
favor_counts = 0  # 收藏数
shopping_cart_counts = 0  # 添加到购物车数
buy_counts = 0  # 购买次数
total=0#总共操作次数

for t in data.values:
    for j in t[-1]:  # j为点击
        total+=1
        if j[-1] == '0':
            click_counts += 1
        if j[-1] == '1':
            shopping_cart_counts += 1
        if j[-1] == '2':
            buy_counts += 1
        if j[-1] == '3':
            favor_counts += 1
        merchandise.append(j[0])
#商品个数
merchandise_num = len(set(merchandise))
##print(merchandise_num)
print(total)
print(click_counts)
print(shopping_cart_counts)
print(buy_counts)
print(favor_counts)


def user_statics(rows):
    user_id=rows.iloc[0,0]
    click_have_add = {}  ##点击次数
    favor_have_add={}    ##收藏次数
    cart_have_add={}     ##添加购物车次数
    buy_have_add={}      ##购买次数
    for t in rows.iloc[:,-1].values:#最后一列
        for j in t:
            if j[-1]=='0' and j[0] not in click_have_add.keys():
                click_have_add[j[0]]=1
            elif j[-1]=='0':
                click_have_add[j[0]]+=1

            if j[-1]=='1' and j[0] not in cart_have_add.keys():
                cart_have_add[j[0]]=1
            elif j[-1]=='1':
                cart_have_add[j[0]]+=1
            if j[-1]=='2' and j[0] not in buy_have_add.keys():
                buy_have_add[j[0]]=1
            elif j[-1]=='2':
                buy_have_add[j[0]]+=1

            if j[-1]=='3' and j[0] not in favor_have_add.keys():
                favor_have_add[j[0]]=1
            elif j[-1]=='3':
                favor_have_add[j[0]]+=1
    print(user_id,buy_have_add)#每个用户商品点击个数

data.groupby(by='user_id').apply(user_statics)