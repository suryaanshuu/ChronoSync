from UI.first_window import InputWindow
from UI.second_window import InputWindow2
from UI.Priority_window import Priority_Output
from UI.fcfs_window import FCFS_Output
from UI.round_robin_window import RR_Output
from Data.insertion_values import insert_values
from Data.insert_result import trial
from Logic.priority_prem import Priority
from Logic.fcfs import Fcfs
from Logic.round_robin import RoundRobin


input_window = InputWindow()
ans = input_window.get_input_values()
input_window2 = InputWindow2(ans)
Tasks, tq = input_window2.get_input_values()

# insert_values(Tasks, tq, ans['algo'])

if ans['algo'] == "Priority":
    priority_instance = Priority()
    res = priority_instance.processData(Tasks)
    # insert_result(res)
    Tasks = list(Tasks)
    newTask = []
    for it in Tasks:
        newTask.append(list(it))
    priority_instance_output = Priority_Output(newTask, res)
    priority_instance_output.mainloop()

elif ans['algo'] == 'FCFS':
    Fcfs_instance = Fcfs()
    res = Fcfs_instance.processData(Tasks)
    # trial(res[1], res[2])
    fcfs_instance_output = FCFS_Output(Tasks, res)
    fcfs_instance_output.mainloop()
    fcfs_instance_output.destroy()

elif ans['algo'] == 'Round Robin':
    rr_instance = RoundRobin()
    res = rr_instance.processData(Tasks, int(tq))
    rr_instance_output = RR_Output(Tasks, res, tq)
    rr_instance_output.mainloop()