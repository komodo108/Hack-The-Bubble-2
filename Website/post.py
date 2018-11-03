# For flask, mysql, crypto
from flask import Blueprint, render_template, Response, request
import mysql.connector
import json
from helper
import datetime

post = Blueprint('post', __name__)

# Expected usage is that when the user clicks on a lounger and it is taken to the lounger_detail page this method will trigger the id
# will be passed into the SQL query
@post.route('/login', methods=['POST'])
def login():
    data = request.json

    if data:
        dataDict = json.loads(json.dumps(data))
        if 'user' in dataDict and 'pass' in dataDict:
            cnx, cur = start()
            query = 'SELECT `id` FROM Client WHERE `username`=%s AND `password`=%s'
            cur.execute(query, (dataDict['user'], dataDict['password']))
            theid = cur.fetchone()
            close(cnx, cur)

            if theid > 0:
                if dataDict['booked']:
                    # deal with booking
                    cnx, cur = start()
                    query = 'SELECT `id` FROM Booking WHERE `client` = %s AND start_time => %s'
                    cur.execute(query, (dataDict['user'], datetime.datetime.now()))
                    ids = cur.fetchall()
                    close(cnx, cur)

                    return Response(json.dumps({'bookings' : ids}), status=200, mimetype='application/json')
                else:
                    return Response(status=200)
            else:
                #dont
                return error()
        else:
            return error()
    else:
        return error()