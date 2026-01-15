# ============================================================
# EXERCISE 10-1: LEARNING PYTHON
# ============================================================
print("="*60)
print("EXERCISE 10-1: LEARNING PYTHON")
print("="*60)

# Create the file with learning notes
with open('learning_python.txt', 'w', encoding='utf-8') as file:
    file.write("In Python I learned about variables and data types.\n")
    file.write("Python uses indentation for code structure.\n")
    file.write("In Python it's easy to work with lists and dictionaries.\n")
    file.write("Python is an excellent language for beginners.\n")

print("\n--- Method 1: Reading entire file ---")
with open('learning_python.txt', encoding='utf-8') as file:
    contents = file.read()
    print(contents)

print("\n--- Method 2: Looping through lines ---")
with open('learning_python.txt', encoding='utf-8') as file:
    for line in file:
        print(line.rstrip())

print("\n--- Method 3: Saving to a list ---")
with open('learning_python.txt', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())