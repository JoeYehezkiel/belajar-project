#by kiel manurung
def hitung_ipk(nilai_list):
    konversi = {'A':4, 'B':3, 'C':2, 'D':1, 'E':0}
    total = 0
    for nilai in nilai_list:
        total += konversi.get(nilai.upper(), 0)
    return total / len(nilai_list)

#dicoba nih
mata_kuliah = ["A", "B", "C", "A"]
ipk = hitung_ipk(mata_kuliah)
print(f"IPK Anda: {ipk:.2f}")