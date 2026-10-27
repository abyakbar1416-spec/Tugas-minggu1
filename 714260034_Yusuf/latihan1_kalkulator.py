#latihan_kalkulator.py
#============================================
# PROGRAM KALKULATOR SEDERHANA
#============================================

print("============================================")
print("     PROGRAM KALKULATOR SEDERHANA")
print("============================================")
print("Pilih operasi matematika: +,-,*,/")
print("--------------------------------------------")

# --- Bagian masukan pengguna ---
angka1 = float(input("Masukkkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+,-,*,/): ")

print("--------------------------------------------")

# --- Bagian proses ---
if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil:.2f}")

elif operator == "-":
    hasil = angka1 - angka2
    print (f"Hasil: {angka1} - {angka2} = {hasil:.2f}")

elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil:.2f}")

elif operator == "/":
    hasil = angka1 / angka2
    print(f"Hasil: {angka1} / {angka2} = {hasil:.2f}")

else:
    print(f"Operator '{operator}' tidak dikenali.")
    print("Gunakan salah satu dari: +, -, *, /")

print("=============================================")
print("Terima kasih telah menggunakan kalkulator ini.!")
