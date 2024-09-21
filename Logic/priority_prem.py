class Priority:

    def processData(self, tasks):
        process_data = []

        for task in tasks:
             temp = [task[0], task[1], task[2], task[3], 0, task[2]]
             process_data.append(temp)
        result = Priority.schedulingProcess(self, process_data)
        return result

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data.sort(key=lambda x: x[1])
        '''
        Sort processes according to the Arrival Time
        '''
        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][4] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3], process_data[i][5]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[i][4] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4], process_data[i][5]])
                    normal_queue.append(temp)
                    temp = []
                    
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3], reverse=False)
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:       #if burst time is zero, it means process is completed
                    process_data[k][4] = 1
                    process_data[k].append(e_time)
                    
            if len(ready_queue) == 0:
                normal_queue.sort(key=lambda x: x[1])
                # idle = [s_time,]
                if s_time < normal_queue[0][1]:
                    # s_time = normal_queue[0][1]
                    sequence_of_process.append(-1)
                    s_time += 1
                    continue
                    # idle.append(s_time)
                    # idle_time.append(idle) if len(idle) > 0 else None
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:        #if burst time is zero, it means process is completed
                    process_data[k][4] = 1
                    process_data[k].append(e_time)
                # print("**", idle_time)
                    
        t_time = Priority.calculateTurnaroundTime(self, process_data)
        w_time = Priority.calculateWaitingTime(self, process_data)
        # Priority.printData(self, process_data, t_time, w_time, sequence_of_process)
        return sequence_of_process, t_time, w_time
        

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][6] - process_data[i][5]
            '''
            turnaround_time = completion_time - arrival_time
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        '''
        average_turnaround_time = total_turnaround_time / no_of_processes
        '''
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][2]
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        '''
        average_waiting_time = total_waiting_time / no_of_processes
        '''
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_process):
        process_data.sort(key=lambda x: x[0])
        '''
        Sort processes according to the Process ID
        '''
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):

                print(process_data[i][j], end="				")
            print()

        print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')

        print(f'Sequence of Process: {sequence_of_process}')