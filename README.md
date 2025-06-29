# Python Project : Super Cashier App

### A. Background

Andi is the owner of a large supermarket in one of Indonesia’s major cities. To improve his business operations, he plans to implement a **self-service cashier system** that allows customers to directly input purchased items, their quantity, and price  without needing a traditional cashier.

### B. Tools

Languages :
* Python

Libraries :
* Tabulate

### C. Objective

Learning objective :
* Create simple app using python for a real-world business use case
* Demonstrate the use of **Object-Oriented Programming** in Python
* Apply PEP8 principles to write clean Python program

Program objective :
* Simulate cashier system that enables item input, order summary, and total calculation
* Provide basic features such as updating and deleting items, applying coupon, and calculating discount

### D. Program Description
1. 'transaction.py' module contains Transaction class to handle the transaction process, with methods to add item to shopping cart, update item (name, quantity, and price), remove item (specific or all item), check cart contents, apply discount coupon, and calculate the total price of items in the cart.
2. 'cashier_app.py' module displays simple cashier app menu that allows user add their transaction by input action.

<img src="img/Flowchart.png" width="300"/>

### E. Guide to Replicate
1. Download zip or clone this repository to local
2. Run cashier_app.py on terminal

### F. Test Cases and Result
1. Adding item to cart
<img src="img/1. Add item 1.png" width="500"/>
<img src="img/1. Add item 2.png" width="500"/>
<img src="img/1. Add item invalid.png" width="500"/>

2. Updating cart item name
<img src="img/2. Update item name.png" width="500"/>

3. Updating cart item quantity
<img src="img/3. Update item quantity.png" width="500"/>

4. Updating cart item price
<img src="img/4. Update item price.png" width="500"/>

5. Remove item from cart
<img src="img/5. Remove item.png" width="500"/>

6. Reset cart item
<img src="img/6. Reset item.png" width="500"/>

7. Check shopping cart
<img src="img/7. Check shopping cart.png" width="500"/>

8. Checkout
<img src="img/8. Checkout.png" width="500"/>

### G. Conclusion
This project demonstrated how Python and OOP can help solving real world task. To further improve the application and simulate better app that fits user's need, there are several improvement I would like to do if I had the time and resources. Firstly, I would like to be able to save the transactions to database (e.g. SQLite/PostgreSQL) and be able to get report of daily transaction as a summary. I would also like to build a web framework using Django/Flask to improve the interface.