from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from ..Create.Event.main import createWindow
from .. import main


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\build\gui\Selection\assets\frame7")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def selectionWindow():
    Selection()

class Selection(Toplevel):
    def handle_button_press(self, btn_name):
        # self.current_window = self.windows.get(btn_name)
        if btn_name == "View":
            print("View button clicked")
            self.destroy()
            main.goView()
            return
        elif btn_name == "Manage":
            print("Manage button clicked")
            self.destroy()
            manageWindow()
            return
        elif btn_name == "Create":
            print("Create button clicked")
            self.destroy()
            createWindow()
            return

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.title("Evenementiel Selection Menu")
        self.geometry("853x556")
        self.current_window = None

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

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command = lambda: self.handle_button_press("View") ,
            relief="sunken",
            cursor="hand2"
        )
        self.button_1.place(
            x=28.0,
            y=209.0,
            width=247.0,
            height=233.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command = lambda: self.handle_button_press("Manage"),
            relief="sunken",
            cursor="hand2"
        )
        self.button_2.place(
            x=303.0,
            y=209.0,
            width=247.0,
            height=233.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command = lambda: self.handle_button_press("Create"),
            relief="sunken",
            cursor="hand2"
        )
        self.button_3.place(
            x=578.0,
            y=209.0,
            width=247.0,
            height=233.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            853.0,
            84.0,
            fill="#FF9D43",
            outline="")

        self.canvas.create_rectangle(
            223.0,
            46.0,
            628.0,
            117.0,
            fill="#F8B475",
            outline="")

        self.canvas.create_text(
            238.0,
            26.0,
            anchor="nw",
            text="Evenementiel",
            fill="#000000",
            font=("Encode Sans SC", 57 * -1)
        )
        self.resizable(False, False)
        self.mainloop()





