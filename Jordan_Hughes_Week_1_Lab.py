n = 0

print('hello!')

name = input("What is your name? ")
birthday = input("What month were you born in? ")

print("Hello, " + name)

if birthday.lower() == "august":
    print("Happy birthday!")

print(f'There are {len(name)} letters in your name.')

numOfClasses = int(input("How many courses are you taking this semester? "))

while n < numOfClasses:
    n = n + 1
    input (f"What is the name of course {(n)}? ")