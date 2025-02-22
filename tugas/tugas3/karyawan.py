# Modul Karyawan

class Karyawan:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary  # Salary bersifat confidential (private)

    def get_info(self):
        # Menampilkan informasi karyawan
        return f"Nama: {self.name}, Posisi: {self.position}"

    def increase_salary(self):
        # Menaikkan gaji berdasarkan posisi
        raise_percentage = {
            "IT": 0.10,
            "HR": 0.15,
            "Director": 0.01
        }
        
        if self.position in raise_percentage:
            self.__salary += self.__salary * raise_percentage[self.position]
        
        return f"Gaji {self.name} telah diperbarui menjadi Rp {self.__salary:,.2f}"

    def get_salary(self):
        # Mengembalikan nilai salary (diakses melalui method ini)
        return f"Gaji {self.name} adalah Rp {self.__salary:,.2f}"