import pygame
from snake import Snake
from food import Food
from settings_manager import SettingsManager
from score_manager import ScoreManager
from constants import *

class Button:
    def __init__(self, x, y, width, height, text, font_size=SMALL_FONT_SIZE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.is_hovered = False

    def draw(self, screen):
        color = GRAY if self.is_hovered else WHITE
        pygame.draw.rect(screen, color, self.rect, 2)
        text_surface = self.font.render(self.text, True, color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class Game:
    def __init__(self):
        """Initialize the game with default settings."""
        self.settings = SettingsManager()
        self.score_manager = ScoreManager()
        self.running = True
        self.state = MENU
        self.game_speed = 10  # Grid cells per second
        self.move_timer = 0
        self.paused = False
        
        # Initialize display
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        
        # Initialize fonts
        self.large_font = pygame.font.Font(None, LARGE_FONT_SIZE)
        self.medium_font = pygame.font.Font(None, MEDIUM_FONT_SIZE)
        self.small_font = pygame.font.Font(None, SMALL_FONT_SIZE)
        
        # Create menu buttons
        button_x = WINDOW_WIDTH // 2 - BUTTON_WIDTH // 2
        button_y = WINDOW_HEIGHT // 2
        self.menu_buttons = {
            'new_game': Button(button_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT, "New Game"),
            'settings': Button(button_x, button_y + BUTTON_HEIGHT + BUTTON_PADDING, 
                            BUTTON_WIDTH, BUTTON_HEIGHT, "Settings"),
            'high_scores': Button(button_x, button_y + (BUTTON_HEIGHT + BUTTON_PADDING) * 2, 
                                BUTTON_WIDTH, BUTTON_HEIGHT, "High Scores"),
            'quit': Button(button_x, button_y + (BUTTON_HEIGHT + BUTTON_PADDING) * 3, 
                        BUTTON_WIDTH, BUTTON_HEIGHT, "Quit")
        }
        
        # Initialize game objects
        self.reset_game()
        
        # Initialize clock
        self.clock = pygame.time.Clock()
        self.fps = 60

    def reset_game(self):
        """Reset the game state."""
        grid_center_x = GRID_WIDTH // 2
        grid_center_y = GRID_HEIGHT // 2
        self.snake = Snake(grid_center_x, grid_center_y)
        self.food = Food(GRID_WIDTH, GRID_HEIGHT)

    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

    def handle_events(self):
        """Handle game events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if self.state == MENU:
                self.handle_menu_events(event)
            elif self.state == PLAYING:
                self.handle_game_events(event)

    def handle_menu_events(self, event):
        """Handle events in the menu state."""
        for button_name, button in self.menu_buttons.items():
            if button.handle_event(event):
                if button_name == 'new_game':
                    self.state = PLAYING
                    self.reset_game()
                elif button_name == 'quit':
                    self.running = False
                # Add other button actions here

    def handle_game_events(self, event):
        """Handle events in the playing state."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.state = MENU
            elif event.key == pygame.K_p:
                self.paused = not self.paused
        
        # Handle snake movement
        self.snake.handle_input(event)

    def update(self):
        """Update game state."""
        if self.state == PLAYING and not self.paused:
            # Update move timer
            self.move_timer += self.clock.get_time()  # Get time since last frame
            move_delay = 1000 / self.game_speed  # Convert to milliseconds
            
            # Move snake when timer exceeds delay
            if self.move_timer >= move_delay:
                self.move_timer = 0
                self.snake.move()
                
                # Check collisions
                if self.snake.check_collision():
                    self.game_over()
                
                # Check food collision
                if self.snake.get_head_position() == self.food.position:
                    self.snake.grow()
                    self.food.respawn()
                    self.score_manager.current_score += 1
                    # Increase game speed
                    self.game_speed = min(20, 10 + self.score_manager.current_score // 5)

    def draw(self):
        """Draw game objects."""
        self.screen.fill(BLACK)
        
        if self.state == MENU:
            self.draw_menu()
        elif self.state == PLAYING:
            self.draw_game()
        
        pygame.display.flip()

    def draw_menu(self):
        """Draw the menu screen."""
        # Draw title
        title = self.large_font.render("Snake Game", True, WHITE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))
        self.screen.blit(title, title_rect)
        
        # Draw buttons
        for button in self.menu_buttons.values():
            button.draw(self.screen)

    def game_over(self):
        """Handle game over state."""
        self.state = GAME_OVER
        self.score_manager.add_score(self.score_manager.current_score)

    def draw_game(self):
        """Draw the game screen."""
        # Fill background
        self.screen.fill(BLACK)
        
        # Draw grid
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (WINDOW_WIDTH, y))
        
        # Draw snake
        for segment in self.snake.positions:
            rect = pygame.Rect(
                segment[0] * GRID_SIZE,
                segment[1] * GRID_SIZE,
                GRID_SIZE - 1,
                GRID_SIZE - 1
            )
            pygame.draw.rect(self.screen, GREEN, rect)
        
        # Draw food
        food_rect = pygame.Rect(
            self.food.position[0] * GRID_SIZE,
            self.food.position[1] * GRID_SIZE,
            GRID_SIZE - 1,
            GRID_SIZE - 1
        )
        pygame.draw.rect(self.screen, RED, food_rect)
        
        # Draw score
        score_text = self.small_font.render(
            f"Score: {self.score_manager.current_score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw game speed
        speed_text = self.small_font.render(
            f"Speed: {self.game_speed}", True, WHITE)
        self.screen.blit(speed_text, (10, 40))
        
        if self.paused:
            pause_text = self.large_font.render("PAUSED", True, WHITE)
            text_rect = pause_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
            self.screen.blit(pause_text, text_rect)
