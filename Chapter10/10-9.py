# ============================================================
# EXERCISE 10-9: SILENT CATS AND DOGS
# ============================================================
print("\n\n" + "="*60)
print("EXERCISE 10-9: SILENT CATS AND DOGS")
print("="*60)

filenames = ['cats.txt', 'dogs.txt', 'birds.txt']

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()
            print(f"\n--- Contents of {filename} ---")
            print(contents.rstrip())
    except FileNotFoundError:
        pass  # Fail silently