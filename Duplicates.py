dup = []
#Taking input using the sentinal method
print("Enter the numbers you want to add in the list (or just Enter done to exit)")

while True:
    num = input("\nEnter the values: ")
    if num.lower() == "done":
        break
    try:
        number = int(num)
        dup.append(number)
       
    except ValueError:
        print("Entered value is not a number.")


og = set(dup)
for i in og:
    print(i)

