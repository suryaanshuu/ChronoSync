import mysql.connector

def insert_values(Tasks, tq, algo):
    '''
        This function takes an array of tasks and time quantum and stores them to database.
        Stores to Process, Simulation table
    '''    
    
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='qwertyytrewq',
        database='process_scheduler'
    )
    myCursor = mydb.cursor()
    
    # Ensure 'Tasks' is a list of tuples where each tuple represents a row to be inserted
    query = "INSERT INTO process (name, arrival_time, burst_time, priority, execution_time, completion_time) VALUES (%s, %s, %s, %s, %s, %s)"
    myCursor.executemany(query, Tasks)
    
    tasks_name = ""
    for i in Tasks:
            tasks_name = tasks_name + i[0] + ' '
            
    if algo == 'FCFS':
        algoID = 3
    elif algo == 'Priority':
        algoID = 1
    else:
        algoID = 2
    
    query = "INSERT INTO simulation (algorithmID, TimeQuantum, Numberof_processes, SimulationTime, processIDs) VALUES (%s, %s, %s, %s, %s)"
    val = (algoID, tq, len(Tasks), -1, tasks_name)
    myCursor.execute(query,val)
    
    mydb.commit()  # Commit the transaction
    print(myCursor.rowcount, "record(s) inserted.")
    
    # myCursor.execute("select * from process")
    # myCursor.execute("select * from simulation")

    myCursor.close()
    mydb.close()
