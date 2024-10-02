## String Formatting
name = "Nambi Rajan"
age = 18
info = f"I am {name} and I'm {age} years old."
print(info)

formatted_string = "I am {} and I'm {} years old, and I am formatted.".format(name, age)
print(formatted_string)
## Finding Substrings
greeting = "Hello World!"
if "World" in greeting:
    print(greeting)

greetings = "I love Python programming!"
print(f'Index of Python is: {greeting.find("Python")}')

## Splitting and Joining Strings
greeting_list = []
for greet in greeting:
    greeting_list.append(greet)
print(greeting_list)

rejoin_greeting = ""
for again_greeting in greeting_list:
    rejoin_greeting += again_greeting
print(f"Rejoined greeting from string: {rejoin_greeting}")

## INteractive Input
first_name = input("What is your first name: ")
last_name = input("What is your last name: ")
print(f"Welcome, {first_name} {last_name}!")

