
def welcome():
    print('''
Bem vindo a minha calculadora''')
    
welcome()
    
def calculator():
    
    operação = input('''
Informe qual operação matemática irá usar:
+ para adição
- para subtração
* para multiplicação
/ para divisão  
''')

    n_1 = int(input('Digite um numéro: '))
    n_2 = int(input('Digite outro numéro: '))

#soma 

    if operação == '+':
        print(f'{n_1} + {n_2} = ')
        print(n_1 + n_2)

#subtração 
    elif operação == '-':
        print(f'{n_1} - {n_2} = ')
        print(n_1 - n_2)

#multiplicação 
    elif operação == '*':
        print(f'{n_1} * {n_2} = ')
        print(n_1 * n_2)

#divisão 
    elif operação == '/':
        print(f'{n_1} / {n_2} = ')
        print(n_1 / n_2)
        
    else:
        print('Erro! Digite um operador válido')
        
    repita() 
           
def repita():
    
    calc_again = input('''
Necessita o uso da calculadora novamente?
Digite S para sim ou N para Nao: ''')
    
    if calc_again.upper() == 'S':
        calculator()
    elif calc_again.upper() == 'N':
        print('Obrigado.')
    else:
        repita()
           
calculator()