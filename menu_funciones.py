import csv,random
from statistics import geometric_mean

def asignar_sueldos(trabajadores):
    sueldos={}
    sueldo_bruto={}
    for trabajador in trabajadores:
        sueldo_inicial=random.randint(300000,2500000)
        sueldo_bruto[trabajador]=sueldo_inicial
        desc_salud =round(sueldo_inicial*0.07)
        desc_afp=round(sueldo_inicial*0.12)
        sueldo_liquido= sueldo_inicial-desc_afp-desc_salud
        sueldos[trabajador]={
        "sueldo inicial":sueldo_inicial,
        "descuento salud":desc_salud,
        "descuento afp": desc_afp,
        "sueldo liquido": sueldo_liquido
        }
    print(sueldos,sueldo_bruto)
    return(sueldos,sueldo_bruto)

def clasificar(sueldos):
    bajo_sueldo={}
    medio_sueldo={}
    alto_sueldo={}
    valor = sueldos["sueldo inicial"]
    if valor < 800000:
        bajo_sueldo[trabajador]=valor
    elif valor>800000 and valor<2000000:
        medio_sueldo[trabajador]=valor
    else:
        alto_sueldo[trabajador]=valor

        print("SUELDOS MENORES A 800000 TOTAL:",len(bajo_sueldo))
        for trabajador,sueldos in bajo_sueldo.items():
            print(trabajador,sueldos)
        print("SUELDOS ENTRE 800000 Y 2000000 TOTAL: ",len(medio_sueldo))
        for trabajador,sueldos in medio_sueldo.items():
            print(trabajador,sueldos)
        print("SUELDOS SUPERIORES A 2000000")
        for trabajador,sueldos in medio_sueldo.items():
            print(trabajador,sueldos)

def estadisticas(sueldo_bruto):
    list_sueldo=list(sueldo_bruto.values())
    sueldo_min=min(list_sueldo)
    sueldo_max=max(list_sueldo)
    promedio=round(sum(list_sueldo)/len(list_sueldo))
    media_geo=round(geometric_mean(list_sueldo))
    print("el sueldo mas bajo es:",sueldo_min)
    print("el sueldo mas alto es:",sueldo_max)
    print("el promedio de sueldos es:",promedio)
    print("la media geometrica de los sueldos es:",media_geo)

def reporte_sueldos(sueldos):
    print("nombre empleado","        sueldo inicial","         descuento salud","        descuento afp","          sueldo liquido")
    for trabajador,datos in sueldos.items():
        print(f"{trabajador}\t\t{datos["sueldo inicial"]}\t\t\t{datos["descuento salud"]}\t\t\t{datos["descuento afp"]}\t\t\t{datos["sueldo liquido"]}")
def generar_csv(sueldos):
    with open("listado.csv","w")as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow (["nombre empleado","sueldo inicial","descuento salud","descuento afp","sueldo liquido"])
        for trabajador, datos in sueldos.items():
            sueldo_inicial=datos["sueldo inicial"]
            desc_salud=datos["descuento salud"]
            desc_afp=datos["descuento afp"]
            sueldo_liquido=datos["sueldo liquido"]
            escritor.writerow([trabajador,sueldo_inicial,desc_salud,desc_afp,sueldo_liquido])