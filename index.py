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

if __name__ == '__main__':
    app.run(debug=True)