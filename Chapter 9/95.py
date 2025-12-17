def __init__(self, first_name, last_name, age, location):
    """Initializes user attributes"""
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.location = location
    self.login_attempts = 0  # New attribute for counting login attempts

def describe_user(self):
    """Prints information about the user"""
    print(f"User: {self.first_name} {self.last_name}")
    print(f"Age: {self.age}")
    print(f"Location: {self.location}")
    print(f"Login attempts: {self.login_attempts}")

def greet_user(self):
    """Greets the user"""
    print(f"Hello, {self.first_name}! Nice to see you again.")

def increment_login_attempts(self):
    """Increases the number of login attempts by 1"""
    self.login_attempts += 1

def reset_login_attempts(self):
    """Resets the number of login attempts to 0"""
    self.login_attempts = 0