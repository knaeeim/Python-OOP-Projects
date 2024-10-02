from food_item import FoodItem
from menu import Menu
from user import Customer, Admin, Employee
from restaurent import Restaurent
from orders import Order


mamar_restaurent = Restaurent("Mamar Restaurent")

def customer_menu(): 

    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your address : ")

    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True: 
        print(f"Welcome to {customer.name} !!")

        print("1. View Menu")
        print("2. Add item to Cart")
        print("3. View Cart")
        print("4. Paybill")
        print("5. Exit")

        choice = int(input("Enter Your Change : "))
        if choice == 1 :
            customer.view_menu(mamar_restaurent)
        elif choice == 2:
            item_name = input("Enter the item Name : ")
            item_quantity = int(input("Enter the item Quantity : "))
            customer.add_to_cart(mamar_restaurent, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4: 
            customer.paybill()
        elif choice == 5:
            break;  
        else:
            print("Invalid Input !!!")


def admin_menu(): 

    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your address : ")

    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True: 
        print(f"Welcome to {admin.name} !!")

        print("1. Add new item")
        print("2. Add new Employee")
        print("3. View Employee")
        print("4. View items")
        print("5. Delete Item")
        print("6. Exit")

        choice = int(input("Enter Your Change : "))
        if choice == 1 :
            item_name = input("Enter your item Name : ")
            item_price = int(input("Enter the item Price : "))
            item_quantity = int(input("Enter the item Quantity : "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_restaurent, item)
        elif choice == 2:
            name = input("Enter the employee Name : ")
            email = input("Enter your Email Address : ")
            phone = input("Enter your Phone Number : ")
            address = input("Enter your address : ")
            age = int(input("Enter your age : "))
            designation = input("Enter the Designation : ")
            salary = int(input("Enter your Salary : "))
            emp = Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(mamar_restaurent, emp)
        elif choice == 3:
            admin.view_employee(mamar_restaurent)
        elif choice == 4: 
            admin.view_menu(mamar_restaurent)
        elif choice == 5:
            item = input("Enter the item name that you want to delete : ")
            admin.remove_item(mamar_restaurent, item)
        elif choice == 6:
            break  
        else:
            print("Invalid Input !!!")

while True:

    print("Welcome To foodies World")

    print("1. Customer ")
    print("2. Admin ")
    print("3. Exit ")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break;
    else:
        print("Input is Invalid !! ")