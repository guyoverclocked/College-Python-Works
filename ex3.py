## Creating a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
## Slicing a List
print(numbers[:5])
print(numbers[7:])
## Iterating Through a LIst
for number in numbers:
    print(number)
## List Comprehension:
squares = []
for number1 in numbers:
    squares.append(number1 * number1)
## Print the new List
print(squares)