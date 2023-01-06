from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from .. import Redirect
from ..View.connector import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame8")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def loginWindow():
    Login()

class Login(Toplevel):
    def __init__(self, *args, **kwargs):
        def getDetails(self):
            print("Continue button clicked")
            userName = self.entry_1.get()
            password = self.entry_2.get()
            if userName == "admin" and password == "admin":
                self.destroy()
                Redirect.goSelection()
            elif password == "user":
                self.destroy()
                Redirect.gouserView()
            else:
                pass

        Toplevel.__init__(self, *args, **kwargs)
        self.title("Evenementiel Login Menu")
        self.geometry("853x556")

        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 556,
            width = 853,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            853.0,
            556.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            501.0,
            853.0,
            556.0,
            fill="#FF7A00",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: getDetails(self),
            relief="sunken",
            bg = "#FFFFFF",
            activebackground="#FFFFFF",
            activeforeground="#FFFFFF",
            cursor="hand2"
        )
        self.button_1.place(
            x=526.0,
            y=357.0,
            width=247.0,
            height=57.0
        )

        self.canvas.create_text(
            492.0,
            155.0,
            anchor="nw",
            text="Username: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        self.canvas.create_text(
            493.0,
            239.0,
            anchor="nw",
            text="Password:",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            701.5,
            169.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=596.0,
            y=155.0,
            width=211.0,
            height=27.0
        )
        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            701.5,
            253.5,
            image=entry_image_2
        )
        self.entry_2 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            show="*"
        )
        self.entry_2.place(
            x=596.0,
            y=239.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            441.0,
            556.0,
            fill="#FF9D43",
            outline="")

        self.canvas.create_text(
            73.0,
            208.0,
            anchor="nw",
            text="Welcome to\nEvenementiel",
            fill="#FFFFFF",
            font=("Encode Sans SC", 44 * -1)
        )
        self.resizable(False, False)
        self.mainloop()
