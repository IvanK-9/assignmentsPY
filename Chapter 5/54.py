print("\n=== 5-4. Alien Colors #2 ===")

# Version 1: Runs the if block (green alien)
alien_color = 'green'

print("Version 1 (green alien):")
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points!")

# Version 2: Runs the else block (non-green alien)
alien_color = 'yellow'

print("\nVersion 2 (yellow alien):")
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points!")