

print("Por favor digite el area: ")
area = float(input())
print("Por favor digite el numero de antenas instaladas: ")
antenasPrevias = int(input())
print("Por favor digite el tipo de las nuevas antenas: ")
tipoAntena = str.upper(input())


if(antenasPrevias >= 0):
    if(tipoAntena == 'A'):
        # 32660
        areaInstaladas = antenasPrevias * 17200
        if (area >= areaInstaladas):
            areaSobrante = area - areaInstaladas
            antenasInstalar = round(areaSobrante / 32600)
            print(antenasInstalar)
        else:
            print("0")
    elif(tipoAntena == 'B'):
        # 31300
        areaInstaladas = antenasPrevias * 17200
        if (area >= areaInstaladas):
            areaSobrante = area - areaInstaladas
            antenasInstalar = round(areaSobrante / 31300)
            print(antenasInstalar)
        else:
            print("0")
    elif(tipoAntena == 'C'):
        # 41300
        areaInstaladas = antenasPrevias * 17200
        if (area >= areaInstaladas):
            areaSobrante = area - areaInstaladas
            antenasInstalar = round(areaSobrante / 41300)
            print(antenasInstalar)
        else:
            print("0")
    elif(tipoAntena == 'D'):
        # 52200
        areaInstaladas = antenasPrevias * 17200
        if (area >= areaInstaladas):
            areaSobrante = area - areaInstaladas
            antenasInstalar = round(areaSobrante / 52200)
            print(antenasInstalar)
        else:
            print("0")
    elif(tipoAntena == 'E'):
        # 38700
        areaInstaladas = antenasPrevias * 17200
        if (area >= areaInstaladas):
            areaSobrante = area - areaInstaladas
            antenasInstalar = round(areaSobrante / 38700)
            print(antenasInstalar)
        else:
            print("0")
    else:
        print("error en los datos")
else:
    print("error en los datos")
