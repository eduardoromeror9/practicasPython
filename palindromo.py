def palindromo(palabra):
    palabra = palabra.replace(' ', '') #Quita los espacios
    palabra = palabra.lower() #Hace las letras minusculas
    palabra_invertida = palabra[::-1] #Genera la palabra al reves
    if palabra == palabra_invertida:
        return True
    else:
        return False
    

def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo!!')
    else:
        print('No es palindromo!!')





if __name__ == '__main__': #entryPoint
    run()