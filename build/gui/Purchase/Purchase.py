from pathlib import Path
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from .. import Redirect
from ..Login import Login
from ..View.connector import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def purchaseWindow():
    Purchase()

class Purchase(Toplevel):
    def __init__(self, *args, **kwargs):
        def handle_btn_press(btn_name, self):
            if btn_name == "Purchase":
                PurchaseID = self.purchaseIDEntry.get()
                userID = Login.Login.getUserID()
                eventID = self.eventIDEntry.get()
                ticketID = self.ticketIDEntry.get()
                sql = "INSERT INTO Purchase VALUES(%s, %s, %s, %s)"
                values = (PurchaseID, userID, ticketID, eventID)
                cursor.execute(sql, values)
                connect.commit()
                messagebox.showinfo("Successful!", "You have successfully ordered a ticket!")
            elif btn_name == "Back":
                self.destroy()
                Redirect.gouserSelection()

        def clearRecord():
            self.timeEntry.delete(0, END)
            self.dateEntry.delete(0, END)
            self.locationEntry.delete(0, END)
            self.eventNameEntry.delete(0, END)
            self.eventIDEntry.delete(0, END)
            self.typeEntry.delete(0, END)
            self.ticketIDEntry.delete(0, END)
            self.purchaseIDEntry.delete(0, END)

        def selectRecord(e):
            clearRecord()

            selected = treeview.focus()
            values = treeview.item(selected, 'values')

            self.timeEntry.insert(0, values[6])
            self.timeEntry.configure(state='readonly')
            self.dateEntry.insert(0, values[5])
            self.dateEntry.configure(state='readonly')
            self.locationEntry.insert(0, values[4])
            self.locationEntry.configure(state='readonly')
            self.eventNameEntry.insert(0, values[3])
            self.eventNameEntry.configure(state='readonly')
            self.eventIDEntry.insert(0, values[2])
            self.eventIDEntry.configure(state='readonly')
            self.typeEntry.insert(0, values[1])
            self.typeEntry.configure(state='readonly')
            self.ticketIDEntry.insert(0, values[0])
            self.ticketIDEntry.configure(state='readonly')

            print("Selected")

        Toplevel.__init__(self, *args, **kwargs)
        self.title("Evenementiel Purchasing Tickets")
        self.geometry("853x556")

        self.canvas = Canvas(self, bg = "#FFFFFF", height = 556, width = 853,bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        columns = {"Ticket ID": ["Ticket ID", 50],"Ticket Type": ["Ticket Type", 70],"Event ID": ["Event ID", 50],"Event Name": ["Event Name", 100],"Location": ["Location", 100],"Date": ["Date", 70],"Time": ["Time", 46]}

        treeview = Treeview(
            self.canvas,
            columns=list(columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
        )

        def display():
            for idx, txt in columns.items():
                treeview.heading(idx, text=txt[0])
                treeview.column(idx, width=txt[1])

            treeview.place(x=13.0, y=58.0, width=490.0, height=358.0)
            treeview.delete(*treeview.get_children())
            event_data = getPurchase()
            for row in event_data:
                treeview.insert("", "end", values=row)

        display()
        treeview.bind("<Double-1>", selectRecord)


        self.canvas.create_rectangle(0.0,501.0,853.0,556.0,fill="#FF7A00",outline="")

        self.canvas.create_rectangle(43.0,0.0,896.0,80.0,fill="#FF7A00",outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(self.canvas,image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: handle_btn_press("Purchase", self),relief="flat")
        self.button_1.place(x=696.0,y=430.0,width=119.0,height=46.0)

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(self.canvas,image=button_image_2,borderwidth=0,highlightthickness=0,command=lambda: handle_btn_press("Back", self),relief="flat")
        self.button_2.place(x=558.0,y=430.0,width=119.0,height=46.0)

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(757.5,364.5,image=entry_image_1)
        self.timeEntry = Entry(self.canvas,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.timeEntry.place(x=679.0,y=350.0,width=157.0,height=27.0)

        self.canvas.create_text(535.0,352.0,anchor="nw",text="Time: ",fill="#000000",font=("Encode Sans SC", 19 * -1))

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(757.5,327.5,image=entry_image_2)
        self.dateEntry = Entry(self.canvas, bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.dateEntry.place(x=679.0,y=313.0,width=157.0,height=27.0)

        self.canvas.create_text(535.0,315.0,anchor="nw",text="Date: ",fill="#000000",font=("Encode Sans SC", 19 * -1))

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(757.5,290.5,image=entry_image_3)
        self.locationEntry = Entry(self.canvas,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.locationEntry.place(x=679.0,y=276.0,width=157.0,height=27.0)

        self.canvas.create_text(535.0,276.0,anchor="nw",text="Location:",fill="#000000",font=("Encode Sans SC", 19 * -1))

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(757.5,254.5,image=entry_image_4)
        self.eventNameEntry = Entry(self.canvas,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.eventNameEntry.place(x=679.0,y=240.0,width=157.0,height=27.0)

        self.canvas.create_text(535.0,242.0,anchor="nw",text="Event Name:",fill="#000000",font=("Encode Sans SC", 19 * -1))

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(757.5,219.5,image=entry_image_5)
        self.eventIDEntry = Entry(self.canvas,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.eventIDEntry.place(x=679.0,y=205.0,width=157.0,height=27.0)

        self.canvas.create_text(536.0,206.0,anchor="nw",text="EventID:",fill="#000000",font=("Encode Sans SC", 19 * -1))

        entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        entry_bg_6 = self.canvas.create_image(757.0,183.5,image=entry_image_6)
        self.typeEntry = Entry(self.canvas,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.typeEntry.place(x=679.0,y=169.0,width=156.0,height=27.0)

        self.canvas.create_text(535.0,169.0,anchor="nw",text="Ticket Type:",fill="#000000",font=("Encode Sans SC", 19 * -1))

        entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_7.png"))
        entry_bg_7 = self.canvas.create_image(757.0,146.5,image=entry_image_7)
        self.ticketIDEntry = Entry(self.canvas,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.ticketIDEntry.place(x=679.0,y=132.0,width=156.0,height=27.0)

        self.canvas.create_text(535.0,132.0,anchor="nw",text="TicketID: ",fill="#000000",font=("Encode Sans SC", 19 * -1))

        entry_image_8 = PhotoImage(
            file=relative_to_assets("entry_8.png"))
        entry_bg_8 = self.canvas.create_image(757.5,108.5,image=entry_image_8)
        self.purchaseIDEntry = Entry(self.canvas, bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.purchaseIDEntry.place(x=679.0,y=94.0,width=157.0,height=27.0)

        self.canvas.create_text(535.0,96.0,anchor="nw",text="PurchaseID: ",fill="#000000",font=("Encode Sans SC", 19 * -1))

        self.canvas.create_rectangle(0.0,0.0,514.0,556.0,fill="#FF9D43",outline="")

        self.canvas.create_rectangle(
            13.0,
            58.0,
            503.0,
            416.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            625.0,
            17.0,
            anchor="nw",
            text="Tickets",
            fill="#000000",
            font=("Encode Sans SC", 37 * -1)
        )

        x = getnextpurchaseID()
        self.purchaseIDEntry.insert(0, x)
        self.purchaseIDEntry.configure(state='readonly')

        self.resizable(False, False)
        self.mainloop()
