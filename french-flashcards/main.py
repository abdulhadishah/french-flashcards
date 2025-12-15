import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# Load data
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

flip_timer = None

def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)

    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)

def is_known():
    """User knows the word → remove from list and go next"""
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------- UI ---------------- #
window = Tk()
window.title("French Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, bd=0, relief="flat", command=next_card)
cross_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, highlightthickness=0, bd=0, relief="flat", command=is_known)
check_button.grid(row=1, column=1)

next_card()
window.mainloop()
