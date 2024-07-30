import laptop_read
import laptop_sale
import laptop_purchase
import overwrite_list
from datetime import datetime
print("\n")
print("\n")
print(" \t\t\t\t\t\t\t\tSarthak Electronics ")
print("\n")
print("\t\t\t\t\t\t  Kamalpokhari, Kathmandu | Phone no: 9807103844")
print("\n")

print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t Welcome to thr system Admin! I hope you have a good day ahead")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("\n")

loop = True
while loop == True:
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t    Given below are some of the options for you to carryout the nedded operations in the system")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t\t\t\tPress 1 to view all the laptops available.")
    print("\t\t\t\t\t\t\tPress 2 to sale the laptop to customer.")
    print("\t\t\t\t\t\t\tPress 3 to purchase from Manufacture.")
    print("\t\t\t\t\t\t\tPress 4 to Exit from the system.")
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    user_input = int(input("\t\t\t\t\t\t\tEnter the option to continue:"))
    print("\n")

    if user_input == 1:
        x = laptop_read.read_file()
        print("------------------------------------------------------------------------------------------------------------------------------------------------")

    elif user_input == 2:
            # Calling the function of file reading to display all the laptops available for sale
            x = laptop_read.read_file()
            # Passing of the returned list from the laptop read file on the sale laptop function 
            y = laptop_sale.sale_laptops(x)
            # Passing of the returned list and dictionary from the laptop read file and sale laptop function respectively to overwrite the txt file
            overwrite_list.over_writing_sale(x, y)
            print()
            # Ask the user to if they'd wish to progress with another transaction or not
            ask = input("Do you wish to proceed with more transactions (Y/N)? ").upper()
            print()
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            if ask == "N":
                print("Thank you for using the system, have a good day Admin!. ")
                print("\n")
                break
        
    elif user_input == 3:
            # Calling the function of file reading to display all the laptops available for purchasing
            x = laptop_read.read_file()
            # Passing of the returned list from the laptop read file on the purchase laptop function
            y = laptop_purchase.purchase_laptops(x)
            # Passing of the returned list and dictionary from the laptop read file and purchase laptop function respectively to overwrite the txt file
            overwrite_list.over_writing_purchase(x, y)
            print()
            # Ask the user to if they'd wish to progress with another transaction or not
            ask = input("Do you wish to proceed with more transactions (Y/N)? ").upper()
            print()
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            if ask == "N":
                print("Thank you for using the system, have a good day Admin!. ")
                print("\n")
                break
            
    elif user_input == 4:
            loop = False
            print("Thank you for using the system, have a good day Admin!. ")
            print("\n")
    else:
            print("\t\t\tYour option", user_input,"does not seem to match as per our requirement. Please look at the provided option.")
            print("\n")
    
    
