from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox
from .. import Redirect
from ..View.connector import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame8")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def loginWindow():
    Login()

class Login(Toplevel):
    def getUserID():
        return userID
    def __init__(self, *args, **kwargs):
        def getDetails(self):
            global userID
            print("Login button clicked")
            userID = self.userIDEntry.get()
            userName = self.nameEntry.get()
            password = self.passwordEntry.get()
            if userID == "0" and userName == "admin" and password == "admin":
                self.destroy()
                Redirect.goSelection()
            testEmpty(userID, userName, password)
            user = checkuserName(userID, userName)
            passw = checkPassword(userID, password)
            if user and passw:
                self.destroy()
                Redirect.gouserSelection()
            else:
                messagebox.showwarning("Invalid username or password", "Please enter the correct credentials!\n Or sign up if you haven't!")
            
        
        def testEmpty(a,b,c):
            if a == "" or b == "" or c == "":
                messagebox.showinfo("Error", "Please fill in all the fields")
                return
            else:
                return

        def handle_button_press(btn_name, self):
            if btn_name == "Signup":
                self.destroy()
                Redirect.goSignup()
            elif btn_name == "Forgor":
                user = self.nameEntry.get()
                password, UserID = forgotPassword(user)
                messagebox.showinfo("Forgot Password", f"Here is your login credentials: \n\nUserID: {UserID} \nusername: {user} \npassword: {password}")

        

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

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handle_button_press("Signup", self),
            relief="flat"
        )
        self.button_2.place(
            x=608.0,
            y=454.0,
            width=84.0,
            height=24.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handle_button_press("Forgor", self),
            relief="flat"
        )
        self.button_3.place(
            x=608.0,
            y=525.0,
            width=84.0,
            height=24.0
        )
        self.canvas.create_text(
            492.0,
            194.0,
            anchor="nw",
            text="Username: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            701.5,
            208.5,
            image=entry_image_1
        )
        self.nameEntry = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.nameEntry.place(
            x=596.0,
            y=194.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            493.0,
            239.0,
            anchor="nw",
            text="Password:",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            701.5,
            253.5,
            image=entry_image_2
        )
        self.passwordEntry = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            show="*"
        )
        self.passwordEntry.place(
            x=596.0,
            y=239.0,
            width=211.0,
            height=27.0
        )
    
        self.canvas.create_text(
            522.0,
            149.0,
            anchor="nw",
            text="UserID:",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            701.5,
            163.5,
            image=entry_image_3
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
            y=149.0,
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

        self.canvas.create_text(
            579.0,
            428.0,
            anchor="nw",
            text="Dont have an account?",
            fill="#000000",
            font=("Encode Sans SC", 13 * -1)
        )

        self.canvas.create_text(
            592.0,
            500.0,
            anchor="nw",
            text="Forgot password?",
            fill="#000000",
            font=("Encode Sans SC", 13 * -1)
        )

        # self.bind("<Return>", getDetails(self))

        self.resizable(False, False)
        self.mainloop()
