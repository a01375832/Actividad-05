#Encoding: UTF-8
#Autor: Manuel Zavala Gomez
#Mezclador de color 

def main():
    c1=raw_input("Primer color")
    c1=c1.lower()
    c2=raw_input("Segundo color")
    c2=c2.lower()
    calcularMezcla(c1,c2)
    
def calcularMezcla(c1,c2):
    if c1==("rojo") and c2==("azul"):
        print("Morado")
    elif c1==("azul") and c2==("rojo"):
        print("Morado")
    elif c1==("rojo") and c2==("amarillo"):
        print("Naranja")
    elif c1==("amarillo") and c2==("rojo"):
        print("Naranja")
    elif c1==("azul") and c2==("amarillo"):
        print("Verde")
    elif c1==("amarillo") and c2==("azul"):
        print("Verde")
    elif c1==("rojo") and c2==("rojo"):
        print("Rojo")
    elif c1==("azul") and c2==("azul"):
        print("Azul")
    elif c1==("amarillo") and c2==("amarillo"):
        print("Amarillo")             
    else:
        print("Error") 
                         
main()                      