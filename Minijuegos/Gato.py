def pranter():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
from random import randrange
import time
rangos = {'10' : '10', '9' : '9', '8' : '8', '7' : '7', '6' : '6', '4' : '4', '3' : '3', '2' : '2', '1' : '1'}
con = 0
xy1 = 1
xy2 = 2
xy3 = 3
xy4 = 4
xy5 = "O"
xy6 = 6
xy7 = 7
xy8 = 8
xy9 = 9
xy10 = 10
br = "none"
def ganador():
    global br
    if xy1 == "X" and xy2 == "X" and xy3 == "X":
        time.sleep(2)
        print("Felicidades, le ganaste a la computadora! :D")
        print("Computadora: MMM >:C te ganare para la siguiente!")
        br = "Break"
    elif xy1 == "O" and xy2 == "O" and xy3 == "O":
        time.sleep(2)
        print("Juego: Noooo, te gano la computadora :C")
        print("Computadora: MUAJAJAJ te gane mugre mortal >:D")
        br = "Break"
    elif xy4 == "X" and xy5 == "X" and xy6 == "X":
        time.sleep(2)
        print("Felicidades, le ganaste a la computadora! :D")
        print("Computadora: MMM >:C te ganare para la siguiente!")
        br = "Break"
    elif xy4 == "O" and xy5 == "O" and xy6 == "O":
        time.sleep(2)
        print("Juego: Noooo, te gano la computadora :C")
        print("Computadora: MUAJAJAJ te gane mugre mortal >:D")
        br = "Break"
    elif xy7 == "X" and xy8 == "X" and xy9 == "X":
        time.sleep(2)
        print("Felicidades, le ganaste a la computadora! :D")
        print("Computadora: MMM >:C te ganare para la siguiente!")
        br = "Break"
    elif xy7 == "O" and xy8 == "O" and xy9 == "O":
        time.sleep(2)
        print("Juego: Noooo, te gano la computadora :C")
        print("Computadora: MUAJAJAJ te gane mugre mortal >:D")
        br = "Break"
    elif xy1 == "X" and xy4 == "X" and xy7 == "X":
        time.sleep(2)
        print("Felicidades, le ganaste a la computadora! :D")
        print("Computadora: MMM >:C te ganare para la siguiente!")
        br = "Break"
    elif xy1 == "O" and xy4 == "O" and xy7 == "O":
        time.sleep(2)
        print("Juego: Noooo, te gano la computadora :C")
        print("Computadora: MUAJAJAJ te gane mugre mortal >:D")
        br = "Break"
    elif xy2 == "X" and xy5 == "X" and xy8 == "X":
        time.sleep(2)
        print("Felicidades, le ganaste a la computadora! :D")
        print("Computadora: MMM >:C te ganare para la siguiente!")
        br = "Break"
    elif xy2 == "O" and xy5 == "O" and xy8 == "O":
        time.sleep(2)
        print("Juego: Noooo, te gano la computadora :C")
        print("Computadora: MUAJAJAJ te gane mugre mortal >:D")
        br = "Break"
    elif xy3 == "X" and xy6 == "X" and xy9 == "X":
        time.sleep(2)
        print("Felicidades, le ganaste a la computadora! :D")
        print("Computadora: MMM >:C te ganare para la siguiente!")
        br = "Break"
    elif xy3 == "O" and xy6 == "O" and xy9 == "O":
        time.sleep(2)
        print("Juego: Noooo, te gano la computadora :C")
        print("Computadora: MUAJAJAJ te gane mugre mortal >:D")
        br = "Break"
    elif xy1 == "X" and xy5 == "X" and xy9 == "X":
        time.sleep(2)
        print("Felicidades, le ganaste a la computadora! :D")
        print("Computadora: MMM >:C te ganare para la siguiente!")
        br = "Break"
    elif xy1 == "O" and xy5 == "O" and xy9 == "O":
        time.sleep(2)
        print("Juego: Noooo, te gano la computadora :C")
        print("Computadora: MUAJAJAJ te gane mugre mortal >:D")
        br = "Break"
    elif xy3 == "X" and xy5 == "X" and xy7 == "X":
        time.sleep(2)
        print("Felicidades, le ganaste a la computadora! :D")
        print("Computadora: MMM >:C te ganare para la siguiente!")
        br = "Break"
    elif xy3 == "O" and xy5 == "O" and xy7 == "O":
        time.sleep(2)
        print("Juego: Noooo, te gano la computadora :C")
        print("Computadora: MUAJAJAJ te gane mugre mortal >:D")
        br = "Break"
    elif xy1 == "X":
        if xy1 == "O":
            if xy2 == "X":
                if xy2 == "O":
                    if xy3 == "X":
                        if xy3 == "O":
                            if xy4 == "X":
                                if xy4 == "O":
                                    if xy5 == "X":
                                        if xy5 == "O":
                                            if xy6 == "X":
                                                if xy6 == "O":
                                                    if xy7 == "X":
                                                        if xy7 == "O":
                                                            if xy8 == "X":
                                                                if xy8 == "O":
                                                                    if xy9 == "X":
                                                                        if xy9 == "O":
                                                                            time.sleep(2)
                                                                            print("Juego: Esto fue un empate!")
                                                                            print("Computadora: Hmmmm, eres inteligente pero intentemoslo de nuevo >:)")
                                                                            br = "Break"
def computadoraEntrada():
 global xy1
 global xy2
 global xy3
 global xy4
 global xy5
 global xy6
 global xy7
 global xy8
 global xy9
 contador = 1
 while True:
  xy = randrange(10)
  if xy == 1:
    xy = "1"
    if xy in rangos:
        print("Computadora: Hmm.. deja escojo uno...")
        time.sleep(2)
        print("Computadora: Elijo este!")
        time.sleep(2)
        pranter()
        del rangos['1']
        xy1 = "O"
        contador = contador + 1
        print("Computadora: Muajajaja! >:D")
        tableroInteractivo()
        break
  elif xy == 2:
    xy = "2"
    if xy in rangos:
        print("Computadora: Hmm.. deja escojo uno...")
        time.sleep(2)
        print("Computadora: Elijo este!")
        time.sleep(2)
        pranter()
        del rangos['2']
        xy2 = "O"
        contador = contador + 1
        print("Computadora: Muajajaja! >:D")
        tableroInteractivo()
        break
  elif xy == 3:
    xy = "3"
    if xy in rangos:
        print("Computadora: Hmm.. deja escojo uno...")
        time.sleep(2)
        print("Computadora: Elijo este!")
        time.sleep(2)
        pranter()
        del rangos['3']
        xy3 = "O"
        contador = contador + 1
        print("Computadora: Muajajaja! >:D")
        tableroInteractivo()
        break
  elif xy == 4:
    xy = "4"
    if xy in rangos:
        print("Computadora: Hmm.. deja escojo uno...")
        time.sleep(2)
        print("Computadora: Elijo este!")
        time.sleep(2)
        pranter()
        del rangos['4']
        xy4 = "O"
        contador = contador + 1
        print("Computadora: Muajajaja! >:D")
        tableroInteractivo()
        break
  elif xy == 5:
    xy = "5"
    if xy in rangos:
        print("Computadora: Hmm.. deja escojo uno...")
        time.sleep(2)
        print("Computadora: Elijo este!")
        time.sleep(2)
        pranter()
        del rangos['5']
        xy5 = "O"
        contador = contador + 1
        print("Computadora: Muajajaja! >:D")
        tableroInteractivo()
        break
  elif xy == 6:
    xy = "6"
    if xy in rangos:
        print("Computadora: Hmm.. deja escojo uno...")
        time.sleep(2)
        print("Computadora: Elijo este!")
        time.sleep(2)
        pranter()
        del rangos['6']
        xy6 = "O"
        contador = contador + 1
        print("Computadora: Muajajaja! >:D")
        tableroInteractivo()
        break
  elif xy == 7:
    xy = "7"
    if xy in rangos:
        print("Computadora: Hmm.. deja escojo uno...")
        time.sleep(2)
        print("Computadora: Elijo este!")
        time.sleep(2)
        pranter()
        del rangos['7']
        xy7 = "O"
        contador = contador + 1
        print("Computadora: Muajajaja! >:D")
        tableroInteractivo()
        break
  elif xy == 8:
    xy = "8"
    if xy in rangos:
        print("Computadora: Hmm.. deja escojo uno...")
        time.sleep(2)
        print("Computadora: Elijo este!")
        time.sleep(2)
        pranter()
        del rangos['8']
        xy8 = "O"
        contador = contador + 1
        print("Computadora: Muajajaja! >:D")
        tableroInteractivo()
        break
  elif xy == 9:
    xy = "9"
    if xy in rangos:
        print("Computadora: Hmm.. deja escojo uno...")
        time.sleep(2)
        print("Computadora: Elijo este!")
        time.sleep(2)
        pranter()
        del rangos['9']
        xy9 = "O"
        contador = contador + 1
        print("Computadora: Muajajaja! >:D")
        tableroInteractivo()
        break
def tableroInteractivo():
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(("|  "), (xy1), ("  |  "),(xy2), ("  |  "), (xy3), ("  |"))
        print("|       |       |       |")
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(("|  "), (xy4), ("  |  "),(xy5), ("  |  "), (xy6), ("  |"))
        print("|       |       |       |")
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(("|  "), (xy7), ("  |  "),(xy8), ("  |  "), (xy9), ("  |"))
        print("|       |       |       |")
        print("+-------+-------+-------+")
print("Juego: Este es el tablero, elije un numero...")
tableroInteractivo()
while True:
  print()
  xy = input("Juego: Escoge tu numero: ")
  while True:
    if xy == "1":
        if xy in rangos:
            del rangos['1']
            xy1 = "X"
            tableroInteractivo()
            break
        else:
            xy = input("Juego: Ese numero ya esta ocupado, escoje otro: ")
    elif xy == "2":
        if xy in rangos:
            del rangos['2']
            xy2 = "X"
            tableroInteractivo()
            break
        else:
            xy = input("Juego: Ese numero ya esta ocupado, escoje otro: ")
    elif xy == "3":
        if xy in rangos:
            del rangos['3']
            xy3 = "X"
            tableroInteractivo()
            break
        else:
            xy = input("Juego: Ese numero ya esta ocupado, escoje otro: ")
    elif xy == "4":
        if xy in rangos:
            del rangos['4']
            xy4 = "X"
            tableroInteractivo()
            break
        else:
            xy = input("Juego: Ese numero ya esta ocupado, escoje otro: ")
    elif xy == "5":
        if xy in rangos:
            del rangos['5']
            xy5 = "X"
            tableroInteractivo()
            break
        else:
            xy = input("Juego: Ese numero ya esta ocupado, escoje otro: ")
    elif xy == "6":
        pranter()
        if xy in rangos:
            del rangos['6']
            xy6 = "X"
            tableroInteractivo()
            break
        else:
            xy = input("Juego: Ese numero ya esta ocupado, escoje otro: ")
    elif xy == "7":
        if xy in rangos:
            del rangos['7']
            xy7 = "X"
            tableroInteractivo()
            break
        else:
            xy = input("Juego: Ese numero ya esta ocupado, escoje otro: ")
    elif xy == "8":
        if xy in rangos:
            del rangos['8']
            xy8 = "X"
            tableroInteractivo()
            break
        else:
            xy = input("Juego: Ese numero ya esta ocupado, escoje otro: ")
    elif xy == "9":
        if xy in rangos:
            del rangos['9']
            xy9 = "X"
            tableroInteractivo()
            break
        else:
            xy = input("Juego: Ese numero ya esta ocupado, escoje otro: ")
    else:
        print("Juego: Solo se permite un rango de 1-9")
        xy = input("escoje otro: ")
  ganador()
  if br == "Break":
    break
  computadoraEntrada()
  ganador()
  if br == "Break":
    break
input()
