import tkinter as tk
from gui.Selection.mainSelection import selectionWindow


# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window


if __name__ == "__main__":

    selectionWindow()
    # mainWindow()

    root.mainloop()

def goSelection():
    selectionWindow()