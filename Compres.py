dni = input("Introdueix el DN: ") #Pregunta por dni
preu = input("Introdueix el preu de l'article: ")  #Pregunta por precio
descompte = input("Introdueix el % de descompte: ") # pregunta por % de descuento
iva = input("Introdueix el % d'IVA: ") # Pregunta por IVA

#Toda esta parte transforma (precio, descuento e iva) en float (numeros con decimal)
#El .replace, remplaza la coma (,) por punto (.) ya que en España solemos confundir los decimales con (,) y python espera punto (.)
preu = float(preu.replace(",", ".")) 
descompte = float(descompte.replace(",", "."))
iva = float(iva.replace(",", "."))

#Calcula precio con descuento
preu_descompte = preu - (preu * descompte / 100)
#Calcula precio final
preu_final = preu_descompte + (preu_descompte * iva / 100)

#"Pinta" en el terminal tanto dni como precio final despues de dar los datos que nos piden mas arriba
print(dni)
print(round(preu_final, 1))