import customtkinter as ctk
import tkinter as tk
from playingfield import PlayingField
# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
ctk.set_appearance_mode("dark")

# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme('green')

appWidth, appHeight = 600, 700
field = PlayingField()

# Create App Class
class App(ctk.CTk):
# Layout of the GUI will be written in the init constructor
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
# Sets the title of our window to "App"
        self.title("App")
# Dimensions of the window will be 200x200
        self.geometry(f"{appWidth}x{appHeight}")

# Name Label
        self.name_label = ctk.CTkLabel(self,
                                       text =  "Name")
        self.name_label.grid(row=0, column = 0,
                             padx = 20, pady = 20,
                             sticky = 'ew')

# Name Entry Field
        self.name_entry = ctk.CTkEntry(self,
                                       placeholder_text = "Name")
        self.name_entry.grid(row=0, column = 1,
                            columnspan = 3, padx = 20,
                            pady = 20, sticky = 'ew')

# Age Label
        self.ageLabel = ctk.CTkLabel(self,
                                     text = "Age")
        self.ageLabel.grid(row = 0, column = 0,
                           padx = 20, pady = 20,
                           sticky = 'ew')

# Age entry Field
        self.ageEntry = ctk.CTkEntry(self,
                                     placeholder_text = "age")
        self.ageEntry.grid(row=1, column = 1,
                           columnspan = 3, padx = 20,
                           pady = 20, sticky = 'ew')

# Gender Label
        self.genderLabel = ctk.CTkLabel(self,
                                        text = "Gender")
        self.genderLabel.grid(row=2, column = 0,
                              padx = 20, pady=20,
                              sticky = 'ew')
# Gender Radio Buttons
        self.genderVar = tk.StringVar(value = "prefer not to say")

        self.maleRadioButton = ctk.CTkRadioButton(self,
                                                  text = "Male",
                                                  variable = self.genderVar,
                                                  value = "He is")
        self.maleRadioButton.grid(row = 2, column = 1,
                                  padx = 20, pady = 20,
                                  sticky = 'ew')

        self.femaleRadioButton = ctk.CTkRadioButton(self,
                                                    text = "Female",
                                                    variable = self.genderVar,
                                                    value = "She is")
        self.femaleRadioButton.grid(row = 2, column = 2,
                                    padx = 20, pady = 20,
                                    sticky = 'ew')

        self.noneRadioButton = ctk.CTkRadioButton(self,
                                                  text = "Prefer not to say",
                                                  variable = self.genderVar,
                                                  value = "They are")
        self.noneRadioButton.grid(row = 2, column = 3,
                                  padx = 20, pady = 20,
                                  sticky = 'ew')

# Choice Check boxes
        self.check_box_var = tk.StringVar(value = "Choice 1")

        self.choice1 = ctk.CTkCheckBox(self, text = "Choice 1",
                                       variable = self.check_box_var,
                                       onvalue = "Choice 1",
                                       offvalue = "c1")
        self.choice1.grid(row= 3, column = 1,
                          padx = 20, pady = 20,
                          sticky = 'ew')

        self.choice2 = ctk.CTkCheckBox(self, text = "choice 2",
                                       variable = self.check_box_var,
                                       onvalue = 'choice2',
                                       offvalue = 'c2')
        self.choice2.grid(row = 3, column = 2,
                          padx = 20, pady = 20,
                          sticky = 'ew')

# Occupation Label
        self.occupation_label = ctk.CTkLabel(self,
                                             text = "Occupation")
        self.occupation_label.grid(row = 4, column = 0,
                                   padx = 20, pady = 20,
                                   sticky = 'ew')

# Occupation combo box
        self.occupation_option_menu = ctk.CTkOptionMenu(self,
                                                        values = ['student', 'working professional'])
        self.occupation_option_menu.grid(row = 4, column = 1,
                                         padx = 20, pady = 20,
                                         columnspan = 2, sticky = 'ew')

# Generate Button
        self.generate_results_button = ctk.CTkButton(self,
                                                     text = 'Generate Results',
                                                     command = self.generateResults)
        self.generate_results_button.grid(row = 5, column = 1,
                                          columnspan = 2,
                                          padx = 20, pady = 20)

# Text box
        self.displayBox = ctk.CTkTextbox(self,
                                         width = 200, height = 100)
        self.displayBox.grid(row = 6, column = 0,
                             columnspan = 4, padx = 20,
                             pady = 20, sticky = 'nsew')


# Adding functionality to the buttons

    def createText(self):
        checkboxValue = ''

        # .get() is used to get the value of the checkboxes
        if self.choice1._check_state and self.choice2._check_state:
            checkboxValue += f'{self.choice1.get()} and {self.choice2.get()}'
        elif self.choice1._check_state:
            checkboxValue += f'{self.choice1.get()}'
        elif self.choice2._check_state:
            checkboxValue += f"{self.choice2.get()}"
        else:
            checkboxValue = "None of the available options"

        # Constructing the text variable
        text = f"{self.name_entry.get()}: \n{self.genderVar.get()} {self.ageEntry.get()} years old and prefers {checkboxValue}\n"
        text += f"{self.genderVar.get()} currently a {self.occupation_option_menu.get()}"


    def generateResults(self):
        self.displayBox.delete("0.0", tk.END)
        text = self.createText()
        self.displayBox.insert('0.0', text)





if __name__ == "__main__":
    app = App()
    app.mainloop()

