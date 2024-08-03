import unittest
from pyground import*

class TesteComprimentos(unittest.TestCase):

    def setUp(self):

        self.configurado, self.pyground = configurar()
    
    def teste_01_pyground_configurado(self):
        
        self.assertTrue(self.configurado)
    
    def teste_02_comprimentos(self):

        comprimentos = ["olá", "oi", "tudo bem?", "como vai?", "olá, tudo bem?"]

        for comprimento in comprimentos:

            print(f"testando comprimento {comprimento}")

            resposta = self.pyground.get_response(comprimento)

            self.assertGreater(resposta.confidence, CONFIANCA_MINIMA)

            self.assertIn("Olá! Meu nome é pyground e sou o chatbot de aprendizado básico da linguagem python. Como posso ajudá-lo no seu aprendizado?", resposta.text)
    
    def teste_03_variacoes_comprimentos(self):
        
        comprimentos = ["oi, tudo bem?", "Olá, tudo bem?", "olá, como vai?", "oi, como vai?"]

        for comprimento in comprimentos:

            print(f"Testando {comprimento}")

            resposta = self.pyground.get_response(comprimento)
            self.assertGreater(resposta.confidence, CONFIANCA_MINIMA)

            self.assertIn("Olá! Meu nome é pyground e sou o chatbot de aprendizado básico da linguagem python. Como posso ajudá-lo no seu aprendizado?", resposta.text)

    def teste_04_comprimentos_dia(self):

        comprimentos = ["bom dia"]

        for comprimento in comprimentos:

            print(f"testando comprimento {comprimento}")

            resposta = self.pyground.get_response(comprimento)

            self.assertGreater(resposta.confidence, CONFIANCA_MINIMA)

            self.assertIn("Bom dia! Nada melhor que começar o dia programando. Meu nome é pyground e sou o chatbot de aprendizado básico da linguagem python. Como posso ajudá-lo no seu aprendizado?", resposta.text)
    
    def teste_05_comprimentos_tarde(self):

        comprimentos = ["boa tarde"]

        for comprimento in comprimentos:

            print(f"testando comprimento {comprimento}")

            resposta = self.pyground.get_response(comprimento)

            self.assertGreater(resposta.confidence, CONFIANCA_MINIMA)

            self.assertIn("Boa tarde! Meu nome é pyground e sou o chatbot de aprendizado básico da linguagem python. Como posso ajudá-lo no seu aprendizado?", resposta.text)

    def teste_06_comprimentos_noite(self):

        comprimentos = ["boa noite"]

        for comprimento in comprimentos:

            print(f"testando comprimento {comprimento}")

            resposta = self.pyground.get_response(comprimento)

            self.assertGreater(resposta.confidence, CONFIANCA_MINIMA)

            self.assertIn("Boa noite! Meu nome é pyground e sou o chatbot de aprendizado básico da linguagem python. Como posso ajudá-lo no seu aprendizado?", resposta.text)

class TestePerguntas(unittest.TestCase):
    
    def setUp(self):
        self.configurado, self.pyground = configurar()
        
    def teste_01_pyground_configurado(self):
        self.assertTrue(self.configurado)
    
    def teste_02_pergunta_01(self):
        perguntas = ["como criar uma variável em python?", "como crio uma variável em python?", "como faço para criar uma variável em Python?", "como faço para criar uma variável?"]

        for pergunta in perguntas:
            print(f"Perguntando {pergunta}")

            resposta = self.pyground.get_response(pergunta)
            print(f"Obtendo a confiança: {resposta.confidence}")
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            
            self.assertIn("Para criar uma varíavel em python, atribuímos um nome a ela, que comece com letras e à direita do sinal de '=' damos um valor a essa variável. Ex: nome = Vitor. Para mais informações acesse: youtube.com", resposta.text)

    def teste_03_pergunta_02(self):
        perguntas = [ "como calcular em python", "como faço operações matemáticas em python?", "como faço operações aritiméticas em python?", "como faço soma em python?", "como faço subtração em python?", "como faço mutiplicação em python?", "como faço divisão em python?", "como fazer soma em python?", "como fazer divisão em python?", "como fazer subtração em python?", "como fazer multiplicação em python?"]
            

        for pergunta in perguntas:
            print(f"Perguntando {pergunta}")

            resposta = self.pyground.get_response(pergunta)
            print(f"Obtendo a confiança: {resposta.confidence}")
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn('Para fazer uma operação matemática em python, precisamos utilizar operadores: + o sinal de mais serve para somar 2 números ou mesmo para somar strings. Porém, esses dados não podem ser misturados, portanto, utilize apenas números ou apenas strings no cálculo. Ex: 2 + 2. A subtração é semelhante, mas funciona apenas com números. Ex: 2 - 2. Para multiplicar, usamos o operador *, que multiplica 2 números ou um caractere. Ex: 2 * 2. E por fim, para dividir utilizamos o operador / com o número que desejamos dividir a direita do divisor. Ex: 4 / 2. Podemos colocar essas informações dentro de um print e elas serão exibidas na tela.', resposta.text)
    
    def teste_04_pergunta_03(self):
        perguntas = ["como coletar valores digitados pelo usuário em python?", "como obter dados do usuário?", "como receber valores do usuário?", "como faço para pegar o que o usuário digitou?" ]
            

        for pergunta in perguntas:
            print(f"Perguntando {pergunta}")

            resposta = self.pyground.get_response(pergunta)
            print(f"Obtendo a confiança: {resposta.confidence}")
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Para receber um valor vindo do teclado do usuário, usamos um comando 'input', que permite receber tal valor e, por exemplo, armazená-lo em uma variável para imprimí-lo na tela. É recomendado sempre escrever uma mensagem dentro desse input para que o usuário possa visualizar Ex: nome = (input('Digite um nome:'))", resposta.text)

    def teste_05_pergunta_04(self):
        perguntas = ["como mostrar valores na tela?", "como exibir um resultado na tela?", "como mostrar na tela?", "como faço para mostrar uma variável na tela?", "como faço para mostrar algo na tela?", "como fazer algo aparecer na tela?"]
            

        for pergunta in perguntas:
            print(f"Perguntando {pergunta}")

            resposta = self.pyground.get_response(pergunta)
            print(f"Obtendo a confiança: {resposta.confidence}")
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Para exibir valores na tela, é necessário utilizar o comando 'print', que nos permite mostrar operações, como 1+1 ou o valor de uma variável. Ex: nome = 'Alfred' print(nome)", resposta.text)

    def teste_06_pergunta_05(self):
        perguntas = ["como mostrar textos formatados na tela?", "como formatar um texto em python?", "como faço para editar um texto?", "como formatar textos?", "como eu edito textos?"]
            

        for pergunta in perguntas:
            print(f"Perguntando {pergunta}")

            resposta = self.pyground.get_response(pergunta)
            print(f"Obtendo a confiança: {resposta.confidence}")
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Para exibir um texto formato na tela, o método mais simples de se fazer é utilizando uma f-string, sendo o f de format. Para tal, utilizamos um print com um f fora das aspas e a váriável entre chaves. Ex: nome = 'Alice' print(f'Seu nome é {nome}!", resposta.text)

#Onde o código é inicializado 
if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteComprimentos))
    testes.addTest(carregador.loadTestsFromTestCase(TestePerguntas))

    executor = unittest.TextTestRunner()
    executor.run(testes)
    print("Teste concluído!")