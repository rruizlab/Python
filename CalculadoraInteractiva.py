# Calculadora interactiva
# Aquest programa demana dos números i una operació (+, -, *, /, %),
# mostra el resultat i es repeteix fins que l'operació no sigui vàlida.

# Bucle principal: es repeteix mentre l'operació sigui reconeguda
while True:
    # Demanar el primer número (accepta enters i decimals)
    primerNumero = float(input("Introdueix el primer número: "))

    # Demanar el segon número (accepta enters i decimals)
    segonNumero = float(input("Introdueix el segon número: "))

    # Demanar l'operació a realitzar
    operacio = input("Introdueix l'operació (+, -, *, /, %): ")

    # Comprovar quina operació s'ha escollit i mostrar el resultat
    if operacio == "+":
        resultat = primerNumero + segonNumero
        print("Resultat:", resultat)
    elif operacio == "-":
        resultat = primerNumero - segonNumero
        print("Resultat:", resultat)
    elif operacio == "*":
        resultat = primerNumero * segonNumero
        print("Resultat:", resultat)
    elif operacio == "/":
        # Evitar divisió per zero
        if segonNumero == 0:
            print("Error: no es pot dividir per zero.")
        else:
            resultat = primerNumero / segonNumero
            print("Resultat:", resultat)
    elif operacio == "%":
        # Evitar mòdul amb zero
        if segonNumero == 0:
            print("Error: no es pot fer mòdul amb zero.")
        else:
            resultat = primerNumero % segonNumero
            print("Resultat:", resultat)
    else:
        # Si l'operació no és vàlida, sortir del bucle
        print("Operació no reconeguda. Finalitzant programa.")
        break
