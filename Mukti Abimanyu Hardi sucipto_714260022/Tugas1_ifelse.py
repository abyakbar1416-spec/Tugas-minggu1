#===================
# Tugas mandiri modul 1 - Program Percabangan
# Nama  : Mukti abimanyu Hardi Sucipto
# NIM   : 714260022
# Kelas : 1B D4 TI
# Kelompok : 3 The panturas
print("===========================")
print("Program nilai rapot siswa")
print("===========================")

nilai = float (input("Nilai Pembelajaran (0-100): "))

if nilai <0 or nilai >100:
     print("error: Nilai harus 0-100: ")
elif nilai >= 90:
    huruf = "A"
    status = "lulus"
    print(f"nilai {nilai} setara dengan mutu {huruf} dan dinyatakan {status}.")
elif nilai >= 80:
    huruf = "B"
    status = "lulus"
    print(f"nilai {nilai} setara dengan mutu {huruf} dan dinyatakan {status}.")
elif nilai >= 70:
    huruf = "C"
    status = "lulus"
    print(f"nilai {nilai} setara dengan mutu {huruf} dan dinyatakan {status}.")
elif nilai >= 60:
    huruf = "D"
    status = "Tidak lulus"
    print(f"nilai {nilai} setara dengan mutu {huruf} dan dinyatakan {status}.")
else:
    huruf = "E"
    status = "Tidak lulus"
    print(f"nilai {nilai} setara dengan mutu {huruf} dan dinyatakan {status}.")

print("============================================")
print("terimakasih telah menggunakan program ini.")
print("============================================")