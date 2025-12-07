# List of current users (existing accounts)
current_users = ['alice', 'bob', 'charlie', 'diana', 'eve']

# List of new users trying to register
new_users = ['frank', 'ALICE', 'george', 'BOB', 'henry']

# Create a lowercase copy of current_users for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Check each new user
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, username '{new_user}' is already taken. Please choose another one.")
    else:
        print(f"Username '{new_user}' is available!")
