from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = 0
timer = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global check, timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text_label.config(text="Timer", fg=GREEN)
    checkMark.config(text="")
    reps = 0
    check = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        text_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        text_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        text_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global check
    count_min = math.floor(count / 60)
    count_sec = round(count % 60)

    if 0 <= count_sec < 10:
        # count_sec = "0" + str(count_sec)
        count_sec = f"0{count_sec}"

    if 0 <= count_min < 10:
        # count_min = "0" + str(count_min)
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        c = "✔"
        if reps % 2 == 0:
            check += 1
            if check == 4:
                checkMark.config(text="")
                check = 0
            else:
                checkMark.config(text=c * check)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# pomodoro means tomato in italian.
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

text_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"))
text_label.config(fg=GREEN, bg=YELLOW)
text_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", width=7, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=7, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkMark = Label(font=(FONT_NAME, 20, "bold"), highlightthickness=0)
checkMark.config(fg=GREEN, bg=YELLOW)
checkMark.grid(column=1, row=3)

window.mainloop()
