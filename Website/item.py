import helper

def getItems():
    con, cur = helper.start()

    cur.execute(
        'SELECT Item.name, Item.price'
        'FROM Item;'
    )

    item_array = cur.fetchall()

    helper.stop(con, cur)

    return item_array