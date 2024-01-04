# latihan konversi satuan temperature
# program konversi celcius ke satuan lain
print("===PROGRAM KONVERSI TEMPERATUR===")

celcius = float(input('Masukkan suhu dalam Celcius = '))
print("Suhu adalah = ", celcius, "Celcius")

#reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah = ", reamur, "Reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah = ", fahrenheit, "Fahrenheit")

#kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah = ", kelvin, "Kelvin")


# TUGAS
# Fahrenheit ke Kelvin
print("\n===Fahrenheit to Kelvin===")
fahrenheit =float(input('Masukkan Suhu dalam Fahrenheit = '))
print("Suhu Awal = ", fahrenheit," Fahrenheit")

kelvin = (5/9*(fahrenheit-32)) + 273
print("suhu dalam kelvin = ", kelvin," Kelvin")

# Kelvin ke Fahrenheit
print("\n===Kelvin to Fahrenheit===")
kelvin = float(input('Masukkan Suhu Awal = '))
print("Suhu Awal = ", kelvin," Kelvin")

fahrenheit = (kelvin - 273) * 9/5 + 32
print("Suhu dalam Kelvin = ", fahrenheit," Fahrenheit")