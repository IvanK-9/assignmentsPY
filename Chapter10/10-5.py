print("\n\n" + "="*60)
print("EXERCISE 10-5: GUEST BOOK")
print("="*60)
print("Enter 'quit' to finish\n")

with open('guest_book.txt', 'w', encoding='utf-8') as file:
    while True:
        name = input("Enter your name: ")
        
        if name.lower() == 'quit':
            break
        
        file.write(f"{name}\n")
        print(f"Thank you, {name}! You've been added to the guest book.\n")

print("All guests have been saved to guest_book.txt")