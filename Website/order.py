import helper

def makeOrder(order):
    cur, con = helper.start()

    cur.execute(
        'SELECT COUNT(Order.id) FROM Order;'
    )

    number_before = cur.fetchone()

    for val in order:
        cur.execute(
            'INSERT INTO Order (booking, item, quantity)'
            'VALUES (%s, %s, %s);',
            (val[0], val[1], val[2])
        )

    cur.execute(
        'SELECT COUNT(Order.id) FROM Order;'
    )

    number_after = cur.fetchone()

    did_work = False

    if((number_after[0] - number_before[0]) == len(order)):
        did_work = True

    con.commit()

    helper.stop(con, cur)

    return did_work