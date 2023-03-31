import customtkinter as ctk
import tkinter as tk
from typing import Optional, Union, Tuple
import pathogen
from playingfield import *


'''
     This is going to be the place where I process all of the Graphical User interface stuff
'''

label_fs = ('Orbitron', 12)
ctk.set_appearance_mode(mode_string='dark')
ctk.set_default_color_theme("blue")
appWidth, appHeight = 1200, 600


class App(ctk.CTk):
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)

# title of the application
          self.title("Pandemic Simulations")
          self.geometry(f"{appWidth}x{appHeight}")

# Playing Field Options
          self.field_options_frame = ctk.CTkFrame(self)
          self.field_options_frame.grid(
               row=0, column=0,
               padx=20, pady=20,
               sticky="ne"
          )

     # Field options Header
          self.field_options_header = ctk.CTkLabel(
               master=self.field_options_frame,
               text="Set Up Options",
               font=("Orbitron", 25),
          )
          self.field_options_header.grid(
               row=0, column=0,
               padx=20, pady=10,
               sticky="n", columnspan=2
          )

     # Number of Healthy People
          self.healthy_input_variable = ctk.StringVar()
          self.healthy_input_label = ctk.CTkLabel(
               master=self.field_options_frame,
               text="Number of Healthy People: ",
               font=("Orbitron", 12),
          )
          self.healthy_input_label.grid(
               row=1, column=0,
               padx=5, pady=5,
               sticky="nw"
          )

          self.healthy_input_entry = ctk.CTkEntry(
               master=self.field_options_frame,
               textvariable=self.healthy_input_variable,
               font=("Orbitron", 12),
          )
          self.healthy_input_entry.grid(
               row=1, column=1,
               padx=5, pady=5,
               sticky="ne"
          )

     # asymptomatic people:
          self.asymp_input_variable = ctk.StringVar()
          self.asymp_input_label = ctk.CTkLabel(
               master=self.field_options_frame,
               text="Number of Asymptomatic People: ",
               font=("Orbitron", 12),
          )
          self.asymp_input_label.grid(
               row=2, column=0,
               padx=5, pady=5,
               sticky="nw"
          )

          self.asymp_input_entry = ctk.CTkEntry(
               master=self.field_options_frame,
               textvariable=self.asymp_input_variable,
               font=("Orbitron", 12),
          )
          self.asymp_input_entry.grid(
               row=2, column=1,
               padx=5, pady=5,
               sticky="ne"
          )

     # Symptomatic people:
          self.symptom_input_variable = ctk.StringVar()
          self.symptom_input_label = ctk.CTkLabel(
               master=self.field_options_frame,
               text="Number of Symptomatic People: ",
               font=("Orbitron", 12),
          )
          self.symptom_input_label.grid(
               row=3, column=0,
               padx=5, pady=5,
               sticky="nw")

          self.symptom_input_entry = ctk.CTkEntry(
               master=self.field_options_frame,
               textvariable=self.symptom_input_variable,
               font=("Orbitron", 12),
          )
          self.symptom_input_entry.grid(
               row=3, column=1,
               padx=5, pady=5,
               sticky="ne"
          )

     # Days you want to run the simulation:
          self.days_to_run_var = ctk.StringVar()
          self.days_to_run_label = ctk.CTkLabel(
               master=self.field_options_frame,
               text="Days to run:",
               font=("Orbitron", 12)
          )
          self.days_to_run_label.grid(
               row=4, column=0,
               padx=5, pady=5,
               sticky="nw"
          )

          self.days_to_run_entry = ctk.CTkEntry(
               master=self.field_options_frame,
               textvariable=self.days_to_run_var,
               font=("Orbitron", 12),
          )
          self.days_to_run_entry.grid(
               row=4, column=1,
               padx=5, pady=5,
               sticky="ne"
          )


     # pathogen Header
          self.pathogen_options_label = ctk.CTkLabel(
               master = self.field_options_frame,
               text = "Pathogen Options",
               font = ('Orbitron', 25)
          )
          self.pathogen_options_label.grid(
               row = 5, column = 0,
               padx = 20, pady = 20,
               sticky = 'n', columnspan = 2
          )

     # pathogen Options
          pathogen_type_var = ctk.StringVar()
          self.pathogen_type_label = ctk.CTkLabel(
               master = self.field_options_frame,
               text = "Pathogen Type: ",
               font = ("Orbitron", 12),
          )
          self.pathogen_type_label.grid(
               row = 6, column = 0,
               padx = 5, pady = 5,
               sticky = 'nw'
          )

          self.pathogen_type_options = ctk.CTkOptionMenu(
               master = self.field_options_frame,
               variable=pathogen_type_var,
               values=list(baddy.value for baddy in pathogen.Baddy),
               font=('Obritron', 15)
          )
          self.pathogen_type_options.grid(
               row = 6, column = 1,
               padx = 5, pady = 5,
               sticky = 'ne'
          )

     # pathogen name
          self.pathogen_name_var = ctk.StringVar()
          self.pathogen_name_label = ctk.CTkLabel(
               master = self.field_options_frame,
               text = "Pathogen Name: ",
               font = label_fs
          )
          self.pathogen_name_label.grid(
               row = 7, column = 0,
               padx = 5, pady = 5,
               sticky = 'nw'
          )

          self.pathogen_name_entry = ctk.CTkEntry(
               master = self.field_options_frame,
               font=label_fs,
               textvariable=self.pathogen_name_var
          )
          self.pathogen_name_entry.grid(
               row = 7, column = 1,
               padx = 5, pady = 5,
               sticky = 'ne',
          )

     # generate Virus Button
          self.virus_generator = ctk.CTkButton(
               master = self.field_options_frame,
               text = "Begin Simulation",
               font = ('Orbitron', 15),
               command=self.generate_everyone
          )
          self.virus_generator.grid(
               row = 8, column = 1,
               padx = 5, pady = 5,
               sticky = 'e')

# Statistics Frame
          self.statistics_frame = ctk.CTkFrame(master = self, width = 200)
          self.statistics_frame.grid(
               row = 0, column = 2,
               padx = 20, pady = 20,
               sticky = 'ne'

          )

     # Statistics Header
          self.statistics_header_label = ctk.CTkLabel(
               master=self.statistics_frame,
               text = "STATISTICS: DAY 0",
               font = ('Orbitron', 25)
          )
          self.statistics_header_label.grid(
               row = 0, column = 0,
               padx = 20, pady = 20,
               sticky = 'n', columnspan = 2
          )

     # Healthy people stat
          self.healthy_num_label = ctk.CTkLabel(
               master = self.statistics_frame,
               text= "Healthy Cases: ",
               font = ('Orbitron', 15)
          )
          self.healthy_num_label.grid(
               row = 1, column = 0,
               padx = 5, pady = 5,
               sticky = 'nw'
          )

     # Asymptomatic People Stat
          self.asymp_num_label = ctk.CTkLabel(
               master = self.statistics_frame,
               text = "Asymptomatic Cases",
               font = ('Orbitron', 15)
          )
          self.asymp_num_label.grid(
               row = 2, column = 0,
               padx = 5, pady = 5,
               sticky = 'nw'
          )

     # Symptomatic People Stat
          self.symp_num_label = ctk.CTkLabel(
               master = self.statistics_frame,
               text = 'Symptomatic Cases: ',
               font=('Orbitron', 15)
          )
          self.symp_num_label.grid(
               row = 3, column = 0,
               padx = 5, pady = 5,
               sticky = 'nw'
          )

     # Pathogen type stat
          self.stat_path_type_label = ctk.CTkLabel(
               master = self.statistics_frame,
               text = "Pathogen Type: ",
               font=('Orbitron', 15)
          )
          self.stat_path_type_label.grid(
               row = 4, column = 0,
               padx = 5, pady = 5,
               sticky = 'nw'
          )

     # Day Increaser
          self.day_increaser_button = ctk.CTkButton(
               master = self.statistics_frame,
               text = "Update Stats",
               font = ('Orbitron', 15),
               command = self.update_stats
          )
          self.day_increaser_button.grid(
               row = 5, column = 0,
               padx = 5, pady = 5,
               sticky = 'e', columnspan = 2
          )

     def update_stats(self):
          field.update()
          self.statistics_header_label.configure(text = f"STATISTICS: DAY {field.day_counter}")
          self.healthy_num_label.configure(text = f'{"Healthy Number:":<25}{field.healthy_people_count:>10}')
          self.asymp_num_label.configure(text = f"{'Asymptomatic Number:':<23}{field.asymp_people_count}")
          self.symp_num_label.configure(text = f"{'Symptomatic Number:':<25}{field.symp_people_count:>3}")
          self.stat_path_type_label.configure(text = f"Pathogen Type: {field.pathogen.type.name}")
          self.statistics_frame.configure(width = 200)

     def generate_population(self):
          healthy_people = int(self.healthy_input_entry.get())
          asymp_people = int(self.asymp_input_entry.get())
          symp_people = int(self.symptom_input_entry.get())
          field.populate(healthy_people, asymp_people, symp_people)

     def generate_virus(self):
          pathogen_name = self.pathogen_name_entry.get()
          pathogen_type = self.pathogen_type_options.get()
          field.add_pathogen(type=pathogen.Baddy(pathogen_type), name = pathogen_name)

     def generate_everyone(self):
          self.generate_population()
          self.generate_virus()
          self.update_stats()



if __name__ == "__main__":
    app = App()
    app.mainloop()
