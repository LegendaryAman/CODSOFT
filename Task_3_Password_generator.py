import  random
import string
def passwordgenerator(length):
    char = string.digits + string.ascii_letters + string.punctuation
    password = ''.join(random.choice(char) for _ in range(length))
    print(password)

passwordgenerator(int(input("Length : ")))
 
