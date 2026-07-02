# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 23:30:56 2026

@author: URVISHA
"""



name = input("Enter Customer Name: ")
unit = int(input("Enter Units Consumed: "))

if unit <= 100:
    bill = unit * 5

elif unit <= 200:
    bill = (100 * 5) + (unit - 100) * 7

elif unit <= 300:
    bill = (100 * 5) + (100 * 7) + (unit - 200) * 10

else:
    bill = (100 * 5) + (100 * 7) + (100 * 10) + (unit - 300) * 12


print("Customer Name :", name)
print("Units Consumed:", unit)
print("Total Bill    : Rs.", bill)

"""

output:
    
Enter Customer Name: Urvi
Enter Units Consumed: 250

Customer Name : Urvi
Units Consumed: 250
Total Bill    : Rs. 1700

"""