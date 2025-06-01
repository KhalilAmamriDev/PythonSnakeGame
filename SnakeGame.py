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
key = curses.KEY_RIGHT  # Initial direction of the snake
while True:
    next_key = window.getch()  # Get the next key pressed
    key = key if next_key == -1 else next_key  # If no key pressed, keep the current direction

    # Calculate new head position based on the current direction
    if key == curses.KEY_DOWN:
        new_head = [snake[0][0] + 1, snake[0][1]]
    elif key == curses.KEY_UP:
        new_head = [snake[0][0] - 1, snake[0][1]]
    elif key == curses.KEY_LEFT:
        new_head = [snake[0][0], snake[0][1] - 1]
    elif key == curses.KEY_RIGHT:
        new_head = [snake[0][0], snake[0][1] + 1]
    else:
        new_head = [snake[0][0], snake[0][1]]

    # Insert new head to the snake
    snake.insert(0, new_head)

    # Check if snake ate the food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, screenHeight - 2),
                random.randint(1, screenWidth - 2)
            ]
            if nf not in snake:
                food = nf
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        # Remove last segment of the snake
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    # Check for collision with walls or itself
    if (
        snake[0][0] in [0, screenHeight] or
        snake[0][1] in [0, screenWidth] or
        snake[0] in snake[1:]
    ):
        curses.endwin()
        quit()

    # Draw the snake's head
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)