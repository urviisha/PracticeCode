# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:50:50 2026

@author: URVISHA
"""

print("1. Decimal to Binary")
print("2. Decimal to Octal")
print("3. Decimal to Hexadecimal")
print("4. Binary to Decimal")
print("5. Octal to Decimal")
print("6. Hexadecimal to Decimal")

choice = int(input("Enter your choice: "))

if choice == 1:
    num = int(input("Enter Decimal Number: "))
    print("Binary =", bin(num))

elif choice == 2:
    num = int(input("Enter Decimal Number: "))
    print("Octal =", oct(num))

elif choice == 3:
    num = int(input("Enter Decimal Number: "))
    print("Hexadecimal =", hex(num))

elif choice == 4:
    num = input("Enter Binary Number: ")
    print("Decimal =", int(num, 2))

elif choice == 5:
    num = input("Enter Octal Number: ")
    print("Decimal =", int(num, 8))

elif choice == 6:
    num = input("Enter Hexadecimal Number: ")
    print("Decimal =", int(num, 16))

else:
    print("Invalid Choice")
    
    
#output:
    
"""  
Enter your choice: 1
Enter Decimal Number: 20

Binary = 0b10100 """