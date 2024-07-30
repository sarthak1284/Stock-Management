# Importing for a regular expression
import re


# Defining a function to purchase Laptops from the manufactures that accepts the following 2D list as the parameter
def purchase_laptops(listed_items):
    # Assigning the parameter list to the new variable and declaring an empty dictionary
    list_data = listed_items
    dictionary_data = {}
    amount_dictionary = {}
    print("For Bill Generation you will have to enter your details first: ")
    print()
    
    # Use of a loop in order for the user to input their valid names
    while True:
        # Asking the user to input their names and checking through the regular expression if correct values are entered
        firstname = input("Please enter your first name: ")
        lastname = input("Please enter your last name: ")
        print()
        if not (re.match("^[a-zA-Z]*$",firstname) and re.match("^[a-zA-Z]*$", lastname)):
            print("Only alphabets are allowed while naming.")
        else:
            fullname = firstname + " " + lastname
            print("Greetings " + fullname)
            break

    # Use of a loop in order for the user to input their valid phone
    while True:
        # Asking the user to input their names and checking through the regular expression if correct values are entered
        phone = input("Please enter your phone number: ")
        if not(re.match("[0-9]",phone)):
            print("Only integers are allowed.")
        else:
            break

    # Use of while loop to iterate through the laptop transaction till the user wants to exit
    laptop_purchasing = True
    laptop_is_added = False
    while laptop_purchasing:
        print()
        # Asking the user to input the laptop ID they wish to purchase and examining for correct values entered
        laptopID = int(input("Enter the ID of the laptop you wish to buy: "))
        # Iterating the code entered with every element's first index stored on the list
        for i in range(len(list_data)):
            if str(laptopID) == list_data[i][0]:
                laptop_is_added = True
                break
            
        
        if laptop_is_added:
            # Use of while loop in order to continously ask the user until correct values are entered
            while True:
                # Exception Handling to handle for any other values than integer
                try:
                    # Asking the user to input the number of laptops they'd want to purchase
                    quantity = int(input("Enter the number of laptops you wish to buy: "))
                    # Insertion of correct valyes for the examination process
                    if quantity > 0:
                        break
                    elif quantity < 0:
                        print("Please enter a positive integer value.")
                        print()
                    elif quantity == 0:
                        print("Please enter a positive integer value.")
                        print()
                except:
                    print("Please enter an integer value.")
                    print()

            # Iterating through the lists to check if the inserted laptop quantity has the actual number of stocks in the store
            for i in range(len(list_data)):
                # Adding the quantity of laptop as the value and Laptop ID as its key on the dictionary initialized
                if str(laptopID) == list_data[i][0]:
                    dictionary_data[laptopID] = quantity
                    break
                
            # Error message when an invalid Laptop ID has been entered
            else:
                print()
                print("Sorry, the laptop with the ID " + str(laptopID) + " is not available on our store.  ")

        # Use of while loop in order to iterate through the user interface till a correct value is entered
        while True:
            print()
            # Asking the user if they'd wish to purchase any more Laptops
            supplement = input("Do you wish to buy any more laptops (Y/N)? ").upper()
            # if yes loop through the top 
            if (supplement == "Y"):
                laptop_purchasing = True
                break
            # if not, break the loop
            elif (supplement == "N"):
                laptop_purchasing = False
                break
            # if an invalid value is provided loop through it again
            else:
                print("Invalid input, try again.")
                continue

    # Calculation of the price to be paid and the grand total
    print()
    amount = 0
    # Iterating through the keys of the dictionary to calculate the total amount by multiplying the value with its unit price
    for keys in dictionary_data.keys():
        for i in range(len(list_data)):
            if str(keys) == list_data[i][0]:
                price = int(list_data[i][3])
                quantity = int(dictionary_data[keys])
                amount_dictionary[keys] = price * quantity 
                amount += amount_dictionary[keys] 
                print("The cost for the laptop with ID " + list_data[i][0] + " and name " + list_data[i][1] + " is: " + "$" + str(price))

    # Printing the output as the total amount or sum of all laptops as the grand total
    print("Hence, the total amount for all the laptops is: " + "$" + str(amount))
    print()

    # Telling the user 13% VAT will be added to their total.
    print("13% VAT will be added to your Total amount.")

    # Calculation of the total amount after VAT      
    total_amount = int(amount + (13 * amount / 100))
    print("Thus, the calculated amount after VAT is: " + "$" + str(total_amount))

    # Creation of purchase notice invoice for the purchased laptops
    # Extraction of date and time to add on the txt file 
    import datetime
    date = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day)
    time = str(datetime.datetime.now().hour) + "-" + str(datetime.datetime.now().minute) + "-" + str(
        datetime.datetime.now().second)
    date_time = str(date) + " " + str(time)
    # File writing with the user's name, date and time and transaction made and other details
    file_write = open(fullname + " " + date_time + " (purchased).txt", "w")
    file_write.write(
        "\t\t\t --------------------------------------------------------------------------- INVOICE ---------------------------------------------------------------------------")
    file_write.write("\n")
    file_write.write("\n")
    file_write.write(
        "\t\t\t --------------------------------------------------------------------------  Purchase --------------------------------------------------------------------------")
    file_write.write("\n")
    file_write.write("\n")
    file_write.write("\t\t\t\t\t\t" + str("Name of the Customer: " + str(fullname) + "\t\t\t" + "Phone: " + str(phone) + "\t\t\t" + "Date: " + str(
        date) + "\t\t\t" + "Time: " + str(time)))
    file_write.write("\n")
    file_write.write("\n")
    file_write.write(
        "\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------")
    file_write.write("\n")
    file_write.write("\n")
    file_write.write("\t\t\t\t\t\t\t\t\t laptop_ID \t\t Name_of_the_laptop \t\t Quantity \t\t Unit_Price \t\t Amount")
    file_write.write("\n")
    file_write.write("\n")

    # Iterating through the keys of the dictionary to find out the total amount to be paid 
    for keys in dictionary_data.keys():
        for i in range(len(list_data)):
            if str(keys) == list_data[i][0]:
                file_write.write(str("\t\t\t\t\t\t\t\t\t\t" + str(keys) + "\t\t " + str(list_data[i][1]) + "\t\t\t\t" + str(dictionary_data[keys]) + "\t\t   " +
                                     "$" + str(list_data[i][3]) + "\t\t\t " + "$" + str(amount_dictionary[keys])))
                file_write.write("\n")
                file_write.write("\n")

    # Writing of the total amount, VAT and the grand total to be paid with a final notice
    file_write.write(
        "\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------")
    file_write.write("\n")
    file_write.write("\n")
    file_write.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t     Total_Amount: " + "$" + str(amount))
    file_write.write("\n")
    file_write.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t     VAT: " + " 13%")
    file_write.write("\n")
    file_write.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t     Grand_Total: " + "$" + str(total_amount))
    file_write.write("\n")
    file_write.write("\n")
    file_write.write(
        "\t\t\t --------------------------------------------------------------------------- THANKYOU --------------------------------------------------------------------------")
    file_write.close()

    # It returns the dictionary that stored the details of laptop ID and quantity purchased
    return dictionary_data
