import tkinter as tk
from tkinter import ttk
from tkinter.constants import DISABLED, NORMAL
import pathogen
from playingfield import *
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
        style.configure(
            "grid.TLabel", font=('Orbitron', 11), background='light blue', padx=20, anchor='right', justify='left'

        )



        # creating a frame and assigning it to container
        container = tk.Frame(self, background='light blue')
        # specifying the region where the frame is packed in root
        container.pack(fill=tk.BOTH)

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
        self.people_options_frame = tk.Frame(self, bg='light blue')

        self.people_options_frame.pack(side='left', fill='both', expand=True, anchor='sw')
        self.people_options_frame.grid_columnconfigure(0, weight=1)
        self.people_options_frame.grid_columnconfigure(1, weight=1)
        self.people_options_label = ttk.Label(
            self.people_options_frame, text="People Options", anchor='center',style='options_headers.TLabel'
        )
        self.people_options_label.grid(row = 0, column= 0, sticky='nsew', columnspan=2)

        # Healthy People
        self.health_count_var = tk.StringVar()
        self.health_count_label = ttk.Label(
            self.people_options_frame,text="Healthy Count: ", style="options_labels.TLabel"
        )
        self.health_count_label.grid(row = 1, column = 0, padx= (10, 0), pady = 10, sticky='w')
        self.health_count_entry = ttk.Entry(
            self.people_options_frame, textvariable=self.health_count_var
        )
        self.health_count_entry.grid(row=1, column = 1,padx=(0, 10), sticky='e')

        # Asymptomatic People
        self.asymp_count_var = tk.StringVar()
        self.asymp_count_label = ttk.Label(
            self.people_options_frame, text="Asymptomatic Count: ", style= "options_labels.TLabel"
        )
        self.asymp_count_label.grid(row = 2, column = 0, padx= (10, 0), pady = 10, sticky='w')
        self.asymp_count_entry = ttk.Entry(
            self.people_options_frame, textvariable=self.asymp_count_var
        )
        self.asymp_count_entry.grid(row = 2, column = 1, sticky='e', padx = (0, 10), pady=10)

        # Symptomatic Peple #
        self.symp_count_var = tk.StringVar()
        self.symp_count_label = ttk.Label(
            self.people_options_frame, text="Symptomatic Count: ", style= "options_labels.TLabel"
        )
        self.symp_count_label.grid(row = 3, column = 0, padx= (10, 0), pady = 10, sticky='w')
        self.symp_count_entry = ttk.Entry(
            self.people_options_frame, textvariable=self.symp_count_var
        )
        self.symp_count_entry.grid(row = 3, column = 1, padx=(0, 10),pady= 10, sticky='e' )


        # Social Factor #
        self.social_factor_var = tk.StringVar()
        self.social_factor_label = ttk.Label(
            self.people_options_frame, text="Social Factor: ", style= "options_labels.TLabel"
        )
        self.social_factor_label.grid(row = 4, column = 0, padx= (10, 0), pady = 10, sticky='w')
        self.social_factor_entry = ttk.Entry(
            self.people_options_frame, textvariable=self.social_factor_var
        )
        self.social_factor_entry.grid(row = 4, column = 1, padx=(0, 10),pady= 10, sticky='e' )



        # pathogen options Frame
        self.patho_options_frame = tk.Frame(self, bg='light blue', height=HEIGHT)
        self.patho_options_frame.pack(side='left', fill='both', expand=True)
        self.patho_options_frame.grid_columnconfigure(0, weight=1)
        self.patho_options_frame.grid_columnconfigure(1, weight=1)
        self.patho_header_label = ttk.Label(
            self.patho_options_frame, text='Pathogen Options', anchor='center', style='options_headers.TLabel',
        )
        self.patho_header_label.grid(row=0, column=0, sticky='nsew', columnspan=2)

        # Pathogen Type #
        self.path_type_var = tk.StringVar()
        self.path_type_label = ttk.Label(
            self.patho_options_frame, text="Type: ", style='options_labels.TLabel',
        )
        self.path_type_label.grid(row=1, column = 0, sticky='w', padx=(10, 0), pady=10)
        self.path_types = ['Bacteria', 'Virus', 'Protazoa', 'Prion', 'Fungus']
        self.path_type_choices = ttk.OptionMenu(
            self.patho_options_frame, self.path_type_var,*self.path_types,
        )
        self.path_type_choices.grid(row=1, column = 1, sticky='e', padx=(0, 10))

        # Pathogen Name #
        self.path_name_var = tk.StringVar()
        self.path_name_label = ttk.Label(
            self.patho_options_frame, text = "Name: ", style='options_labels.TLabel'
        )
        self.path_name_label.grid(row=2, column = 0, sticky='w', padx=(10, 0), pady=10)
        self.path_name_entry = ttk.Entry(
            self.patho_options_frame, textvariable=self.path_name_var
        )
        self.path_name_entry.grid(row = 2, column = 1, sticky='e', padx=(0, 10), pady=10)

        # Incubation Length #
        self.incubation_len_var = tk.StringVar()
        self.incubation_len_label = ttk.Label(
            self.patho_options_frame, text = "Incubation Length: ", style='options_labels.TLabel'
        )
        self.incubation_len_label.grid(row=5, column = 0, sticky='w', padx=(10, 0), pady=10)
        self.incubation_len_entry = ttk.Entry(
            self.patho_options_frame, textvariable=self.incubation_len_var
        )
        self.incubation_len_entry.grid(row = 5, column = 1, sticky='e', padx=(0, 10), pady=10)


        # Symptomatic Infectability #
        self.symptom_infect_var = tk.StringVar()
        self.symptom_infect_label = ttk.Label(
            self.patho_options_frame, text = "Symptomatic Power: ", style='options_labels.TLabel'
        )
        self.symptom_infect_label.grid(row=6, column = 0, sticky='w', padx=(10, 0), pady=10)
        self.symptom_infect_entry = ttk.Entry(
            self.patho_options_frame, textvariable=self.symptom_infect_var
        )
        self.symptom_infect_entry.grid(row = 6, column = 1, sticky='e', padx=(0, 10), pady=10)



        # Asymptomatic Infectability #
        self.asymptom_infect_var = tk.StringVar()
        self.asymptom_infect_label = ttk.Label(
            self.patho_options_frame, text = "Asymptomatic Power: ", style='options_labels.TLabel'
        )
        self.asymptom_infect_label.grid(row=7, column = 0, sticky='w', padx=(10, 0), pady=10)
        self.asymptom_infect_entry = ttk.Entry(
            self.patho_options_frame, textvariable=self.asymptom_infect_var
        )
        self.asymptom_infect_entry.grid(row = 7, column = 1, sticky='e', padx=(0, 10), pady=10)


        # Infection Length #
        self.path_len_var = tk.StringVar()
        self.path_len_label = ttk.Label(
            self.patho_options_frame, text = "Infection Length ", style='options_labels.TLabel'
        )
        self.path_len_label.grid(row=9, column = 0, sticky='w', padx=(10, 0), pady=10)
        self.path_len_entry = ttk.Entry(
            self.patho_options_frame, textvariable=self.path_len_var
        )
        self.path_len_entry.grid(row = 9, column = 1, sticky='e', padx=(0, 10), pady=10)

        self.help_label = ttk.Label(self.people_options_frame, text='''
Use Integers for Each value except for pathogen name.
Simulation works by having each person meet up with
Social Factor amount of people each day.
Each person they meet will either add SYMPTOMATIC POWER
amount of points or ASYMPTOMATIC POWER
amount of points based on if that person is
symptomatic or not. If the person is HEALTHY and
the threshold of 50 points is reached,
they now have an 80% chance of becoming infected.
Simulation goes until everyone has immunity.''', style='grid.TLabel')
        self.help_label.grid(row=5, column = 0, columnspan=2)
        # Run Simulation Button #
        self.run_sim_button = ttk.Button(
            self.people_options_frame, text="Run Simulation", style='run.TButton', command=self.run_simulation
        )
        self.run_sim_button.grid(row=6, column=0, sticky='sw')
        self.people_options_frame.grid_rowconfigure(5, weight=8)
        self.progress_bar = ttk.Label(
            self.people_options_frame, style='options_labels.TLabel'
        )
        self.progress_bar.grid(row=6, column = 1, sticky='se')

    def generate_population(self):
        healthy_people = int(self.health_count_entry.get()) if self.health_count_entry.get().isnumeric() else 0
        asymp_people = int(self.asymp_count_entry.get()) if self.asymp_count_entry.get().isnumeric() else 0
        symp_people = int(self.symp_count_entry.get()) if self.symp_count_entry.get().isnumeric() else 0
        field.populate(healthy_people, asymp_people, symp_people)

    def generate_virus(self):
        pathogen_name = self.path_name_entry.get()
        pathogen_type = self.path_type_var.get()
        symptomatic_infectability = int(self.symptom_infect_entry.get()) if self.symptom_infect_entry.get().isnumeric() else 0
        asymptomati_infectability = int(self.asymptom_infect_entry.get()) if self.asymptom_infect_entry.get().isnumeric() else 0
        longevity_factor = int(self.path_len_entry.get()) if self.path_len_entry.get().isnumeric() else 0


        field.add_pathogen(
            type=pathogen.Baddy(pathogen_type),
            name = pathogen_name,
            symptomatic_infectability=symptomatic_infectability,
            asymptomatic_infectability=asymptomati_infectability,
            longevity_factor=longevity_factor,
        )

    def run_simulation(self):
        field.clear_data()
        self.generate_population()
        self.generate_virus()
        self.progress_bar.config(text="Loading")
        while field.healthy_people_count != len(field.population):
            field.update()
        self.progress_bar.config(text='Finished!')


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

        buttons_frame = ttk.Frame(self)
        buttons_frame.pack(fill='x')
        plotbutton = ttk.Button(
            buttons_frame, text = "Plot", command= self.plot
        )
        plotbutton.pack(side='left')
        rerun_buttom = ttk.Button(
            buttons_frame, text="Rerun simulation", command=self.rerun
        )
        rerun_buttom.pack(side='left')


        self.graph_frame = ttk.Frame(self)
        self.graph_frame.pack(fill='both', expand=1)
        self.fig = Figure(figsize=(7,5), dpi=100)
        self.plot1 = self.fig.add_subplot(111)
        self.plot1.set_xlabel('Days')
        self.plot1.set_ylabel('Healthy Counter')
        self.canvas = FigureCanvasTkAgg(self.fig, self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()


    def plot(self):
        healthy_vals = field.hist_pop_data.show()['Healthy']
        asympt_vals = field.hist_pop_data.show()['Asymptomatic']
        sympt_vals = field.hist_pop_data.show()['Symptomatic']
        self.graph_frame.destroy()
        self.graph_frame = ttk.Frame(self)
        self.graph_frame.pack(fill='both', expand=1)
        self.fig = Figure(figsize=(7,5), dpi = 100)
        self.plot1 = self.fig.add_subplot(111)
        self.plot1.grid(visible=True, color='r')
        self.plot1.plot(sympt_vals)
        self.plot1.set_xlim(xmin=0, xmax=field.day_counter+1)
        self.plot1.set_xlabel('Days')
        self.plot1.set_ybound(lower=0)
        self.plot1.set_ylabel('Symptomatic Counter')
        self.plot1.text(1, 0.9, f'Simulation took {field.day_counter} days to finish', horizontalalignment='right',verticalalignment='center', transform = self.plot1.transAxes)
        self.plot1.set_title(f"{field.pathogen.name} Infections over Time")
        self.canvas = FigureCanvasTkAgg(self.fig, self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()


    def rerun(self):
        health_initial = field.hist_pop_data.show()['Healthy'][0]
        asymp_initial = field.hist_pop_data.show()['Asymptomatic'][0]
        symp_initial = field.hist_pop_data.show()['Symptomatic'][0]
        pathogen = field.pathogen
        field.clear_data()
        field.population = []
        field.populate(healthy_people= health_initial, asymp_people=asymp_initial, symp_people=symp_initial)
        field.add_pathogen(pathogen.type, pathogen.name, pathogen.damage_factor, pathogen.cure_defense, pathogen.longevity_factor, pathogen.incubation_len, pathogen.symptomatic_infectability, pathogen.asymptomatic_infectability, pathogen.surface_infect_factor)
        while field.healthy_people_count != len(field.population):
            field.update()
        self.plot()



class TablePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= 'light blue')
        nav_bar = tk.Frame(self, bg='light blue')
        nav_bar.pack(side = tk.TOP, fill='x')
        nav_bar.grid_columnconfigure(0, weight=1)
        nav_bar.grid_columnconfigure(1, weight=1)
        nav_bar.grid_columnconfigure(2, weight=1)

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

        buttons_frame = ttk.Frame(self)
        buttons_frame.pack(fill='x')
        plotbutton = ttk.Button(
            buttons_frame, text = "Show Table", command= self.show_table
        )
        plotbutton.pack(side='left')
        rerun_buttom = ttk.Button(
            buttons_frame, text="Rerun simulation", command=self.rerun
        )
        rerun_buttom.pack(side='left')

        self.table_field = ttk.Frame(self)
        self.table_field.pack(fill='both', expand=1, anchor='center')
        self.table_text = ttk.Label(master=self.table_field)
        self.table_text.pack()

    def show_table(self):
        self.table_text.configure(text=field.hist_pop_data.show().to_string(max_rows=24), style='grid.TLabel')

    def rerun(self):
        health_initial = field.hist_pop_data.show()['Healthy'][0]
        asymp_initial = field.hist_pop_data.show()['Asymptomatic'][0]
        symp_initial = field.hist_pop_data.show()['Symptomatic'][0]
        pathogen = field.pathogen
        field.clear_data()
        field.population = []
        field.populate(healthy_people= health_initial, asymp_people=asymp_initial, symp_people=symp_initial)
        field.add_pathogen(pathogen.type, pathogen.name, pathogen.damage_factor, pathogen.cure_defense, pathogen.longevity_factor, pathogen.incubation_len, pathogen.symptomatic_infectability, pathogen.asymptomatic_infectability, pathogen.surface_infect_factor)
        while field.healthy_people_count != len(field.population):
            field.update()
        self.show_table()


if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()
