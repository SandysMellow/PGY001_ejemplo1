import funciones as fu

while True:
    fu.lp()
    fu.pv("SISTEMA VENTABOOKS")
    fu.pv("-------------------")
    print("1) Guardar")
    print("2) Buscar")
    print("3) Certificados")
    print("0) Salir")

    opcion = int(input("Seleccione: "))
    if opcion==0:
        fu.pa("Adios")
        break

    elif opcion==1:
        fu.pv("GUARDAR")

    elif opcion==1:
        fu.pv("BUSCAR")

    elif opcion==1:
        fu.pv("CERTIFICADOS")
        
    else:
        fu.pr("NO VALIDO")