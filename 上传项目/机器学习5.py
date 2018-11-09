import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

data = pd.read_excel('C:\\Users\\Asus\\Desktop\\traintest.xlsx')

data = data.dropna(how='any')
data = data.iloc[:, [1, 2, 5]]
data.loc[(data.age_range == 7) | (data.age_range == 8), 'age_range'] = 7

ohe = OneHotEncoder(n_values=[8, 3])
data1 = ohe.fit_transform(data.iloc[:, :-1]).toarray()

def convert_log(row):
    log = row[-1]
    items = log.split('#')
    click, card, purchase, favour = 0, 0, 0, 0  # click点击数，card加入购物车数，purchase购买数，favar收藏夹数
    for t in items:
        click += 1
        ts = t.split(':')[4]
        if ts == '1':
            card += 1
        if ts == '2':
            purchase += 1
        if ts == '3':
            favour += 1
    return [float(click), float(round(purchase / click, 3)), float(card), float(favour)]


data2 = np.apply_along_axis(convert_log, 1, data)

data = np.hstack([data1, data2])
print(data[0])

