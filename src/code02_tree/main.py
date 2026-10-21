class Negara:
    def __init__(self, id, nama):
        self.id = id
        self.nama = nama

    def __str__(self):
            return f"{self.nama}"

class Provinsi:
     def __init__(self, id, nama, negara):
             self.id = id
             self.nama = nama
             self.negara = negara
             
     def __str__(self):
             return f"{self.nama}"

class ProfilMahasiswa:
    def __init__(self, nim, nama, provinsi):
        self.nim = nim
        self.nama = nama
        self.provinsi = provinsi

    def __str__(self):
        return f"Mhs(name={self.nama}, nim={self.nim}, negara={self.provinsi.negara}, provinsi={self.provinsi})"

n1 = Negara(1, "Indonesia")
n2 = Negara(2, "Malaysia")
n3 = Negara(3, "Konoha")

daftar_negara = [n1, n2, n3]

pro1 = Provinsi(1001, "Aceh", daftar_negara[0])
pro2 = Provinsi(1002, "Sumut", daftar_negara[0])
pro3 = Provinsi(1003, "Riau", daftar_negara[0])

daftar_provinsi = [pro1, pro2, pro3]

p1 = ProfilMahasiswa("1234","Affan", daftar_provinsi[2])

print(p1)