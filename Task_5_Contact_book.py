def Contact_Book():
    Contact = {}
    while True:
        print("Enter 1 : To save new Contact \nEnter 2 : TO update any Contact \nEnter 3 : To Delete Contact \nEnter 4 : To view the Contact \nEnter 5. Exit")
        button = input("Enter : ")
        if button == '1':
            print('Enter \t 1. Name \t 2. Number \t 3. Email \t 4. Address')
            name = input("Name : ")
            Contact["Name"] = name
            number = input("Number : ")
            Contact["Number"] = number
            email = input("Email : ")
            Contact["Email"] = email
            address = input("Address : ")
            Contact["Address"] = address
        elif button == '2':
            while True:
                print('Enter to update  \t 1. Name \t 2. Number \t 3. Email \t 4. Address \t 5. Exit')
                update = input("Enter : ")
                if update == '1':
                    update_name = input("Name : ")
                    Contact["Name"] = update_name
                elif update == '2':
                    update_number = input("Number : ")
                    Contact["Number"] = update_number
                elif update == '3':
                    update_email = input("Email : ")
                    Contact["Email"] = update_email
                elif update == '4':
                    update_address = input("Address : ")
                    Contact["Address"] = update_address
                elif update == '5':
                    break
                else:
                    print("Please enter a valid input")
        elif button == '3':
            Contact.clear()
        elif button == '4':
            print(Contact)
        elif button == '5':
            break
        else:
            print("Enter a valid output")

Contact_Book()