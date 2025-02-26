print("De 1 a 100, indique el valor de la calificación")

evaluacion1=float(input("¿Cuál es la calificación en la evaluación 1?"))
evaluacion2=float(input("¿Cuál es la calificación en la evaluación 2?"))
evaluacion3=float(input("¿Cuál es la calificación en la evaluación 3?"))
evaluacion4=float(input("¿Cuál es la calificación en la evaluación 4?"))
evaluacion5=float(input("¿Cuál es la calificación en la evaluación 5?"))

promedio=(evaluacion1+evaluacion2+evaluacion3+evaluacion4+evaluacion5)/5

print("Promedio: ", promedio) 

if promedio >=60:
    print("Aprobado")
elif promedio <40:
    print("Reprobado")
else:
    print("En recuperación")