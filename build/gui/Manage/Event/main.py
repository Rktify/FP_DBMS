from pathlib import Path
from tkinter import *
from tkinter.ttk import Treeview
from ..connector import *
from .. import Redirect


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def eventWindow():
    Event()

class Event(Toplevel):
    def __init__(self, *args, **kwargs):
        def handle_button_press(btn_name, self):
            if btn_name == "Refresh":
                print("Clicked")
                refresh()
            elif btn_name == "Add":
                time = self.entry_1.get()
                date = self.entry_2.get()
                location = self.entry_3.get()
                eventName = self.entry_4.get()
                eventID = self.entry_5.get()
                sql = "INSERT INTO Event VALUES(%s, %s, %s, %s, %s);"
                value = (eventID, eventName, location, date, time)
                cursor.execute(sql, value)
                connect.commit()
                refresh()
            elif btn_name == "Edit":
                pass
            elif btn_name == "Delete":
                removeRecord()
            elif btn_name == "Continue":
                self.destroy()
                Redirect.goCommittees()
            elif btn_name == "Back":
                self.destroy()
                Redirect.goSelection()

        def refresh():
            display()
            clearRecord()

        def clearRecord():
            self.entry_1.delete(0, END)
            self.entry_2.delete(0, END)
            self.entry_3.delete(0, END)
            self.entry_4.delete(0, END)
            self.entry_5.delete(0, END)

        def selectRecord(e):
            clearRecord()

            selected = treeview.focus()
            values = treeview.item(selected, 'values')

            self.entry_1.insert(0, values[4])
            self.entry_2.insert(0, values[3])
            self.entry_3.insert(0, values[2])
            self.entry_4.insert(0, values[1])
            self.entry_5.insert(0, values[0])

        def removeRecord():
            selected = treeview.focus()
            eid = treeview.item(selected, 'values')[0]
            sql = "DELETE FROM Event WHERE EventID=%s"
            value = (eid,)
            cursor.execute(sql, value)
            connect.commit()
            treeview.delete(selected)
            refresh()

        Toplevel.__init__(self, *args, **kwargs)
        self.title("Evenementiel Managing Events")
        self.geometry("853x556")
        self.current_window = None

        self.canvas = Canvas(self, bg = "#FFFFFF", height = 556, width = 853,bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        columns = {"Event ID": ["Event ID", 50],"Event Name": ["Event Name", 100],"Location": ["Location", 100],"Date": ["Date", 100],"Time": ["Time", 50]}

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
            event_data = getEvents()
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

        button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        self.button_4 = Button(self.canvas,image=button_image_4,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Continue", self),relief="sunken", cursor="hand2")
        self.button_4.place(x=722.0,y=418.0,width=119.0,height=46.0)

        button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.button_5 = Button(self.canvas,image=button_image_5,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Refresh", self),relief="sunken", cursor="hand2")
        self.button_5.place(x=589.0,y=418.0,width=119.0,height=46.0)

        button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        self.button_6 = Button(self.canvas,image=button_image_6,borderwidth=0,highlightthickness=0,command=lambda: handle_button_press("Back", self),relief="sunken", cursor="hand2")
        self.button_6.place(x=456.0,y=418.0, width=119.0, height=46.0)

        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(711.5,304.5,image=entry_image_1)
        self.entry_1 = Entry(self.canvas,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.entry_1.place(x=606.0,y=290.0,width=211.0,height=27.0)

        self.canvas.create_text(
            480.0,
            293.0,
            anchor="nw",
            text="Time: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            711.5,
            258.5,
            image=entry_image_2
        )
        self.entry_2 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=606.0,
            y=244.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            480.0,
            247.0,
            anchor="nw",
            text="Date: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            711.5,
            213.5,
            image=entry_image_3
        )
        self.entry_3 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=606.0,
            y=199.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            480.0,
            201.0,
            anchor="nw",
            text="Location: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            712.5,
            167.5,
            image=entry_image_4
        )
        self.entry_4 = Entry(self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=607.0,
            y=153.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            480.0,
            155.0,
            anchor="nw",
            text="Event Name:",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            711.5,
            121.5,
            image=entry_image_5
        )
        self.entry_5 = Entry(self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=606.0,
            y=107.0,
            width=211.0,
            height=27.0
        )

        self.canvas.create_text(
            480.0,
            109.0,
            anchor="nw",
            text="EventID: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        self.canvas.create_text(
            542.0,
            17.0,
            anchor="nw",
            text="Event Table",
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


        treeview.bind("<Double-1>", selectRecord)

        self.resizable(False, False)
        self.mainloop()
