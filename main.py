from flask import Flask, render_template #Importando flask para a sua criação
from flask import request, redirect

import this
this.resultado = ""
this.num1 = 0
this.num2 = 0
import menu #chamando uma classe
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/soma", methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        this.resultado = soma.sum(num1,num2)
        return redirect('/soma/resultado')
    elif request.method == 'GET':
        this.resultado = 5+5
    return render_template("soma.html", titulo="Soma")

@app.route("/soma/resultado", methods=['POST', 'GET'])
def result():
    return render_template("resultado.html", titulo="Resultado", resultado=this.resultado)

if __name__ == "__main__":
    app.run(debug=True)