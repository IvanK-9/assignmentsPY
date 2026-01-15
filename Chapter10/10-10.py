# ============================================================
# EXERCISE 10-10: COMMON WORDS
# ============================================================
print("\n\n" + "="*60)
print("EXERCISE 10-10: COMMON WORDS")
print("="*60)

# Create a test file
with open('sample_text.txt', 'w', encoding='utf-8') as file:
    file.write("""The sun was shining on the sea,
Shining with all its might:
The Walrus and the Carpenter
Were walking close at hand;
They wept like anything to see
Such quantities of sand.
If this were only cleared away,
They said, it would be grand!
The time has come, the Walrus said,
To talk of many things.
""")

try:
    with open('sample_text.txt', encoding='utf-8') as file:
        contents = file.read()
    
    # Count the word 'the'
    contents_lower = contents.lower()
    count = contents_lower.count('the')
    
    print(f"\n📊 The word 'the' appears {count} time(s) in the file.")
    print(f"\nFirst 200 characters of text:")
    print(contents[:200] + "...")
    
except FileNotFoundError:
    print("\n⚠️ File not found.")


print("\n\n" + "="*60)
print("ALL EXERCISES COMPLETED!")
print("="*60)