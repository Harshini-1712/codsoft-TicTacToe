import tkinter as tk
import math

# Board
board = [" " for _ in range(9)]
buttons = []

# Check winner
def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Draw
def is_draw():
    return " " not in board

# Minimax
def minimax(is_max):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(score, best)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(score, best)
        return best

# AI move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"
    buttons[move].config(text="O")

# Button click
def click(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i].config(text="X")

        if check_winner("X"):
            status_label.config(text="You win 🎉")
            disable_buttons()
            return

        if is_draw():
            status_label.config(text="Draw 😐")
            return

        ai_move()

        if check_winner("O"):
            status_label.config(text="AI wins 🤖")
            disable_buttons()
            return

        if is_draw():
            status_label.config(text="Draw 😐")

# Disable buttons
def disable_buttons():
    for b in buttons:
        b.config(state="disabled")

# Reset game
def reset_game():
    global board
    board = [" " for _ in range(9)]
    for b in buttons:
        b.config(text=" ", state="normal")
    status_label.config(text="Your turn")

# GUI
window = tk.Tk()
window.title("Tic Tac Toe AI 🤖")

title_label = tk.Label(window, text="You (X) vs AI (O)", font=("Arial", 16))
title_label.grid(row=0, column=0, columnspan=3)

# Buttons grid
for i in range(9):
    btn = tk.Button(window, text=" ", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: click(i))
    btn.grid(row=(i//3)+1, column=i%3)
    buttons.append(btn)

# Status label
status_label = tk.Label(window, text="Your turn", font=("Arial", 14))
status_label.grid(row=4, column=0, columnspan=3)

# Reset button
reset_btn = tk.Button(window, text="Restart", command=reset_game)
reset_btn.grid(row=5, column=0, columnspan=3)

window.mainloop()