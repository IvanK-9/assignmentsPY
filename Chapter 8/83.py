def make_shirt(size, message):
    """Prints a summary message about the t-shirt."""
    print(f"A {size}-sized t-shirt with the message: '{message}'.")

# 1. Positional arguments
make_shirt('M', 'Hello, World!')

# 2. Keyword arguments
make_shirt(size='L', message='Python is awesome!')