from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox, END
from .. import Redirect
from ..View.connector import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def hubWindow():
    Hub()

class Hub(Toplevel):
    def __init__(self, *args, **kwargs):
        def handle_button_press(name, self):
            if name == "Event":
                self.destroy()
                Redirect.goEvent()
            elif name == "Committees":
                self.destroy()
                Redirect.goCommittees()
            elif name == "Position":
                self.destroy()
                Redirect.goPosition()
            elif name == "Tickets":
                self.destroy()
                Redirect.goTickets()
            elif name == "TicketStatus":
                self.destroy()
                Redirect.goTicketStatus()
            elif name == "UserInfo":
                self.destroy()
                Redirect.goUserInfo()
            elif name == "Purchase":
                self.destroy()
                Redirect.goPurchased()
            elif name == "Salary":
                self.destroy()
                Redirect.goSalary()
            elif name == "Back":
                self.destroy()
                Redirect.goSelection()
        Toplevel.__init__(self, *args, **kwargs)
        self.title("Evenementiel Select Table Menu")
        self.geometry("853x556")
        self.canvas = Canvas(self,bg = "#FFFFFF",height = 556,width = 853,bd = 0,highlightthickness = 0,relief = "ridge")

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(0.0,0.0,853.0,556.0,fill="#FFFFFF",outline="")

        self.canvas.create_rectangle(0.0,0.0,853.0,84.0,fill="#FF9D43",outline="")

        self.canvas.create_rectangle(0.0,501.0,853.0,556.0,fill="#FF7A00",outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(self.canvas,image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("UserInfo", self),relief="sunken",activebackground="#FFFFFF",activeforeground="#FFFFFF",bg="#FFFFFF")
        self.button_1.place(x=187.0,y=400.0,width=203.0,height=69.0)

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(self.canvas,image=button_image_2,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Purchase", self),relief="sunken",activebackground="#FFFFFF",activeforeground="#FFFFFF",bg="#FFFFFF")
        self.button_2.place(x=597.0,y=299.0,width=203.0,height=69.0)

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(self.canvas,image=button_image_3,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("TicketStatus", self),relief="sunken",activebackground="#FFFFFF",activeforeground="#FFFFFF",bg="#FFFFFF")
        self.button_3.place(x=325.0,y=299.0,width=203.0,height=69.0)

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(self.canvas,image=button_image_4,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Tickets", self),relief="sunken",activebackground="#FFFFFF",activeforeground="#FFFFFF",bg="#FFFFFF")
        self.button_4.place(x=54.0,y=299.0,width=203.0,height=69.0)

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(self.canvas,image=button_image_5,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Committees", self),relief="sunken",activebackground="#FFFFFF",activeforeground="#FFFFFF",bg="#FFFFFF")
        self.button_5.place(x=597.0,y=200.0,width=203.0,height=69.0)

        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(self.canvas,image=button_image_6,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Position", self),relief="sunken",activebackground="#FFFFFF",activeforeground="#FFFFFF",bg="#FFFFFF")
        self.button_6.place(x=312.0,y=200.0,width=230.0,height=69.0)

        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(self.canvas,image=button_image_7,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Event", self),relief="sunken",activebackground="#FFFFFF",activeforeground="#FFFFFF",bg="#FFFFFF")
        self.button_7.place(x=54.0,y=200.0,width=203.0,height=69.0)

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(self.canvas,image=button_image_8,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Back", self),relief="sunken",activebackground="#FFFFFF",activeforeground="#FFFFFF",bg="#FFFFFF")
        self.button_8.place(x=223.0,y=42.0,width=405.0,height=75.0)

        button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        self.button_9 = Button(self.canvas,image=button_image_9,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Salary", self),relief="sunken",activebackground="#FFFFFF",activeforeground="#FFFFFF",bg="#FFFFFF")
        self.button_9.place(x=461.0,y=400.0,width=230.0,height=69.0)
        
        self.resizable(False, False)
        self.mainloop()
