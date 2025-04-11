#for i in range(0,5+1):
    #print("tabla del", i)
    #for j in range(0,10+1):
        #print(i,"*",j,"=",i*j)
        
        
        
for i in[0,1,2]:
    print("Emeneses:",i)

for i in [1,4,8]:
    print("El valor de",i, "y su cuadrado es", i**2)
    
for i in ["Edison", 20, "Ecuador", True]:
    print("El valor de i es", i)
    
for i in[1,2,3,4,5]:
    print("Tabla del", i)
    for j in [1,2,3,4,5]:
        print(i,"*",j,"=",i*j)

resto=5%2
print("El resto de la division de 5 entre 2 es:",resto)
if resto==0:
    print("El número es par") 
else:
    print("El número es impar")
    
#EJERCICIO
#1 al 10 son pares o impares
print("*"*22)
lista=[1,2,3,4,5,6,7,8,9,10]
for i in lista:
    if i%2==0:
        print("Es par",i)
    else:
        print("No es par",i)
        
print("*"*22)
for i in range(1,11):
    if i%2!=0:
        print("Es impar",i)
print("*"*22)
for i in range(1,11):
    if i%2==0:
        print("Es par",i)

