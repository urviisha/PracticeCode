# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 23:18:39 2026

@author: URVISHA
"""

a = [10000, 20000, 30000, 50000, 70000]
x = 20000

l, h = 0, len(a)-1
ans = -1

while l <= h:
    m = (l+h)//2
    if a[m] >= x:
        ans = m
        h = m-1
    else:
        l = m+1

print(ans)