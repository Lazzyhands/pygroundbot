from chatterbot import ChatBot
import time

CONFIANCA_MINIMA = 0.80

def configurar():
    time.clock = time.time
    
    pyground = ChatBot("Pygroundbot, robô de auxílio de aprendizagem Python", read_only = True, logic_adpters = [{"import_path": "chatterbot.logic.BestMatch"}])
    
    return True, pyground

def executar(pyground):
    while True:
        mensagem = input("Digite alguma coisa.. \n")
        resposta = pyground.get_response(mensagem.lower())
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(f"Pyground: {resposta.text} | [Confiança: {resposta.confidence}] ")
        else:
            print(f"Infelizmente eu nao sei responder esta pergunta, \n Pergunte outra coisa | [Confiança: {resposta.confidence}]")


if __name__ == "__main__":
    configurado, pyground = configurar()
    
    if configurado:
        executar(pyground)