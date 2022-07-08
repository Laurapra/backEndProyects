import re


def ingreso_datos():
    ingreso = input().split()
    return [int(ingreso[i]) for i in range(len(ingreso))]


def buscarMenor(lista):
    menor = 0
    contador = 0
    for i in range(len(lista)):
        if i == 0 or menor > lista[i]:
            menor = lista[i]
            contador = i

    return (contador + 1), menor

def incializarSucursales(n):
    lista = []
    for i in range(n):
        lista.append(0)
    return lista

def buscarMayor(lista):
    mayor = 0
    contador = 0
    for i in range(len(lista)):
        if i == 0 or mayor < lista[i]:
            mayor = lista[i]
            contador = i

    return (contador + 1), mayor

def promedio(lista):
    suma=0
    
    for i in range (len(lista)):
        suma = suma + lista[i]
    return suma/len(lista)

def promedioPacientes(lista, pacientesSucursal):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]

    if pacientesSucursal != 0:
        return suma/pacientesSucursal
    else:
        return 0

def entrega_medicamento():
    if ps < 90 and pd < 70:
        return True
    elif 90 <= ps < 130 and 70 <= pd < 90:
        return False
    elif 130 <= ps < 140 and 90 <= pd < 95:
        return False
    elif 140 <= ps < 150 and 95 <= pd < 100:
        return True
    elif 150 <= ps < 170 and 100 <= pd < 110:
        return True
    elif 170 <= ps < 190 and 110 <= pd < 120:
        return True
    elif ps >= 190 and pd >= 120:
        return True
    elif ps >= 150 and pd < 100:
        return True
    else:
        return False

incorrecto = True
while incorrecto:
    ingreso = input()
    lista = ingreso.split()
    n, k, m = lista
    n, k, m = int(n), int(k), int(m)
    incorrecto = False if n > 0 and k > 0 else True

existencias = [ingreso_datos() for i in range(n)]

entregas = [[0 for j in range(k)] for i in range(n)]
cantidadPacientesSucursal=incializarSucursales(n)

for i in range(m):
    sucursal, tipom, cantidad, ps, pd = input().split()
    sucursal, tipom, cantidad, ps, pd = int(sucursal), int(
        tipom), int(cantidad), int(ps), int(pd)
    cantidadPacientesSucursal[sucursal-1] = cantidadPacientesSucursal[sucursal-1]  + 1
    if entrega_medicamento():
        entregas[sucursal - 1][tipom - 1] += cantidad

loquequeda = [[existencias[i][j] - entregas[i][j]
               for j in range(k)] for i in range(n)]


for i in range(len(loquequeda)):
    print(i+1)
    tipoMedicamento, existencia = buscarMenor(loquequeda[i])
    print(tipoMedicamento, existencia)
    tipoMedicamento, existencia = buscarMayor(loquequeda[i])
    print(tipoMedicamento, existencia)
    contador, menor = buscarMenor(entregas[i])
    contador1, mayor = buscarMayor(entregas[i])
    _promedio = promedio(entregas[i])

    print(f"{menor:.2f} {_promedio:.2f} {mayor:.2f}")
    prome=promedioPacientes(entregas[i], cantidadPacientesSucursal[i])
    print(f"{prome:.2f}")
        

medicamentosTipo1=[]
for i in range(len(entregas)):
    medicamentosTipo1.append(entregas[i][0])

contador2, menor2=buscarMenor(medicamentosTipo1)
contador3, mayor2=buscarMayor(medicamentosTipo1)
print(contador2, menor2)
print(contador3, mayor2)
