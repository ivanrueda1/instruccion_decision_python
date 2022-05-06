"""Ejercicio 1
Programa que lea las coordenadas cartesianas (X, Y) de un punto en el plano y calcule el cuadrante
al cual pertenece el punto. si el punto está sobre un eje también debe indicarlo"""

print("-----------------------------------")
print("-------------LECTOR DE COORDENADAS-------------")
print("-----------------------------------")

# input

X = int(input("digite la coordenada en X:  "))
Y = int(input("digite la coordenada en Y:  "))

# prossecing

if X==0 and Y==0:
    resultado=("El punto esta sobre el origen")
elif X==0 and Y>0:
    resultado=("El punto esta sobre el eje positivo de las abscisas") 
elif X==0 and Y<0:
    resultado=("El punto esta sobre el eje negativo de las abscisas")
elif X>0 and Y>0:
    resultado=("El punto esta en el primer cuadrante")
elif X<0 and Y>0:
    resultado=("El punto esta en el segundo cuadrante") 
elif X<0 and Y<0:
    resultado=("El punto esta en el tercer cuadrante")
elif X>0 and Y<0:
    resultado=("El punto esta en el cuarto cuadrante")              
elif X>0 and Y==0:
    resultado=("El punto esta sobre el eje positivo de las ordenadas")
elif X<0 and Y==0:
    resultado=("El punto esta sobre el eje negativo de las ordenadas")

# output

print("Si X equivale a : " + str(X) + " y Y equivale a " + str(Y) + " entonces..." + str(resultado)) 
                