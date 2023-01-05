from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from ...Selection.mainSelection import selectionWindow


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def successfulWindow():
    Success()

class Success(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.title("Successfully added into database")
        self.geometry("853x556")
        self.configure(bg = "#FFFFFF")
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
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            426.0,
            278.0,
            image=image_image_1
        )

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
            command=lambda: self.handle_button_press(),
            relief="flat"
        )
        self.button_1.place(
            x=303.0,
            y=278.0,
            width=247.0,
            height=57.0
        )

        self.canvas.create_rectangle(
            113.0,
            75.0,
            744.0,
            147.0,
            fill="#DB8709",
            outline="")

        self.canvas.create_text(
            126.0,
            87.0,
            anchor="nw",
            text="Successfully created a new event!",
            fill="#FFFFFF",
            font=("Encode Sans SC", 36 * -1)
        )
        self.resizable(False, False)
        self.mainloop()
    def handle_button_press(self):
        print("Continue button clicked")
        self.destroy()
        selectionWindow()
        return