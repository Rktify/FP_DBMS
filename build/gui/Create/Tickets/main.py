from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
# from ..Successful.main import successfulWindow


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\build\gui\Create\Tickets\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def ticketsWindow():
    Tickets()

class Tickets(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.title("Evenementiel Adding Tickets")
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
            command=lambda: self.handle_button_press(),
            relief="flat"
        )
        self.button_1.place(
            x=533.0,
            y=390.0,
            width=247.0,
            height=57.0
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            713.5,
            288.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=608.0,
            y=274.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            468.0,
            276.0,
            anchor="nw",
            text="TicketStatusID: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            713.5,
            242.5,
            image=entry_image_2
        )
        entry_2 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=608.0,
            y=228.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            468.0,
            231.0,
            anchor="nw",
            text="Price: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            713.5,
            196.5,
            image=entry_image_3
        )
        entry_3 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=608.0,
            y=182.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            468.0,
            184.0,
            anchor="nw",
            text="Type: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            712.5,
            151.5,
            image=entry_image_4
        )
        entry_4 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_4.place(
            x=607.0,
            y=137.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            468.0,
            139.0,
            anchor="nw",
            text="EventID:",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            712.5,
            105.5,
            image=entry_image_5
        )
        entry_5 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_5.place(
            x=607.0,
            y=91.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            468.0,
            93.0,
            anchor="nw",
            text="TicketID: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
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
            text="Ticket\nTable",
            fill="#FFFFFF",
            font=("Encode Sans SC", 44 * -1)
        )
        self.resizable(False, False)
        self.mainloop()
    def handle_button_press(self):
        print("Continue button clicked")
        self.destroy()
        # successfulWindow()
        return
