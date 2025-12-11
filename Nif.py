LLETRES = "TRWAGMYFPDXBNJZSQVHLCKE"

while True:  #While se encarga de hacer un bucle para pedir varios DNI's 
    dni_text = input("Introdueix el DNI: ").strip() #Strip = quitar espacios
    if dni_text == "":
        break #Cerrar bucle si se pulsa ENTER sin valores escogidos
    
    if not dni_text.isdigit():  #Devuelve True si el valor de "dni_text" es solamente digitos, si no es el caso salta el aviso
        print("Només es permeten números.")
        continue
    
    dni = int(dni_text) #Convierte en numero entero el "dni_text" que hasta ahora era un String
    lletra = LLETRES[dni % 23] #Divido el valor de dni por las 23 letras del alfabeto colocadas anteriormente en el puesto oficial de los DNI 
    print(f"El NIF és {dni_text}{lletra}")