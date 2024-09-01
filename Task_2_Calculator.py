def Calculator():
        print("Entet two Number")
        num1 = int(input("Number 1 : "))
        num2 = int(input("Number 2 : "))
        while True : 
                print("1. Addition /t 2. Subtraction /t 3. Multiplication /t 4. Division /t 5. ReEnter Number /t 6. Exit ")
                input_number = int(input())
                if (input_number == 1):
                        print(f"Addition : {num1 + num2}")
                elif (input_number == 2):
                        print(f"Subtraction {num1 - num2}")
                elif (input_number == 3):
                        print(f"Multipliction : {num1 * num2}")
                elif (input_number == 4):
                        print(f"Division : {num1 / num2}")
                elif (input_number == 5):
                        num1 = int(input("Number 1 : "))
                        num2 = int(input("Number 2 : "))
                elif (input_number == 6):
                        break
                else :
                        print("Enter a valid input")
Calculator()