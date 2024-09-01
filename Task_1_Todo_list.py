def ToDo_list():
    list = []
    print("!!! Welcome to the to do list !!!")
    Num_of_list = int(input("Enter the number of list you want to add : "))
    for x in range(1,Num_of_list+1):
        print("list",x,":",end = '')
        list_value = input("")
        list.append(list_value)
    print(list)
    add = " "
    update = 0
    while True :
        print(" 1. Add /t 2. Delete /t 3. Update /t 4.Delete all /t 5. View /t 6. exit")
        value = int(input())
        if(value == 1):
            add = input("1. Add : ")
            list.append(add)
            print(f"Task {add} has succesfully added")      
        elif(value == 2):
            add = int(input("Enter the number of element to delete: "))
            list.pop(add-1)
            print(f"Task {add} has succesfully Deleted")
        
        elif(value == 3):
            add = int(input("Enter the number of element to update : "))
            update = input("Enter the element : ")
            list.insert(add-1,update)
            list.pop(add)
            print(f"Task {add} has succesfully updated")
        
        elif(value == 4):
            for x in range(0,len(list)):
                list.pop(0)
            print("all Task in the list has successfully deleted")

        elif(value == 5):
            print(list)

        elif(value == 6):
            break
        else:
            print("Please enter correct option")  
ToDo_list()

