


3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
 
# Import
import os
import time
import random
 
# Define the board
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
 
 
# Print the header
def print_header():
    print(
    """
 _____  _  ____     _____  ____  ____     _____  ____  _____
/__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/    
  / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \      
  | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_     
  \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\
 
 
 
""")
 
 
# Define the print_board function
def print_board():
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + "  ")
    print("   |   |   ")
 
 
def is_winner(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
            (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False
 
 
def is_board_full(board):
    if " " in board:
        return False
    else:
        return True
 
 
def get_computer_move(board, player):
    # if the center square is empty choose that
    if board[5] == " ":
        return 5
 
    while True:
        move = random.randint(1, 9)
        # if the move is blank, go ahead and return, otherwise try again
        if board[move] == " ":
            return move
            break
 
    return 5
 
 
while True:
    os.system("cls")
    print_header()
    print_board()
 
    # Get Player X Input
    choice = input("Please choose an empty space for X. ")
    choice = int(choice)
 
    # Check to see if the space is empty first
    if board[choice] == " ":
        board[choice] = "X"
    else:
        print("Sorry, that space is not empty!")
        time.sleep(1)
 
    # Check for X win
    if is_winner(board, "X"):
        os.system("cls")
        print_header()
        print_board()
        print("X wins! Congratulations")
        break
 
    os.system("cls")
   # print_header()
    print_board()
 
    # Check for a tie (is the board full)
    # If the board is full, do something
    if is_board_full(board):
        print("Tie!")
        break
 
    # Get Player O Input
    choice = get_computer_move(board, "O")
 
    # Check to see if the space is empty first
    if board[choice] == " ":
        board[choice] = "O"
    else:
        print
        "Sorry, that space is not empty!"
        time.sleep(1)
 
    # Check for O win
    if is_winner(board, "O"):
        os.system("cls")
        print_header()
        print_board()
        print("O wins! Congratulations")
        break
 
    # Check for a tie (is the board full)
    # If the board is full, do something
    if is_board_full(board):
        print("Tie!")
        break