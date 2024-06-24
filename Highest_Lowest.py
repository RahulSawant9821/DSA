High_Low = []

size = int(input("Enter the size of the list : "))

for i in range(size):
    num = int(input("Enter the number to be added in the list : "))
    High_Low.append(num)

highest = max(High_Low)
lowest = min(High_Low)
print(f"\n So the maximum value in the List is :{highest}")
print(f"\n And the Minimum value in the List is :{lowest}")