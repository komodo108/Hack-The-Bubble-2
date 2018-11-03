import mysql.connector

def start (): 
    connect = mysql.connector.connect(
        user = 'password', 
        password = 'username123',
        host = 'hackin.cvv0hvbeezdl.us-east-2.rds.amazonaws.com',
        database = 'password', 
        buffered = True
    )
    cursor = connect.cursor()
    return connect, cursor

def stop (con, cursor):
    cursor.close()
    con.close()

