import mysql.connector

def notification(name):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='qwertyytrewq',
        database='process_scheduler'
    )

    myCursor = mydb.cursor()

    # Create a temporary table to store the result of the subquery
    myCursor.execute("CREATE TEMPORARY TABLE temp_table SELECT MAX(id) AS max_id FROM process WHERE name = %s", (name,))

    # Update the status using the temporary table
    myCursor.execute("UPDATE process SET status = 1 WHERE id IN (SELECT max_id FROM temp_table)")

    # Drop the temporary table
    myCursor.execute("DROP TEMPORARY TABLE IF EXISTS temp_table")

    # Fetch the max(simulationID) from the simulation table
    simQuery = "SELECT MAX(simulationID) FROM simulation"
    myCursor.execute(simQuery)
    simID = myCursor.fetchone()[0]

    # Update the latest notifications row with the simulationID
    update_query = "UPDATE notifications, (SELECT MAX(notification_id) AS max_id FROM notifications) AS temp SET notifications.simulation_id = %s WHERE notifications.notification_id = temp.max_id"
    myCursor.execute(update_query, (simID,))

    mydb.commit()

    myCursor.close()
    mydb.close()

