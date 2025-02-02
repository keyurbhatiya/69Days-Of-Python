################################## Day 48: 69 Days of Python #####################################

# Ping Pong Game Using Turtle in Python
import os
import turtle
from typing import Tuple
import time

class PongGame:
    def __init__(self):
        # Constants
        self.WINDOW_WIDTH = 1050
        self.WINDOW_HEIGHT = 650
        self.PADDLE_SPEED = 20
        self.BALL_SPEED = 6
        self.PADDLE_WIDTH = 20
        self.PADDLE_HEIGHT = 120
        self.BALL_SIZE = 20
        
        self.setup_screen()
        self.setup_paddles()
        self.setup_ball()
        self.setup_scoreboard()
        self.setup_controls()
        
        # Game state
        self.is_paused = False
        self.game_running = True
        self.last_frame_time = time.time()
        self.FPS = 60
        self.frame_delay = 1.0 / self.FPS
    
    def setup_screen(self) -> None:
        """Initialize the game screen with optimized settings."""
        self.screen = turtle.Screen()
        self.screen.title("Optimized Ping-Pong Game")
        self.screen.bgcolor("Yellow")
        self.screen.setup(width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)
        self.screen.tracer(0)  # Turn off automatic updates for better performance
    
    def setup_paddles(self) -> None:
        """Create and initialize paddle objects with optimized properties."""
        # Left paddle
        self.left_paddle = turtle.Turtle()
        self._configure_paddle(self.left_paddle, "Red", -400)
        
        # Right paddle
        self.right_paddle = turtle.Turtle()
        self._configure_paddle(self.right_paddle, "Blue", 400)
    
    def _configure_paddle(self, paddle: turtle.Turtle, color: str, x_pos: int) -> None:
        """Configure paddle properties with optimized settings."""
        paddle.speed(0)
        paddle.shape("square")
        paddle.color(color)
        paddle.shapesize(stretch_wid=6, stretch_len=2)
        paddle.penup()
        paddle.goto(x_pos, 0)
    
    def setup_ball(self) -> None:
        """Initialize the ball with optimized properties."""
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("Black")
        self.ball.penup()
        self.reset_ball()
    
    def reset_ball(self) -> None:
        """Reset ball position and speed."""
        self.ball.goto(0, 0)
        self.ball.dx = self.BALL_SPEED
        self.ball.dy = -self.BALL_SPEED
    
    def setup_scoreboard(self) -> None:
        """Initialize the scoreboard with optimized properties."""
        self.score = {"left": 0, "right": 0}
        self.scoreboard = turtle.Turtle()
        self.scoreboard.speed(0)
        self.scoreboard.color("blue")
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0, 260)
        self.update_scoreboard()
    
    def update_scoreboard(self) -> None:
        """Update the score display."""
        self.scoreboard.clear()
        self.scoreboard.write(
            f"Left Player : {self.score['left']}    Right Player: {self.score['right']}",
            align="center",
            font=("Courier", 24, "normal")
        )
    
    def setup_controls(self) -> None:
        """Set up game controls with improved key bindings."""
        self.screen.listen()
        # Using more intuitive controls (W/S for left paddle, Up/Down for right paddle)
        self.screen.onkeypress(self.paddle_L_up, "w")
        self.screen.onkeypress(self.paddle_L_down, "s")
        self.screen.onkeypress(self.paddle_R_up, "Up")
        self.screen.onkeypress(self.paddle_R_down, "Down")
        self.screen.onkeypress(self.toggle_pause, "p")
        self.screen.onkeypress(self.quit_game, "q")
    
    def paddle_movement(self, paddle: turtle.Turtle, direction: int) -> None:
        """Handle paddle movement with boundary checking."""
        new_y = paddle.ycor() + (self.PADDLE_SPEED * direction)
        if abs(new_y) < (self.WINDOW_HEIGHT / 2 - self.PADDLE_HEIGHT/2):
            paddle.sety(new_y)
    
    def paddle_L_up(self): self.paddle_movement(self.left_paddle, 1)
    def paddle_L_down(self): self.paddle_movement(self.left_paddle, -1)
    def paddle_R_up(self): self.paddle_movement(self.right_paddle, 1)
    def paddle_R_down(self): self.paddle_movement(self.right_paddle, -1)
    
    def toggle_pause(self) -> None:
        """Toggle game pause state."""
        self.is_paused = not self.is_paused
    
    def quit_game(self) -> None:
        """Safely exit the game."""
        self.game_running = False
    
    def check_collision(self, paddle: turtle.Turtle) -> bool:
        """Optimized collision detection."""
        return (abs(self.ball.xcor() - paddle.xcor()) < self.PADDLE_WIDTH and 
                abs(self.ball.ycor() - paddle.ycor()) < self.PADDLE_HEIGHT/2)
    
    def update_game_state(self) -> None:
        """Update game state with improved physics and collision detection."""
        if self.is_paused:
            return
            
        # Move ball
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)
        
        # Border checking
        if abs(self.ball.ycor()) > self.WINDOW_HEIGHT/2 - 20:
            self.ball.dy *= -1
            
        # Score checking
        if abs(self.ball.xcor()) > self.WINDOW_WIDTH/2:
            if self.ball.xcor() > 0:
                self.score["left"] += 1
            else:
                self.score["right"] += 1
            self.update_scoreboard()
            self.reset_ball()
            
        # Paddle collisions
        if self.check_collision(self.right_paddle) and self.ball.dx > 0:
            self.ball.dx *= -1.1  # Gradually increase speed
            
        if self.check_collision(self.left_paddle) and self.ball.dx < 0:
            self.ball.dx *= -1.1  # Gradually increase speed
    
    def maintain_frame_rate(self) -> None:
        """Maintain consistent frame rate."""
        current_time = time.time()
        elapsed = current_time - self.last_frame_time
        if elapsed < self.frame_delay:
            time.sleep(self.frame_delay - elapsed)
        self.last_frame_time = time.time()
    
    def run(self) -> None:
        """Main game loop with improved performance."""
        while self.game_running:
            self.screen.update()
            self.update_game_state()
            self.maintain_frame_rate()
        
        self.screen.bye()

if __name__ == "__main__":
    game = PongGame()
    game.run() 


# Controls
# Left Paddle: w, s
# Right Paddle: up, down
# Quit: q
# Pause: p
