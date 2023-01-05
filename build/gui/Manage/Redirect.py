import gui.Manage.Committees.main
import gui.Manage.Event.main
import gui.Manage.Participants.main
import gui.Manage.Position.main
import gui.Manage.Tickets.main
# import Manage.TicketStats.main
from .. import Redirect

def goEvent():
    gui.Manage.Event.main.eventWindow()
def goCommittees():
    gui.Manage.Committees.main.committeesWindow()
def goParticipants():
    gui.Manage.Participants.main.participantsWindow()
def goPosition():
    gui.Manage.Position.main.positionWindow()
def goTickets():
    gui.Manage.Tickets.main.ticketsWindow()
def goSelection():
    Redirect.goSelection()