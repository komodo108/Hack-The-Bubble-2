# For flask, mysql, crypto
from flask import Blueprint, render_template, Response, request
import mysql.connector
import json
import helper
import datetime

post = Blueprint('post', __name__)

@post.route('/booking', methods=['POST'])
def book():
    data = request.json

    if data:
        dataDict = json.loads(json.dumps(data))
        if 'lounger' in dataDict and 'start_time' in dataDict and 'finish_time' in dataDict and 'client' in dataDict:
            now = datetime.datetime.now()
            if datetime.datetime.strptime(dataDict['start_time'], "%Y-%m-%d %H:%M:%S") >= now and datetime.datetime.strptime(dataDict['finish_time'], "%Y-%m-%d %H:%M:%S") > datetime.datetime.strptime(dataDict['start_time'], "%Y-%m-%d %H:%M:%S"):
                # Check client
                cnx, cur = helper.start()
                query = 'SELECT `id` FROM Client WHERE `id` = %s'
                cur.execute(query, (dataDict['client'], ))
                num = cur.rowcount
                cur.close()

                if num > 0:
                    # Times & Client are okay
                    # Check if the thing is free
                    cur = cnx.cursor()
                    query = 'SELECT `id` FROM Booking WHERE `start_time` <= %s AND `finish_time` >= %s'
                    cur.execute(query, (dataDict['start_time'], dataDict['finish_time']))
                    num = cur.rowcount
                    cur.close()

                    if num == 0 and dataDict['lounger'] > 0:
                        #Everything is good!
                        cur = cnx.cursor()
                        query = 'INSERT INTO Booking (`lounger`, `start_time`, `finish_time`, `client`) VALUES (%s, %s, %s, %s)'
                        cur.execute(query, (dataDict['lounger'], dataDict['start_time'], dataDict['finish_time'], dataDict['client']))
                        cnx.commit()
                        cur.close()

                        # Now get the deails!
                        cur = cnx.cursor()
                        query = 'SELECT `id` FROM Booking WHERE `lounger` = %s AND `start_time` = %s AND `finish_time` = %s AND `client` = %s'
                        cur.execute(query, (dataDict['lounger'], dataDict['start_time'], dataDict['finish_time'], dataDict['client']))
                        theid = cur.fetchone()
                        helper.stop(cnx, cur)

                        return Response(json.dumps({'booking' : theid}), status=200, mimetype='application/json')
                    else:
                        print("1")
                        return helper.error()
                else:
                    print("2")
                    return helper.error()
            else:
                print("3")
                return helper.error()
        else:
            return helper.error()
    else:
        return helper.error()

@post.route('/login', methods=['POST'])
def login():
    print(request.json)
    data = request.json

    if data:
        dataDict = json.loads(json.dumps(data))
        if 'user' in dataDict and 'pass' in dataDict:
            cnx, cur = helper.start()
            query = 'SELECT `id` FROM Client WHERE `username`=%s AND `password`=%s'
            cur.execute(query, (dataDict['user'], dataDict['pass']))
            theid = cur.fetchone()
            helper.stop(cnx, cur)

            if theid[0] > 0:
                if dataDict['booking']:
                    # deal with booking
                    cnx, cur = helper.start()
                    query = 'SELECT MAX(id) FROM Booking WHERE `client` = %s AND `start_time` >= %s'
                    cur.execute(query, (theid[0], datetime.datetime.now()))
                    ids = cur.fetchone()
                    helper.stop(cnx, cur)

                    return Response(json.dumps({'bookings' : ids}), status=200, mimetype='application/json')
                else:
                    return Response(status=200)
            else:
                return helper.error()
        else:
            return helper.error()
    else:
        return helper.error()