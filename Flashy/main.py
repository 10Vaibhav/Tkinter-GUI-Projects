from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
list_of_dict_to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    list_of_dict_to_learn = original_data.to_dict(orient="records")
else:
    list_of_dict_to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(list_of_dict_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    window.after(3000, func=flip_card)


def known():
    list_of_dict_to_learn.remove(current_card)
    print(len(list_of_dict_to_learn))
    data1 = pandas.DataFrame(list_of_dict_to_learn)
    data1.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_img)


window = Tk()
window.title("Flashy")
window.minsize(width=900, height=700)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="", fill="black")
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"), text="", fill="black")
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known)
right_button.grid(column=1, row=2)

next_card()

window.mainloop()
