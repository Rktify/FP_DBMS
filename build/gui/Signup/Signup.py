from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox, END
from .. import Redirect
from ..View.connector import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def signupWindow():
    Signup()

class Signup(Toplevel):
    def __init__(self, *args, **kwargs):
        def getDetails(self):
            print("Signup button clicked")
            userID = self.userIDEntry.get()
            firstName = self.firstEntry.get()
            lastName = self.lastEntry.get()
            userName = self.userEntry.get()
            password = self.passwordEntry.get()
            x = checkuserAvailability(userName)
            if x:
                testEmpty(userID, firstName, lastName, userName, password)
                sql = "INSERT INTO UserInfo VALUES(%s, %s, %s, %s, %s)"
                value = (userID, firstName, lastName, userName, password)
                cursor.execute(sql, value)
                connect.commit()
                messagebox.showinfo("Successful!", "You have successfully signed up, please log in")
                self.destroy()
                Redirect.goLogin()
            else:
                messagebox.showwarning("Invalid Username!", "This username is already taken, please try again!")
                self.userEntry.delete(0, END)

        def testEmpty(a,b,c,d,e):
            if a == "" or b == "" or c == "" or d == "" or e == "":
                messagebox.showinfo("Error", "Please fill in all the fields")
                return
            else:
                return

        def handle_button_press(self):
            self.destroy()
            Redirect.goLogin()


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
            501.0,
            853.0,
            556.0,
            fill="#FF7A00",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            0.0,
            441.0,
            556.0,
            fill="#FF9D43",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: getDetails(self),
            relief="flat"
        )
        self.button_1.place(
            x=526.0,
            y=355.0,
            width=247.0,
            height=57.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handle_button_press(self),
            relief="flat"
        )
        self.button_2.place(
            x=608.0,
            y=454.0,
            width=84.0,
            height=24.0
        )

        self.canvas.create_text(
            73.0,
            208.0,
            anchor="nw",
            text="Sign up to\nEvenementiel",
            fill="#FFFFFF",
            font=("Encode Sans SC", 44 * -1)
        )

        self.canvas.create_text(
            569.0,
            428.0,
            anchor="nw",
            text="Already have an account?",
            fill="#000000",
            font=("Encode Sans SC", 13 * -1)
        )

        self.canvas.create_text(
            519.0,
            65.0,
            anchor="nw",
            text="UserID:",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            701.5,
            79.5,
            image=entry_image_1
        )
        self.userIDEntry = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.userIDEntry.place(
            x=596.0,
            y=65.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            485.0,
            138.0,
            anchor="nw",
            text="First Name: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            701.5,
            150.5,
            image=entry_image_2
        )
        self.firstEntry = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.firstEntry.place(
            x=596.0,
            y=136.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            489.0,
            182.0,
            anchor="nw",
            text="Last Name:",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            701.5,
            195.5,
            image=entry_image_3
        )
        self.lastEntry = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.lastEntry.place(
            x=596.0,
            y=181.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            492.0,
            228.0,
            anchor="nw",
            text="Username: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            701.5,
            240.5,
            image=entry_image_4
        )
        self.userEntry = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.userEntry.place(
            x=596.0,
            y=226.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            493.0,
            273.0,
            anchor="nw",
            text="Password:",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            701.5,
            285.5,
            image=entry_image_5
        )
        self.passwordEntry = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.passwordEntry.place(
            x=596.0,
            y=271.0,
            width=211.0,
            height=27.0
        )

        x = getnextuserID()
        self.userIDEntry.insert(0, x)
        self.userIDEntry.configure(state='readonly')

        self.resizable(False, False)
        self.mainloop()
