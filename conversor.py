def conversor(tipo_pesos, valor_dolar):
    pesos = int(input(f'Cuantos pesos {tipo_pesos} tienes?: '))
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' Dolares')

menu = """
Bienvenidos al conversor de Monedas 💸
1- Pesos Chilenos
2- Pesos Argentinos
3- Pesos Mexicanos
Elige una opcion:        
"""

option = input(menu)

if option == '1':
    conversor('Chilenos', 720)
elif option == '2':
    conversor('Argentinos', 95)
elif option == '3':
    conversor('Mexicanos', 20)
else:
    print('Ingresa una opcion conrrecta!!')