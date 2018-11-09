import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import r2_score


data = pd.read_excel('C:\\Users\\Asus\\Desktop\\traintest.xlsx')
data=data.dropna(how='any')
users=len(data.drop_duplicates(['user_id']))
print(users)                #用户个数
merchants=len(data.drop_duplicates(['merchant_id']))




print(merchants)            #商店个数
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
#3print(data)
# 用户个数
user_num = len(set(data['user_id']))

##print(user_num)

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
    click_have_add = {}
    favor_have_add={}
    cart_have_add={}
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
    ##print(user_id,favor_have_add)#每个用户商品点击个数

data.groupby(by='user_id').apply(user_statics)

data=data.iloc[:,[1,2,5]]
data.loc[(data.age_range == 7) | (data.age_range == 8), 'age_range'] = 7
ohe = OneHotEncoder(n_values=[8, 3])
data1 = ohe.fit_transform(data.iloc[:, :-1]).toarray()
def split_log(row):
    lab=row[-1]
    lines=lab.split('#')
    click=0
    card=0
    purchase=0
    favourite=0
    for line in lines:
        click += 1
        ts = line.split(':')[4]
        if ts == '1':
            card += 1
        if ts == '2':
            purchase += 1
        if ts == '3':
            favourite += 1
    return [float(click), float(round(purchase / click, 3)), float(card), float(favourite)]
data2 = np.apply_along_axis(split_log, 1, data)
data = np.hstack([data1, data2])
data1=data[:,:14]
data2=data[:,14]
x=np.array(data1)
y=np.array(data2)
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=1,test_size=0.3)
tree=DecisionTreeClassifier()
tree.fit(x_train,y_train)
tree_y_pre=tree.predict(x_test)
##print(classification_report(y_test,tree_y_pre))


