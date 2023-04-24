import tkinter as tk
from tkinter import ttk
from tkinter.constants import DISABLED, NORMAL
import pathogen
from playingfield import *


'''
     This is going to be the place where I process all of the Graphical User interface stuff
'''

WIDTH, HEIGHT = 1100, 500


class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Test Application")
        self.geometry(f"{WIDTH}x{HEIGHT}")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (OptionsPage, GraphPage, TablePage):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(OptionsPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


class OptionsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Button(
            self, text="Options",
            state=DISABLED,
        )
        label.grid(
            row = 0, column = 0,
            padx = 10, pady=10,
            sticky='nsew',
        )

        switch_to_graph_button = ttk.Button(
            self,
            text="Graph",
            command=lambda: controller.show_frame(GraphPage),
        )
        switch_to_graph_button.grid(
            row = 0 , column = 1,
            padx = 10, pady = 10,
            sticky='nsew'

        )
        switch_to_table_button = ttk.Button(
            self,
            text="Table",
            command=lambda: controller.show_frame(TablePage),
        )
        switch_to_table_button.grid(
            row = 0 , column = 2,
            padx = 10, pady = 10,
            sticky='nsew'

        )



class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Button(
            self,
            text="Graph",
            state=DISABLED,
        )
        label.grid(
            row = 0, column = 1,
            padx=10, pady=10,
            sticky='nsew'
            )

        switch_to_options_button = ttk.Button(
            self,
            text="Options",
            command=lambda: controller.show_frame(OptionsPage),
        )
        switch_to_options_button.grid(
            row = 0 , column = 0,
            padx = 10, pady = 10,
            sticky='nsew'

        )
        switch_to_table_button = ttk.Button(
            self,
            text="Table",
            command=lambda: controller.show_frame(TablePage),
        )
        switch_to_table_button.grid(
            row = 0 , column = 2,
            padx = 10, pady = 10,
            sticky='nsew'

        )

class TablePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Button(
            self, text="Table Page",
            state=DISABLED
        )
        label.grid(
            row = 0, column = 2,
            padx=10, pady=10,
            sticky='nsew'
            )


        switch_to_options_button = ttk.Button(
            self,
            text="Options",
            command=lambda: controller.show_frame(OptionsPage),
        )
        switch_to_options_button.grid(
            row = 0 , column = 0,
            padx = 10, pady = 10,
            sticky='nsew'

        )

        switch_to_graph_button = ttk.Button(
            self,
            text="Graph",
            command=lambda: controller.show_frame(GraphPage),
        )
        switch_to_graph_button.grid(
            row = 0 , column = 1,
            padx = 10, pady = 10,
            sticky='nsew'

        )


if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()
