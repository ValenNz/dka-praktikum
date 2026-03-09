celsius = float(input("Masukkan suhu Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius:.1f} °C = {fahrenheit:.2f} °F = {kelvin:.2f} K")