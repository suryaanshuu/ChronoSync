import customtkinter as ctk
import tkinter as tk

class InputWindow2:
    '''
        After taking the number of tasks and type of algo from the first window, this one will take n task name,
        arrival time, burst time, priority(in Priority_S), time quantum(in RoundRobin_S) 
    '''
    def __init__(self,ans):
        self.n = ans['n']
        self.algo = ans['algo']
        self.root = ctk.CTk()
        self.tasks = []
        self.at = []
        self.bt = []
        self.pt = []
        self.task_info = []
        self.tQ = -1
        if self.algo == 'Priority':
            self.priority_s_input(self.n)
        elif self.algo == 'Round Robin':    
            self.rr_s_input(self.n)
        elif self.algo == 'FCFS':
            self.fcfs_input(self.n)
            
        
    def Priority_handleSubmit(self):
        for i in range(len(self.tasks)):
            self.task_info.append((
                self.tasks[i].get(),
                int(self.at[i].get()),
                int(self.bt[i].get()),
                int(self.pt[i].get()),
                -1,  #Execution time initialized to -1
                -1   #Completion time initialized to -1
            ))
        self.root.destroy()
        
        # for i in self.task_info:
        #     print(i)
    
    def priority_s_input(self,n):
        self.root.title("Priority Scheduling")

        self.main_frame = tk.Frame(self.root, width=600, height=max(600,150*n))
        self.main_frame.pack_propagate(False)
        self.main_frame.pack()

        background_image = tk.PhotoImage(file="Assect/bg1.png")
        background_label = tk.Label(self.main_frame, image=background_image)
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        x, y = 40, 40
        for i in range(0,n):
            placeholder = 'Task ' + str(i+1)
            self.task = ctk.CTkEntry(
                self.main_frame,
                width=100,
                height=40,
                placeholder_text=placeholder,
                corner_radius=10,
                bg_color='#1d1c22',
                placeholder_text_color='#e9e084',
                font=("Verdana", 12)
            )
            self.task.place(x=x, y=y)
            self.tasks.append(self.task)
            x += 105
            
            
            placeholder = 'Arrival Time ' + str(i+1)
            
            self.arrivalTime = ctk.CTkEntry(
                self.main_frame,
                width=100,
                height=40,
                placeholder_text=placeholder,
                corner_radius=10,
                bg_color='#1d1c22',
                placeholder_text_color='#e9e084',
                font=("Verdana", 12)
            )
            self.arrivalTime.place(x=x, y=y)
            self.at.append(self.arrivalTime)
            x += 105
            
            placeholder = 'Burst Time ' + str(i+1)
            self.burstTime = ctk.CTkEntry(
                self.main_frame,
                width=100,
                height=40,
                placeholder_text=placeholder,
                corner_radius=10,
                bg_color='#1d1c22',
                placeholder_text_color='#e9e084',
                font=("Verdana", 12)
            )
            self.burstTime.place(x=x, y=y)
            self.bt.append(self.burstTime)
            x += 105

            placeholder = 'Priority  ' + str(i+1)
            self.taskPriority = ctk.CTkEntry(
                self.main_frame,
                width=100,
                height=40,
                placeholder_text=placeholder,
                corner_radius=10,
                bg_color='#1d1c22',
                placeholder_text_color='#e9e084',
                font=("Verdana", 12)
            )
            self.taskPriority.place(x=x, y=y)
            self.pt.append(self.taskPriority)
            x += 105
            
            y += 100
            x = 40

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
            command=self.Priority_handleSubmit
        )
        submitButton.place(x=200, y=y)
        
        self.root.mainloop()
        
    
    def rr_handleSubmit(self):
        self.tQ = self.tq.get()
        for i in range(len(self.tasks)):
            self.task_info.append((
                self.tasks[i].get(),
                int(self.at[i].get()),
                int(self.bt[i].get()),
                -1,  #Priority set to -1 in RR algo
                -1,  #Execution time initialized to -1
                -1   #Completion time initialized to -1
            ))
        self.root.destroy()
        
        # for i in self.task_info:
        #     print(i)
    
    def rr_s_input(self,n):
        self.root.title("Round Robin Scheduling")

        self.main_frame = tk.Frame(self.root, width=600, height=max(600,150*n))
        self.main_frame.pack_propagate(False)
        self.main_frame.pack()

        background_image = tk.PhotoImage(file="Assect/bg2.png")
        background_label = tk.Label(self.main_frame, image=background_image)
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.tq = ctk.CTkEntry(
            self.main_frame,
            width=130,
            height=40,
            placeholder_text="Time Quantum",
            corner_radius=10,
            bg_color='#2e2e2e',
            placeholder_text_color='#e9e084',
            font=("Verdana", 12)
        )
        self.tq.place(x=160, y=10)
        
        x, y = 40, 80
        for i in range(0,n):
            placeholder = 'Task ' + str(i+1)
            self.task = ctk.CTkEntry(
                self.main_frame,
                width=100,
                height=40,
                placeholder_text=placeholder,
                corner_radius=10,
                bg_color='#2e2e2e',
                placeholder_text_color='#e9e084',
                font=("Verdana", 12)
            )
            self.task.place(x=x, y=y)
            self.tasks.append(self.task)
            x += 120
            
            
            placeholder = 'Arrival Time ' + str(i+1)
            
            self.arrivalTime = ctk.CTkEntry(
                self.main_frame,
                width=120,
                height=40,
                placeholder_text=placeholder,
                corner_radius=10,
                bg_color='#2e2e2e',
                placeholder_text_color='#e9e084',
                font=("Verdana", 12)
            )
            self.arrivalTime.place(x=x, y=y)
            self.at.append(self.arrivalTime)
            x += 140
            
            placeholder = 'Burst Time ' + str(i+1)
            self.burstTime = ctk.CTkEntry(
                self.main_frame,
                width=100,
                height=40,
                placeholder_text=placeholder,
                corner_radius=10,
                bg_color='#2e2e2e',
                placeholder_text_color='#e9e084',
                font=("Verdana", 12)
            )
            self.burstTime.place(x=x, y=y)
            self.bt.append(self.burstTime)
            x += 140

            y += 80
            x = 40

        submitButton = ctk.CTkButton(
            self.main_frame,
            text='Submit',
            corner_radius=25,
            fg_color='#e9e084',
            hover_color='#9c9658',
            border_color='purple',
            text_color='black',
            bg_color='#1f1f1f',
            width=100,
            height=35,
            command=self.rr_handleSubmit
        )
        submitButton.place(x=170, y=y)
        
        self.root.mainloop()
    

    def fcfs_input(self,n):
        self.root.title("FCFS Scheduling")

        self.main_frame = tk.Frame(self.root, width=600, height=max(600,150*n))
        self.main_frame.pack_propagate(False)
        self.main_frame.pack()

        background_image = tk.PhotoImage(file="Assect/bg2.png")
        background_label = tk.Label(self.main_frame, image=background_image)
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # self.tq = ctk.CTkEntry(
        #     self.main_frame,
        #     width=130,
        #     height=40,
        #     placeholder_text="Time Quantum",
        #     corner_radius=10,
        #     bg_color='#2e2e2e',
        #     placeholder_text_color='#e9e084',
        #     font=("Verdana", 12)
        # )
        # self.tq.place(x=160, y=10)
        
        x, y = 40, 40
        for i in range(0,n):
            placeholder = 'Task ' + str(i+1)
            self.task = ctk.CTkEntry(
                self.main_frame,
                width=100,
                height=40,
                placeholder_text=placeholder,
                corner_radius=10,
                bg_color='#2e2e2e',
                placeholder_text_color='#e9e084',
                font=("Verdana", 12)
            )
            self.task.place(x=x, y=y)
            self.tasks.append(self.task)
            x += 120
            
            
            placeholder = 'Arrival Time ' + str(i+1)
            
            self.arrivalTime = ctk.CTkEntry(
                self.main_frame,
                width=120,
                height=40,
                placeholder_text=placeholder,
                corner_radius=10,
                bg_color='#2e2e2e',
                placeholder_text_color='#e9e084',
                font=("Verdana", 12)
            )
            self.arrivalTime.place(x=x, y=y)
            self.at.append(self.arrivalTime)
            x += 140
            
            placeholder = 'Burst Time ' + str(i+1)
            self.burstTime = ctk.CTkEntry(
                self.main_frame,
                width=100,
                height=40,
                placeholder_text=placeholder,
                corner_radius=10,
                bg_color='#2e2e2e',
                placeholder_text_color='#e9e084',
                font=("Verdana", 12)
            )
            self.burstTime.place(x=x, y=y)
            self.bt.append(self.burstTime)
            x += 140

            y += 80
            x = 40

        submitButton = ctk.CTkButton(
            self.main_frame,
            text='Submit',
            corner_radius=25,
            fg_color='#e9e084',
            hover_color='#9c9658',
            border_color='purple',
            text_color='black',
            bg_color='#1f1f1f',
            width=100,
            height=35,
            command=self.fcfs_handleSubmit
        )
        submitButton.place(x=170, y=y)
        
        self.root.mainloop()
        
    def fcfs_handleSubmit(self):
        for i in range(len(self.tasks)):
            self.task_info.append((
                self.tasks[i].get(),
                int(self.at[i].get()),
                int(self.bt[i].get()),
                -1,  #Priority set to -1 in RR algo
                -1,  #Execution time initialized to -1
                -1   #Completion time initialized to -1
            ))
        self.root.destroy()
    

    def get_input_values(self):
        '''
            This function returns an array of tasks(with its info) and Time Quantum (only in RR), all these
            necessary things are called by the constructor itself
        '''
        return self.task_info,self.tQ
