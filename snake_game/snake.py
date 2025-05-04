import pygame
from constants import GRID_WIDTH, GRID_HEIGHT

class Snake:
    """Class representing the snake in the game."""
    
    def __init__(self, x, y):
        """Initialize snake at the given position."""
        self.positions = [(x, y)]  # List of positions for snake body
        self.direction = (1, 0)  # Start moving right
        self.length = 1
        self.grow_pending = False
        
        # Direction vectors
        self.UP = (0, -1)
        self.DOWN = (0, 1)
        self.LEFT = (-1, 0)
        self.RIGHT = (1, 0)
        
        # Mapping of keys to directions
        self.direction_map = {
            pygame.K_UP: self.UP,
            pygame.K_DOWN: self.DOWN,
            pygame.K_LEFT: self.LEFT,
            pygame.K_RIGHT: self.RIGHT
        }
    
    def handle_input(self, event):
        """Handle keyboard input for snake movement."""
        if event.type == pygame.KEYDOWN:
            if event.key in self.direction_map:
                new_direction = self.direction_map[event.key]
                # Prevent 180-degree turns
                if not self._is_opposite_direction(new_direction):
                    self.direction = new_direction
    
    def _is_opposite_direction(self, new_direction):
        """Check if the new direction is opposite to current direction."""
        return (self.direction[0] + new_direction[0] == 0 and 
                self.direction[1] + new_direction[1] == 0)
        
    def move(self):
        """Move the snake in its current direction."""
        # Calculate new head position
        head = self.positions[0]
        new_head = (
            (head[0] + self.direction[0]) % GRID_WIDTH,
            (head[1] + self.direction[1]) % GRID_HEIGHT
        )
        
        # Add new head
        self.positions.insert(0, new_head)
        
        # Remove tail if no growth is pending
        if not self.grow_pending:
            self.positions.pop()
        else:
            self.grow_pending = False
            self.length += 1
        
    def grow(self):
        """Mark the snake to grow on next move."""
        self.grow_pending = True
        
    def check_collision(self):
        """Check if snake has collided with itself."""
        head = self.positions[0]
        # Check if head collides with any part of body
        return head in self.positions[1:]
        
    def get_head_position(self):
        """Get the current position of snake's head."""
        return self.positions[0]
