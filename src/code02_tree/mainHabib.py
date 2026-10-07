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
        return f"{self.nama} ({self.negara})"

class ProfilMahasiswa:
    def __init__(self, nim, nama, provinsi):
        self.nama = nama
        self.nim = nim
        self.provinsi = provinsi

    def __str__(self):
        return f"Mhs(name={self.nama}, nim={self.nim}, provinsi={self.provinsi})"

n1 = Negara(1, "Indonesia")
n2 = Negara(2, "Malaysia")
n3 = Negara(3, "Konoha")

daftar_negara = [n1, n2, n3]

pro1 = Provinsi(1, "Jawa Barat", daftar_negara[0])
pro2 = Provinsi(2, "Jawa Timur", daftar_negara[0])
pro3 = Provinsi(3, "Selat Malaka", daftar_negara[1])

p1 = ProfilMahasiswa("1234", "Affan", pro1)

print(p1)