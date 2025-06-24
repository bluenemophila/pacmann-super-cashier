from tabulate import tabulate

class Transaction:
    '''
    Class Transaction
    Handles user input and calculate the total of the transaction

    Attributes
    ----------
    cart : empty list to store user's shopping item
    total : the total price for all item on cart
    coupon : conditional value to apply discount coupon

    '''


    def __init__(self):
        self.cart = []
        self.total = 0
        self.coupon = False
    
    def add_item(self, item):
        '''
        Method add_item
        Adds item input to shopping cart

        Parameters
        ----------
        item : dictionary of item_name, item_qty, and item_price passed by user input

        '''
        self.cart.append(item)
        print(f"{item["item_name"]} added to the shopping cart.")
    
    def update_item_name(self, old_name, new_name):
        '''
        Method update_item_name
        Changes item name in cart to new name from user input

        Parameters
        ----------
        old_name : string of item name on shopping cart
        new_name : string of item name passed by user input
        '''
        for item in self.cart:
            if old_name in [item.get("item_name")]:
                item["item_name"] = new_name
                print(f"{old_name} is changed to {new_name}")
                return
        print(f"{old_name} is not in shopping cart!")
    
    def update_item_qty(self, item_name, new_qty):
        '''
        Method update_item_qty
        Changes item quantity on shopping cart to new quantity passed by user input

        Parameters
        ----------
        item_name : string of item name on shopping cart
        new_qty : int of quantity passed by user input
        '''
        for item in self.cart:
            if item_name in [item.get("item_name")]:
                item["item_qty"] = new_qty
                print(f"{item_name} quantity is changed to {new_qty}")
                return
        print(f"{item_name} is not in shopping cart!")

    def update_item_price(self, item_name, new_price):
        '''
        Method update_item_price
        Changes item price on shopping cart to new price passed by user input

        Parameters
        ----------
        item_name : string of item name on shopping cart
        new_price : int of price passed by user input
        '''
        for item in self.cart:
            if item_name in [item.get("item_name")]:
                item["item_price"] = new_price
                print(f"{item_name} price is changed to {new_price}")
                return
        print(f"{item_name} is not in shopping cart!")
    
    def delete_item(self, item_name):
        '''
        Method delete_item
        Removes single item on cart

        Parameters
        ----------
        item_name : string of item name on shopping cart
        '''
        for item in self.cart:
            if item_name in [item.get("item_name")]:
                self.cart.remove(item)
                print(f"{item_name} is removed from the shopping cart.")
                return
        print(f"{item_name} is not in shopping cart!")
    
    def reset_transaction(self):
        '''
        Method reset_transaction
        Removes all item on shopping cart
        '''
        self.cart.clear()
        print("All items deleted from shopping cart!")
    
    def check_order(self):
        '''
        Method check_order
        Checks if cart is not empty with non-null valid values
        Displays order detail as table
        '''
        if not(self.cart):
            print("Shopping cart is empty. Please add items from Menu 1.")
        
        else:
            error = False

            for item in self.cart:
                values = item.values()
                if any(val in [None, "",0] for val in values):
                    error = True

            if error :
                print("Order declined. Invalid input.")

            else :
                print("Order success!")
                table = [list(item.values()) for item in self.cart]
                header = ["Item Name", "Item Qty", "Item Price"]

                print(tabulate(table, header, tablefmt="simple_outline"))  
    
    def check_coupon(self, coupon_code):
        '''
        Method check_coupon
        Checks if user passed coupon code
        Sets true condition if coupon code matched with available code

        Parameters
        ----------
        coupon_code : string of coupon code passed by user input
        '''
        if not(self.cart):
            pass
        else:
            if coupon_code.lower() == "newuser":
                self.coupon = True
                print("Successfuly applied coupon.")
            else:
                print("Invalid coupon code.")
    
    def total_price(self):
        '''
        Method total_price
        Calculates total price for all item on shopping cart
        Applies discount if conditions are satisfied
        '''
        for item in self.cart:
            self.total += item["item_qty"] * item["item_price"]
        
        if self.total > 500_000 :
            discount = 0.1
        elif self.total > 300_000:
            discount = 0.08
        elif self.total > 200_000:
            discount = 0.05
        else :
            discount = 0
        
        if self.coupon:
            self.total -= 20000
            print("You got Rp 20000 discount from new user coupon.")
        
        if discount > 0:
            print(f"You saved Rp {int(discount*self.total)} from discount.")
        
        print(f"Total price: Rp {int(self.total*(1-discount))}")
