from pathlib import Path
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from ..connector import *
from .. import Redirect


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def userWindow():
    User()

class User(Toplevel):
    def __init__(self, *args, **kwargs):
        def handle_button_press(btn_name, self):
            if btn_name == "Refresh":
                print("Refreshed")
                refresh()
            elif btn_name == "Edit":
                id = self.userIDEntry.get()
                firstname = self.firstEntry.get()
                lastname = self.lastEntry.get()
                testEmpty(id, firstname, lastname)
                sql = "UPDATE UserInfo SET UserID = %s, firstName = %s, lastName = %s WHERE UserID = %s"
                value = (id, firstname, lastname, id)
                cursor.execute(sql, value)
                connect.commit()
                refresh()
                print("Updated Database")
            elif btn_name == "Delete":
                removeRecord()
            elif btn_name == "Continue":
                self.destroy()
                Redirect.goSelection()
            elif btn_name == "Back":
                self.destroy()
                Redirect.goPurchase()

        def testEmpty(a,b,c):
            if a == "" or b == "" or c == "":
                messagebox.showinfo("Error", "Please fill in all the fields")
                return
            else:
                return

        def refresh():
            display()
            clearRecord()

        def clearRecord():
            self.lastEntry.delete(0, END)
            self.firstEntry.delete(0, END)
            self.userIDEntry.delete(0, END)

        def selectRecord(e):
            clearRecord()

            selected = treeview.focus()
            values = treeview.item(selected, 'values')

            self.lastEntry.insert(0, values[2])
            self.firstEntry.insert(0, values[1])
            self.userIDEntry.insert(0, values[0])
            self.userIDEntry.configure(state='readonly')

            print("Selected")

        def removeRecord():
            selected = treeview.focus()
            eid = treeview.item(selected, 'values')[0]
            sql = "DELETE FROM UserInfo WHERE UserID=%s"
            value = (eid,)
            cursor.execute(sql, value)
            connect.commit()
            treeview.delete(selected)
            refresh()
            print("Removed from Database")

        Toplevel.__init__(self, *args, **kwargs)
        self.title("Evenementiel Managing User Info")
        self.geometry("853x556")

        self.canvas = Canvas(self, bg = "#FFFFFF", height = 556, width = 853,bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        columns = {"User ID": ["User ID", 50],"First Name": ["First Name", 175],"Last Name": ["Last Name", 170]}

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

            treeview.place(x=20.0, y=62.0, width=400.0, height=358.0)
            treeview.delete(*treeview.get_children())
            event_data = getUserInfo()
            for row in event_data:
                treeview.insert("", "end", values=row)

        display()
        treeview.bind("<Double-1>", selectRecord)

        self.canvas.create_rectangle(0.0, 0.0, 853.0, 556.0, fill="#FFFFFF", outline="")

        self.canvas.create_rectangle(0.0, 501.0, 853.0, 556.0, fill="#FF7A00", outline="")

        self.canvas.create_rectangle(43.0,0.0,896.0,80.0,fill="#FF7A00",outline="")

        self.canvas.create_text(
            507.0,
            17.0,
            anchor="nw",
            text="UserInfo Table",
            fill="#000000",
            font=("Encode Sans SC", 37 * -1)
        )

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(self.canvas,image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: handle_button_press("Edit", self), relief="sunken", cursor="hand2")
        self.button_1.place( x=662.0, y=356.0, width=119.0, height=46.0)

        button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3 = Button(self.canvas,image=button_image_3,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Delete", self),relief="sunken", cursor="hand2")
        self.button_3.place(x=515.0,y=356.0, width=119.0, height=46.0)

        button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        self.button_4 = Button(self.canvas,image=button_image_4,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Continue", self),relief="sunken", cursor="hand2")
        self.button_4.place(x=722.0,y=418.0,width=119.0,height=46.0)

        button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.button_5 = Button(self.canvas,image=button_image_5,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Refresh", self),relief="sunken", cursor="hand2")
        self.button_5.place(x=589.0,y=418.0,width=119.0,height=46.0)

        button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        self.button_6 = Button(self.canvas,image=button_image_6,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Back", self),relief="sunken", cursor="hand2")
        self.button_6.place(x=456.0,y=418.0, width=119.0, height=46.0)

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            724.5,
            174.5,
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
            x=619.0,
            y=160.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            468.0,
            162.0,
            anchor="nw",
            text="UserID:",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            724.5,
            219.5,
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
            x=619.0,
            y=205.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            468.0,
            205.0,
            anchor="nw",
            text="First Name:",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            724.5,
            264.5,
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
            x=619.0,
            y=250.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            468.0,
            252.0,
            anchor="nw",
            text="Last Name:",
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

        self.canvas.create_rectangle(
            20.0,
            62.0,
            420.0,
            420.0,
            fill="#FFFFFF",
            outline="")
    
        self.resizable(False, False)
        self.mainloop()
