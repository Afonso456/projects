import json
import os

class SettingsManager:
    """Class for managing game settings and preferences."""
    
    def __init__(self):
        """Initialize settings with default values."""
        self.settings_file = os.path.expanduser("~/snake_game_settings.json")
        self.default_settings = {
            "difficulty": "medium",
            "theme": "default",
            "speed": 5
        }
        self.current_settings = self.load_settings()
        
    def load_settings(self):
        """Load settings from file or create with defaults."""
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, 'r') as f:
                    return json.load(f)
            return self.default_settings.copy()
        except Exception as e:
            print(f"Error loading settings: {e}")
            return self.default_settings.copy()
        
    def save_settings(self):
        """Save current settings to file."""
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(self.current_settings, f)
        except Exception as e:
            print(f"Error saving settings: {e}")

