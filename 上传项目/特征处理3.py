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
# print(data)
# 用户个数
user_num = len(set(data['user_id']))


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
# print(merchandise_num)
print(total)
print(click_counts)
print(shopping_cart_counts)
print(buy_counts)
print(favor_counts)


def user_statics(rows):
    user_id=rows.iloc[0,0]
    click_have_add = {}
    favor_have_add={}
    cart_have_add={}
    buy_list=[]#购买序列

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

            if j[-1]=='3' and j[0] not in favor_have_add.keys():
                favor_have_add[j[0]]=1
            elif j[-1]=='3':
                favor_have_add[j[0]]+=1
            buy_list.append(j[-1])
    # print(user_id,buy_list)


    print(user_id,favor_have_add)#每个用户商品点击个数

data.groupby(by='user_id').apply(user_statics)

#生成以商品为索引的数据
def merchandise_static(df):
    data1=df.iloc[:,:-3].sum().values
    data2=(df.iloc[0,-3:].values)
    result=pd.Series(np.concatenate([data1,data2]))
    return result

merchandise_data=[]
for t in data.iloc[:,-1].values:
    for j in t:
        merchandise_data.append([j[0],j[1],j[2],j[-1]])
merchandise_data=pd.DataFrame(merchandise_data)

#输出
# print('shangpin xinxi',len(merchandise_data))

from sklearn.preprocessing import OneHotEncoder

ohe=OneHotEncoder(categorical_features=[3],n_values=[4])

merchandise_data=pd.DataFrame(ohe.fit_transform(merchandise_data.values).toarray())
print(len(merchandise_data))
result=merchandise_data.groupby(4).apply(merchandise_static)
result.columns=['点击数','添加购物车数','购买数','添加收藏夹','商品id','品类id','品牌id']
print(len(merchandise_data.groupby(4)))
result.to_excel('商品信息.xlsx',index=False)



