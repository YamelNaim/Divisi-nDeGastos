total_a_pagar= float(input("Total a pagar: "))

print("Cuantos son? ")
c_pers=int(input())

print("Alguien ya puso plata? ")
rta=str(input("Y or N: "))

total_a_pagar= total_a_pagar/c_pers

if rta=="y" or rta=="Y":
    print("Quien? ")
    rta2=str(input()) 
    plata_rta2=float(input("Cuanto? "))

    plata_rta2= total_a_pagar-plata_rta2

    print(str(total_a_pagar) + " pesos cada uno. ")
    print("Excepto", str(rta2 )+": " + str( plata_rta2) + " pesos. " )
else:
    print(str(total_a_pagar) + " pesos cada uno. " )




