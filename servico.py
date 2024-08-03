from flask import Flask, jsonify
from pyground import *

servico = Flask("Pyground")

configurado, pyground = configurar()

@servico.get("/pyground/info")
def get_informacoes():
    return jsonify(
        descricao = "Bot de aprendizagem Python, versão beta",
        email = "vitinhonascimentoadv@gmail.com",
        versao = "1.0",
        robo_online = configurado
    )

@servico.get("/pyground/resposta/<string:mensagem>")
def get_resposta(mensagem):
    resposta = pyground.get_response(mensagem)
    return jsonify(
        resposta = resposta.text,
        confianca = resposta.confidence
    )
    
if __name__ == "__main__":
    servico.run(debug=True)