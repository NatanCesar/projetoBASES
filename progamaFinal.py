
# Converte de Hexa para Decimal
def hexa (numero):
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
def hexa1 (numero):
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
            restoDivisao = hexa1(restoDivisao)  
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
            numero = hexa(numero)
        posicaoDecimal += 1 
        numero = int(numero)
        resultadoDecimal = (resultadoDecimal) + ((numero) * (baseNumerica**posicaoDecimal))
        numero = str(numero)
    return resultadoDecimal



tipoDeBase = input("\nQual base você deseja converter? ").upper()
numeroBase = input(f"Digite um número em base {tipoDeBase}: ")



if (tipoDeBase == "HEXA" or tipoDeBase == "16"):   
    #Hexa para Decimal
    resultadoDecimal = baseParaDecimal(numeroBase,16)
    print (f"\nDecimal: {resultadoDecimal}")

    #Hexa para Binario 
    resultadoBinario = decimalParaBinario(resultadoDecimal,2)
    print (f"Binário: {resultadoBinario}")

    #Hexa para Octal
    resultadoOctal = decimalParaBinario(resultadoDecimal,8)
    print (f"Octal: {resultadoOctal}")

    
elif (tipoDeBase == "BINARIO" or tipoDeBase == "2"):
    #Binario para decimal
    resultadoDecimal = baseParaDecimal(numeroBase, 2)
    print (f"\nDecimal: {resultadoDecimal}")

    #Binario para Hexa
    resultadoHexa = decimalParaBinario(resultadoDecimal, 16)
    print (f"Hexa: {resultadoHexa}")

    #Binario para Octal
    resultadoOctal = decimalParaBinario(resultadoDecimal, 8)
    print (f"Octal: {resultadoOctal}")


elif (tipoDeBase == "OCTAL" or tipoDeBase == "8"):
    #Octal para decimal
    resultadoDecimal = baseParaDecimal(numeroBase, 8)
    print (f"\nDecimal: {resultadoDecimal}")

    #Octal para Hexa
    resultadoHexa = decimalParaBinario(resultadoDecimal, 16)
    print (f"Hexa: {resultadoHexa}")

    #Octal para Binário
    resultadoBinario = decimalParaBinario(resultadoDecimal,2)
    print (f"Binário: {resultadoBinario}")



elif (tipoDeBase == "DECIMAL" or tipoDeBase == "10"):
    numeroBase = int(numeroBase)
    #Decimal para Binario
    resultadoBinario = decimalParaBinario(numeroBase,2)
    print (f"Binário: {resultadoBinario}")

    #Decimal para Hexa
    resultadoHexa = decimalParaBinario(numeroBase, 16)
    print (f"Hexa: {resultadoHexa}")

    #Decimal para Octal
    resultadoBinario = decimalParaBinario(numeroBase,8)
    print (f"Octal: {resultadoBinario}")

else:
    print ("Base INVÁLIDA")