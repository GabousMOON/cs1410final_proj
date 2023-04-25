import tkinter as tk
from tkinter import ttk
from tkinter.constants import DISABLED, NORMAL
import pathogen
from playingfield import *


'''
     This is going to be the place where I process all of the Graphical User interface stuff
'''

WIDTH, HEIGHT = 950, 600

data = None


class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Test Application")
        self.geometry(f"{WIDTH}x{HEIGHT}")

        style = ttk.Style(self)
        style.configure(
            "nav.TButton",
            background='light blue', borderwidth=0, borderradius=0,forground='light blue',
            font=('Orbitron', 25)
        )
        style.configure(
            'run.TButton',
            font=('Orbitron', 20, 'bold')
        )

        style.configure(
            "options.TFrame", background = 'light blue',
        )
        style.configure(
            "options_headers.TLabel", font=('Orbitron', 25), background='light blue'
        )
        style.configure(
            "options_labels.TLabel", font=('Orbitron', 15), background='light blue'

        )



        # creating a frame and assigning it to container
        container = tk.Frame(self)
        # specifying the region where the frame is packed in root
        container.pack(side=tk.TOP, fill=tk.BOTH)

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
        tk.Frame.__init__(self, parent, bg='light blue')
        # navigation Bar
        nav_bar = tk.Frame(self, bg="light blue")
        nav_bar.pack(fill='x', side='top')
        nav_bar.grid_columnconfigure(0, weight=1)
        nav_bar.grid_columnconfigure(1, weight=1)
        nav_bar.grid_columnconfigure(2, weight=1)
        label = ttk.Button(
            nav_bar, text="Options",
            state=DISABLED,
            style="nav.TButton"
        )
        label.grid(
            row = 0, column = 0,
            padx = 0, pady=0,
            sticky='nsew',
        )

        switch_to_graph_button = ttk.Button(
            nav_bar,
            text="Graph",
            command=lambda: controller.show_frame(GraphPage),
            style='nav.TButton'
        )
        switch_to_graph_button.grid(
            row = 0 , column = 1,
            padx = 0, pady = 0,
            sticky='nsew',
        )

        switch_to_table_button = ttk.Button(
            nav_bar,
            text="Table",
            command=lambda: controller.show_frame(TablePage),
            style='nav.TButton'
        )
        switch_to_table_button.grid(
            row = 0 , column = 2,
            padx = 0, pady = 0,
            sticky='nsew'

        )

        # People options Frame
        people_options_frame = tk.Frame(self, bg='light blue')

        people_options_frame.pack(side='left', fill='both', expand=True, anchor='sw')
        people_options_frame.grid_columnconfigure(0, weight=1)
        people_options_frame.grid_columnconfigure(1, weight=1)
        people_options_label = ttk.Label(
            people_options_frame, text="People Options", anchor='center',style='options_headers.TLabel'
        )
        people_options_label.grid(row = 0, column= 0, sticky='nsew', columnspan=2)

        # Healthy People
        health_count_var = tk.StringVar()
        health_count_label = ttk.Label(
            people_options_frame,text="Healthy Count: ", style="options_labels.TLabel"
        )
        health_count_label.grid(row = 1, column = 0, padx= (10, 0), pady = 10, sticky='w')
        health_count_entry = ttk.Entry(
            people_options_frame, textvariable=health_count_var
        )
        health_count_entry.grid(row=1, column = 1,padx=(0, 10), sticky='e')

        # Asymptomatic People
        asymp_count_var = tk.StringVar()
        asymp_count_label = ttk.Label(
            people_options_frame, text="Asymptomatic Count: ", style= "options_labels.TLabel"
        )
        asymp_count_label.grid(row = 2, column = 0, padx= (10, 0), pady = 10, sticky='w')
        asymp_count_entry = ttk.Entry(
            people_options_frame, textvariable=asymp_count_var
        )
        asymp_count_entry.grid(row = 2, column = 1, sticky='e', padx = (0, 10), pady=10)

        # Symptomatic Peple #
        symp_count_var = tk.StringVar()
        symp_count_label = ttk.Label(
            people_options_frame, text="Symptomatic Count: ", style= "options_labels.TLabel"
        )
        symp_count_label.grid(row = 3, column = 0, padx= (10, 0), pady = 10, sticky='w')
        symp_count_entry = ttk.Entry(
            people_options_frame, textvariable=symp_count_var
        )
        symp_count_entry.grid(row = 3, column = 1, padx=(0, 10),pady= 10, sticky='e' )


        # Social Factor #
        social_factor_var = tk.StringVar()
        social_factor_label = ttk.Label(
            people_options_frame, text="Symptomatic Count: ", style= "options_labels.TLabel"
        )
        social_factor_label.grid(row = 4, column = 0, padx= (10, 0), pady = 10, sticky='w')
        social_factor_entry = ttk.Entry(
            people_options_frame, textvariable=social_factor_var
        )
        social_factor_entry.grid(row = 4, column = 1, padx=(0, 10),pady= 10, sticky='e' )



        # pathogen options Frame
        patho_options_frame = tk.Frame(self, bg='light blue', height=HEIGHT)
        patho_options_frame.pack(side='left', fill='both', expand=True)
        patho_options_frame.grid_columnconfigure(0, weight=1)
        patho_options_frame.grid_columnconfigure(1, weight=1)
        patho_header_label = ttk.Label(
            patho_options_frame, text='Pathogen Options', anchor='center', style='options_headers.TLabel',
        )
        patho_header_label.grid(row=0, column=0, sticky='nsew', columnspan=2)

        # Pathogen Type #
        path_type_var = tk.StringVar()
        path_type_label = ttk.Label(
            patho_options_frame, text="Type: ", style='options_labels.TLabel',
        )
        path_type_label.grid(row=1, column = 0, sticky='w', padx=(10, 0), pady=10)
        path_types = ['Bacteria', 'Virus', 'Protazoa', 'Prion', 'Fungus']
        path_type_choices = ttk.OptionMenu(
            patho_options_frame, path_type_var,*path_types,
        )
        path_type_choices.grid(row=1, column = 1, sticky='e', padx=(0, 10))

        # Pathogen Name #
        path_name_var = tk.StringVar()
        path_name_label = ttk.Label(
            patho_options_frame, text = "Name: ", style='options_labels.TLabel'
        )
        path_name_label.grid(row=2, column = 0, sticky='w', padx=(10, 0), pady=10)
        path_name_entry = ttk.Entry(
            patho_options_frame, textvariable=path_name_var
        )
        path_name_entry.grid(row = 2, column = 1, sticky='e', padx=(0, 10), pady=10)


        # Damage Factor #
        damage_factor_var = tk.StringVar()
        damage_factor_label = ttk.Label(
            patho_options_frame, text = "Damage Factor: ", style='options_labels.TLabel'
        )
        damage_factor_label.grid(row=3, column = 0, sticky='w', padx=(10, 0), pady=10)
        damage_factor_entry = ttk.Entry(
            patho_options_frame, textvariable=damage_factor_var
        )
        damage_factor_entry.grid(row = 3, column = 1, sticky='e', padx=(0, 10), pady=10)


        # Cure Defense
        cure_defense_var = tk.StringVar()
        cure_defense_label = ttk.Label(
            patho_options_frame, text = "Cure Defense: ", style='options_labels.TLabel'
        )
        cure_defense_label.grid(row=4, column = 0, sticky='w', padx=(10, 0), pady=10)
        cure_defense_entry = ttk.Entry(
            patho_options_frame, textvariable=cure_defense_var
        )
        cure_defense_entry.grid(row = 4, column = 1, sticky='e', padx=(0, 10), pady=10)


        # Incubation Length #
        incubation_len_var = tk.StringVar()
        incubation_len_label = ttk.Label(
            patho_options_frame, text = "Incubation Length: ", style='options_labels.TLabel'
        )
        incubation_len_label.grid(row=5, column = 0, sticky='w', padx=(10, 0), pady=10)
        incubation_len_entry = ttk.Entry(
            patho_options_frame, textvariable=incubation_len_var
        )
        incubation_len_entry.grid(row = 5, column = 1, sticky='e', padx=(0, 10), pady=10)


        # Symptomatic Infectability #
        symptom_infect_var = tk.StringVar()
        symptom_infect_label = ttk.Label(
            patho_options_frame, text = "Symptomatic Power: ", style='options_labels.TLabel'
        )
        symptom_infect_label.grid(row=6, column = 0, sticky='w', padx=(10, 0), pady=10)
        symptom_infect_entry = ttk.Entry(
            patho_options_frame, textvariable=symptom_infect_var
        )
        symptom_infect_entry.grid(row = 6, column = 1, sticky='e', padx=(0, 10), pady=10)



        # Asymptomatic Infectability #
        asymptom_infect_var = tk.StringVar()
        asymptom_infect_label = ttk.Label(
            patho_options_frame, text = "Asymptomatic Power: ", style='options_labels.TLabel'
        )
        asymptom_infect_label.grid(row=7, column = 0, sticky='w', padx=(10, 0), pady=10)
        asymptom_infect_entry = ttk.Entry(
            patho_options_frame, textvariable=asymptom_infect_var
        )
        asymptom_infect_entry.grid(row = 7, column = 1, sticky='e', padx=(0, 10), pady=10)



        # Surface Infectability Factor
        surface_infect_var = tk.StringVar()
        surface_infect_label = ttk.Label(
            patho_options_frame, text = "Surface Power: ", style='options_labels.TLabel'
        )
        surface_infect_label.grid(row=8, column = 0, sticky='w', padx=(10, 0), pady=10)
        surface_infect_entry = ttk.Entry(
            patho_options_frame, textvariable=surface_infect_var
        )
        surface_infect_entry.grid(row = 8, column = 1, sticky='e', padx=(0, 10), pady=10)


        # Run Simulation Button
        run_sim_button = ttk.Button(
            people_options_frame, text="Run Simulation", style='run.TButton', command=self.run_simulation
        )
        run_sim_button.grid(row=5, column=0, sticky='sw')
        people_options_frame.grid_rowconfigure(5, weight=7)










class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light blue')
        nav_bar = tk.Frame(self, bg='light blue')
        nav_bar.pack(side = tk.TOP, fill='x')
        nav_bar.grid_columnconfigure(0, weight=1)
        nav_bar.grid_columnconfigure(1, weight=1)
        nav_bar.grid_columnconfigure(2, weight=1)

        label = ttk.Button(
            nav_bar,
            text="Graph",
            state=DISABLED,
            style= "nav.TButton"

        )
        label.grid(
            row = 0, column = 1,
            padx=0, pady=0,
            sticky='nsew'
            )

        switch_to_options_button = ttk.Button(
            nav_bar,
            text="Options",
            command=lambda: controller.show_frame(OptionsPage),
            style= "nav.TButton",
        )
        switch_to_options_button.grid(
            row = 0 , column = 0,
            padx = 0, pady = 0,
            sticky='nsew'

        )
        switch_to_table_button = ttk.Button(
            nav_bar,
            text="Table",
            command=lambda: controller.show_frame(TablePage),
            style= "nav.TButton",
        )
        switch_to_table_button.grid(
            row = 0 , column = 2,
            padx = 0, pady = 0,
            sticky='nsew'

        )

class TablePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= 'light blue')
        nav_bar = tk.Frame(self, bg='light blue')
        nav_bar.grid(row = 0, column = 0, sticky='nsew')
        label = ttk.Button(
            nav_bar, text="Table",
            state=DISABLED,
            style= "nav.TButton"
        )
        label.grid(
            row = 0, column = 2,
            padx=0, pady=0,
            sticky='nsew'
            )

        switch_to_options_button = ttk.Button(
            nav_bar,
            text="Options",
            command=lambda: controller.show_frame(OptionsPage),
            style= "nav.TButton",
        )
        switch_to_options_button.grid(
            row = 0 , column = 0,
            padx = 0, pady = 0,
            sticky='nsew',

        )

        switch_to_graph_button = ttk.Button(
            nav_bar,
            text="Graph",
            command=lambda: controller.show_frame(GraphPage),
            style= "nav.TButton",
        )
        switch_to_graph_button.grid(
            row = 0 , column = 1,
            padx = 0, pady = 0,
            sticky='nsew'

        )


if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()
