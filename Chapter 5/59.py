# List of usernames (initially empty for testing)
usernames =  ['admin', 'jaden']

# Check if the list is empty
if not usernames:
    print("We need to find some users!")
else:
    # Loop through each user and print appropriate greeting
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
