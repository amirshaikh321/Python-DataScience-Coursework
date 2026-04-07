print("Billing System".center(40))
print('--'*20)
breakfast_menu = {
        "Kande Pohe": 25,
        "Misal Pav": 60,
        "Sabudana Khichdi": 40,
        "Thalipeeth": 50,
        "Kanda Batata Poha": 30,
        "Shira": 35,
        "Vada Pav": 15,
        "Dadape Pohe": 30}
items_list =[]
price_list = []
order_items = {}
items = []
while True: 
    i= 1
    for dish, price in breakfast_menu.items():
        items_list.append(dish)
        price_list.append(price)
        print(f"{i}. {dish}: ₹{price}")
        i+=1
    print()
    ch = eval(input("Select Dish: "))

    if ch == 1:
        quantity = int(input("Quantity: "))
        order_items[items_list[ch-1]] = {}
        order_items[items_list[ch-1]]['Quantity'] = quantity
        order_items[items_list[ch-1]]['Rate'] = price_list[ch-1]
        order_items[items_list[ch-1]]['Price'] = price_list[ch-1]*quantity
        a = input("Something else (yes/no): ")
        print()
        if a.lower() != 'yes':
            break
    elif ch == 2:
        quantity = int(input("Quantity: "))
        order_items[items_list[ch-1]] = {}
        order_items[items_list[ch-1]]['Quantity'] = quantity
        order_items[items_list[ch-1]]['Rate'] = price_list[ch-1]
        order_items[items_list[ch-1]]['Price'] = price_list[ch-1]*quantity
        a = input("Something else (yes/no): ")
        print()
        if a.lower() != 'yes':
            break
    elif ch == 3:
        quantity = int(input("Quantity: "))
        order_items[items_list[ch-1]] = {}
        order_items[items_list[ch-1]]['Quantity'] = quantity
        order_items[items_list[ch-1]]['Rate'] = price_list[ch-1]
        order_items[items_list[ch-1]]['Price'] = price_list[ch-1]*quantity
        a = input("Something else (yes/no): ")
        print()
        if a.lower() != 'yes':
            break
    elif ch == 4:
        quantity = int(input("Quantity: "))
        order_items[items_list[ch-1]] = {}
        order_items[items_list[ch-1]]['Quantity'] = quantity
        order_items[items_list[ch-1]]['Rate'] = price_list[ch-1]
        order_items[items_list[ch-1]]['Price'] = price_list[ch-1]*quantity
        a = input("Something else (yes/no): ")
        print()
        if a.lower() != 'yes':
            break
    elif ch == 5:
        quantity = int(input("Quantity: "))
        order_items[items_list[ch-1]] = {}
        order_items[items_list[ch-1]]['Quantity'] = quantity
        order_items[items_list[ch-1]]['Rate'] = price_list[ch-1]
        order_items[items_list[ch-1]]['Price'] = price_list[ch-1]*quantity
        a = input("Something else (yes/no): ")
        print()
        if a.lower() != 'yes':
            break
    elif ch == 6:
        quantity = int(input("Quantity: "))
        order_items[items_list[ch-1]] = {}
        order_items[items_list[ch-1]]['Quantity'] = quantity
        order_items[items_list[ch-1]]['Rate'] = price_list[ch-1]
        order_items[items_list[ch-1]]['Price'] = price_list[ch-1]*quantity
        a = input("Something else (yes/no): ")
        print()
        if a.lower() != 'yes':
            break
    elif ch == 7:
        quantity = int(input("Quantity: "))
        order_items[items_list[ch-1]] = {}
        order_items[items_list[ch-1]]['Quantity'] = quantity
        order_items[items_list[ch-1]]['Rate'] = price_list[ch-1]
        order_items[items_list[ch-1]]['Price'] = price_list[ch-1]*quantity
        a = input("Something else (yes/no): ")
        print()
        if a.lower() != 'yes':
            break
    elif ch == 8:
        quantity = int(input("Quantity: "))
        order_items[items_list[ch-1]] = {}
        order_items[items_list[ch-1]]['Quantity'] = quantity
        order_items[items_list[ch-1]]['Rate'] = price_list[ch-1]
        order_items[items_list[ch-1]]['Price'] = price_list[ch-1]*quantity
        a = input("Something else (yes/no): ")
        print()
        if a.lower() != 'yes':
            break
        else:
            print("Invalid input...")
    else :
        print("Invalid input...")

print("Total Bill".center(53,'*'))
total =0
for dish, details in order_items.items():
    print(f"{dish:^53}")
    print('-'*53)
    
    for key, val in details.items(): 
        print(f"|{key:^25}|{val:^25}|")
        print("-"*53)
        if key == 'Price':
            total += val
    print()
print(f"Total amount to Pay : {total}")
print()
    