import random
import json
import yaml
import os.path
import xml.etree.ElementTree as ET

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
total_rolls = 0

print("--- Welcome to the Dice Rolling Game ---")

while True:
    game_start_choice = input(
        "Press 0 to start a new game\nPress 1 to load JSON-save-file\nPress 2 to load YAML-save-file\nPress 3 to load XML-save-file\n"
    )
    if game_start_choice == "0":
        print("A new Game has been started")
        break
    elif game_start_choice == "1":
        # Populate stats from previous game for json
        if os.path.exists("data.json"):
            with open("data.json") as f:
                data = json.load(f)
                stats["rolled_1"] = data["rolled_1"]
                stats["rolled_2"] = data["rolled_2"]
                stats["rolled_3"] = data["rolled_3"]
                stats["rolled_4"] = data["rolled_4"]
                stats["rolled_5"] = data["rolled_5"]
                stats["rolled_6"] = data["rolled_6"]
                total_rolls = data["total_rolls"]
                print("JSON Save-file has been loaded")
                break
        else:
            print("JSON Save-file does not exist. Starting a new Game")
            break
    elif game_start_choice == "2":
        # Populate stats from previous game from yaml
        if os.path.exists("data.yaml"):
            with open("data.yaml") as f:
                data = yaml.safe_load(f)
                stats["rolled_1"] = data["rolled_1"]
                stats["rolled_2"] = data["rolled_2"]
                stats["rolled_3"] = data["rolled_3"]
                stats["rolled_4"] = data["rolled_4"]
                stats["rolled_5"] = data["rolled_5"]
                stats["rolled_6"] = data["rolled_6"]
                total_rolls = data["total_rolls"]
                print("YAML Save-file has been loaded")
                break
        else:
            print("YAML Save-file does not exist. Starting a new Game")
            break
    elif game_start_choice == "3":
        # Populate stats from previous game from XML
        if os.path.exists("rolls.xml"):
            tree = ET.parse("rolls.xml")
            root = tree.getroot()
            # Conversion to integer required for XML
            stats["rolled_1"] = int(root.find("rolled_1").text)
            stats["rolled_2"] = int(root.find("rolled_2").text)
            stats["rolled_3"] = int(root.find("rolled_3").text)
            stats["rolled_4"] = int(root.find("rolled_4").text)
            stats["rolled_5"] = int(root.find("rolled_5").text)
            stats["rolled_6"] = int(root.find("rolled_6").text)
            total_rolls = int(root.find("total_rolls").text)
            break
        else:
            print("XML Save-file does not exist. Starting a new Game")
            break
    else:
        print("Enter a valid number")


# Start an loop so the game doesn't close after one roll
while total_rolls < 50:
    # Pause the code and wait for the user to hit the 'Enter' key
    choice = input(
        "Press Enter to roll the die or type quit to leave the Game: "
    ).lower()

    if choice == "quit":
        break

    # Generate a random integer between 1 and 6
    roll = random.randint(1, 6)

    # Update our counter: add 1 to the total rolls
    total_rolls += 1

    # Show the user current roll
    print(f"You rolled a: {roll}")

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

    stats["total_rolls"] = total_rolls

    # Display stats
    print(f"\n--- Current Statistics (Total Rolls: {total_rolls}) ---")

    print(f"Rolled one: {stats["rolled_1"]} times")
    print(f"Rolled two: {stats["rolled_2"]} times")
    print(f"Rolled three: {stats["rolled_3"]} times")
    print(f"Rolled four: {stats["rolled_4"]} times")
    print(f"Rolled five: {stats["rolled_5"]} times")
    print(f"Rolled six: {stats["rolled_6"]} times")

# Reset stats
if total_rolls == 50:
    stats["rolled_1"] = 0
    stats["rolled_2"] = 0
    stats["rolled_3"] = 0
    stats["rolled_4"] = 0
    stats["rolled_5"] = 0
    stats["rolled_6"] = 0
    stats["total_rolls"] = 0

while True:
    save_file_choice = input(
        "\nPress 1 to save as JSON-file\nPress 2 to save as YAML-file\nPress 3 to save as XML-file\n"
    )
    if save_file_choice == "1":
        # Save stats to json file
        with open("data.json", "w") as f:
            json.dump(stats, f)
            break
    elif save_file_choice == "2":
        # Save stats to yaml file
        with open("data.yaml", "w") as f:
            yaml.dump(stats, f)
            break
    elif save_file_choice == "3":
        # Save stats to XML file
        root = ET.Element("dice_results")
        # Build the XML structure from the dictionary
        for key, value in stats.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Create the tree object
        tree = ET.ElementTree(root)

        # Write to a file
        # 'encoding="utf-8"' and 'xml_declaration=True' ensure a proper header
        with open("rolls.xml", "wb") as file:
            tree.write(file, encoding="utf-8", xml_declaration=True)
            break
    else:
        print("Enter a valid number")

print("\nYour results have been Saved!")
print("Thank you for playing :)")
