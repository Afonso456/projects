def start_game():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself at the entrance of a dark forest.")
    print("There are two paths ahead:")
    print("1. The left path seems quiet and peaceful.")
    print("2. The right path is dark and eerie, with strange noises.")
    choice = input("Which path do you take? (left/right): ").strip().lower()
    
    if choice == "left":
        peaceful_path()
    elif choice == "right":
        dark_path()
    else:
        print("Invalid choice. Let's try again.")
        start_game()

def peaceful_path():
    print("\nYou walk along the peaceful path, enjoying the scenery.")
    print("Suddenly, you encounter a sparkling river with a small bridge.")
    print("What do you do?")
    print("1. Cross the bridge.")
    print("2. Follow the river upstream.")
    choice = input("Your decision? (cross/follow): ").strip().lower()

    if choice == "cross":
        print("\nYou cross the bridge and find a treasure chest!")
        print("Congratulations! You've discovered hidden riches and won the game!")
    elif choice == "follow":
        print("\nYou follow the river upstream and find a friendly village.")
        print("The villagers welcome you and offer you a home. You've found a new life!")
    else:
        print("Invalid choice. Let's try again.")
        peaceful_path()

def dark_path():
    print("\nYou cautiously tread along the dark path.")
    print("You hear growls and see glowing eyes in the distance.")
    print("What do you do?")
    print("1. Confront the source of the noise.")
    print("2. Turn back and run.")
    choice = input("Your decision? (confront/run): ").strip().lower()

    if choice == "confront":
        print("\nYou bravely face the glowing eyes and discover a pack of wolves!")
        print("Unfortunately, they are not friendly. You didn't survive the encounter.")
        print("Game Over.")
    elif choice == "run":
        print("\nYou run back to the forest entrance and escape safely.")
        print("Perhaps it's best to take the peaceful path instead.")
        start_game()
    else:
        print("Invalid choice. Let's try again.")
        dark_path()

# Start the game
start_game()
