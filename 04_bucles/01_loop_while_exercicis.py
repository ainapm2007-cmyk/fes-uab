###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
numero = 10
while numero >= 1:
    print(f"{numero}")
    numero -= 1


# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
numero = 1
suma_parells = 0
while numero <= 20:
    if numero % 2 == 0:
        suma_parells += numero
    numero += 1
print(f"La suma dels números parells fins a 20 és: {suma_parells}")


# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
numero = int(input("Introdueix un numero enter positiu:"))
comptador = 1
factorial = 1
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
while comptador <= numero:
    factorial *= comptador
    comptador += 1
print(f"El factorial del {numero} es: {factorial}")


# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
contrasenya = ""
while len(contrasenya) < 8:
  contrasenya = input("Introdueix una contrasenya (almenys 8 caràcters): ")
      if len(contrasenya) < 8:
    print("La contrasenya ha de tenir almenys 8 caràcters. Torna-ho a provar.")

print("Contrasenya vàlida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
numero = int(input("introdueix un numero:"))
multiplicador = 1
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
while multiplicador <=10:
   resultat = numero * multiplicador
   print(f"{numero} * {multiplicador} = {resultat}")
   multiplicador += 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
N = int(input("introdueix un numero enter positiu:"))
numero = 2
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
while numero <=N:
   es_primer = True
   divisor = 2
   while divisor * divisor <= numero:  # Optimitzem: no cal provar divisors fins a numero
    if numero % divisor == 0:
      es_primer = False  # Si trobem un divisor, no és primer
      break  # Sortim del bucle interior
    divisor += 1
  if es_primer:
    print(numero)

  numero += 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
suma = 0
numero = int(input("Introdueix el primer numero enter (0 per acabar):"))
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
while numero != 0:
   suma += numero
   numero = int(input("introdueix un altre numero enter (0 per acabar):"))
print(f"La suma total es {suma}")


# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
numero = int(input("introdueix un numero enter positiu:"))
comptador = 0
# Comptabilitza quantes xifres té fent servir un bucle while.
while numero > 0: 
   numero = numero // 10 
   comptador += 1
# Finalment, imprimeix el nombre de xifres.
print(f"el numero {numero} té {comptador} xifres")


# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
termes = int(input("quants termes de Fibonacci vols veure? "))
comptador = 0
a = 0 #(anterior)
b = 1 #(actual)
# Imprimeix aquest nombre de termes fent servir un bucle while. 
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
while comptador < termes:
   print(f"{a}")
   seguent = a + b
   b = a
   a = seguent
   comptador += 1



# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
secret = 7
numero = int(input("introdueix un numero:"))
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
while numero != secret:
   if numero < secret:
      print(f"més gran")
    else:
      print(f"més petit")
    numero = int(input("tornar a escriure un numero:"))
print(f"Correcte! has endevinat el numero secret")