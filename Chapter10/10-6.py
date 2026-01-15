print("\n\n" + "="*60)
print("EXERCISE 10-6: ADDITION")
print("="*60 + "\n")

try:
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")
    
    result = int(first_number) + int(second_number)
    print(f"\nSum: {first_number} + {second_number} = {result}")
    
except ValueError:
    print("\n❌ Error! Please enter numbers, not text.")