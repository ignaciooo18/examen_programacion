import menu_funciones as fn
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"] 
sueldos={}
sueldo_bruto={}
while True:
    try:
        opc=int(input("***MENU PRINCIPAL***\ningrese una de las opciones que desee ejecutar\n1.asignar sueldos aleatorios\n2.clasificar de suelos\n3.ver estadisticas\n4.reporte de suelos\n5.salir del programa\n---->"))
        if opc == 1:
            sueldos,sueldo_bruto=fn.asignar_sueldos(trabajadores)
        elif opc == 2:
            if sueldo_bruto:
                fn.clasificar(sueldo_bruto)
            else:
                print("debe generar aleatoriamente los sueldos primero")
        elif opc == 3:
            if sueldo_bruto:
                fn.estadisticas(sueldo_bruto)
            else:
                print("debe generar aleatoriamente los suelos primero")
        elif opc == 4:
            if sueldos:
                fn.reporte_sueldos(sueldos)
                fn.generar_csv(sueldos)
            else:
                print("debe generar aleatoriamente los sueldos primero")
        elif opc==5:
            print("gracias por probar nuestro sistema de sueldos aleatorio\nsaliendo...")
            break
        else:
            print("debe ingresar una de las opciones que se muestran en patalla por favor")
    except ValueError:
        print("ingrese una de las opciones que se muestren en pantalla y no un valor alfabetico")
    except KeyError:
        print("funcion no terminada, las siguientes funcionan")