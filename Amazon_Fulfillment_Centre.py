# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 01:16:00 2026

@author: URVISHA
"""

belt = ["Book", "Pen", "Bag", "Box", "Toy", "Bottle", "Mouse", "Phone"]


slot = int(input("Enter slot (0-7): "))
print("Product:", belt[slot])


item = input("Enter product to find: ")

if item in belt:
    print("Found")
else:
    print("Not Found")


slot = int(input("Enter slot to update: "))
new = input("Enter new product: ")
belt[slot] = new

print("Updated Belt:", belt)


if len(belt) == 8:
    print("Belt is Full")
else:
    print("Belt is Not Full")
        
        
"""
output:

Enter slot: 2
Product: Bag
Enter product to find: Toy
Found
Enter slot to update: 3
Enter new product: Laptop
Updated Belt:
['Book', 'Pen', 'Bag', 'Laptop', 'Toy', 'Bottle', 'Mouse', 'Phone']
Belt is Full

"""