import mysql.connector
import helper
import datetime

def getBooked():
    con, cur = helper.start()
    current_dt = datetime.datetime.now()

    # Get Data
    cur.execute(
        'SELECT Lounger.id'
        ' FROM Booking'
        ' INNER JOIN Lounger ON Booking.lounger = Lounger.id'
        ' WHERE Booking.start_time < %s AND Booking.finish_time > %s;',
        (current_dt, current_dt)
    )
    booking_result = cur.fetchall()

    for val in booking_result:
        print(val)
    
    # Close Down
    helper.stop(con, cur)

    # Return array of integers
    return booking_result

getBooked()
    
def getLoungerInfo(id):
    con, cur = helper.start() 

    cur.execute(
        'SELECT Lounger.name, Lounger.desc'
        'FROM Lounger'
        'WHERE Lounger.id = %s'
        'LIMIT 1;',
        (id)
    )
    lounger_info = cur.fetchall()

    helper.stop(cur, con)

    return lounger_info