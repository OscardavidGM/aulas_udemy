nombre = input("digite su nombre: ")
edad = int(input("Digite su edad: "))

if nombre and edad:
    print(f"su nombre es {nombre}")
    print(f"su nombre invertido es {nombre[::-1]}")

    if " " in nombre:
      print("Tu nombre contiene espacios")
    else: 
      print("Tu nombre no contiene espacios")    

      print(f"su nombre tiene {len(nombre[0:])} letras")   
      print(f"a primeira letra de tu nombre es {nombre[0]}")
      print(f"la ultima letra de tu nombre es: {nombre[-1]}")  
else:
    print("Disculpa usted no digitó su nombre y edad")   

    
