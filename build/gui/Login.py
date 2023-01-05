from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from Selection import Selection
from Login import Login
from Participants import Participants
from Tickets import Tickets
from Position import Position


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame8")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("853x556")
window.configure(bg = "#FFFFFF")

def handle_button_press(btn_name):
    global current_window
    if btn_name == "selection":
        continue_button_clicked()
        current_window = Selection(window)

def continue_button_clicked():
    print("Continue button clicked")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 556,
    width = 853,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    853.0,
    556.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    0.0,
    501.0,
    853.0,
    556.0,
    fill="#FF7A00",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: handle_button_press("selection"),
    relief="sunken",
    bg = "#FFFFFF",
    activebackground="#FFFFFF",
    activeforeground="#FFFFFF",
    cursor="hand2"
)
button_1.place(
    x=526.0,
    y=357.0,
    width=247.0,
    height=57.0
)

canvas.create_text(
    492.0,
    155.0,
    anchor="nw",
    text="Username: ",
    fill="#000000",
    font=("Encode Sans SC", 19 * -1)
)

canvas.create_text(
    493.0,
    239.0,
    anchor="nw",
    text="Password:",
    fill="#000000",
    font=("Encode Sans SC", 19 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    701.5,
    169.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=596.0,
    y=155.0,
    width=211.0,
    height=27.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    701.5,
    253.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=596.0,
    y=239.0,
    width=211.0,
    height=27.0
)

canvas.create_rectangle(
    0.0,
    0.0,
    441.0,
    556.0,
    fill="#FF9D43",
    outline="")

canvas.create_text(
    73.0,
    208.0,
    anchor="nw",
    text="Welcome to\nEvenementiel",
    fill="#FFFFFF",
    font=("Encode Sans SC", 44 * -1)
)
window.resizable(False, False)
window.mainloop()
