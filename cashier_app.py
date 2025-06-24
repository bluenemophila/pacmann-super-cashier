from tabulate import tabulate
from transaction import Transaction

transct_123 = Transaction()

while True:
    header = ["WELCOME TO ANDIMART GROCERIES CASHIER APP"]
    table = [
        ["Choose Transaction Menu"],
        ["1. Add item to cart"],
        ["2. Change shopping cart item name"],
        ["3. Change shopping cart item quantity"],
        ["4. Change shopping cart item price"],
        ["5. Remove item from shopping cart"],
        ["6. Reset shopping cart"],
        ["7. Check shopping cart"],
        ["8. Checkout"]
    ]
    print(tabulate(table, header, tablefmt="simple_outline"))

    menu_choice = input("Menu : ")

    if menu_choice == '1':
        add = True
        while add:
            try:
                item_name = str(input("Input item name: "))
                item_qty = int(input("Input item quantity: "))
                item_price = int(input("Input item price: "))
            
            except ValueError:
                print("Item quantity and price must be integer")
                item_name = str(input("Input item name: "))
                item_qty = int(input("Input item quantity: "))
                item_price = int(input("Input item price: "))
        
            transct_123.add_item({
                "item_name" : item_name,
                "item_qty" : item_qty,
                "item_price" : item_price
            })

            add_more_item = input("Do you want to add more item? (y/n): ")
            if add_more_item.lower() == 'y':
                pass
            elif add_more_item.lower() == 'n':
                break
            else:
                print("Invalid input!")
    
    elif menu_choice == "2":
        old_name = str(input("Enter item name: "))
        new_name = str(input("Enter changed item name: "))
        transct_123.update_item_name(old_name, new_name)
    
    elif menu_choice == "3":
        item_name = str(input("Enter item name: "))
        new_qty = int(input("Enter new quantity: "))
        transct_123.update_item_qty(item_name, new_qty)

    elif menu_choice == "4":
        item_name = str(input("Enter item name: "))
        new_price = int(input("Enter new price: "))
        transct_123.update_item_price(item_name, new_price)

    elif menu_choice == "5":
        item_name = str(input("Enter item name: "))
        transct_123.delete_item(item_name)

    elif menu_choice == "6":
        transct_123.reset_transaction()

    elif menu_choice == "7":
        transct_123.check_order()

    elif menu_choice == "8":
        coupon = str(input("Do you have coupons? (y/n): "))
        if coupon.lower() == "y":
            coupon_code = str(input("Please input your coupon code: "))
            transct_123.check_coupon(coupon_code)
            break
        elif coupon.lower() == "n":
            break
        else:
            print("Invalid input.")

print("")
transct_123.check_order()
print("")
transct_123.total_price()