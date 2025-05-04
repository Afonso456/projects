content = '''import random
from constants import GRID_WIDTH, GRID_HEIGHT

class Food:
    """Class representing the food in the game."""
    
    def __init__(self, max_x, max_y):
        """Initialize food with maximum boundaries."""
        self.max_x = max_x
        self.max_y = max_y
        self.position = self.generate_position()
        
    def generate_position(self, snake_positions=None):
        """Generate a random position for the food."""
        if snake_positions is None:
            snake_positions = []
        
        while True:
            x = random.randint(0, self.max_x)
            y = random.randint(0, self.max_y)
            position = (x, y)
            
            if position not in snake_positions:
                return position
        
    def respawn(self, snake_positions=None):
        """Move food to a new random position, avoiding the snake."""
        self.position = self.generate_position(snake_positions)
'''

with open('food.py', 'w') as f:
    f.write(content)

