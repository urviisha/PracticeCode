# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 23:15:28 2026

@author: URVISHA
"""

a = [10, 20, 30, 40, 50]
x = 40

for i in range(len(a)):
    if a[i] == x:
        print("Found")
        break
else:
    print("Not Found")