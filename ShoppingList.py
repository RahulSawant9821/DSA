to_shop =[]

number_of_items = int(input("Enter the number of items to be purchased : "))

for _ in range(number_of_items):
    item = input("\n Enter the item name :")
    if item.lower() == "done" :
        break
    to_shop.append(item)

print("\n Your List of Items is as follows : ")
for items in to_shop :
    print(items)
