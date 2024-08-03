from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import json

CONVERSAS = [

    "C:/Users/vitin/OneDrive/Área de Trabalho/pyground/conversas/comprimentos.json",
    "C:/Users/vitin/OneDrive/Área de Trabalho/pyground/conversas/perguntas.json"
    
]

#1 devolve um "treinador de robô"
def configurar():
    time.clock = time.time
    
    pyground = ChatBot("pyground, bot de auxílio a aprendizagem python")
    treinador = ListTrainer(pyground)
    
    return True, treinador

#2 carrega as conversas a partir dos jsons
def carregar_conversas():
    carregadas, conversas = True, []
    
    for arquivo_de_conversas in CONVERSAS:
        try:
            with open(arquivo_de_conversas, "r", encoding="utf-8") as arquivo:
                para_treinar = json.load(arquivo)
                conversas.append(para_treinar["conversas"])
                
                arquivo.close()
        except Exception as e:
            carregadas = False
            
    return carregadas, conversas

# 3 usa o treinador para treinar o robô com as conversas

def treinar(treinador, conversas):
    for conversa in conversas:
        for mensagens_resposta in conversa:
            mensagens = mensagens_resposta["mensagens"]
            resposta = mensagens_resposta["resposta"]
        
            print(f"treinando o robô, mensagens: {mensagens}, resposta: {resposta}")
            for mensagem in mensagens:
                treinador.train([mensagem, resposta])

if __name__ == "__main__":
    configurado, treinador = configurar()
    
    if configurado:
        carregadas, conversas = carregar_conversas()
        if carregadas:
            treinar(treinador, conversas)