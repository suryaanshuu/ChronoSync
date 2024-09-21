import mysql.connector

def trial(avgWaiting, avgTurn ):

        mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='qwertyytrewq',
        database='process_scheduler'
        )

        myCursor = mydb.cursor()
        myCursor.execute("select max(simulationID) from simulation")
        simID = myCursor.fetchone()[0]
        print("SIM : ", simID)
        
        myCursor.execute("select max(id) from process")                 
        processID = myCursor.fetchone()[0]
        print("PROC : ", processID)
        
        query = "INSERT INTO result (simulationID, processIDs,averageWaitingTime,averegeTurnAroundTime) VALUES (%s, %s, %s, %s)"
        val = (simID, processID, avgWaiting, avgTurn)
        myCursor.execute(query,val)
        
        mydb.commit()  # Commit the transaction
        myCursor.close()
        mydb.close()


