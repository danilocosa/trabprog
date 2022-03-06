from config.Config import Config
from config.Database import Database
from dao.CarroDao import CarroDao
from model.Carro import Carro
from flask import Flask, request, render_template

app = Flask(__name__)

dao = CarroDao(Database(Config().config).conn)

@app.route('/carro/novo', methods=["GET"])
def novo():
    return render_template("inserir.html")

@app.route('/carro/novo', methods=["POST"])
def inserir():
    carro = Carro()
    carro.id = request.form.get("id")
    carro.modelo = request.form.get("modelo")
    carro.categoria = request.form.get("categoria")
    carro.valor = request.form.get("valor")

    dao.inserirCarro(carro)

    lista = dao.selecionarCarros()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/carro/remover/<id>', methods=["GET"])
def remover(id):
    carro = Carro()
    carro.id = id
    dao.excluirCarro(carro)
    
    lista = dao.selecionarCarros()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/', methods=["GET"])
def listar():
    lista = dao.selecionarCarros()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/carro/<id>', methods=["GET"])
def editarPagina(id):
    carro = dao.selecionarCarro(id)
    return render_template("editar.html", carro=carro)
    
@app.route('/carro/editar', methods=["POST"])
def editar():
    carro = Carro()
    carro.id = request.form.get("id")
    carro.modelo = request.form.get("modelo")
    carro.categoria = request.form.get("categoria")
    carro.valor = request.form.get("valor")
    carro = dao.alterarCarro(carro)

    lista = dao.selecionarCarros()
    return render_template(
        "listagem.html",
        lista=lista
    )
    


if __name__ == '__main__':
    app.run()
