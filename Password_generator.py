#Password Generator Project

#Import Libraries
import random

#Global Variables
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Headers
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []  #start off with an empty list

#create a for loop to get a list of requested letters, symbols, and numbers
for num_letter in range(
        1, nr_letters + 1
):  #get the rand set of letters from first letter to end-user's required amount of letters + 1
    rand_char = random.choice(letters)
    password += rand_char  # aka password = password + num_letter
# print(password)

for num_sym in range(
        1, nr_symbols + 1
):  #get the rand set of symbols from first symbol to end-user's required amount of symbols + 1
    rand_sym = random.choice(symbols)
    password += rand_sym
# print(password)

for num in range(
        1, nr_numbers + 1
):  #get the rand set of numbers from first number to end-user's required amount of numbers + 1
    password = random.choice(numbers)
    # aka
    # rand_num = random.choice(numbers)
    # password = password + rand_num
print(
    password
)  #print to see what the end result is for the ordered generated password

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(
    password
)  # scramble the generated password and output it in a random format
print(password)  #print to see what it looks like

str_password = ''  # start the string of word with nothing

#create a for loop to take each character in the list and string them together as a word
for char in password:  # aka password(char)
    str_password = str_password + char
print(str_password)  #print to see the result
