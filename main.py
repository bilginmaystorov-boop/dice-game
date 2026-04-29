import os
import json
from pick import pick
import random
from datetime import datetime

MAX_ROLLS = 50

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

# Step 2: check for existing Save files
try:
    # Ensure the directory exists so listdir doesn't fail
    if not os.path.exists("save_files"):
        os.makedirs("save_files")

    save_files = os.listdir("save_files")
except Exception as e:
    print("Something went wrong when loading save files: ", e)
    save_files = []

save_files.append("New game file")
save_files_prompt = "Choose a save file or start a new game: "

selected_save_file = pick(save_files, save_files_prompt)


def load_save_file(save_file_name):
    try:
        if save_file_name != "New game file":
            with open(f"save_files/{save_file_name}", "r") as f:
                data = json.load(f)
    except Exception as e:
        print("Something went wrong when loading save file: ", e)
    finally:
        # stats["rolled_1"] = data["rolled_1"]
        # stats["rolled_2"] = data["rolled_2"]
        # stats["rolled_3"] = data["rolled_3"]
        # stats["rolled_4"] = data["rolled_4"]
        # stats["rolled_5"] = data["rolled_5"]
        # stats["rolled_6"] = data["rolled_6"]
        if save_file_name != "New game file":
            for element in data:
                stats[element] = data[element]


load_save_file(selected_save_file[0])

# Step 3 implement Game logic
while stats["total_rolls"] < MAX_ROLLS:
    # Pause the code and wait for the user to hit the 'Enter' key
    choice = input(
        "Press Enter to roll the die or type quit to leave the Game: "
    ).lower()

    if choice == "quit":
        break

    # Generate a random integer between 1 and 6
    roll = random.randint(1, 6)

    # Update our counter: add 1 to the total rolls
    stats["total_rolls"] += 1

    # Update our stats
    if roll == 1:
        stats["rolled_1"] = stats["rolled_1"] + 1
    if roll == 2:
        stats["rolled_2"] = stats["rolled_2"] + 1
    if roll == 3:
        stats["rolled_3"] = stats["rolled_3"] + 1
    if roll == 4:
        stats["rolled_4"] = stats["rolled_4"] + 1
    if roll == 5:
        stats["rolled_5"] = stats["rolled_5"] + 1
    if roll == 6:
        stats["rolled_6"] = stats["rolled_6"] + 1

    stats["total_rolls"] = stats["total_rolls"]

    # Display stats
    print(f"\n--- Current Statistics (Total Rolls: {stats["total_rolls"]}) ---")

    print(f"Rolled one: {stats["rolled_1"]} times")
    print(f"Rolled two: {stats["rolled_2"]} times")
    print(f"Rolled three: {stats["rolled_3"]} times")
    print(f"Rolled four: {stats["rolled_4"]} times")
    print(f"Rolled five: {stats["rolled_5"]} times")
    print(f"Rolled six: {stats["rolled_6"]} times")

    # Show the user current roll
    print(f"\nYou rolled a: {roll}")

# Step 4 Save progres or result to a new or existing save file


def get_current_time_stamp():
    # 1. Get the current local date and time
    now = datetime.now()

    # 2. Format it: %Y (Year), %m (Month), %d (Day), %H (Hour), %M (Minute)
    timestamp = now.strftime("%Y%m%d_%H%M")

    # 3. Create your filename
    filename = f"save_{timestamp}.json"
    return filename


save_file_prompt = "Rewrite save file or create a new one: "
save_file_choice = pick(save_files, save_file_prompt)


def save_game():
    if save_file_choice[0] == "New game file":
        file_path = f"save_files/{get_current_time_stamp()}"

        with open(file_path, "w") as f:
            json.dump(stats, f)
    else:
        with open(f"save_files/{save_file_choice[0]}", "r") as f:
            data = json.load(f)

        for stat in stats:
            data[stat] = stats[stat]

        with open(f"save_files/{save_file_choice[0]}", "w") as f:
            json.dump(data, f)


save_game()

print("\nYour results have been Saved!")
print("Thank you for playing :)")

# Step 5 reset initial data and save finished game
if stats["total_rolls"] == MAX_ROLLS:
    file_path = f"save_files/{get_current_time_stamp()}"
    with open(file_path, "w") as f:
        json.dump(stats, f)

    for element in stats:
        stats[element] = 0
