pila=[]
#push
pila.append("A")
pila.append("B")

#peek
print("Tope:", pila[-1])#B

#pop
print("Elemento retirado:", pila.pop())#B

#isEmpty
print("¿Pila vacía?", len(pila) == 0) #False (por queda "A")

#######################################################################
