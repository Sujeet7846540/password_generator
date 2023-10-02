#Password Generator Project
import random
import pyperclip
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")




#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

k="G"

while k=="G":
    S=input("Enter G To 'Generate' else Enter Q to 'Quit': ")
    
    if S=="Q" or S== "q":
        break

    if S=="G" or S=="g":
        nr_letters= int(input("How many letters would you like in your password?\n")) 
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        a=random.choice(letters)*nr_letters
        b=random.choice(symbols)*nr_symbols
        c=random.choice(numbers)*nr_numbers
        # print(a)
        # print(b)
        # print(c)
        s=[]

        for i in range(1,nr_letters+1):
            a=random.choice(letters)
            s.append(a)

        # print(s)

        for i in range(1,nr_symbols+1):
            a=random.choice(symbols)
            s.append(a)


        for i in range(1,nr_numbers+1):
            a=random.choice(numbers)
            s.append(a)

        # print(s)
        p=""
        for i in s:
            a=random.choice(s)
            p+=a

        print("Here is Your Password: ",p)
        pyperclip.copy(p)
        print("Password Copied to Clipboard.")
    
    else:
        print("Invalid Input! (-_-)")
        


        

    