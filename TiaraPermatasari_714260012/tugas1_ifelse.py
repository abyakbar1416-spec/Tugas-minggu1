# ============================================== #
# Tugas Mandiri Modul 1 - Program Percabangan   
# Nama  : Tiara Permatasari
# Nim   : 714260012
# Kelas : 11 D4TI
#=============================================== #

def main():
    print("=" * 50)
    print("PROGRAM KONVERSI NILAI AKHIR - SISTEM IF-ELSE")
    print("=" * 50)
    try:
        nilai = int(input("Masukkan nilai akhir (0 - 100): "))
    except ValueError:
        print("-" * 50)
        print("[ERROR] Input tidak valid! Harap masukkan angka 0 - 100.")
        print("-" * 50)
        print("Terima kasih telah menggunakan program ini.")
        return

    if nilai < 0 or nilai > 100:
        print("-" * 50)
        print(f"[ERROR] Nilai {nilai} tidak valid! Nilai harus berada di rentang 0 - 100.")
        print("-" * 50)
        print("Terima kasih telah menggunakan program ini.")
        return

    if nilai >= 85:
        huruf_mutu = "A"
        status = "Lulus"
    elif nilai >= 70:
        huruf_mutu = "B"
        status = "Lulus"
    elif nilai >= 60:
        huruf_mutu = "C"
        status = "Lulus"
    elif nilai >= 50:
        huruf_mutu = "D"
        status = "Tidak Lulus"
    else:
        huruf_mutu = "E"
        status = "Tidak Lulus"

    print("-" * 50)
    print("HASIL KONVERSI NILAI:")
    print(f"Nilai Angka  : {nilai}")
    print(f"Huruf Mutu   : {huruf_mutu}")
    print(f"Keterangan   : {status}")
    print("-" * 50)
    print("Terima kasih telah menggunakan program ini.")
    print("=" * 50)

if __name__ == "__main__":
    main()