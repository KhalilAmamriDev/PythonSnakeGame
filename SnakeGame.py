import random
import curses

screen = curses.initscr()
curses.curs_set(0)  # Hide the cursor
screenHeight, screenWidth = screen.getmaxyx()  # Get the height and width of the screen
window = curses.newwin(screenHeight, screenWidth, 0, 0)  # Create a new window
window.keypad(1)  # Enable keypad input
window.timeout(100)  # Set a timeout for input
# Initial snake and food positions
snake_x = screenWidth // 4
snake_y = screenHeight // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]
food = [screenHeight // 2, screenWidth // 2]
window.addch(int(food[0]), int(food[1]), curses.ACS_PI)  # Place food on the screen