tahun = int(input("Masukkan Tahun: "))

def isKabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 4 == 0 and tahun % 100 != 0:
        return True
    else:
        return False

hasil = isKabisat(tahun)

if hasil:
    print(f"{tahun} adalah kabisat")
else:
    print(f"{tahun} bukan kabisat")