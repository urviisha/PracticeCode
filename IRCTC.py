# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 23:18:07 2026

@author: URVISHA
"""

a = [1, 3, 5]
b = [2, 4, 6]

i = j = 0
c = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

while i < len(a):
    c.append(a[i])
    i += 1

while j < len(b):
    c.append(b[j])
    j += 1

print(c)