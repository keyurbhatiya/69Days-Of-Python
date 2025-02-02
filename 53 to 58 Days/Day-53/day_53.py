 ################################## Day 53: 69 Days of Python #####################################

# Colour game using PyQt5 in Python

# Steps for implementation of the GUI :
# 1. Create a head label to display the game's name and specify its characteristics, such as alignment colour, etc.
# 2. Make an instruction label to provide the user the instructions.
# 3. Design a push button to launch or restart the game.
# 4. Make a label to display the score.
# 5. Create a line edit to collect user input.
# 6. Create a label for a countdown of 30 seconds.

# Python program to create a colour game using PyQt5  
# import all the required libraries  
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QApplication
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
import random
import sys
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class GameState:
    """Class to manage game state"""
    score: int = 0
    time_remaining: int = 30
    current_color: str = ""
    is_active: bool = False
    
class ColorGame(QMainWindow):
    COLORS: List[str] = [
        'blue', 'red', 'pink', 'green', 'black',
        'orange', 'yellow', 'brown', 'purple'
    ]
    
    GAME_DURATION: int = 30
    WINDOW_SIZE = (550, 550)
    WINDOW_POSITION = (150, 150)
    
    def __init__(self):
        super().__init__()
        self.state = GameState()
        self.timer: Optional[QTimer] = None
        self.setup_ui()
        
    def setup_ui(self):
        """Initialize and setup all UI components"""
        self.setWindowTitle("Color Game")
        self.setGeometry(*self.WINDOW_POSITION, *self.WINDOW_SIZE)
        
        self._setup_heading()
        self._setup_instructions()
        self._setup_start_button()
        self._setup_score_display()
        self._setup_color_display()
        self._setup_input()
        self._setup_timer_display()
        
        self.show()
        
    def _setup_heading(self):
        """Setup game heading"""
        heading = QLabel("Color Game", self)
        heading.setGeometry(100, 10, 300, 60)
        
        font = QFont('Times', 14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        
        heading.setFont(font)
        heading.setAlignment(Qt.AlignCenter)
        
    def _setup_instructions(self):
        """Setup instruction text"""
        instructions = (
            "Instructions: Enter the color of the text, not the word shown. "
            "Press Start button to begin. Time limit: 30 seconds"
        )
        inst_label = QLabel(instructions, self)
        inst_label.setWordWrap(True)
        inst_label.setGeometry(20, 60, 460, 60)
        
    def _setup_start_button(self):
        """Setup start/reset button"""
        start = QPushButton("Start / Reset", self)
        start.setGeometry(200, 120, 100, 35)
        start.clicked.connect(self.start_game)
        
    def _setup_score_display(self):
        """Setup score display"""
        self.score_label = QLabel("Score: 0", self)
        self.score_label.setGeometry(160, 170, 180, 50)
        self.score_label.setAlignment(Qt.AlignCenter)
        self.score_label.setFont(QFont('Times', 16))
        self.score_label.setStyleSheet("""
            QLabel {
                border: 2px solid black;
                color: green;
                background: lightgrey;
            }
        """)
        
    def _setup_color_display(self):
        """Setup color display area"""
        self.color_label = QLabel("Color Name", self)
        self.color_label.setGeometry(50, 230, 400, 120)
        self.color_label.setAlignment(Qt.AlignCenter)
        self.color_label.setFont(QFont('Times', 30))
        
    def _setup_input(self):
        """Setup input field"""
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(150, 340, 200, 50)
        self.input_field.setFont(QFont('Arial', 14))
        self.input_field.setEnabled(False)
        self.input_field.returnPressed.connect(self.check_answer)
        
    def _setup_timer_display(self):
        """Setup timer display"""
        self.timer_label = QLabel(str(self.GAME_DURATION), self)
        self.timer_label.setGeometry(225, 430, 50, 50)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setFont(QFont('Times', 14))
        self.timer_label.setStyleSheet("""
            QLabel {
                border: 2px solid black;
                background: lightgrey;
            }
        """)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)
        
    def generate_new_round(self):
        """Generate a new color combination"""
        display_color = random.choice(self.COLORS)
        text_color = random.choice(self.COLORS)
        
        self.state.current_color = text_color
        self.color_label.setStyleSheet(f"color: {text_color};")
        self.color_label.setText(display_color)
        
    def start_game(self):
        """Start or reset the game"""
        self.state = GameState(time_remaining=self.GAME_DURATION)
        self.state.is_active = True
        
        self.score_label.setText("Score: 0")
        self.timer_label.setText(str(self.GAME_DURATION))
        self.input_field.clear()
        self.input_field.setEnabled(True)
        self.input_field.setFocus()
        
        self.generate_new_round()
        
    def check_answer(self):
        """Verify user input"""
        if not self.state.is_active:
            return
            
        user_input = self.input_field.text().lower().strip()
        if user_input == self.state.current_color:
            self.state.score += 1
            self.score_label.setText(f"Score: {self.state.score}")
            self.input_field.clear()
            self.generate_new_round()
            
    def update_timer(self):
        """Update game timer"""
        if not self.state.is_active:
            return
            
        self.state.time_remaining -= 1
        self.timer_label.setText(str(max(0, self.state.time_remaining)))
        
        if self.state.time_remaining <= 0:
            self.end_game()
            
    def end_game(self):
        """End the current game"""
        self.state.is_active = False
        self.input_field.setEnabled(False)
        self.color_label.setText("Game Over!")
        self.color_label.setStyleSheet("color: red;")

def main():
    app = QApplication(sys.argv)
    game = ColorGame()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()