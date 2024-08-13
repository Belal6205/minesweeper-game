from tkinter import *
from tkinter import messagebox
from random import randint
import json, os

rows = None
columns = None
mines = None
game_state = "playing"
name = ""

VALUE_COLORS = {
    0: "black",
    1: "lightblue",
    2: "green",
    3: "lightcoral",
    4: "blue",
    5: "red",
    6: "cyan",
    7: "gray25",  # dark gray
    8: "gray75",  # light gray
}

DIFFICULTIES = {"easy": (8, 8, 10), "normal": (16, 16, 40), "hard": (16, 30, 99)}

class Cell:
    def __init__(self, row, column, button, value=0):
        self.row = row
        self.column = column
        self.value = value
        self.revealed = False
        self.flagged = False
        self.button = button

window = Tk()
window.title("Minesweeper")

game_frame = Frame(window)
game_frame.pack()

welcome_label = Label(window, text="Welcome to Minesweeper!", font=("Arial", 20))
welcome_label.pack()

label_name = Label(window, text="Welcome User!!")
label_name.pack()

difficulty_buttons = []
cells = []

def save_game():
    if game_state != "playing":
        messagebox.showinfo(
            title="Warning", message="You can only save the game while playing"
        )
        return
    try:
        game_state_data = {
            "rows": rows,
            "columns": columns,
            "mines": mines,
            "game_state": game_state,
            "name": name,
            "cells": [
                [
                    {
                        "value": cell.value,
                        "revealed": cell.revealed,
                        "flagged": cell.flagged,
                    }
                    for cell in row
                ]
                for row in cells
            ],
        }
        file_path = f"{name}.json"
        with open(file_path, "w") as file:
            json.dump(game_state_data, file, indent=2)
    except Exception as e:
        print(f"Error: {e}")

def load_game():
    file_path = f"{name}.json"
    with open(file_path, "r") as file:
        game_state_data = json.load(file)

    global rows, columns, mines, game_state, cells
    rows = game_state_data["rows"]
    columns = game_state_data["columns"]
    mines = game_state_data["mines"]
    game_state = game_state_data["game_state"]
    cells_data = game_state_data["cells"]

    for row in range(rows):
        cell_row = []
        for column in range(columns):
            cell_button = Button(
                game_frame,
                width=3,
                height=1,
                command=lambda r=row, c=column: reveal_cell(r, c),
            )
            cell_button.bind(
                "<Button-3>", lambda event, r=row, c=column: show_flag(r, c)
            )
            cell_button.grid(row=row, column=column)
            cell = Cell(row, column, cell_button)
            cell_row.append(cell)
        cells.append(cell_row)

    for row in range(rows):
        for column in range(columns):
            cells[row][column].value = cells_data[row][column]["value"]
            cells[row][column].revealed = cells_data[row][column]["revealed"]
            cells[row][column].flagged = cells_data[row][column]["flagged"]

            if cells[row][column].revealed:
                reveal_cell(row, column)
            if cells[row][column].flagged:
                cells[row][column].button.configure(bg="orange")

def generate_board():
    global cells
    cells = []
    for row in range(rows):
        cell_row = []
        for column in range(columns):
            cell_button = Button(
                game_frame,
                width=3,
                height=1,
                command=lambda r=row, c=column: reveal_cell(r, c),
            )
            cell_button.bind(
                "<Button-3>", lambda event, r=row, c=column: show_flag(r, c)
            )
            cell_button.grid(row=row, column=column)
            cell = Cell(row, column, cell_button)
            cell_row.append(cell)
        cells.append(cell_row)

    for _ in range(mines):
        while True:
            row = randint(0, rows - 1)
            column = randint(0, columns - 1)
            if cells[row][column].value != -1:
                cells[row][column].value = -1
                for r in range(row - 1, row + 2):
                    for c in range(column - 1, column + 2):
                        if 0 <= r < rows and 0 <= c < columns and cells[r][c].value != -1:
                            cells[r][c].value += 1
                break

def get_name():
    global name
    name = entry.get()
    if name == "":
        return
    label.destroy()
    entry.destroy()
    start_game()

def check_unfinished_game():
    return os.path.exists(f"{name}.json")

def delete_saved_game():
    if check_unfinished_game():
        os.remove(f"{name}.json")

def start_game(forced=False):
    global label_name
    label_name.configure(text=f"Welcome, {name.capitalize()}")
    welcome_label.destroy()

    global button_start, save_button, main_menu
    button_start.destroy()

    if check_unfinished_game() and not forced:
        load_game()
        save_button = Button(window, text="Save Game", command=save_game)
        save_button.pack()
        button_start = Button(window, text="Start Over", command=restart)
        button_start.pack()
        main_menu = Button(window, text="Main Menu", command=main_menu_back)
        main_menu.pack()
    else:
        generate_difficulty_page()

def handle_difficulty_click(r, c, m):
    global rows, columns, mines
    rows, columns, mines = r, c, m

    for btn in difficulty_buttons:
        btn.destroy()
    generate_board()
    save_button = Button(window, text="Save Game", command=save_game)
    save_button.pack()
    button_start = Button(window, text="Start Over", command=restart)
    button_start.pack()
    main_menu = Button(window, text="Main Menu", command=main_menu_back)
    main_menu.pack()

def main_menu_back():
    global cells, save_button, button_start, main_menu
    for row in cells:
        for cell in row:
            cell.button.pack_forget()
            cell.button.destroy()
    cells = []

    save_button.destroy()
    button_start.destroy()
    main_menu.destroy()

    start_game(forced=True)

def generate_difficulty_page():
    for dif, vals in DIFFICULTIES.items():
        rows, columns, mines = vals
        btn = Button(
            window,
            text=dif.capitalize(),
            command=lambda r=rows, c=columns, m=mines: handle_difficulty_click(r, c, m),
        )
        btn.pack()
        difficulty_buttons.append(btn)

def show_flag(row, column):
    cell = cells[row][column]

    if not cell.revealed:
        if cell.flagged:
            cell.button.configure(bg="white")
            cell.flagged = False
        else:
            cell.button.configure(bg="orange")
            cell.flagged = True

def reveal_cell(row, column):
    global game_state, label_name
    cell = cells[row][column]
    if cell.flagged or game_state == "game_over":
        return
    if cell.value == -1:
        game_state = "game_over"
        label_name.config(text="Game Over")
        for row in range(rows):
            for column in range(columns):
                if cells[row][column].value == -1:
                    cells[row][column].revealed = True
                    cells[row][column].button.configure(bg="red")
        delete_saved_game()
    else:
        cell.revealed = True
        if cell.value == 0:
            for r in range(row - 1, row + 2):
                for c in range(column - 1, column + 2):
                    if 0 <= r < rows and 0 <= c < columns and not cells[r][c].revealed:
                        reveal_cell(r, c)
        cell.button.configure(
            text=str(cell.value),
            fg=VALUE_COLORS.get(cell.value, "black"),
        )
    if check_win():
        label_name.config(text="Congratulations!!!")

def check_win():
    global game_state
    if game_state == "game_over":
        return False
    for row in range(rows):
        for column in range(columns):
            if not cells[row][column].revealed and cells[row][column].value != -1:
                return False
    game_state = "win"
    delete_saved_game()
    return True

def restart():
    global label_name, name, cells, game_state
    for row in cells:
        for cell in row:
            cell.button.pack_forget()
            cell.button.destroy()
    cells = []
    game_state = "playing"
    label_name.configure(text=f"Try Again, {name.capitalize()}")
    generate_board()

label = Label(window, text="Enter your name:")
label.pack()
entry = Entry(window)
entry.pack()
button_start = Button(window, text="Start", command=get_name)
button_start.pack()

window.mainloop()
