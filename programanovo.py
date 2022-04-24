from funcaotriangulo import calculos

while True:
    print('Bem vindo a nossa calculadora de area')
    print('-'*10)
    print('Você vai calcular a area de um: ')
    print('[1] Retangulo')
    print('[2] Triangulo')
    print('[3] Circulo')
    print('[0] Sair')
    tabela = int(input('Digite aqui: '))

    if tabela == 0:
        break
    elif tabela == 3:
        raio = float(input('Digite o raio da sua forma: '))
        resultado = calculos(tabela, 0, 0, raio)

    else:
        base = float(input('Digite a base da sua forma: '))
        altura = float(input('Digite a altura da sua forma: '))
        resultado = calculos(tabela, base, altura, 0)
