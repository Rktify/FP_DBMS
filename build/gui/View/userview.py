from pathlib import Path
from tkinter import *
from tkinter.ttk import Treeview
from .connector import *
from .. import Redirect

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def userviewWindow():
    userView()

class userView(Toplevel):
    def __init__(self, *args, **kwargs):
        def handle_refresh(self, tableName):
            self.treeview.delete(*self.treeview.get_children())
            if tableName == "Events":
                self.event_data = getEvents()
            elif tableName == "Participants":
                self.event_data = handleID()
            elif tableName == "Tickets":
                self.event_data = getTicketss()
            for row in self.event_data:
                self.treeview.insert("", "end", values=row)
        def handle_button_press(btn_name, self):
            if btn_name == "Events":
                print("Events pressed")
                self.columns = {
                    "Event ID": ["Event ID", 100],
                    "Event Name": ["Event Name", 160],
                    "Location": ["Location", 100],
                    "Date": ["Date", 100],
                    "Time": ["Time", 96]
                }

                self.treeview = Treeview(
                    self,
                    columns=list(self.columns.keys()),
                    show="headings",
                    height=200,
                    selectmode="browse",
                )

                for idx, txt in self.columns.items():
                    self.treeview.heading(idx, text=txt[0])
                    self.treeview.column(idx, width=txt[1])

                self.treeview.place(x=265.0, y=80.0, width=560.0, height=300.0)
                handle_refresh(self, btn_name)
            elif btn_name == "Participants":
                print("Participants pressed")
                self.columns = {
                    "Name": ["Name", 80],
                    "Ticket ID": ["Ticket ID", 80],
                    "Ticket Status": ["Ticket Status", 80],
                    "Event Name": ["Event Name", 80],
                    "Location": ["Location", 80],
                    "Date": ["Date", 80],
                    "Time": ["Time", 76],

                }

                self.treeview = Treeview(
                    self,
                    columns=list(self.columns.keys()),
                    show="headings",
                    height=200,
                    selectmode="browse",
                )

                for idx, txt in self.columns.items():
                    self.treeview.heading(idx, text=txt[0])
                    self.treeview.column(idx, width=txt[1])

                self.treeview.place(x=265.0, y=80.0, width=560.0, height=300.0)
                handle_refresh(self, btn_name)
            elif btn_name == "Tickets":
                print("Tickets pressed")
                self.columns = {
                    "Ticket ID": ["Ticket ID", 50],
                    "Event Name": ["Event Name", 160],
                    "Price": ["Price", 100],
                    "Ticket Type": ["Ticket Type", 100],
                    "Status": ["Status", 96]
                }

                self.treeview = Treeview(
                    self,
                    columns=list(self.columns.keys()),
                    show="headings",
                    height=200,
                    selectmode="browse",
                )

                for idx, txt in self.columns.items():
                    self.treeview.heading(idx, text=txt[0])
                    self.treeview.column(idx, width=txt[1])

                self.treeview.place(x=265.0, y=80.0, width=560.0, height=300.0)
                handle_refresh(self, btn_name)

            elif btn_name == "Back":
                print("Back button clicked")
                self.destroy()
                Redirect.goLogin()
                return

        def handleID():
            pid = self.IDEntry.get()
            sql = "Select u.firstName, p.TicketID, s.TicketStatus, e.EventName, e.Location, e.Date, e.Time from Participants p join UserInfo u ON u.UserID = p.UserID join Event e ON e.EventID = p.EventID join Tickets t ON t.EventID = e.EventID join TicketStatus s ON t.TicketStatusID = s.TicketStatusID WHERE ParticipantsID = %s;"
            value = (pid,)
            cursor.execute(sql, value)
            self.IDEntry.delete(0, END)
            return cursor.fetchall()

        Toplevel.__init__(self, *args, **kwargs)
        self.title("Evenementiel User View")
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
            fill="#FF7A00",
            outline="")

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            545.0,
            278.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handle_button_press("Tickets", self),
            relief="sunken",
            bg = '#FF7A00',
            cursor = 'hand2',
        )
        self.button_1.place(
            x=22.0,
            y=357.0,
            width=234.0,
            height=47.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handle_button_press("Participants", self),
            relief="sunken",
            bg = '#FF7A00',
            cursor = 'hand2',
        )
        self.button_2.place(
            x=22.0,
            y=270.0,
            width=234.0,
            height=47.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handle_button_press("Events", self),
            relief="sunken",
            bg = '#FF7A00',
            cursor = 'hand2',
        )
        self.button_3.place(
            x=22.0,
            y=183.0,
            width=234.0,
            height=47.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handle_button_press("Back", self),
            relief="sunken",
            bg = '#FF7A00',
            cursor = 'hand2',
        )
        self.button_4.place(
            x=22.0,
            y=49.0,
            width=234.0,
            height=47.0
        )

        self.canvas.create_text(
            28.0,
            434.0,
            anchor="nw",
            text="Your ID: ",
            fill="#000000",
            font=("Encode Sans SC", 19 * -1)
        )

        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(130.5, 478.5, image=entry_image_1)
        self.IDEntry = Entry(self.canvas,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.IDEntry.place(x=27.0,y=467.0,width=211.0,height=27.0)

        self.resizable(False, False)
        self.mainloop()
