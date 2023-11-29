from tkinter import *
import random

root = Tk()
root.geometry("455x355+400+100")
root.title("Random Number Guessing Game")

Cnumber = random.randrange(1, 101)

def initialize_game():
    global Cnumber, attempt
    Cnumber = random.randrange(1, 101)
    result_label.config(text="Guess any number between 1-100.")
    entry.delete(0, 'end')  # Clear the entry field
    attempt = 0  # Reset the attempt counter

global attempt
attempt = 0

def guessnum():
    global attempt
    num = int(entry.get())
    attempt += 1
    if num == Cnumber:
        result_label.config(text=f"Congratulations...You have guessed the correct number!\nTotal Attempts = {attempt}")
    elif num > Cnumber:
        result_label.config(text="Please Guess any lower number..")
        entry.delete(0, 'end')
    elif num < Cnumber:
        result_label.config(text="Please Guess any higher number..")
        entry.delete(0, 'end')

# BACKGROUND COLORS
background = "#06283D"
button_color = "#EE0000"
activebackground = "#EE0000"

root.config(bg=background)

label = Label(root, text="Random Number Guessing Game", bg=background, fg="white", font="arial 15 bold").place(x=80, y=40)

# ENTRY INPUT
entry = Entry(root, width=25, border=5, relief=RIDGE)
entry.place(x=100, y=132)

# GUESS BUTTON
guess_button = Button(root, text="Guess", font="arial 12 ", bg=button_color, command=guessnum, activeforeground=activebackground).place(x=300, y=130)

result_label = Label(root, text="Guess any number between 1-100.", bg=background, fg="white", font="arial 12", wraplength=250)
result_label.place(x=230, y=210, anchor="center")

# PLAY AGAIN BUTTON
play_again_button = Button(root, text="Play Again", font="arial 12 ", bg=button_color, command=initialize_game,
                           activebackground=activebackground, width=10)
play_again_button.place(x=120, y=300)

exit_button = Button(root, text="Exit", command=quit, font="arial 12 ", background=button_color, width=10,
                      activebackground=activebackground).place(x=250, y=300)

root.mainloop()
