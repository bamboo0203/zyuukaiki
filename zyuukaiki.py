#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:35:28 2020

@author: takeuchiyuuki
"""

import pandas as pd
import numpy as np
 
kaiki = pd.read_csv('py.csv', sep=',' ,index_col= 0)
kaiki.head

from sklearn import linear_model
clf = linear_model.LinearRegression()

 
# 説明変数に "quality (品質スコア以外すべて)" を利用
#zyukaiki= kaiki.drop("0.001","0.02","0.1","10.0","5.0","3.0","1.0","0.5","0.1")
#X = zyukaiki.as_matrix()
 
# 目的変数に "quality (品質スコア)" を利用
#Y = kaiki['6.627245',"16.18966","17.36282","15.45642","43.64852","47.2504","25.65352","74.88353","81.54477","45.71304","137.2792","149.8247","38.12101","143.5363","155.1293","9.926292","112.8372","128.0852"].as_matrix()
 
# 予測モデルを作成
X = ((0.001,10),(0.02,10),(0.1,10),(0.001,5),(0.02,5),(0.1,5),(0.001,3),(0.02,3),(0.1,3),(0.001,1),(0.02,1),(0.1,1),(0.001,0.5),(0.02,0.5),(0.1,0.5),(0.001,0.1),(0.02,0.1),(0.1,0.1))
Y = [6.627245,16.18966,17.36282,15.45642,43.64852,47.2504,25.65352,74.88353,81.54477,45.71304,137.2792,149.8247,38.12101,143.5363,155.1293,9.926292,112.8372,128.0852]
print(len(X))
print(len(Y))
clf.fit(X, Y)
print(kaiki)
# 偏回帰係数
#print(pd.DataFrame({"Name":kaiki.columns.values,
                   # "Coefficients":clf.coef_}).sort_values(by='Coefficients') )
 
# 切片 (誤差)
print(clf.intercept_)
