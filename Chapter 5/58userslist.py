# list of usernames
usernames = ['admin', 'jaden', 'alice', 'bob', 'charlie']

# loop through the list and greet each user
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
