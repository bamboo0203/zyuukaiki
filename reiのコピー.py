#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 19:44:40 2020

@author: takeuchiyuuki
"""
import numpy as np


x1 = np.array([[0.001, 0.02, 0.1]])#x1

x2 = np.array([[10],[5],[3]])#x2

x12 = x1 * x2#x1x2

r = np.linalg.det(x12)
print(r)

r4 = np.linalg.inv(r)
print(r4)

y = np.array([[6.627245,16.18966,17.36282],[15.45642,43.64852,47.2504],[25.65352,74.88353,81.54477]])
print(y)

w = y * r
print(w)