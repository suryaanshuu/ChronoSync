import customtkinter as ctk
import tkinter as tk

class InputWindow:
    '''
        The first window which comes up in the program, necessary to take inputs such as number of tasks and algorithm
        This information is later used to call second window where user inputs the details of n tasks
    '''
    def __init__(self):
        self.root = ctk.CTk()
        self.input_values = {'n': None, 'algo': None}
        self.create_first_window()
        
    def handleSubmit(self):
        n = int(self.entry1.get())
        algo = self.algo_input.get()
        if 0 <= n <= 10:
            self.input_values['n'], self.input_values['algo'] = n, algo
            self.root.destroy()
        else:
            invalid_label = ctk.CTkLabel(
                self.main_frame,
                text='Invalid number of Tasks!!',
                text_color='red',
                bg_color='#1d1c22'
            )
            invalid_label.place(x=220, y=290)
    
    def create_first_window(self):
        self.root.title("CPU Task Scheduler")

        self.main_frame = tk.Frame(self.root, width=740, height=493)
        self.main_frame.pack_propagate(False)
        self.main_frame.pack()

        background_image = tk.PhotoImage(file="Assect/bg_img.png")  # Replace with your image file path
        background_label = tk.Label(self.main_frame, image=background_image)
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.entry1 = ctk.CTkEntry(
            self.main_frame,
            width=120,
            height=40,
            placeholder_text='Number of tasks',
            corner_radius=10,
            bg_color='#1d1c22',
            placeholder_text_color='#e9e084',
            font=("Verdana", 12)
        )
        self.entry1.place(x=235, y=90)

        self.algo_input = ctk.CTkComboBox(
            self.main_frame,
            values=['Priority', 'Round Robin', 'FCFS'],
            bg_color='#1d1c22',
            font=("Verdana", 12),
            dropdown_fg_color='#1d1c22',
            dropdown_text_color='#e9e084',
            text_color='#e9e084',
            dropdown_hover_color='blue',
            width=150,
            height=35
        )
        self.algo_input.place(x=227, y=160)

        submitButton = ctk.CTkButton(
            self.main_frame,
            text='Submit',
            corner_radius=25,
            fg_color='#e9e084',
            hover_color='#9c9658',
            border_color='purple',
            text_color='black',
            bg_color='#1d1c22',
            width=100,
            height=35,
            command=self.handleSubmit
        )
        submitButton.place(x=245, y=240)
        
        self.root.mainloop()

    def get_input_values(self):
        return self.input_values
