#Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” encargada de devolver el 
#número más alto de los dos introducidos.

num1=int(input("Introduzca el primer número: "))
num2=int(input("Introduzca el segundo número: "))

def DevuelveMax (n1, n2):
    if n1>n2:
        print(n1)
    elif n2>n1:
        print(n2)    
    else:
        print("Los dos números son iguales")    

print("El número más alto es: ")        

DevuelveMax (num1, num2)        
