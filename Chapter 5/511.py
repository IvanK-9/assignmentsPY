# List of numbers 1 through 9
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through each number and print with proper ordinal suffix
for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
