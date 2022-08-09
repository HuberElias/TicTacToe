# Imports
import os
from random import randint, randrange
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
mixer.init()

# Classes
class TTT_Button:
    def __init__(self, root, column, row) -> None:
        self.btn = Button(root, height="4", width="9", command=lambda: btn_on_press(self), border=0)
        self.btn.grid(column=column, row=row, padx=5, pady=5)
        self.img = None
        self.form = None
        self.isWinner = False

    
    def change_image(self):
        img = Image.open("./images/"+str(player)+".gif").resize((60, 60))
        self.img = ImageTk.PhotoImage(img)
        self.btn.config(image=self.img)
        self.btn.config(height=65, width=67)

    
    def disabled(self):
        mixer.music.load("./sounds/gnome-sound-effect.mp3")
        mixer.music.play()
    

    def after_win(self):
        pass


    def destroy(self):
        self.btn.destroy()
        self = None


    def __str__(self) -> str:
        return f"({self.btn.grid_info()['column']}|{self.btn.grid_info()['row']})"


# Vaiables
field: list[list[TTT_Button]] = list()
player = True  # True = X / False = O
forms = ("O", "X", "Draw!")
win_message = None
won = False
win_sounds = ["./sounds/mem-yippee-meme-sound.mp3",
              "./sounds/Super Mario Power Up Sound Effect.mp3",
              "./sounds/Ok I Pull Up Sound Effect.mp3",
              "./sounds/Okay let's go meme sound.mp3",
              "./sounds/Travis Scott Sound Effect.mp3",
              "./sounds/monke meme - sound effect.mp3",
              "./sounds/Moai sound.mp3.mp3"]


# Functions
def check_draw():
    global won
    global field
    for liste in field:
        for btn in liste:
            if btn.form is None:
                return None
    if not(won):
        win(2)


def handle_restart(root):
    global win_message
    global player
    global field
    global won
    won = False
    mixer.music.load("./sounds/echo-fart-sound-effect-no-copyright.mp3")
    mixer.music.play()
    for liste in field:
        for btn in liste:
            btn.destroy()
    field.clear()
    player = True
    if win_message is not None:
        win_message.destroy()
    win_message = None
    create_field(root)


def win(form):
    global win_message
    global forms
    global win_sounds

    # disable buttons
    for liste in field:
        for btn in liste:
            btn.btn.config(command=btn.after_win)
            if btn.isWinner:
                btn.btn.config(bg="pink")
    
    # Display win message
    if win_message is None:
        win_message = Label(root, font=("Arial", 30, "bold"), highlightthickness=3, highlightbackground="gray", width=8)
        win_message.grid(columnspan=3, row=1)
    if form == 2:
        win_message.config(text=forms[form])
        mixer.music.load("./sounds/poop-sound-effect.mp3")
        mixer.music.play()
    else:
        win_message.config(text=f"{forms[form]} wins!")
        mixer.music.load(win_sounds[randrange(0, len(win_sounds))])
        mixer.music.play()


def win_condition():
    global field
    global win_message
    global won
    # Horizantal
    if field[0][0].form == field[1][0].form == field[2][0].form and field[2][0].form is not None:
        field[0][0].isWinner, field[1][0].isWinner, field[2][0].isWinner = True, True, True
        won = True
        win(field[0][0].form)
    elif field[0][1].form == field[1][1].form == field[2][1].form and field[2][1].form is not None:
        field[0][1].isWinner, field[1][1].isWinner, field[2][1].isWinner = True, True, True
        won = True
        win(field[0][1].form)
    elif field[0][2].form == field[1][2].form == field[2][2].form and field[2][2].form is not None:
        field[0][2].isWinner, field[1][2].isWinner, field[2][2].isWinner = True, True, True
        won = True
        win(field[0][2].form)

    # Vertical
    elif field[0][0].form == field[0][1].form == field[0][2].form and field[0][2].form is not None:
        field[0][0].isWinner, field[0][1].isWinner, field[0][2].isWinner = True, True, True
        won = True
        win(field[0][0].form)
    elif field[1][0].form == field[1][1].form == field[1][2].form and field[1][2].form is not None:
        field[1][0].isWinner, field[1][1].isWinner, field[1][2].isWinner = True, True, True
        won = True
        win(field[1][0].form)
    elif field[2][0].form == field[2][1].form == field[2][2].form and field[2][2].form is not None:
        field[2][0].isWinner, field[2][1].isWinner, field[2][2].isWinner = True, True, True
        won = True
        win(field[2][0].form)

    # Diagonal
    elif field[0][0].form == field[1][1].form == field[2][2].form and field[2][2].form is not None:
        field[0][0].isWinner, field[1][1].isWinner, field[2][2].isWinner = True, True, True
        won = True
        win(field[0][0].form)
    elif field[2][0].form == field[1][1].form == field[0][2].form and field[0][2].form is not None:
        field[2][0].isWinner, field[1][1].isWinner, field[0][2].isWinner = True, True, True
        won = True
        win(field[2][0].form)   


def create_field(root):
    global field
    for x in range(3):
        field.append(list())
        for y in range(3):
            b = TTT_Button(root, x, y)
            field[x].append(b)


def btn_on_press(self: TTT_Button):
    global player
    mixer.music.load("./sounds/the-rock-eyebrow-raise-sound-effect.mp3")
    mixer.music.play()
    self.change_image()
    self.form = player
    self.btn.config(command=self.disabled)  # comment out this line for fun
    player = not(player)
    win_condition()
    check_draw()


# Main
root = Tk()
root.title("TikTakToe")
root.resizable(False, False)
root.config(bg="black", padx=20, pady=20)
os.system("CLS")

create_field(root)

restart = Button(root, text="Restart", width=11, font=("Ariabl", 25, "bold"), command=lambda: handle_restart(root))
restart.grid(columnspan=3, row=3, pady=(15, 0))

root.mainloop()
