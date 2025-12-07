# 5-2. More Conditional Tests

print("=== String Equality/Inequality Tests ===")
# Test 1: String equality - True
language = 'Python'
print("Is language == 'Python'? I predict True.")
print(language == 'Python')

# Test 2: String inequality - True
print("\nIs language != 'Java'? I predict True.")
print(language != 'Java')

# Test 3: String equality - False
print("\nIs language == 'python'? I predict False.")
print(language == 'python')  # Different case

# Test 4: String inequality - False
print("\nIs language != 'Python'? I predict False.")
print(language != 'Python')

print("\n=== Tests using lower() method ===")
# Test 5: lower() method - True
name = 'ALICE'
print("Is name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')

# Test 6: lower() method - False
print("\nIs name == 'alice'? I predict False.")
print(name == 'alice')

print("\n=== Numerical Tests ===")
# Test 7: Numerical equality - True
x = 10
print("Is x == 10? I predict True.")
print(x == 10)

# Test 8: Numerical inequality - True
print("\nIs x != 5? I predict True.")
print(x != 5)

# Test 9: Greater than - True
print("\nIs x > 5? I predict True.")
print(x > 5)

# Test 10: Less than - True
print("\nIs x < 20? I predict True.")
print(x < 20)

# Test 11: Greater than or equal - True
print("\nIs x >= 10? I predict True.")
print(x >= 10)

# Test 12: Less than or equal - True
print("\nIs x <= 10? I predict True.")
print(x <= 10)

# Test 13: Numerical equality - False
print("\nIs x == 15? I predict False.")
print(x == 15)

# Test 14: Numerical inequality - False
print("\nIs x != 10? I predict False.")
print(x != 10)

# Test 15: Greater than - False
print("\nIs x > 15? I predict False.")
print(x > 15)

# Test 16: Less than - False
print("\nIs x < 5? I predict False.")
print(x < 5)

# Test 17: Greater than or equal - False
print("\nIs x >= 15? I predict False.")
print(x >= 15)

# Test 18: Less than or equal - False
print("\nIs x <= 5? I predict False.")
print(x <= 5)

print("\n=== Tests using 'and' and 'or' keywords ===")
# Test 19: Using 'and' - True
age = 25
has_license = True
print("Is age >= 18 and has_license == True? I predict True.")
print(age >= 18 and has_license == True)

# Test 20: Using 'and' - False
score = 75
attendance = 0.8
print("\nIs score >= 80 and attendance >= 0.9? I predict False.")
print(score >= 80 and attendance >= 0.9)

# Test 21: Using 'or' - True
temperature = 35
is_weekend = False
print("\nIs temperature > 30 or is_weekend == True? I predict True.")
print(temperature > 30 or is_weekend == True)

# Test 22: Using 'or' - False
balance = 50
is_premium = False
print("\nIs balance > 100 or is_premium == True? I predict False.")
print(balance > 100 or is_premium == True)

print("\n=== Tests for item in a list ===")
# Test 23: Item in a list - True
colors = ['red', 'green', 'blue', 'yellow']
print("Is 'green' in colors? I predict True.")
print('green' in colors)

# Test 24: Item in a list - False
print("\nIs 'purple' in colors? I predict False.")
print('purple' in colors)

print("\n=== Tests for item not in a list ===")
# Test 25: Item not in a list - True
print("Is 'purple' not in colors? I predict True.")
print('purple' not in colors)

# Test 26: Item not in a list - False
print("\nIs 'red' not in colors? I predict False.")
print('red' not in colors)

# Test 27: Additional test with mixed types
mixed_list = [1, 'apple', True, 3.14]
print("\n=== Additional mixed type tests ===")
print("Is 'apple' in mixed_list? I predict True.")
print('apple' in mixed_list)

print("\nIs 2 in mixed_list? I predict False.")
print(2 in mixed_list)

print("\nIs False not in mixed_list? I predict True.")
print(False not in mixed_list)