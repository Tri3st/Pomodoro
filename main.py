from tkinter import *
from Clock import Clock
# ---------------------------- CONSTANTS ------------------------------- #
#cokors from Color Hunt
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def count_down():
  if not klk.is_time_up():
    
    canvas.itemconfig(clock_display, text=klk)
    klk.minus()
    window.after(1000, count_down)
  else:
    pass
    #AAAAALAAAARM
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

klk = Clock(WORK_MIN, 0)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(height=200, width=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
clock_display = canvas.create_text(100, 130, text=klk, fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

button_start = Button(text="Start", command=count_down)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset")
button_reset.grid(row=2, column=2)

check_label = Label(text="✔️", fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)




window.mainloop()