def fibonnaci(n):
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[:n]

n = int(input("Jumlah fibonnaci: "))

print("Bilangan fibonnaci: ", fibonnaci(n))