import customtkinter as ctk
from PIL import Image, ImageTk
import time
# from Data.notification import notification



class Priority_Output(ctk.CTk):
    def __init__(self, Tasks, Sqe_Result):
        super().__init__()
        self.geometry("1000x550")
        self.progress_bar_list = []
        self.Tasks = list(Tasks)
        
        self.avg_waiting = round(Sqe_Result[1],2)
        self.avg_turnAround = round(Sqe_Result[2],2)
        self.Sqe_Result = Sqe_Result[0]
        
        for i in range(len(self.Tasks)):
            self.Tasks[i][4] = 0
        self.counter = 0
        
        # Main Frame
        self.main_frame = ctk.CTkFrame(self, width=1000, height=550)
        self.main_frame.pack_propagate(False)
        self.main_frame.pack()

        # Background Image
        image_path = "Assect/back01_big.png"
        img = Image.open(image_path)
        background_image = ImageTk.PhotoImage(img)
        background_label = ctk.CTkLabel(
            self.main_frame, image=background_image, text=""
        )
        background_label.image = background_image
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Title Label
        Title_Label = ctk.CTkLabel(
            self.main_frame,
            text="Priority Scheduling (preemptive)",
            font=("Verdana", 30),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='transparent'
        )
        Title_Label.place(x=170, y=10)

        # Time Labels
        self.time = 1   
        self.Time_Time = ctk.CTkLabel(
            self.main_frame,
            text="Time: ",
            font=("Verdana", 25),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='transparent',
        )
        self.Time_Time.place(x=30, y=100)

        self.Time_Value = ctk.CTkLabel(
            self.main_frame,
            text=self.time,
            font=("Verdana", 35),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='transparent',
        )
        self.Time_Value.place(x=170, y=95)

        # Other Labels
        Waiting_Label = ctk.CTkLabel(
            self.main_frame,
            text="Avg Waiting Time: ",
            font=("Verdana", 25),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='transparent',
        )
        Waiting_Label.place(x=30, y=300)
        
        Waiting_Label_Value = ctk.CTkLabel(
            self.main_frame,
            text=self.avg_waiting,
            font=("Verdana", 25),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='transparent',
        )
        Waiting_Label_Value.place(x=285, y=300)

        TurnAround = ctk.CTkLabel(
            self.main_frame,
            text="Avg Turn Around Time: ",
            font=("Verdana", 25),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='transparent',
        )
        TurnAround.place(x=30, y=400)

        TurnAround_value = ctk.CTkLabel(
            self.main_frame,
            text=self.avg_turnAround,
            font=("Verdana", 25),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='transparent',
        )
        TurnAround_value.place(x=350, y=400)

        # Task Labels and Progress Bars
        i = 0
        x = 550
        y = 100

        for k in range(len(Tasks)):
            TurnAround = ctk.CTkLabel(
                self.main_frame,
                text=Tasks[k][0],
                font=("Verdana", 25),
                text_color='#37c9ef',
                bg_color='transparent',
            )
            TurnAround.place(x=x, y=y)

            progress_bar = ctk.CTkProgressBar(
                self.main_frame,
                orientation='horizontal',
                width=280,
                height=30,
                progress_color='#2588a2',
            )
            progress_bar.place(x=x + 100, y=y)
            progress_bar.set(0.0)
            self.progress_bar_list.append(progress_bar)
            i += 1
            y += 75

        # Start the updates after initialization
        print("")
        print("")
        print("")
        self.update_progress_bars(0)

    def update_progress_bars(self, index):
        if index < len(self.Sqe_Result):
            self.counter += 1
            task = self.Sqe_Result[index]
            self.Time_Value.configure(text=self.time)
            self.time += 1
            if task != -1:
                for j in range(len(self.Tasks)):
                    if self.Tasks[j][0] == task:
                        break
                self.Tasks[j][4] += 1
                completion_percentage = (self.Tasks[j][4] / self.Tasks[j][2]) 
                self.progress_bar_list[j].set(round(completion_percentage,3))
                if round(completion_percentage,3) == 1:
                    print(self.Tasks[j][0], " done!!!")
                    print("")
                    # notification(self.Tasks[j][0])

            # Schedule the next update after 1000 milliseconds (1 second)
            self.after(1000, self.update_progress_bars, index + 1)
        else:
            print("")
            print("Priority Scheduling DONE !!")