import os
import json
from pick import pick
import random
from datetime import datetime
from player import Player

# 1. --- CONFIG & DIRECTORY SETUP ---
MAX_ROLLS = 50
SAVE_DIR = "save_files"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


# 2. --- FUNCTIONS ---
def get_save_files():
    files = os.listdir(SAVE_DIR)
    files.append("New game file")
    return files


def display_stats_with_leader(players):
    print("\n" + "=" * 50)
    print(f"{'Player':<12} | {'1s  2s  3s  4s  5s  6s':<18} | {'Total Rolls'}")
    print("-" * 50)
    leader_name = ""
    high_score = -1
    for p in players:
        s = p.get_stats()
        current_score = 0
        for i in range(1, 7):
            current_score += i * s[f"rolled_{i}"]
        if current_score > high_score:
            high_score = current_score
            leader_name = p.get_name()
        dice_line = f"{s['rolled_1']}   {s['rolled_2']}   {s['rolled_3']}   {s['rolled_4']}   {s['rolled_5']}   {s['rolled_6']}"
        print(f"{p.get_name():<12} | {dice_line:<18} | {s['total_rolls']}")
    print("-" * 50)
    if high_score > 0:
        print(f"🏆 CURRENTLY WINNING: {leader_name}!")
    print("=" * 50 + "\n")


def save_game(players_list, original_filename):
    data_to_save = [
        {"name": p.get_name(), "stats": p.get_stats()} for p in players_list
    ]
    if original_filename == "New game file":
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"save_{timestamp}.json"
    else:
        filename = original_filename
    with open(os.path.join(SAVE_DIR, filename), "w") as f:
        json.dump(data_to_save, f, indent=4)
    print(f"\nGame saved to {filename}!")


# 3. --- INITIALIZATION & LOADING ---
save_files = get_save_files()
selected_file, _ = pick(save_files, "Choose a save file or start a new game:")
players = []

if selected_file == "New game file":
    player_count = int(input("Enter number of players: "))
    for i in range(player_count):
        name = input(f"Enter name for Player {i+1}: ")
        players.append(Player(name))
else:
    with open(os.path.join(SAVE_DIR, selected_file), "r") as f:
        saved_data = json.load(f)
        for p_data in saved_data:
            new_player = Player(p_data["name"])
            new_player.load_stats(p_data["stats"])
            players.append(new_player)

# 4. --- CHECK IF LOADED GAME IS FINISHED ---
last_player_total_rolls = players[-1].get_stats()["total_rolls"]

if last_player_total_rolls >= MAX_ROLLS:
    print("\n" + "!" * 50)
    print("THIS GAME IS ALREADY FINISHED!")
    display_stats_with_leader(players)
    print("!" * 50)
    exit()

# 5. --- THE GAME LOOP ---
while last_player_total_rolls < MAX_ROLLS:
    quit_game = False
    for i in range(len(players)):
        choice = input(
            f"{players[i].get_name()}'s turn. [Enter] to roll, 'quit' to save: "
        ).lower()
        if choice == "quit":
            quit_game = True
            break
        roll = random.randint(1, 6)
        players[i].update_stats(roll)
        display_stats_with_leader(players)
        last_player_total_rolls = players[-1].get_stats()["total_rolls"]
    if quit_game:
        break

# 6. --- FINAL SAVE ---
save_game(players, selected_file)
