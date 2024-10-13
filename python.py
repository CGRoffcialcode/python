# Importing libraries
import os
import time
import random

# Creating variables for key features of snake
width = 20
height = 10
snake = [(5, 5)]
snake_direction = "RIGHT"
food = (random.randint(0, height - 1), random.randint(0, width - 1))
score = 0

# Creating operating system clear function
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Drawing the Grid

def draw_grid():
    clear_console()
    for y in range(height):
        for x in range(width):
            if (y, x) == snake[0]:
                print("S", end="")  # Start
            elif (y, x) in snake:
                print("O", end="")  # Snake body
            elif (y, x) == food:
                print("F", end="")  # Food
            else:
                print(".", end="")  # Grid
        print()
    print(f"Score: {score}")
# Key code for moving snake
def move_snake():
    global snake, food, score
    head_y, head_x = snake[0]

    if snake_direction == "UP":
        new_head = (head_y - 1, head_x)  # Moving up
    elif snake_direction == "DOWN":
        new_head = (head_y + 1, head_x)  # Moving down
    elif snake_direction == "LEFT":
        new_head = (head_y, head_x - 1)  # Moving left
    elif snake_direction == "RIGHT":
        new_head = (head_y, head_x + 1)  # Moving right

    # Code for Game Over - hit wall
    if new_head[0] < 0 or new_head[0] >= height or new_head[1] < 0 or new_head[1] >= width:
        print("Game Over! You hit the wall")
        quit()

    # Code for Game Over - hit the snake
    if new_head in snake:
        print("Game over! You hit yourself")
        quit()

    # Snake eating food
    if new_head == food:
        score += 10
        while True:
            food = (random.randint(0, height - 1), random.randint(0, width - 1))
            if food not in snake:  # Ensure food does not spawn on the snake
                break
    else:
        snake.pop()  # Grows snake

    snake.insert(0, new_head)  # Update snake position

# Game loop
while True:
    draw_grid()
    move_snake()
    time.sleep(0.2)  # Slows time for a bit
    # Snake controls
    direction = input("Next direction (W/A/S/D): ").upper()
    if direction == "W" and snake_direction != "DOWN":
        snake_direction = "UP"
    elif direction == "S" and snake_direction != "UP":
        snake_direction = "DOWN"
    elif direction == "A" and snake_direction != "RIGHT":
        snake_direction = "LEFT"
    elif direction == "D" and snake_direction != "LEFT":
        snake_direction = "RIGHT"



