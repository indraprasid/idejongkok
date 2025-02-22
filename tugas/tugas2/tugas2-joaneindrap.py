# Loop dari 1 sampai 30
angka = 1
while angka < 30:
    # Cek kelipatan 3 dan 5, maka cetak kata dangdut
    if angka % 3 == 0 and angka % 5 == 0:
        print("dangdut")
    # Cek kelipatan 3, maka cetak kata dang
    elif angka % 3 == 0:
        print("dang")
    # Cek kelipatan 5, maka cetak kata dut
    elif angka % 5 == 0:
        print("dut")
    # Cetak angka biasa
    else:
        print(angka)
    angka += 1