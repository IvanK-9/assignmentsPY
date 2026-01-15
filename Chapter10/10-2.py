print("\n\n" + "="*60)
print("EXERCISE 10-2: LEARNING C")
print("="*60 + "\n")

with open('learning_python.txt', encoding='utf-8') as file:
    for line in file:
        modified_line = line.replace('Python', 'C')
        print(modified_line.rstrip())