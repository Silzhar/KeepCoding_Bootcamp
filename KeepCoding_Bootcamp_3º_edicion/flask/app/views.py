
from app import app
from flask import render_template, request, redirect, url_for, flash
import csv, sqlite3
from os import remove, rename
from app.forms import CompraForm, UpdateForm

ficheromovimientos = 'data/movimientos.txt'
ficheronuevo = 'data/nuevomovimientos.txt'
database = 'data/movimientos.db'

def diccionarioMonedas():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    query = '''
            SELECT id, symbol FROM monedas;
            '''
    rows = cursor.execute(query)
    resp = {}
    for row in rows:
        resp[row[0]] = row[1]
    conn.close()
    return resp

@app.route('/')
def index():
    #leer movimientos
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    _dMonedas = diccionarioMonedas()

    rows = cursor.execute("select fecha, concepto, id_moneda_comprada, cantidadComprada, id_moneda_pagada, cantidadPagada, id from movimientos order by fecha;")

    movements = []
    for row in rows:
        print(row)
        row = list(row)
        nombreMoneda = _dMonedas[row[2]]
        row[2] = nombreMoneda

        nombreMoneda = _dMonedas[row[4]]
        row[4] = nombreMoneda
        movements.append(row)
    '''
    fMovimientos = open(ficheromovimientos, "r")
    csvreader = csv.reader(fMovimientos, delimiter=',', quotechar='"')
    movements = []
    for movimiento in csvreader: 
        movements.append(movimiento)
    '''
    conn.close()
    #enviar movimientos a index.html
    return render_template('index.html', movimientos=movements)

@app.route('/nuevacompra', methods=['GET', 'POST'])
def compra():
    form = CompraForm(request.form)
    


    if request.method == 'GET':
        return render_template('nuevacompra.html', form=form)
    else:
        form.monedaComprada.data = int(form.monedaComprada.data)
        form.monedaPagada.data = int(form.monedaPagada.data)
        if form.validate():
            conn = sqlite3.connect(database)
            cursor = conn.cursor()
            query = '''
            INSERT INTO movimientos 
                (fecha, concepto, id_moneda_Comprada, cantidadComprada, id_moneda_pagada, cantidadPagada)
                values (?, ?, ?, ?, ?, ?);
            '''

            try:
                rows = cursor.execute(query,(request.form['fecha'],
                                            request.form['concepto'], 
                                            request.form['monedaComprada'], 
                                            request.form['cantidadComprada'], 
                                            request.form['monedaPagada'], 
                                            request.form['cantidadPagada']
                ))
            except sqlite3.Error as e:
                form.monedaComprada.data = str(form.monedaComprada.data)
                form.monedaPagada.data = str(form.monedaPagada.data)
                return render_template('nuevacompra.html', form=form)


            conn.commit()
            conn.close()
            return redirect(url_for('index'))

        form.errors['general'] = ['Error acceso a base de datos']

        return render_template('nuevacompra.html', form=form)

        '''
        fMovimientos = open(ficheromovimientos, "a+")
        precioUnitario = float(request.values['cantidadPagada'])/float(request.values['cantidadComprada'])
        registro = '{},"{}",{},{},{},{},{}\n'.format(request.values['fecha'], 
                    request.values['concepto'], 
                    request.values['monedaComprada'], 
                    request.values['cantidadComprada'], 
                    request.values['monedaPagada'], 
                    request.values['cantidadPagada'], 
                    precioUnitario)
        fMovimientos.write(registro)
        fMovimientos.close()
        '''
            

        


@app.route('/modificar', methods=['GET', 'POST'])
def update():
    form = UpdateForm(request.form)

    if request.method == 'GET':
        if request.values.get('ix'):
            movimiento = recuperarregistro(request.values.get('ix'))
            print(movimiento)

            nombre = ['ix', 'fecha', 'concepto', 'monedaComprada', 'cantidadComprada', 'monedaPagada', 'cantidadPagada']
            for i in range(len(nombre)):
                form[nombre[i]].data = movimiento[i]

            '''
            contador = 0
            for campo in nombre:
                form[campo].data = movimiento[contador]
                contador += 1
            form.fecha.data = movimiento[0]
            form.concepto.data = movimiento[1]
            form.monedaComprada.data = movimiento[2]
            form.cantidadComprada.data = movimiento[3]
            form.monedaPagada.data = movimiento[4]
            form.cantidadPagada.data = movimiento[5]
            '''
            return render_template('update.html', form=form)
        
    else:
        form.monedaComprada.data = int(form.monedaComprada.data)
        form.monedaPagada.data = int(form.monedaPagada.data)

        if form.validate():
            registro_seleccionado = [
                form.fecha.data,
                request.values['fecha'],
                request.values['concepto'],
                request.values['monedaComprada'],
                request.values['cantidadComprada'],
                request.values['monedaPagada'],
                request.values['cantidadPagada']
            ]
            modificarregistro(request.values)
            return redirect(url_for('index'))
        return render_template('update.html', form=form)

@app.route('/procesarregistro', methods=['POST'])
def procesar():
    if request.values.get('ix'):
        if request.values['btnselected'] == 'Borrar':
            borrar(int(request.values['ix']))
        else:
            #modificar(int(request.values['ix']))
            return redirect(url_for('update', ix=request.values['ix']))
    return redirect(url_for('index'))

def recuperarregistro(ix):
    ix = int(ix)

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    query = '''
            select id, fecha, concepto, id_moneda_comprada, cantidadComprada, id_moneda_pagada, cantidadPagada from movimientos where id = ?;
            '''

    rows = cursor.execute(query, (ix,))


    resp = []
    for row in rows:
        resp.append(row)

    conn.close()

    if len(resp) > 0:
        registro = list(resp[0])
        registro[3] = str(registro[3])
        registro[5] = str(registro[5])
        return registro
    else:
        return ()    


    
def modificarregistro(values):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    query = '''
        update movimientos 
           set fecha = ?,
               concepto = ?,
               id_monedaComprada = ?,
               cantidadComprada = ?,
               id_monedaPagada = ?,
               cantidadPagada = ?
          where id = ?;
          ''' 
    rows = cursor.execute(query, (values.get('fecha'), values.get('concepto'),
                                  values.get('monedaComprada'), values.get('cantidadComprada'),
                                  values.get('monedaPagada'), values.get('cantidadPagada'),
                                  values.get('ix')
            ))
    conn.commit()
    conn.close() 


    '''
    fe = open(ficheromovimientos, 'r')
    fs = open(ficheronuevo, 'w')
    ix = int(values.get('ix'))
    precioUnitario = float(values['cantidadPagada'])/float(values['cantidadComprada'])
    registro = '{},"{}",{},{},{},{},{}\n'.format(values['fecha'], 
                values['concepto'], 
                values['monedaComprada'], 
                values['cantidadComprada'], 
                values['monedaPagada'], 
                values['cantidadPagada'], 
                precioUnitario)
    contador = 1
    for linea in fe:
        if contador == ix:
            linea = registro
        fs.write(linea)
        contador += 1
    fe.close()
    fs.close()
    remove(ficheromovimientos)
    rename(ficheronuevo, ficheromovimientos)
    '''
    
def borrar(ix):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    query = '''
            delete from movimientos
            where id = ?;
            '''

    try:
        rows = cursor.execute(query, (ix,))
    except Exception as e:
        print(e)
        return

    conn.commit()
    conn.close()





    '''
    fe = open(ficheromovimientos, 'r')
    fs = open(ficheronuevo, 'w')

    contador = 1
    for linea in fe:
        if contador != ix:
            fs.write(linea)
        contador += 1
    fe.close()
    fs.close()

    remove(ficheromovimientos)
    rename(ficheronuevo, ficheromovimientos)   '''


def validar(values):
    errores = []
    if values['fecha'] == '':
        errores.append('Debe informar la fecha')
    
    if values['concepto'] == '':
        errores.append('Debe informar el concepto')

    if values['cantidadComprada'] == '':
        errores.append('Debe informar la cantidad comprada')

    if values['cantidadPagada'] == '':
        errores.append('Debe informar la cantidad pagada')   

    if len(errores) == 0:
        return True
    else:
        return errores    

        
''''

msg = validar(request.values)
        if msg != True:
            return render_template('nuevacompra.html', errores=msg)



    if request.method == 'GET':
        registro = request.value('ix')
        return redirect(url_for('compra')) 
    else:
        msg = validar(request.values)
        if msg != True:
            return  redirect(url_for('compra', errores=msg))  

    
        fMovimientos = open(ficheromovimientos, "a+")
        precioUnitario = float(request.values['cantidadPagada'])/float(request.values['cantidadComprada'])
        registro = '{},"{}",{},{},{},{},{}\n'.format(request.values['fecha'], 
                    request.values['concepto'], 
                    request.values['monedaComprada'], 
                    request.values['cantidadComprada'], 
                    request.values['monedaPagada'], 
                    request.values['cantidadPagada'], 
                    precioUnitario)
        fMovimientos.seek(registro, ix)
        fMovimientos.close()
        return redirect(url_for('index'))   '''