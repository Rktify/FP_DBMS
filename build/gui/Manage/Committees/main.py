from pathlib import Path
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview, Combobox
from ..connector import *
from .. import Redirect


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def committeesWindow():
    Committees()

class Committees(Toplevel):
    def __init__(self, *args, **kwargs):
        def handle_button_press(btn_name, self):
            if btn_name == "Refresh":
                print("Refreshed")
                refresh()
            elif btn_name == "Add":
                committeesID = self.committeesIDEntry.get()
                name = self.nameEntry.get()
                eventID = self.eventIDEntry.get()
                posname = positiondropDown.get()
                positionID = getPositionID(posname)
                salaryID = self.salaryIDEntry.get()
                testEmpty(committeesID, name, positionID, eventID, salaryID)
                sql = "INSERT INTO Committees VALUES(%s, %s, %s, %s, %s);"
                value = (committeesID, name, positionID, eventID, salaryID)
                cursor.execute(sql, value)
                connect.commit()
                refresh()
            elif btn_name == "Edit":
                committeesID = self.committeesIDEntry.get()
                name = self.nameEntry.get()
                eventID = self.eventIDEntry.get()
                posname = positiondropDown.get()
                positionID = getPositionID(posname)
                salaryID = self.salaryIDEntry.get()
                testEmpty(committeesID, name, positionID, eventID, salaryID)
                sql = "UPDATE Committees SET CommitteesID = %s, Name = %s, PositionID = %s, EventID = %s, SalaryID = %s WHERE PositionID = %s"
                value = (committeesID, name, positionID, eventID, salaryID, committeesID)
                cursor.execute(sql, value)
                connect.commit()
                refresh()
                print("Updated Database")
            elif btn_name == "Delete":
                removeRecord()
            elif btn_name == "Back":
                self.destroy()
                Redirect.goHub()

        def testEmpty(a,b,c,d,e):
            if a == "" or b == "" or c == "" or d == "" or e == "":
                messagebox.showinfo("Error", "Please fill in all the fields")
                return
            else:
                return

        def refresh():
            display()
            clearRecord()

        def clearRecord():
            self.eventIDEntry.configure(state='normal')
            self.committeesIDEntry.configure(state='normal')
            self.eventIDEntry.delete(0, END)
            self.nameEntry.delete(0, END)
            self.committeesIDEntry.delete(0, END)
            self.salaryIDEntry.delete(0, END)

        def selectRecord(e):
            getdropdownList(self)
            self.committeesIDEntry.configure(state='normal')
            clearRecord()

            selected = treeview.focus()
            values = treeview.item(selected, 'values')
            positionID = values[2]
            positionName = getPositionName(positionID)
            options = getPositionlist()
            for i in range(len(options)):
                if positionName == options[i]:
                    positiondropDown.current(i)
            self.committeesIDEntry.insert(0, values[0])
            self.nameEntry.insert(0, values[1])
            self.eventIDEntry.insert(0, values[3])
            self.salaryIDEntry.insert(0, values[4])
            self.committeesIDEntry.configure(state='readonly')

            print("Selected")

        def selectdropRecord(e):
            posname = positiondropDown.get()
            posID = getPositionID(posname)

        def removeRecord():
            selected = treeview.focus()
            eid = treeview.item(selected, 'values')[0]
            sql = "DELETE FROM Committees WHERE CommitteesID=%s"
            value = (eid,)
            cursor.execute(sql, value)
            connect.commit()
            treeview.delete(selected)
            refresh()

        def getdropdownList(self):
            options = getPositionlist()
            positiondropDown["values"] = options
            positiondropDown.current(0)

        Toplevel.__init__(self, *args, **kwargs)
        self.title("Evenementiel Managing Committees")
        self.geometry("853x556")
        self.current_window = None

        self.canvas = Canvas(self, bg = "#FFFFFF", height = 556, width = 853,bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        columns = {"Committees ID": ["Committees ID", 95], "Name": ["Name", 100], "Position ID": ["Position ID", 60], "Event ID": ["Event ID", 45], "Salary ID": ["Salary ID", 60]}

        treeview = Treeview(
            self.canvas,
            columns=list(columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
        )

        positiondropDown = Combobox(self.canvas, postcommand = lambda: getdropdownList(self), state="readonly")

        def display():
            for idx, txt in columns.items():
                treeview.heading(idx, text=txt[0])
                treeview.column(idx, width=txt[1])

            treeview.place(x=20.0, y=62.0, width=400.0, height=358.0)
            positiondropDown.place(x=607.0, y=199.0, width=211.0, height=27.0)
            treeview.delete(*treeview.get_children())
            event_data = getCommittees()
            for row in event_data:
                treeview.insert("", "end", values=row)

        display()

        self.canvas.create_rectangle(0.0, 0.0, 853.0, 556.0, fill="#FFFFFF", outline="")

        self.canvas.create_rectangle(0.0, 501.0, 853.0, 556.0, fill="#FF7A00", outline="")

        self.canvas.create_rectangle(43.0,0.0,896.0,80.0,fill="#FF7A00",outline="")

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(self.canvas,image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: handle_button_press("Edit", self), relief="sunken", cursor="hand2")
        self.button_1.place( x=722.0, y=356.0, width=119.0, height=46.0)

        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(self.canvas, image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: handle_button_press("Add", self), relief="sunken", cursor="hand2")
        self.button_2.place( x=589.0, y=356.0, width=119.0, height=46.0)

        button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3 = Button(self.canvas,image=button_image_3,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Delete", self),relief="sunken", cursor="hand2")
        self.button_3.place(x=456.0,y=356.0, width=119.0, height=46.0)

        button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.button_5 = Button(self.canvas,image=button_image_5,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Refresh", self),relief="sunken", cursor="hand2")
        self.button_5.place(x=656.0,y=418.0,width=119.0,height=46.0)

        button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        self.button_6 = Button(self.canvas,image=button_image_6,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Back", self),relief="sunken", cursor="hand2")
        self.button_6.place(x=523.0,y=418.0, width=119.0, height=46.0)

        self.canvas.create_text(
            484.0,
            17.0,
            anchor="nw",
            text="Committees Table",
            fill="#000000",
            font=("Encode Sans SC", 37 * -1)
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

        self.canvas.create_text(
            465.0,
            117.0, #155
            anchor="nw",
            text="CommitteesID: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )
        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(711.5,304.5,image=entry_image_1)
        self.committeesIDEntry = Entry(self.canvas,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.committeesIDEntry.place(x=607.0,y=117.0,width=211.0,height=27.0)


        self.canvas.create_text(
            465.0,
            155.0,
            anchor="nw",
            text="Name: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(711.5,258.5,image=entry_image_2)
        self.nameEntry = Entry(self.canvas,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.nameEntry.place(x=606.0,y=155.0,width=211.0,height=27.0)

        self.canvas.create_text(
            465.0,
            247.0,
            anchor="nw",
            text="EventID: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )
        entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(712.5,167.5,image=entry_image_4)
        self.eventIDEntry = Entry(self.canvas,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.eventIDEntry.place(x=606.0,y=247.0,width=211.0,height=27.0)

        self.canvas.create_text(
            465.0, 290.0,
            anchor="nw",
            text="SalaryID: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(711.5,213.5,image=entry_image_3)
        self.salaryIDEntry = Entry(self.canvas,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.salaryIDEntry.place( x=606.0, y=290.0, width=211.0, height=27.0)
        
        self.canvas.create_text(
            465.0,
            199.0,
            anchor="nw",
            text="Position Name",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        treeview.bind("<Double-1>", selectRecord)
        positiondropDown.bind("<<ComboboxSelected>>", selectdropRecord)

        self.resizable(False, False)
        self.mainloop()
