print("\n=== 5-6. Stages of Life ===")

# Test with different ages
test_ages = [1, 3, 10, 15, 30, 70]

for age in test_ages:
    print(f"\nAge: {age}")
    
    if age < 2:
        print("This person is a baby.")
    elif age < 4:  # age >= 2 is implied
        print("This person is a toddler.")
    elif age < 13:  # age >= 4 is implied
        print("This person is a kid.")
    elif age < 20:  # age >= 13 is implied
        print("This person is a teenager.")
    elif age < 65:  # age >= 20 is implied
        print("This person is an adult.")
    else:  # age >= 65
        print("This person is an elder.")