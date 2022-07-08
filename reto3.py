def calculo(p1,p2):
    if p1<90 and p2 <70:
        categoria= "Hipotension"
        Dosis= 15
    elif 90<=p1<130 and 70<=p2<90:
        categoria= "Optima"
        Dosis= 0
    elif 130<=p1<140 and 90<=p2<95:
        categoria= "Normal"
        Dosis= 0
    elif 140<=p1<150 and 95<=p2<100:
        categoria= "Normal - Alta"
        Dosis= 10
    elif 150<=p1<170 and 100<=p2<110:
        categoria= "HTA Grado 1"
        Dosis= 10
    elif 170<=p1<190 and 110<=p2<120:
        categoria= "HTA Grado 2"
        Dosis= 20
    elif 190<=p1 and 120<=p2:
        categoria= "HTA Grado 3"
        Dosis= 50
    elif 150<=p1 and p2<100:
        categoria= "HTA Sistolica Aislada"
        Dosis= 20
    else:
        Dosis= "No"
    return Dosis

#Recibir datos
print("Ingrese la cantidad de sucursales y de pacientes: ")
datos=input()
valores=datos.split()
n=int(valores[0])
m=int(valores[1])
while n<1:
    print("Sucursales invalida, digite nuevamente: ")
    datos=input()
    valores=datos.split()
    n=int(valores[0])
    m=int(valores[1])
else:
    sucursales=[]
    sucursales2=[]
    for i in range(n):
        print("Digite la cantidad de medicamentos existentes en la sucursal ",i+1)
        MedicamentosExistentes=int(input())
        while MedicamentosExistentes<1:
            print("Cantidad invalida, digite nuevamente: ",i+1)
            MedicamentosExistentes=int(input())
        sucursales.append(MedicamentosExistentes)
        sucursales2.append(MedicamentosExistentes)

    i=0
    while i<m:
        i+=1
        print("Digite la sucursal, la presion Sistólica y la Diastolica:")
        datos2=input()
        valores2=datos2.split()
        sucursal=int(valores2[0])
        presion=float(valores2[1])
        presion2=float(valores2[2])
        dosis=calculo(presion,presion2)
        if dosis=="No":
            continue
        sucursales[sucursal-1]-=dosis       
    else:
        mayor=sucursales[0]
        for i in range(1,len(sucursales)):
            if sucursales[i]>mayor:
                mayor=sucursales[i]

        menor=sucursales[0]
        posicion=0
        for i in range(1,len(sucursales)):
            if sucursales[i]<menor:
                menor=sucursales[i]
                posicion=i
        print((sucursales.index(menor)+1), menor)
        print((sucursales.index(mayor)+1), mayor)
        
        for i in range(1,len(sucursales)+1):
            dosis2=sucursales2[i-1]-sucursales[i-1]
            porcentaje=(dosis2*100)/sucursales2[i-1]
            print(i, "{:.2f}%".format(porcentaje))
    





        

            
        

