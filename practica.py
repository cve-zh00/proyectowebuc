import time
import random


malas = 0
buenas = 0
for i in range(1,11):
    numero1 = random.randint(2,99)
    numero2 = random.randint(2,99)
    print(f"Cuanto es {numero1} * {numero2}")
    print(f"Inicia la cuenta regresiva")
    for j in range(10,-1,-1):
        
        time.sleep(1)
        if j == 0:
            respuesta = int(input("Escribe tu respuesta\n"))
            resultado = numero1 * numero2
            if respuesta == (numero1 * numero2):
                print("respuesta correcta ")
                buenas +=1
                
            else:
                
                print("respuesta incorrecta")
                malas += 1
                print(f"La respuesta correcta es {resultado}")
    if i == 10:
        print(f"Tuviste {buenas} buenas y {malas} malas")