def isKabisat(tahun):
    return tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0)

tahun = int(input())
print(isKabisat(tahun))