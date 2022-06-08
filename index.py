from tkinter import SW
from flask import Flask, redirect, request,render_template, url_for

app= Flask(__name__)

tareasPendientes = []

@app.route('/' )

def principal():
    return render_template('inicio.html')

if __name__ == '__main__':
    app.run(debug=True)