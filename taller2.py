#PROGRAMA DE CALIFICACION
print("."*30)
print("Bienvenido al sistema de calificaciones")
print("."*30)


   #Usamos este bloque para manejar errores.
while True:
 try:
            #SE SOLICITA AL USUARIO INGRESAR DATO   
            nota=float(input("ingrese una calificación entre 0 y 100:"))
            print("."*30)
            #verificar rango correcto
            if 0 <= nota <=100:
                if nota >=60:
                    print("El estudiante aprobó el curso")
                else:
                    print("El estudiante reprobó el curso")    
            else:
                print("ERROR:ingrese un número permitido en el rango de 0 a 100")        
                break
 except ValueError:
        print ("Error:ingresa un numero valido")
        print("."*30)
 
    # se pide lista de notas al usuario separada por comas
 lista= input("Ingresa una lista de calificaciones separadas por comas:")
    #se convierte esa cadena  en una lista de numeros 
 notas= [float(x.strip()) for x in lista.split(",")]
 #se hace ṕara el promedio 
 promedio= sum(notas)/ len(notas)
 print(f"El promedio de las calificaciones es:{promedio}")


______________________________
