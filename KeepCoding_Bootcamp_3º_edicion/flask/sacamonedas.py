import sqlite3

conn = sqlite3.connect('data/movimientos.db')
cursor = conn.cursor()

def consultaMonedas():
    query = '''
            SELECT symbol,name FROM MONEDAS:
            '''

    rows = cursor.execute(query)

    respuesta = []
    for row in rows:
        respuesta.append(row)


    conn.close()
    return respuesta


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