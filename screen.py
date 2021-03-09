from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk
import pygame

# this will be the top-level program, rename to main.py

# Reference Links:
# resizing the image to scalr to screen: https://stackoverflow.com/questions/24061099/tkinter-resize-background-image-to-window-size (how do you put buttons on top of that?)
# playing the sound: https://stackoverflow.com/questions/44472162/how-do-play-audio-playsound-in-background-of-python-script
# placing the image behind the buttons: https://stackoverflow.com/questions/15795916/image-behind-buttons-in-tkinter-photoimage
# no way to create a rounded button other than creating an image of the button and then putting it in the button
# how to open up a new top-level window: https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/
# how to create a text box in tkinter: https://codeloop.org/how-to-create-textbox-in-python-tkinter/, http://www.pythonlake.com/tkinterentrygrid

class Player:
    def __init__(self, name):
        self.name = name

def start_up():
    root = Tk()
    root.title("Yahtzee Deluxe")
    list_of_names = []

    # music plays when the screen opens, do this until all of the players have been selected
    def initialize_music():
        pygame.mixer.init()
        pygame.mixer.music.load('yahtzee_music.mp3')
        pygame.mixer.music.play(999)

    # can enter up to four players
    def give_names():
        # function within a function so that the necessary variables are still in scope
        def submit_names():
            name_1 = first_entry.get()
            if name_1 and not name_1.isspace():
                list_of_names.append(name_1)
            name_2 = second_entry.get()
            if name_2 and not name_2.isspace():
                list_of_names.append(name_2)
            name_3 = third_entry.get()
            if name_3 and not name_3.isspace():
                list_of_names.append(name_3)
            name_4 = fourth_entry.get()
            if name_4 and not name_4.isspace():
                list_of_names.append(name_4)
            root.quit()

        # setup
        new_window = Toplevel(root)
        new_window.title("Enter player names")
        new_window.geometry("300x150")
        universal_font = Font(family="Times New Roman", size=12)

        # first player
        first_label = Label(new_window, text="Player #1", font=universal_font)
        first_label.grid(row=0)
        first_name = StringVar()
        first_entry = ttk.Entry(new_window, textvariable=first_name)
        first_entry.grid(row=0, column=1)

        # second player
        second_label = Label(new_window, text="Player #2", font=universal_font)
        second_label.grid(row=1)
        second_name = StringVar()
        second_entry = ttk.Entry(new_window, textvariable=second_name)
        second_entry.grid(row=1, column=1)

        # third player
        third_label = Label(new_window, text="Player #3", font=universal_font)
        third_label.grid(row=2)
        third_name = StringVar()
        third_entry = ttk.Entry(new_window, textvariable=third_name)
        third_entry.grid(row=2, column=1)

        # fourth player
        fourth_label = Label(new_window, text="Player #4", font=universal_font)
        fourth_label.grid(row=3)
        fourth_name = StringVar()
        fourth_entry = ttk.Entry(new_window, textvariable=fourth_name)
        fourth_entry.grid(row=3, column=1)

        # submit button
        submit_button = Button(new_window, text="Submit", command=submit_names, font=universal_font)
        submit_button.grid(row=4, column=1)

    image = Image.open('yahtzee_pic.png')
    image = image.resize((1200,800))
    image = ImageTk.PhotoImage(image)
    canvas = Canvas(width=1200, height=800)
    canvas.create_image(600, 400, image=image)
    canvas.pack()
    font = Font(family="Times New Roman", size=50, weight="bold")
    open_game_button = Button(root, text="PLAY", bg="red", fg="orange", font=font, command=give_names, anchor="center", relief=GROOVE, activeforeground="orange")
    open_game_button_window = canvas.create_window(50, 620, anchor='nw', window=open_game_button)
    initialize_music()

    root.mainloop()
    return list_of_names

list_of_names = start_up()
list_of_players = []
for name in list_of_names:
    list_of_players.append(Player(name))
for player in list_of_players:
    print(player.name)
