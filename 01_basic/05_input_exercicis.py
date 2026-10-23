###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
tècnic = input("nom del tècnic:")
xarxa = input("nom de la xarxa:")
# Després, mostra un missatge amb aquesta informació.
print(f"El tècnic {tècnic} està instal·lant la xarxa {xarxa}")


# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
longitud_fibra = float(input("Longitud de la fibra en km:"))
velocitat_gbps = float(input("Velocitat de transmissió en Gbps:"))
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
temps_segons = 8/velocitat_gbps
print(f"L'enllaç de {longitud_fibra} km necessita{temps_segons} segons per transmetre 1GB.")


# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
hores_feina = float(input("nombre d'hores de feina:"))
preu_hora = float(input("preu per hora en euros:"))
# Demana també el preu del material.
preu_material = float(input("preu del material:"))
# Mostra el cost total de la instal·lació.
cost_total = hores_feina * preu_hora + preu_material
print(f"El cost total de la instal·lació és {cost_total} euros.")