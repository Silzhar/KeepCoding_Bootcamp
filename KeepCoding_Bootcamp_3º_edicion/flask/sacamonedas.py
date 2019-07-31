import sqlite3

conn = sqlite3.connect('data/movimientos.db')
cursor = conn.cursor()

def consultaMonedas():
    query = '''
            SELECT symbol, name FROM monedas;
            '''

    rows = cursor.execute(query) 

    resp = []
    for row in rows:
        resp.append(row)

    conn.close()
    return resp

def diccMonedas():
    query = '''
            SELECT id, symbol FROM monedas;
            '''
    rows = cursor.execute(query)
    resp = {}
    for row in rows:
        resp[row[0]] = row[1]
    print(resp)
    conn.close()
    return resp

diccMonedas()