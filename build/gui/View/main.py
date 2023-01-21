from pathlib import Path
from tkinter import *
from tkinter.ttk import Treeview
from .connector import *
from .. import Redirect

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\Viewassets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def viewWindow():
    View()

class View(Toplevel):
    def __init__(self, *args, **kwargs):
        def handle_refresh(self, tableName):
            self.treeview.delete(*self.treeview.get_children())
            if tableName == "Events":
                self.event_data = getEvents()
            elif tableName == "UserInfo":
                self.event_data = getUserInfo()
            elif tableName == "Purchase":
                self.event_data = getPurchased()
            elif tableName == "Positions":
                self.event_data = getPositions()
            elif tableName == "Committees":
                self.event_data = getCommittees()
            elif tableName == "Tickets":
                self.event_data = getTickets()
            elif tableName == "TicketStatus":
                self.event_data = getTicketStats()
            for row in self.event_data:
                self.treeview.insert("", "end", values=row)
        def handle_button_press(btn_name, self):
            if btn_name == "Events":
                print("Events pressed")
                self.columns = {
                    "Event ID": ["Event ID", 100],
                    "Event Name": ["Event Name", 100],
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

                self.treeview.place(x=295.0, y=80.0, width=500.0, height=300.0)
                handle_refresh(self, btn_name)

            elif btn_name == "Committees":
                print("Committees pressed")
                self.columns = {
                    "Committees ID": ["Committees ID", 100],
                    "Name": ["Name", 200],
                    "Position ID": ["Position ID", 100],
                    "Event ID": ["Event ID", 96]
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

                self.treeview.place(x=295.0, y=80.0, width=500.0, height=300.0)
                handle_refresh(self, "Committees")

            elif btn_name == "Purchase":
                print("Purchase pressed")
                self.columns = {
                    "Purchase ID": ["Purchase ID", 100],
                    "UserID": ["UserID", 200],
                    "Ticket ID": ["Ticket ID", 100],
                    "Event ID": ["Event ID", 96]
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

                self.treeview.place(x=295.0, y=80.0, width=500.0, height=300.0)
                handle_refresh(self, btn_name)

            elif btn_name == "Positions":
                print("Position pressed")
                self.columns = {
                    "Position ID": ["Position ID", 100],
                    "Name": ["Name", 200],
                    "Salary": ["Salary", 100],
                    "Event ID": ["Event ID", 96]
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

                self.treeview.place(x=295.0, y=80.0, width=500.0, height=300.0)
                handle_refresh(self, btn_name)

            elif btn_name == "Tickets":
                print("Tickets pressed")
                self.columns = {
                    "Ticket ID": ["Ticket ID", 150],
                    "Event ID": ["Event ID", 100],
                    "Ticket Type": ["Ticket Type", 100],
                    "Status ID": ["Status ID", 96]
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

                self.treeview.place(x=295.0, y=80.0, width=500.0, height=300.0)
                handle_refresh(self, btn_name)

            elif btn_name == "TicketStats":
                print("Tickets Status pressed")
                self.columns = {
                    "Ticket Status ID": ["Ticket Status ID", 250],
                    "Ticket Status": ["Ticket Status", 246]
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

                self.treeview.place(x=295.0, y=80.0, width=500.0, height=300.0)
                handle_refresh(self, btn_name)

            elif btn_name == "UserInfo":
                print("UserInfo pressed")
                self.columns = {
                    "User ID": ["User ID", 60],
                    "First Name": ["First Name", 190],
                    "Last Name": ["Last Name", 176],
                    "Username": ["Username", 70]
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

                self.treeview.place(x=295.0, y=80.0, width=500.0, height=300.0)
                handle_refresh(self, btn_name)

            elif btn_name == "Home":
                print("Home button clicked")
                self.destroy()
                Redirect.goSelection()
                return

        #View tkinter
        Toplevel.__init__(self, *args, **kwargs)
        self.title("Evenementiel Viewing Menu")
        self.geometry("853x556")
        self.current_window = None

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

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handle_button_press("UserInfo", self),
            relief="sunken",
            bg = '#FF7A00',           
            cursor = 'hand2',
            activebackground='#FF7A00',
            activeforeground='#FF7A00'
        )
        self.button_1.place(
            x=22.0,
            y=143.0,
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
            command=lambda: handle_button_press("TicketStats", self),
            relief="sunken",
            bg = '#FF7A00',
            cursor = 'hand2',
            activebackground='#FF7A00',
            activeforeground='#FF7A00'
        )
        self.button_2.place(
            x=22.0,
            y=461.0,
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
            command=lambda: handle_button_press("Tickets", self),
            relief="sunken",
            bg = '#FF7A00',
            cursor = 'hand2',
            activebackground='#FF7A00',
            activeforeground='#FF7A00'
        )
        self.button_3.place(
            x=22.0,
            y=408.0,
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
            command=lambda: handle_button_press("Positions", self),
            relief="sunken",
            bg = '#FF7A00',
            cursor = 'hand2',
            activebackground='#FF7A00',
            activeforeground='#FF7A00'
        )
        self.button_4.place(
            x=22.0,
            y=355.0,
            width=234.0,
            height=47.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handle_button_press("Purchase", self),
            relief="sunken",
            bg = '#FF7A00',
            cursor = 'hand2',
            activebackground='#FF7A00',
            activeforeground='#FF7A00'
        )
        self.button_5.place(
            x=22.0,
            y=302.0,
            width=234.0,
            height=47.0
        )

        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            self.canvas,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handle_button_press("Committees", self),
            relief="sunken",
            bg = '#FF7A00',
            cursor = 'hand2',
            activebackground='#FF7A00',
            activeforeground='#FF7A00'
        )
        self.button_6.place(
            x=22.0,
            y=249.0,
            width=234.0,
            height=47.0
        )

        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            self.canvas,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handle_button_press("Events", self),
            relief="sunken",
            bg = '#FF7A00',
            cursor = 'hand2',
            activebackground='#FF7A00',
            activeforeground='#FF7A00'
        )
        self.button_7.place(
            x=22.0,
            y=196.0,
            width=234.0,
            height=47.0
        )

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            self.canvas,
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handle_button_press("Home", self),
            relief="sunken",
            bg = '#FF7A00',
            cursor = 'hand2',
            activebackground='#FF7A00',
            activeforeground='#FF7A00'
        )
        self.button_8.place(
            x=22.0,
            y=49.0,
            width=234.0,
            height=47.0
        )


        self.resizable(False, False)
        self.mainloop()
