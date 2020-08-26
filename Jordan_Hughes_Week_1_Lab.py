# I need to instantiate all this stuff for global use (outside for/if statements), right?
# Or am I thinking too much along the lines of Java and C#?
# Will look into soon.
n = 0
courses = []
returnSentence = ""

print('hello!')

name = input("What is your name? ")
birthday = input("What month were you born in? ")

print("Hello, " + name)

# I can already tell it's going to take a moment to remember to use a colon instead of curly brackets.
if birthday.lower() == "august":
    print("Happy birthday!")

print(f'There are {len(name)} letters in your name.')

numOfClasses = int(input("How many courses are you taking this semester? "))

while n < numOfClasses:
    n = n + 1 # Can you do something like n++ in Python, or does it have to be done like this?
    newCourse = input (f"What is the name of course {(n)}? ")
    courses.append(newCourse)

for course in courses:
    print(course)

message = input("Give me a sentence! ")

splitSentence = message.split()

for word in splitSentence:
    word = word.lower()
    # Could do everything except this one part.
    # Will likely update to properly camel case on a later day for the sake of practice.
    returnSentence = returnSentence + word # I can't remember if there's a function to do this same task, will look into later

print(returnSentence)