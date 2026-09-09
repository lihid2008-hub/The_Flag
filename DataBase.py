import csv
import os
import pandas as pd


# df = pd.read_csv('data.csv')
# print(df.to_string())

csv_file_path = "windows.csv"

def open_new_file():
    if os.path.exists(csv_file_path):
        os.remove(csv_file_path)

    with open(csv_file_path, "wb") as csvfile:
        csvfile.close()


def draw_one(game_state):
    pass

def save_in_one(game_state):
    print("save in one")
    with open(csv_file_path, "w") as file:
        writer = csv.writer(file)
        writer.writerow(game_state["soldier_location"])


def draw_two(game_state):
    pass


def save_in_two(game_state):
    pass


def draw_three(game_state):
    pass

def save_in_three(game_state):
    pass


def save_in_four(game_state):
    pass


def draw_four(game_state):
    pass


def save_in_five(game_state):
    pass


def draw_five(game_state):
    pass


def save_in_six(game_state):
    pass


def draw_six(game_state):
    pass


def save_in_seven(game_state):
    pass


def draw_seven(game_state):
    pass


def save_in_eight(game_state):
    pass


def draw_eight(game_state):
    pass


def save_in_nine(game_state):
    pass


def draw_nine(game_state):
    pass
