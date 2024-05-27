from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/Capi')
def Capi():
    return render_template("Capi.html")

@app.route('/Perro')
def Perro():
    return render_template("Perro.html")

@app.route('/Gato')
def Gato():
    return render_template("Gato.html")

# @app.route('/Contacto',)
# def Contacto():
#     return render_template("contacto.html")
#     # return redirect("https://www.youtube.com/watch?reload=9&v=dQw4w9WgXcQ")
@app.route('/Contacto')
def contacto():
    return render_template("Contacto.html")

@app.route('/Contacto', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Comentarios = request.form['comentarios']
        try:
            conn= pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        except Exception:
            print("ERROR")
        cursor = conn.cursor()
        cursor.execute('insert into comenta (correo,comentarios) values (%s, %s)',(aux_Correo, aux_Comentarios))
        conn.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
