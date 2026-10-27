float(input("masukkan nilai akihir anda (0-100):"))

print("====================================")

if nilai < 0 or nilai > 100:
    print("kesalahan: Nilai harus berada dalam rentang 0 hingga 100.")
else:
    if nilai >= 88:
        huruf = "A"
        status = "LULUS"
    elif nilai >= 78:
        huruf = "B"
        status = "LULUS"
    elif nilai >= 65:
        huruf = "C"
        status = "LULUS"
    elif nilai >= 60:
        huruf = "D"
        status = "Tidak Lulus"

    print(f"Nilai Anda : {nilai:.1f}")
    print(f"Huruf Mutu : {huruf}")
    print(f"Status : {status}")

print("====================================")
print("Terima Kasih telah menggunakan program ini.")  