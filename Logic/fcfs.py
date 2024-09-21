class Fcfs:
    def processData(self, Tasks):
        ans = []
        for task in Tasks:
            ans.append(list(task))
        Tasks = ans
        # Sort tasks according to their arrival time
        Tasks = sorted(Tasks, key=lambda x: x[1])

        sequence = []
        waiting_time = []
        turnAround_time = []
        avg_waiting_time = 0
        avg_turnAround_time = 0
        time = 0
        task_count = len(Tasks)
        indx = 0
        firstFlag = True
        while indx < len(Tasks):
            # Check if current task is ready
            if Tasks[indx][2] > 0 and time >= Tasks[indx][1]:
                # Execute the current task
                sequence.append(Tasks[indx][0])
                Tasks[indx][2] -= 1
                time += 1
                if firstFlag:
                    firstFlag = False
                    waiting_time.append(time - Tasks[indx][1] - 1)
                    turnAround_time.append(Tasks[indx][2] + waiting_time[-1] + 1)
            elif time < Tasks[indx][1]:
                time += 1
                sequence.append(-1)
            else:
                indx += 1
                firstFlag = True
                
        
        
        avg_waiting_time = round(sum(waiting_time) / len(Tasks),2)
        avg_turnAround_time = round(sum(turnAround_time) / len(Tasks),2)
        return sequence, avg_waiting_time, avg_turnAround_time

