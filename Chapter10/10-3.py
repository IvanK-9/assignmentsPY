print("\n\n" + "="*60)
print("EXERCISE 10-3: SIMPLER CODE")
print("="*60 + "\n")

with open('learning_python.txt', encoding='utf-8') as file:
    for line in file.read().splitlines():
        print(line)
