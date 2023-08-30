import bibliScaico

tipoDeBase = input("\nQual base você deseja converter? ").upper()
numeroBase = input(f"Digite um número em base {tipoDeBase}: ")



if (tipoDeBase == "HEXA" or tipoDeBase == "16"):   
    #Hexa para Decimal
    resultadoDecimal = bibliScaico.baseParaDecimal(numeroBase,16)
    print (f"\nDecimal: {resultadoDecimal}")

    #Hexa para Binario 
    resultadoBinario = bibliScaico.decimalParaBinario(resultadoDecimal,2)
    print (f"Binário: {resultadoBinario}")

    #Hexa para Octal
    resultadoOctal = bibliScaico.decimalParaBinario(resultadoDecimal,8)
    print (f"Octal: {resultadoOctal}")

    
elif (tipoDeBase == "BINARIO" or tipoDeBase == "2"):
    #Binario para decimal
    resultadoDecimal = bibliScaico.baseParaDecimal(numeroBase, 2)
    print (f"\nDecimal: {resultadoDecimal}")

    #Binario para Hexa
    resultadoHexa = bibliScaico.decimalParaBinario(resultadoDecimal, 16)
    print (f"Hexa: {resultadoHexa}")

    #Binario para Octal
    resultadoOctal = bibliScaico.decimalParaBinario(resultadoDecimal, 8)
    print (f"Octal: {resultadoOctal}")


elif (tipoDeBase == "OCTAL" or tipoDeBase == "8"):
    #Octal para decimal
    resultadoDecimal = bibliScaico.baseParaDecimal(numeroBase, 8)
    print (f"\nDecimal: {resultadoDecimal}")

    #Octal para Hexa
    resultadoHexa = bibliScaico.decimalParaBinario(resultadoDecimal, 16)
    print (f"Hexa: {resultadoHexa}")

    #Octal para Binário
    resultadoBinario = bibliScaico.decimalParaBinario(resultadoDecimal,2)
    print (f"Binário: {resultadoBinario}")



elif (tipoDeBase == "DECIMAL" or tipoDeBase == "10"):
    numeroBase = int(numeroBase)
    #Decimal para Binario
    resultadoBinario = bibliScaico.decimalParaBinario(numeroBase,2)
    print (f"Binário: {resultadoBinario}")

    #Decimal para Hexa
    resultadoHexa = bibliScaico.decimalParaBinario(numeroBase, 16)
    print (f"Hexa: {resultadoHexa}")

    #Decimal para Octal
    resultadoBinario = bibliScaico.decimalParaBinario(numeroBase,8)
    print (f"Octal: {resultadoBinario}")

else:
    print ("Base INVÁLIDA")