var =[]

while True:
    user_input = input("Enter the values or done to exit : ")
    if user_input.lower() == 'done':
        break
    try:
        numbers = int(user_input)
        var.append(numbers)
    except ValueError:
        print("Incorrect value has been entered ")


if var:

    sum_of_list = sum(var)
    average_of_list = sum_of_list/len(var)
    mini = min(var)
    maxi = max(var)
    print(f"Sum: {sum_of_list}, average: {average_of_list}, minimum : {mini} and maximum : {maxi}")