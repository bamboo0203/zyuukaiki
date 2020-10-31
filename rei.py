#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 19:44:40 2020

@author: takeuchiyuuki
"""
import numpy as np


np_arr1 = np.array([[0.001, 0.02, 0.1]])
print(np_arr1)

np_arr2 = np.array([[10],[5],[3],[1],[0.5],[0.1]])
print(np_arr2)

r1 = np_arr1 * np_arr2
print(r1)