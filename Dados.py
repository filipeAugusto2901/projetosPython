## Dados

import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Gostaria de rodar o dado?'
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's'or resposta == 'Sim':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n'or resposta == 'Não':
                print('Obrigado por participar do meu teste')
            else:
                print('Por favor digitar sim ou não')
        except:
            print('Erro ao receber parametro')
        
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()