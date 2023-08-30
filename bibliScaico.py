# Converte de Hexa para Decimal
def hexaParaDecimal (numero):
    if (numero == "A" or numero == "a"):
        numero = 10
    elif (numero == "B" or numero == "b"):
        numero = 11
    elif (numero == "C" or numero == "c"):
        numero = 12
    elif (numero == "D" or numero == "d"):
        numero = 13
    elif (numero == "E" or numero == "e"):
        numero = 14
    elif (numero == "F" or numero == "f"):
        numero = 15
    return numero


# Converte de Decimal para Hexa
def decimalParaHexa (numero):
    if (numero == 10):
        numero = "A"
    elif (numero == 11):
        numero = "B"
    elif (numero == 12):
        numero = "C"
    elif (numero == 13):
        numero = "D"
    elif (numero == 14):
        numero = "E"
    elif (numero == 15):
        numero = "F"
    return numero



# Converte de Decimal para binário, Octal ou Hexa
def decimalParaBinario (numeroDecimal, baseNumerica):
    listaBinario = []
    
    while (numeroDecimal > 0):
        restoDivisao = numeroDecimal % baseNumerica
        numeroDecimal = numeroDecimal // baseNumerica  
        if (baseNumerica == 16):
            restoDivisao = decimalParaHexa(restoDivisao)  
        listaBinario.append(restoDivisao)
    listaBinario.reverse()
    return listaBinario



# Converte qualquer base para Decimal
def baseParaDecimal (numeroBase, baseNumerica):
    posicaoDecimal = -1
    resultadoDecimal = 0
    listaNumeros = []
    listaNumeros = list(numeroBase)
    listaNumeros.reverse()

    for numero in listaNumeros:
        if (numero == str(numero)):
            numero = hexaParaDecimal(numero)
        posicaoDecimal += 1 
        numero = int(numero)
        resultadoDecimal = (resultadoDecimal) + ((numero) * (baseNumerica**posicaoDecimal))
        numero = str(numero)
    return resultadoDecimal