import random
import pygame
import time

pygame.init()

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        return damage
#Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Action game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def print_slow(text, delay=0.10):
    #Print text slowly for dramatic effect.
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def game_intro():
    print_slow("Welcome to the Text-Based Action Game!")
    print_slow("You will fight against various enemies to prove your strength.")
    print_slow("Defeat all enemies to win the game!")
# Display score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Start:", True, WHITE)
    screen.blit(score_text, (10, 10))

def create_player():
    name = input("Enter your character's name: ")
    return Character(name, health=20, attack_power=5)

def create_enemy():
    enemy_names = ["Goblin", "Orc", "Dragon"]
    name = random.choice(enemy_names)
    health = random.randint(10, 20)
    attack_power = random.randint(2, 5)
    return Character(name, health, attack_power)

def battle(player, enemy):
    print(f"\nA wild {enemy.name} appears with {enemy.health} health!")
    
    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name}'s Health: {player.health}")
        print(f"{enemy.name}'s Health: {enemy.health}")
        
        action = input("Choose your action: (attack/run) ").lower()
        
        if action == "attack":
            damage = player.attack(enemy)
            print(f"You dealt {damage} damage to {enemy.name}!")
        elif action == "run":
            print("You ran away from the battle!")
            return False
        else:
            print("Invalid action! Please choose again.")
            continue

        if enemy.health > 0:
            damage = enemy.attack(player)
            print(f"{enemy.name} dealt {damage} damage to you!")

    if player.health <= 0:
        print(f"You have been defeated by {enemy.name}!")
        return False
    else:
        print(f"You have defeated {enemy.name}!")
        return True

def main_game_loop():
    game_intro()
    player = create_player()
    
    while player.health > 0:
        enemy = create_enemy()
        if not battle(player, enemy):
            break

    print("Game Over!")

# Start the game
main_game_loop()
