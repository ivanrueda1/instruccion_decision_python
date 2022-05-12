"""Ejercicio4
calcular la masa calcular"""

print("-----------------------")
print("-----CALCULAR PESO-----")
print("-----------------------")

# input
peso=int(input(" ponga su peso: "))
altura=float(input(" Ponga su altura: "))

#processing

imc=peso/(altura**2)

# output

if imc<16:
    print(" criterio de ingreso en hospital")
elif imc>=16 and imc<=17:
    print(" infrapeso  ")
elif imc>17 and imc<=18:
    print(" bajo peso ")
elif imc>18 and imc<=25:
    print(" peso normal ")
elif imc>25 and imc<=30:
    print(" sobrepeso ")
elif imc>30 and imc<=35:
    print(" sobrepeso cronico ")
elif imc>35 and imc<=40:
    print(" obecidad premorbida ")
elif imc>40:
    print(" obecidad morbida ")    
