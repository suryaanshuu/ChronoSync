# '''
#     This part of code is used to create database and tables. 
#     Replace the connector creds with yours, 
#     then run the commented commands one by one to create database, table and more
# '''

# import mysql.connector
# # myCursor.execute("CREATE DATABASE process_scheduler")

# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='qwertyytrewq',
#     database='process_scheduler'
# )

# myCursor = mydb.cursor()

# #creating the table

# myCursor.execute("""
#     CREATE TABLE process (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(20),
#         arrival_time INT,
#         burst_time INT,
#         priority INT DEFAULT -1,
#         execution_time INT DEFAULT -1,
#         completion_time INT DEFAULT -1
#     )
# """)

# myCursor.execute("""
#     CREATE TABLE algorithm (
#         id INT PRIMARY KEY,
#         name VARCHAR(20)
#     )
# """)

# myCursor.execute("""
#     CREATE TABLE simulation (
#         simulationID INT AUTO_INCREMENT PRIMARY KEY,
#         algorithmID INT,
#         Timequantum INT,
#         Numberof_processes INT,
#         SimulationTime INT,
#         FOREIGN KEY (algorithmID) REFERENCES algorithm(id),
#         processIDs VARCHAR(255)
#     )
# """)


# myCursor.execute("""
#     CREATE TABLE result (
#         resultID INT AUTO_INCREMENT PRIMARY KEY,
#         simulationID INT,
#         processIDs VARCHAR(255),
#         averageWaitingTime INT,
#         averegeTurnAroundTime INT,
#         FOREIGN KEY (simulationID) REFERENCES simulation(simulationID),
#     )
# """)

# sql = "INSERT INTO algorithm (id, name) VALUES (%s, %s)"
# val = (1, "Priority_S")
# myCursor.execute(sql, val)

# sql = "INSERT INTO algorithm (id, name) VALUES (%s, %s)"
# val = (2, "RRobin_S")
# myCursor.execute(sql, val)

# mydb.commit()

