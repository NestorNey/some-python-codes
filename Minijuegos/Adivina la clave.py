import time
i = 3
print("=================================")
print("* Hmmm con que quieres pasar no? ")
print("* bien, entonces dime la clave...")
print("=================================")
print()
time.sleep(3)
clave = input("* Escribe la clave: ")
print()
while True:
    if clave == "Chupacabras":
        print()
        print(("Ahuevo si sabias que "), (clave), ("era la clave secreta >:D"))
        print()
        break
    time.sleep(1)
    print(("Esa no es >:v, tienes "), (i), ("intentos."))
    print("asi que no repetire, cual es la clave? >:v")
    print()
    time.sleep(3)
    clave = input("* Escribe la clave: ")
    print()
    i = i - 1
    if i == 0:
        print("Esas no fueron las claves")
        time.sleep(2)
        print("estas muerto >:v")
        time.sleep(2)
        print()
        print("As perdido")
        print()
        break
time.sleep(1)
print("Si quieres volver a jugar, cierra y vuelve a abrir el juego!")
