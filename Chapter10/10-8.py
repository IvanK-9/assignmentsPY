============================================================
# EXERCISE 10-8: CATS AND DOGS
# ============================================================
print("\n\n" + "="*60)
print("EXERCISE 10-8: CATS AND DOGS")
print("="*60)

# Create the files
with open('cats.txt', 'w', encoding='utf-8') as file:
    file.write("Whiskers\nMittens\nFelix\nLuna\n")

with open('dogs.txt', 'w', encoding='utf-8') as file:
    file.write("Buddy\nMax\nBella\nCharlie\n")

# Read files (including non-existent one)
filenames = ['cats.txt', 'dogs.txt', 'birds.txt']

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()
            print(f"\n--- Contents of {filename} ---")
            print(contents.rstrip())
    except FileNotFoundError:
        print(f"\n⚠️ Sorry, the file '{filename}' was not found.")

