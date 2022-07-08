from math import ceil

sumAntenasInstalar = 0

antenasA = 0
antenasB = 0
antenasC = 0
antenasD = 0
antenasE = 0

sumAntenasA = 0
sumAntenasB = 0
sumAntenasC = 0
sumAntenasD = 0
sumAntenasE = 0

perA = float(0)
perB = float(0)
perC = float(0)
perD = float(0)
perE = float(0)

#print("Por favor digite el numero de areas:")
numAreas = int(input())

while numAreas > 0:
    #print("Por favor digite el area: ")
    area = float(input())
    #print("Por favor digite el numero de antenas instaladas: ")
    antenasPrevias = int(input())
    #print("Por favor digite el tipo de las nuevas antenas: ")
    tipoAntena = str.upper(input())

    areaInstaladas = antenasPrevias * 17200
    areaSobrante = area - areaInstaladas

    if(antenasPrevias >= 0):
        if(tipoAntena == 'A'):
            # 32660
            if (area >= areaInstaladas):
                antenasA = ceil(areaSobrante / 32600)
            else:
                antenasA = 0
        elif(tipoAntena == 'B'):
            # 31300
            if (area >= areaInstaladas):
                antenasB = ceil(areaSobrante / 31300)
            else:
                antenasB = 0
        elif(tipoAntena == 'C'):
            # 41300
            if (area >= areaInstaladas):
                antenasC = ceil(areaSobrante / 41300)
            else:
                antenasC = 0
        elif(tipoAntena == 'D'):
            # 52200
            if (area >= areaInstaladas):
                antenasD = ceil(areaSobrante / 52200)
            else:
                antenasD = 0
        elif(tipoAntena == 'E'):
            # 38700
            if (area >= areaInstaladas):
                antenasE = ceil(areaSobrante / 38700)
            else:
                antenasE = 0
        else:
            print("error en los datos")
    # else:
        #print("error en los datos")
        # print("A: ", antenasA, "B: ", antenasB, "C: ",
        #      antenasC, "D: ", antenasD, "E: ", antenasE)
    sumAntenasA += antenasA
    sumAntenasB += antenasB
    sumAntenasC += antenasC
    sumAntenasD += antenasD
    sumAntenasE += antenasE

    antenasA = 0
    antenasB = 0
    antenasC = 0
    antenasD = 0
    antenasE = 0

    numAreas -= 1  # numAreas = numAreas - 1
sumAntenasInstalar = sumAntenasA + sumAntenasB + \
    sumAntenasC + sumAntenasD + sumAntenasE

perA = float(sumAntenasA / sumAntenasInstalar)*100 if sumAntenasA > 0 else 0.00
perB = float(sumAntenasB / sumAntenasInstalar)*100 if sumAntenasB > 0 else 0.00
perC = float(sumAntenasC / sumAntenasInstalar)*100 if sumAntenasC > 0 else 0.00
perD = float(sumAntenasD / sumAntenasInstalar)*100 if sumAntenasD > 0 else 0.00
perE = float(sumAntenasE / sumAntenasInstalar)*100 if sumAntenasE > 0 else 0.00


print(sumAntenasInstalar)
print("a ", f"{perA:.2f}%")
print("b ", f"{perB:.2f}%")
print("c ", f"{perC:.2f}%")
print("d ", f"{perD:.2f}%")
print("e ", f"{perE:.2f}%")
