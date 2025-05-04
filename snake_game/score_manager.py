import json
import os
from datetime import datetime

class ScoreManager:
    """Class for managing game scores."""
    
    def __init__(self):
        """Initialize score manager."""
        self.scores_file = os.path.expanduser("~/snake_game_scores.json")
        self.current_score = 0
        self.high_scores = self.load_scores()
        
    def load_scores(self):
        """Load high scores from file."""
        try:
            if os.path.exists(self.scores_file):
                with open(self.scores_file, 'r') as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Error loading scores: {e}")
            return []
        
    def save_scores(self):
        """Save high scores to file."""
        try:
            with open(self.scores_file, 'w') as f:
                json.dump(self.high_scores, f)
        except Exception as e:
            print(f"Error saving scores: {e}")
            
    def add_score(self, score):
        """Add a new score to high scores."""
        score_entry = {
            "score": score,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.high_scores.append(score_entry)
        self.high_scores.sort(key=lambda x: x["score"], reverse=True)
        self.high_scores = self.high_scores[:10]  # Keep only top 10
        self.save_scores()

