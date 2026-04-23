import random

# Initialize our data storage
# This dictionary 'stats' acts like 6 little boxes to count rolls
stats = {
    "rolled_1": 0,
    "rolled_2": 0,
    "rolled_3": 0,
    "rolled_4": 0,
    "rolled_5": 0,
    "rolled_6": 0,
    "total_rolls": 0,
}
print("--- Welcome to the Dice Rolling Game ---")

# Start an loop so the game doesn't close after one roll
while stats["total_rolls"] < 50:
    # Pause the code and wait for the user to hit the 'Enter' key
    input("\nPress Enter to roll the die...")

    # Generate a random integer between 1 and 6
    roll = random.randint(1, 6)

    # Show the user current roll
    print(f"You rolled a: {roll}")

    stats["total_rolls"] += 1

    # Update our stats
    if roll == 1:
        stats["rolled_1"] += 1
    if roll == 2:
        stats["rolled_2"] += 1
    if roll == 3:
        stats["rolled_3"] += 1
    if roll == 4:
        stats["rolled_4"] += 1
    if roll == 5:
        stats["rolled_5"] += 1
    if roll == 6:
        stats["rolled_6"] += 1

    # Display stats
    print(f"\n--- Current Statistics (Total Rolls: {stats["total_rolls"]}) ---")

    print(f"Rolled one: {stats["rolled_1"]} times")
    print(f"Rolled two: {stats["rolled_2"]} times")
    print(f"Rolled three: {stats["rolled_3"]} times")
    print(f"Rolled four: {stats["rolled_4"]} times")
    print(f"Rolled five: {stats["rolled_5"]} times")
    print(f"Rolled six: {stats["rolled_6"]} times")

print("\n--- Game Over ---")
print("Thank you for playing :)")
