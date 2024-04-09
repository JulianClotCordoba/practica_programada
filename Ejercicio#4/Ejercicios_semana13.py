

personas_data = open("personas.txt", "w")

def ingresar():
    for i in range(1, 11):
        cantidad_de_personas = input("Cual es tu nombre para ingresarte? ")

        personas_data.write( "\n" +cantidad_de_personas + "\n")
    personas_data.close()

def egresar():
    for x in range(1, 11):
        cantidad_de_personas_egresadas = input("Cual es tu nombre para egresarte? ")
