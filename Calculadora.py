print('-------- Calculadora --------')
n1 = int(input(print('Digite o primeiro numero: ')))#Seleciona o primeiro numero e manda pra variavel 'n1'
n2 = int(input(print('Digite o segundo numero: ')))#Seleciona o segundo numero e manda pra variavel 'n2'
O = str(input(print('Selecione uma operação Valida\n + --> Soma:\n - --> Subtração:\n x --> Multiplicação:\n / --> Divisão: ')))#Menu de seleção de opção
#Condiçoes de escolha do menu Abaixo:
if (O == '+'):
    print(f'A Soma de {n1} e {n2} é:',(n1+n2),'\n -------- Fim --------' )
elif (O == '-'):
    print(f'A Subtraçao de {n1} e {n2} é:',(n1-n2),'\n -------- Fim --------' )
elif (O == 'x'):
    print(f'A Multiplicação de {n1} e {n2} é:',(n1*n2),'\n -------- Fim --------' )
elif (O =='/'):
    print(f'A Divisão de {n1} e {n2} é:',(n1/n2),'\n -------- Fim --------' )
else:
    print('Selecione uma opção valida!!!\n -------- Fim --------')