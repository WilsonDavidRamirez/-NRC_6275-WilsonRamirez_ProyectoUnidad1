from tkinter import SW
from flask import Flask, redirect, request,render_template, url_for

app= Flask(__name__)

tareasPendientes = []

@app.route('/' )

def principal():
    return render_template('pagina1.html', tareasLista = tareasPendientes)


@app.route('/enviar',  methods=['GET','POST'])

def enviar():
    if(request.method == "POST"):
        tareas = request.form['tarea']
        correos = request.form['correo']
        prioridades = request.form['prioridad']
        tareasPendientes.append({'tarea': tareas, 'correo': correos, 'prioridad': prioridades })
        return redirect(url_for('principal'))


# main del programa 
if __name__ == '__main__':
    #debug = true, para reiniciar automaticamente el servidor, tiempo de desarrollo 
    app.run(debug=True)