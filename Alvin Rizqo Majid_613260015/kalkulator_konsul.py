print("====================================")
print("     KALKULATOR KONSOL SEDERHANA")
print("====================================")
print("Operasi tersedia: + - * /")
print("-------------------------------------")

angka1 = float(input("Masukkan bilangan pertama : "))
angka2 = float(input("Masukkan bilangan kedua : "))
operator = input("Masukkan operator (+ - * /): ")

print("----------------------------------")

if operator == "+":
    hasil = angka1 + angka2
    print (f"Hasil: {angka1} + {angka2} = {hasil:.2f}")

elif operator == "-":
    hasil = angka1 + angka2
    print(f"hasil: {angka1} - {angka2} = {hasil:.2f}")

elif operator == "*":
    hasil = angka1 * angka2
    print(f"hasil: {angka1} x {angka2} = {hasil:.2f}")

elif operator == "/":
    if angka2 == 0:
        print("kesalahan: bilangan tidak dapat dibagi dengan nol. ")
    else:
        hasil = angka1 / angka2
        print(f"hasil: {angka1} : {angka2} = {hasil:.2f}")

else:
    print(f"operator '{operator}' tidak dikenali.")
    print("gunakan salah satu dari: + - * /")

print("==================")
print("terima kasih telah menggunakan kalkulator ini.")