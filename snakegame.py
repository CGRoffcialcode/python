import turtle
import pygame
import time
import random 
import os

# inistialise pygame
pygame.init()
# sizing window
window_width = 600
window_height = 400

#creating varibles for colors

white = (255,255,255)
yellow = (255,255,102)
black = (0,0,0)
red = (213,50,80)
green = (0,255,0)
blue = (50,153,213)
gray = (150,150,150)


# creating the size of each of the snakes body sections
block_size = 20

# creating fonts for snake game
font_style = pygame.font.SysFont("bahnschrist",35)
score_font = pygame.font.SysFont("comicsanms", 25)
menu_font = pygame.font.SysFont("bahnschrist",45)

# creating game menu 
game_window  = pygame.display.set_mode((window_width, window_height))

clock = pygame.time.Clock
# creating score 
def Your_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    game_window.blit(value, 0,0)
# creating level
def Your_level(level):
    value = score_font.render("Level: " + str(level), True, black)
    game_window.blit(value, [window_width - 100,0])
# score
def  message(msg, color, y_displace=0):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [window_width / 6, window_height / 3 + y_displace])
# making snake
def draw_snake(block_size,snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, green, x[0], x[1], block_size,block_size)
# saving high score on a txt file
def save_high_score(name, score):
    if not os.path.exists("high_scores.txt"):
        with open("high_score.txt", "w") as file:
            file.write("Name: score\n")
    # open the txt file if it is created and write another score
    with open("high_scores.txt", "a") as file:
        file.write(f"{name}: {score}\n")
# reading the high scores and interpeting them into the system
def read_high_scores():
    if not os.path.exists("high_scores.txt"):
        return[]
    
    scores =  []
    with open("high_Scores.txt", "r") as file:
        for line in file.readlines()[1:]: # skip the first line
            name, score = line.strip().split(": ")
            scores.append((name, int(score)))
    
    return sorted(scores, key=lambda x: x[1], reverse=True)[:5]

#
def get_name():
    name = ""
    input_active = True
    while input_active:
        game_window.fill(blue)
        message("Enter your name: "+ name, black, y_displace =-30)
        message("Press Enter when done", black, x_displace = 30)
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = True
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
    return name

# showing high scores
def show_high_scores():
    scores = read_high_scores()

    game_window.fill(blue)
    message("High Scores", black, y_displace=-100)

    for idx, (name, score) in enumerate(scores):
        score_text = f"{idx + 1}, {name}: {score}"
        score_surface = score_font.render(score_text, True, black)
        game_window.blit(score_surface, [window_width / 6, window_height / 3 + 50 + idx * 30])

    message("Press any key to return", black, y_displace=150)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def startScreen():
    start = True
    while start:
        game_window.fill(blue)
        message("Welcome to Snake Game", black, y_displace=-100)
        message("Press P to Play", black, y_displace=-50)
        message("Press H for High Scores", black, y_displace=0)
        message("Press Q to Quit", black, y_displace=50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            