#Encoding: UTF-8
#Autor: Manuel Zavala Gmez
#Indice de Masa Corporal 

def main():
    kg= float(input("¿Cual es tu peso?"))
    m= float(input("¿Cual es tu estatura?"))
    calcularIndice (kg, m)
    
def calcularIndice (kg,m):
    if kg==0 or m==0:
        print("Error") 
    elif kg< 0 or m<0:
        print("Error")       
    else:
        i= (kg/(m**2))
        print ("Tu masa corporal es:",i)
        if kg< 0 or m<0:
            print("Error")
        elif i <= 18.5 and i >0:
            print("Bajo peso")
        elif i >= 18.5 and i <= 25:
            print("Peso Normal")
        elif i> 25 :
            print("Sobre peso")

main()