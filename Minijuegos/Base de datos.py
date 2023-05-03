BDcorreo = {"Hola@correo.com": "123", "Adios@correo.com": "123"}
hA = "No"

print(" \n " * 5)
print("Iniciar secion (1)         Registrar cuenta(2)")
print(" \n " * 5)
varCN = input()

if varCN == "2":
    print(" \n " * 5)
    print("Escribe el usuario del correo con el dominio que quieras, siempre")
    print("y cuando contenga un @ y una extencion ejemplo .com o .net")
    print(" \n " * 5)
    varCN = input("Escribe el correo: ")
    for n in varCN:
        if n == "@":
            hA = "Si"
        if hA == "Si":
            if n == ".":
                haveAP = True
    if haveAP == True:
        print("Correo aceptado")
    varC2 = input("Escribe la contraseña:")
