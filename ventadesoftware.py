#Encoding: UTF-8
#Autor: Manuel Zavala Gmez
#Venta de software 
def main():
    numero= int(input("Cuantos paquetes compraste?"))
    aplicarDescuento(numero)
    
def aplicarDescuento (numero):
    if numero >= 1 and numero <= 9 :
        t= (numero*1500)
        print ("Tu total es:$%.2f"% t)
        
    elif numero >= 10 and numero <= 19 :
        t1= ((numero*1500)*.80)
        print ("Tu total es:$%.2f"% t1)
        
    elif numero >= 20 and numero <= 49 :
        t2= ((numero*1500)*.70)
        print ("Tu total es:$%.2f"% t2)
        
    elif numero >= 50 and numero <= 99 : 
        t3= ((numero*1500)*.60)
        print ("Tu total es:$%.2f"% t3)
        
    elif numero >= 100 :
        t4= ((numero*1500)*.50)
        print ("Tu total es:$%.2f"% t4)
        
    elif numero < 0 :
        print ("Error")
        
main()