from pathlib import Path
from tkinter import *
from tkinter.ttk import Treeview
from .connector import *
from .. import Redirect
from ..Login import Login

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
            elif tableName == "Purchase":
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
            elif btn_name == "Purchase":
                print("Purchase pressed")
                self.columns = {
                    "PurchaseID": ["PurchaseID", 70],
                    "Name": ["Name", 70],
                    "Ticket Type": ["Ticket Type", 70],
                    "Ticket Status": ["Ticket Status", 70],
                    "Event Name": ["Event Name", 70],
                    "Location": ["Location", 70],
                    "Date": ["Date", 70],
                    "Time": ["Time", 66],
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
                Redirect.gouserSelection()
                return

        def handleID():
            pid = Login.Login.getuserID()
            sql = "SELECT p.PurchaseID, u.firstName, t.TicketType, s.TicketStatus, e.EventName, e.Location, e.Date, e.Time FROM Purchase p JOIN UserInfo u ON p.UserID = u.UserID JOIN Tickets t ON p.TicketID = t.TicketID JOIN Event e ON e.EventID = p.EventID JOIN TicketStatus s ON t.TicketStatusID = s.TicketStatusID WHERE p.UserID = %s"
            value = (pid,)
            cursor.execute(sql, value)
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


        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handle_button_press("Purchase", self),
            relief="sunken",
            bg = '#FF7A00',
            cursor = 'hand2',
            activebackground='#FF7A00',
            activeforeground='#FF7A00',
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
            activebackground='#FF7A00',
            activeforeground='#FF7A00',
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
            activebackground='#FF7A00',
            activeforeground='#FF7A00',
        )
        self.button_4.place(
            x=22.0,
            y=49.0,
            width=234.0,
            height=47.0
        )


        self.resizable(False, False)
        self.mainloop()
