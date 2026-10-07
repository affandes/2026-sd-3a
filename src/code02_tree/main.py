class Negara:
    def __init__(self, id, nama):
        self.id = id
        self.nama = nama

    def __str__(self):
            return f"{self.nama}"

class ProfilMahasiswa:
    def __init__(self, nim, nama, negara):
        self.nim = nim
        self.nama = nama
        self.negara = negara

    def __str__(self):
        return f"Mhs(name={self.nama}, nim={self.nim}, negara={self.negara})"

n1 = Negara(1, "Indonesia")
n2 = Negara(2, "Malaysia")
n3 = Negara(3, "Konoha")

daftar_negara = [n1, n2, n3]

p1 = ProfilMahasiswa("1234","Affan", daftar_negara[0])

print(p1)