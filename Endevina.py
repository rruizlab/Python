import random

# Joc: endevina un número entre 1 i 10 amb màxim 3 intents
numero_secret = random.randint(1, 10)
intents_maxims = 3
intents = 0
encertat = False

print("He pensat un número entre 1 i 10. Tens 3 intents per endevinar-lo.")

while intents < intents_maxims and not encertat:
    intents += 1
    resposta = int(input("Quin número he pensat? "))

    if resposta == numero_secret:
        encertat = True
    elif resposta < numero_secret:
        print("És més gran")
    else:
        print("És més petit")

if encertat:
    print(f"Has guanyat! Has encertat en {intents} intents.")
else:
    print(f"Has perdut. El número era {numero_secret}.")
