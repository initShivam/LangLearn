from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data  =  pandas.read_csv(r"C:\Users\SHIVAM SINHG\Desktop\100DaysofCode\flash-card-project-start\data\English_Hindi_Vocabulary.csv")
except:
    original_data = pandas.read_csv(r"C:\Users\SHIVAM SINHG\Desktop\100DaysofCode\flash-card-project-start\data\English_Hindi_Vocabulary.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    
current_card= {}

def next_card():
    global current_card, flip
    window.after_cancel(flip)
    current_card= random.choice(to_learn)
    canvas.itemconfig(card_title, text="Hindi", font=("Ariel", 40, "italic"), fill="black")
    canvas.itemconfig(card_word, text=current_card["Hindi"])
    canvas.itemconfig(card_background, image=card_front_img)
    flip = window.after(3000, func=flip_card)  


def flip_card():
      canvas.itemconfig(card_title, text="English", font=("Ariel", 40, "italic"), fill="White")
      canvas.itemconfig(card_word, text=current_card["English"])
      canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(r"C:\Users\SHIVAM SINHG\Desktop\100DaysofCode\flash-card-project-start\data\words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
flip = window.after(3000, func=flip_card)

window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

window.config(bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file=r"C:\Users\SHIVAM SINHG\Desktop\100DaysofCode\flash-card-project-start\images\card_front.png")
card_back_img = PhotoImage(file=r"C:\Users\SHIVAM SINHG\Desktop\100DaysofCode\flash-card-project-start\images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

card_title  = canvas.create_text(400, 150, text="Hindi", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "italic"), fill="black")

cross_img = PhotoImage(file=r"C:\Users\SHIVAM SINHG\Desktop\100DaysofCode\flash-card-project-start\images\wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0,command=next_card)
cross_button.grid(column=0, row=1)
check_img = PhotoImage(file=r"C:\Users\SHIVAM SINHG\Desktop\100DaysofCode\flash-card-project-start\images\right.png")
check_button = Button(image=check_img, highlightthickness=0, command=is_known)
check_button.grid(column=1, row=1)

next_card()
window.mainloop()