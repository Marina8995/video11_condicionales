#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos deberán ser almacenados en una lista y 
#mostrar en consola el mensaje: “Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado).

nombre=(input("Escribe tu nombre: "))
direccion=(input("Escribe tu dirección: "))
telefono=(input("Escribe tu número de teléfono: "))

lista=[nombre, direccion, telefono]

print("La lista de los datos son: " +lista[0]+" "+lista[1]+" " + lista[2])