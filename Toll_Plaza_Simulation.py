# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 01:28:45 2026

@author: URVISHA
"""

queue = []
size = 5

while True:
    print("\n1. Add Vehicle")
    print("2. Remove Vehicle")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        if len(queue) == size:
            print("Queue Full")
        else:
            vehicle = input("Enter Vehicle Number: ")
            queue.append(vehicle)

    elif ch == 2:
        if len(queue) == 0:
            print("Queue Empty")
        else:
            print("Removed:", queue.pop(0))

    elif ch == 3:
        print(queue)

    elif ch == 4:
        break

    else:
        print("Invalid Choice")
        
        
        
"""
# output:
    
    
    
Enter Vehicle: Car
Enter Vehicle: Bus
Enter Vehicle: Bike
Enter Vehicle: Van
Enter Vehicle: Taxi

Queue:
['Car', 'Bus', 'Bike', 'Van', 'Taxi']

Enter New Vehicle: Truck

Updated Queue:
['Bus', 'Bike', 'Van', 'Taxi', 'Truck']

"""