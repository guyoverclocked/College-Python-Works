# Use case 1 - Student Registration System

# 1. Create a dictionary by getting input from the user:
students = {}
for i in range(5):
    name = input("Enter student's name: ")
    grade = input("Enter student's grade: ")
    students[name] = grade

# 2. Iterating over keys, values, and both keys and values:
print()
for name in students.keys():
    print(name)

print()
for grade in students.values():
    print(grade)

print()
for name, grade in students.items():
    print(f"Student: {name}, grade: {grade}")

# 3. Iterating with a condition:
print()
for name, grade in students.items():
    if grade == "A":
        print(name)

# 4. Accessing the dictionary elements using keys(), values(), and items() methods:
print()
for name in students.keys():
    print(name)

print()
for grade in students.values():
    print(grade)

print()
for name, grade in students.items():
    print(f"Student: {name}, grade: {grade}")

# 5. Updating the dictionary using update() and setdefault():
print()
students.update({"Bob": "B+"})
print(students["Bob"])

if "Frank" in students.keys():
    pass
else:
    students.setdefault("Frank", "A-")

# 6. Check whether the key or value exists in a dictionary:
print()
for name in students.keys():
    if name == "Alice":
        print("Alice is present!")
        break
    else:
        print("No Alice!")

print()
for grade in students.values():
    if grade == "C":
        print("Grade C is available in the dict.")
        break
    else:
        print("No C")
        break
    
# 7. Usage of fromkeys() method:
print()
hello = students.fromkeys(["Alice", "Bob", "Charlie", "Diana", "Eve"], "Not Assigned")
hello["Alice"] = "A"
hello["Bob"] = "B+"
print(hello)

# 8. Delete operations in a dictionary:
del students["Diana"]
eve_grade = students.pop("Eve")
print(f"Eve's grade: {eve_grade}")
students.popitem()
students.clear()

# Use case 2 - Student Course Registration System
# 1. Create a nested dictionary with the following structure:
students = {
    "Alice" : {
        "Math": "A",
        "English": "B+"
    },

    "Bob": {
        "Math": "B",
        "Science": "A"
    }
}

# Bob's grade in science:
stud = students["Bob"]["Science"]
print(f"Bob's grade in science is: {stud}")

students["Charlie"] = {
    "History": "B"
}

for name in students.items():
    for course, grade in name[1].items():
        print(f"{name[0]}, has registered in {course} course and has scored {grade} grade.")