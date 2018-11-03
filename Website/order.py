import helper

# Expecting an array of tuples as input parameter
def makeOrder(order):
    # Make the connection and cursor
    con, cur = helper.start()

    all_orders = order[0]


    # Get the size of order table before the new order is added
    cur.execute(
        'SELECT COUNT(Order.id) FROM password.Order;'
    )

    number_before = cur.fetchone()
    number_before = number_before[0]

    # Iterate through the array of arrays in the order
    # Adding them to the table
    # Is there a better way to generate this? 
    # Can i pre calculate the order values as a string

    for val in all_orders:
        

        cur.execute(
            'INSERT INTO password.Order (booking, item, quantity) '
            'VALUES (%s, %s, %s);',
            (booking, item, quantity)
        )

        con.commit();

    # Get the size of order table after the new order is added
    cur.execute(
        'SELECT COUNT(Order.id) FROM password.Order;'
    )

    number_after = cur.fetchone()
    number_after = number_after[0]

    # Check th right number of orders have been added
    did_work = False
    if((number_after - number_before) == len(order)):
        did_work = True

    print(did_work)

    helper.stop(con, cur)

    return did_work
