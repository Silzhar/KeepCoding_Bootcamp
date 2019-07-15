
from app import app
from flask import render_template
import csv

ficheromovimientos = 'data/movimientos.txt'

@app.route('/')
def index():
    # leer movimientos
    fMovimientos = open(ficheromovimientos, "r")
    csvreader = csv.reader(fMovimientos, delimiter=',', quotechar='"')
    movimientos = []
    for movimiento in csvreader:
        movimientos.append(movimiento)
        
    # enviarlos a index.html

    return render_template('index.html')

@app.route('/adios')
def second_page():
    return render_template('adios.html', datos_asociados)
    