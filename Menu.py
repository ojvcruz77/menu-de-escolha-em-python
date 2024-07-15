# Importação da bibioteca time
from time import sleep
from os import system

# Inicio do contador do while
c = 0

# Loop do sistema
while c !=5:
    
   
    # "Menu" de opções
    print('-'*15)
    print('Escolha umas das opções')
    print('-'*15)
    
    print('')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    print('')
    
    # Variável da escolha do usuário
    op = int(input('Digite qual opção quer: '))
    
    
    # Inicio do switch/match case
    match op:
       
        # Somando as variaveis n1 e n2
        case 1:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            print('O valor da soma dos números {} e {} é {}'.format(n1, n2, n1+n2))
           
               
        # Multiplicando as variaveis n1 e n2 
        case 2:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            print('O valor da multiplicação dos números {} e {} é {}'.format(n1, n2, n1*n2))
            
            
        # Analisando qual das variaveis n1 e n2 é a maior
        case 3:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            
            print('O maior valor entre os números {} e {} é {}'.format(n1, n2, max(n1,n2)))
            

        # Reiniciando o loop para a escolha de novos números e outra escolha
        case 4:
            ...
            system('cls') or None      
        
        # Saindo dop sistema
        case 5:
                print('Desligando programa')
                
                for i in range(0,5):
                     print('.')
                     sleep(1)
                
                system('cls') or None      
                c = 5
