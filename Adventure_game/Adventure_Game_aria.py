def intro():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself in a dark forest. There are paths to the north, south, and east.")
    print("Your goal is to find the treasure hidden in the forest.")
    print("Be careful of monsters lurking around!")

def choose_path():
    path = ""
    while path not in ["north", "south", "east"]:
        path = input("Which path will you choose? (north/south/east): ").lower()
    return path

def encounter_monster():
    print("Oh no! You've encountered a monster!")
    action = input("Do you want to (fight/run)? ").lower()
    
    if action == "fight":
        print("You bravely fight the monster and emerge victorious!")
        return True
    elif action == "run":
        print("You run away safely but lose some time.")
        return False
    else:
        print("Invalid action! The monster attacks you while you hesitate.")
        return False

def main_game_loop():
    intro()
    
    has_treasure = False
    while not has_treasure:
        path = choose_path()

        if path == "north":
            print("You walk north and find an abandoned cabin.")
            if encounter_monster():
                print("You search the cabin and find the treasure!")
                has_treasure = True
            else:
                print("You decide to leave the cabin empty-handed.")
        
        elif path == "south":
            print("You walk south and discover a beautiful waterfall.")
            print("You take a moment to relax and enjoy the view.")
            print("You find some gold coins hidden behind the waterfall!")
            has_treasure = True

        elif path == "east":
            print("You walk east and enter a dark cave.")
            if encounter_monster():
                print("You find a treasure chest inside the cave!")
                has_treasure = True
            else:
                print("You decide to leave the cave before more monsters appear.")

    print("Congratulations! You've found the treasure and completed your adventure!")

# Start the game
main_game_loop()
