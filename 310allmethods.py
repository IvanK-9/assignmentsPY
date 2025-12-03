# Practical Example: Book Library
print("\n" + "-" * 60)
print("PRACTICAL EXAMPLE: LIBRARY MANAGEMENT")
print("-" * 60)

# Create book list
library = ['1984', 'Harry Potter', 'War and Peace', 'The Master and Margarita']

print(f"Initial library: {library}")

# 1. Adding books
library.append('Crime and Punishment')
library.insert(2, 'Three Comrades')
library.extend(['The Little Prince', 'Anna Karenina'])
print(f"\nAfter adding books: {library}")

# 2. Sorting
library.sort()
print(f"After A-Z sorting: {library}")

# 3. Searching
book_to_find = 'War and Peace'
if book_to_find in library:
    position = library.index(book_to_find) + 1
    print(f"\nBook '{book_to_find}' found at position {position}")

# 4. Removing
removed = library.pop(3)
print(f"\nBook '{removed}' checked out by reader")
print(f"Remaining books: {library}")

# 5. Statistics
print(f"\nLibrary Statistics:")
print(f"Total books: {len(library)}")
print(f"Earliest book (alphabetically): {min(library)}")
print(f"Latest book (alphabetically): {max(library)}")

# 6. Iterating with conditions
print(f"\nBooks starting with 'T':")
t_books = [book for book in library if book.startswith('T')]
for book in t_books:
    print(f"  - {book}")