#解説 1：ライブラリのインポート--------------------------------
import numpy as np #numpyという行列などを扱うライブラリを利用
import pandas as pd #pandasというデータ分析ライブラリを利用
import matplotlib.pyplot as plt #プロット用のライブラリを利用
from sklearn import linear_model, metrics, preprocessing, model_selection #機械学習用のライブラリを利用
from mlxtend.plotting import plot_decision_regions #学習結果をプロットする外部ライブラリを利用
 
#解説 2：Wineのデータセットを読み込む--------------------------------
data = pd.read_csv('tdl_tds.csv')
#x = data['land']
#y = data['day']
#z = data['month']
print(list(data[['land','sea']]))
print(1)

#x1 = data[data.index.str.contains('2015')]
#y1 = data.day

#x2 = data.sea
#y2 = data.day

#plt.scatter(x1,y1, c='red', label='group1')
#plt.scatter(x2,y2, c='blue', label='group1')
#plt.show()
#plt.colorbar()