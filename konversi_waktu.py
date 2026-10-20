total_detik = 3725

jam = total_detik // 3600
sisa = total_detik % 3600
menit = sisa // 60
detik = sisa % 60

print(f"(total_detik) detik = (jam) jam (menit) menit (detik) detik")