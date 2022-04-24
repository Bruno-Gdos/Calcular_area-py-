def calculos(tabela, base, altura, raio):

    if tabela == 1:
        area = base * altura
        return print(f'A area do retangulo é {area}')

    if tabela == 2:
        area = (base * altura) /2
        return print(f'A area do triangulo é {area}')

    if tabela == 3:
        area = 3.14 * (raio ** 2)
        return print(f'A area do circulo é {area}')

