import re
from karyawan import Karyawan

def get_valid_name():
    # Memastikan pengguna hanya memasukkan nama yang berisi huruf dan angka
    while True:
        name = input("Masukkan Nama: ").strip()
        if name and re.match(r'^[a-zA-Z0-9 ]+$', name):  # Hanya alphanumeric dan tidak boleh kosong
            return name
        else:
            print("Nama hanya boleh berisi huruf dan angka, serta tidak boleh kosong!")

def get_valid_position():
    # Memastikan pengguna hanya memasukkan posisi IT, HR, atau Director
    valid_positions = ["IT", "HR", "DIRECTOR"]
    while True:
        position = input("Masukkan posisi (IT/HR/Director): ").strip().upper()  # Ubah ke huruf besar
        if position in valid_positions:
            return "Director" if position == "DIRECTOR" else position  # Pastikan "DIRECTOR" -> "Director"
        else:
            print("Posisi tidak valid! Silakan masukkan IT, HR, atau Director.")

def get_valid_salary():
    # Memastikan pengguna hanya memasukkan gaji berupa angka positif
    while True:
        try:
            salary = float(input("Masukkan Gaji: ").strip())
            if salary > 0:
                return salary
            else:
                print("Gaji harus lebih dari 0!")
        except ValueError:
            print("Input tidak valid! Masukkan angka.")

# Inputan dari pengguna
name = get_valid_name()
position = get_valid_position()
salary = get_valid_salary()

# Instance karyawan
karyawan = Karyawan(name, position, salary)

# Menampilkan informasi karyawan
print("\n=== Informasi Karyawan ===")
print(karyawan.get_info())
print(karyawan.get_salary())

# Menampilkan gaji karyawan setelah kenaikan
print("\n=== Proses Kenaikan Gaji ===")
print(karyawan.increase_salary())