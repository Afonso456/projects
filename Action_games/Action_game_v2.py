import random
import time

def print_slow(text, delay=0.05):
    """Print text slowly for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def start_game():
    print_slow("Welcome to the Action Text Game!")
    print_slow("You are a warrior venturing into a monster-infested dungeon.")
    print_slow("Your mission: Defeat the monster and survive.")
    print("\n")
    print("⚔️  Let the battle begin! ⚔️")
    combat()

def combat():
    # Initialize player and monster stats
    player_health = 100
    monster_health = 80
    player_attack = 15
    monster_attack = 10

    while player_health > 0 and monster_health > 0:
        print(f"\n💪 Your Health: {player_health} | 🐉 Monster's Health: {monster_health}")
        print("Choose your action:")
        print("1. Attack")
        print("2. Defend")
        print("3. Heal")

        action = input("What will you do? (1/2/3): ").strip()

        if action == "1":
            # Attack
            damage = random.randint(player_attack - 5, player_attack + 5)
            monster_health -= damage
            print_slow(f"\nYou strike the monster and deal {damage} damage!")
        elif action == "2":
            # Defend
            reduced_damage = max(0, monster_attack - random.randint(5, 10))
            player_health -= reduced_damage
            print_slow(f"\nYou defend against the monster's attack and take only {reduced_damage} damage!")
        elif action == "3":
            # Heal
            heal = random.randint(10, 20)
            player_health = min(100, player_health + heal)
            print_slow(f"\nYou quickly drink a potion and heal {heal} health!")
        else:
            print("\nInvalid action! The monster attacks you while you're indecisive.")
            player_health -= monster_attack
            continue

        # Monster attacks
        if monster_health > 0:
            monster_damage = random.randint(monster_attack - 3, monster_attack + 3)
            player_health -= monster_damage
            print_slow(f"\nThe monster claws at you and deals {monster_damage} damage!")

    # End of combat
    if player_health > 0:
        print("\n🏆 Congratulations! You defeated the monster and survived!")
    else:
        print("\n☠️ The monster has overpowered you. Game Over.")

# Start the game
start_game()