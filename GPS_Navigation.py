# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 01:29:23 2026

@author: URVISHA
"""

back = []
forward = []

back.append("Home")
back.append("Park")
back.append("Hill")

print("Current:", back[-1])

forward.append(back.pop())
print("Back:", back[-1])

back.append(forward.pop())
print("Forward:", back[-1])

"""
output:
    
Current: Hill
Back: Park
Forward: Hill

"""