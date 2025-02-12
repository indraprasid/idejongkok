# Input dari pengguna
nama = input("Masukkan Nama: ")
pekerjaan = input("Masukkan Pekerjaan: ")
gaji = int(input("Masukkan Gaji: "))

# Perhitungan pajak
pajak = 0.05 * gaji
gaji_bersih = gaji - pajak

# Output hasil
print(f"Nama saya {nama}, pekerjaan saya seorang {pekerjaan}, penghasilan bersih saya sebesar Rp. {gaji_bersih:,.2f} setelah dipotong pajak.")