import os 
os.system("cls")

f=open("data.csv")
def entrega_med(ps, pd):
    if ps<91 and pd <63:
        return True
    elif 91<=ps<134 and 63<=pd<77:
        return False
    elif 134<=ps<162 and 77<=pd<105:
        return False
    elif 162<=ps<188 and 105<=pd<119:
        return True
    elif 188<=ps<201 and 119<=pd<126:
        return True
    elif 201<=ps<214 and 126<=pd<146:
        return True
    elif ps >= 214 and pd >=146:
        return True
    elif ps >= 152 and pd < 77:
        return True
    else:
        return False

datos=f.readlines()
f.close()
for i in range(len(datos)):
    datos[i]=datos[i].replace("\n","")
campos=datos.pop(0).split(",")
informacion=[]
for i in range(len(datos)):
    elemento={}
    fila=datos[i].split(",")
    for j in range(len(fila)):
        elemento[campos[j]]=fila[j]
    informacion.append(elemento)
id=input()
cont_h=0
cont_m=0
cont_t=0
cant_e=0
cant_q = 0
for fila in informacion:
    cant_e+=1
    if fila["id_branch"]==id:
        ciudad=fila["city_name"]
        dpto=fila["department_name"]
        if entrega_med(int(fila["systolic_pressure"]), int(fila["diastolic_pressure"])):
            if fila["gender"]=="f":
                cont_m+=1
            if fila["gender"]=="m":
                cont_h+=1
            cont_t+=1
            cant_q = cant_q + (int(fila["medicine_quantity"]))

print(f"{id} {ciudad } {dpto}")
print("scheduled patients")
print(f"male {cont_h}")
print(f"female {cont_m}")
print(f"total {cont_t}")
print("scheduled medicine quantity")
promedio = (cant_q / cont_t)
print(f"mean {promedio:.2f}")
print(f"total {cant_q}")