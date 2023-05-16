from flask import Flask, render_template, request, flash, redirect
import json

import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/home", methods=['POST'])
def home2():
    with open('estoque.json') as estoque:
        lista = list(json.load(estoque))

        return render_template("exibir.html", nomeUsuario="Quantidade de estoque é:", nomecadastro=lista)




@app.route("/buscaexibe", methods=['POST'])
def home3():
    nome3 = request.form.get('nomeBE')
    with open('estoque.json') as estoque:
        lista = json.load(estoque)
        cont = 0
        for g in lista:
            cont += 1
            if nome3 == g['bebida']:
                return render_template("exibir2.html", campo2="lista atualizada",nomecadastro=lista)
            if cont >= len(lista):
                flash('produto sem estoque')
                return redirect("/")

@app.route("/enviarbebida", methods=['POST'])
def home4():
    LOTE = []
    nome33 = request.form.get('nomeEB')
    nome44 = request.form.get('nomeEBB')
    LOTE =[{
        "bebida": nome33,
        "quantidade": nome44

    }]
    with open("estoque.json") as bom:
        arquivo = json.load(bom)
    arquivo2 = arquivo + LOTE
    with open("estoque.json","w") as arquivo:
        json.dump(arquivo2,arquivo,indent=2)
    return render_template("exibir2.html", nomecadastro=nome33, campo2=" cadastrado!!")

if __name__ in '__main__':
    app.run(debug=True)
