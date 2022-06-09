from tkinter import SW
from flask import Flask, redirect, request,render_template, url_for

app= Flask(__name__)

usuarios = []

@app.route('/' )
def principal():
    return render_template('inicio.html')

@app.route('/Login' )
def Login():
    return render_template('login.html')

@app.route('/Registro')
def Registo():
    return render_template('registro.html')

@app.route('/Acerda_de')
def AcerdaDe():
    return render_template('acercaDe.html')

@app.route('/Introduccion')
def Introduccion():
    return render_template('intro.html')

@app.route('/Componentes1')
def Componentes1():
    return render_template('componentes.html')

@app.route('/Componentes2')
def Componentes2():
    return render_template('componentes1.html')

@app.route('/Ejemplos')
def Ejemplos():
    return render_template('ejemplo.html')

@app.route('/Plugins')
def Plugins():
    return render_template('pluginOpcionaes.html')

@app.route('/Ejemplos1')
def Ejemplos1():
    return render_template('ejemplos1.html')

if __name__ == '__main__':
    app.run(debug=True)