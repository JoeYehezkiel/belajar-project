import csv
import os
from datetime import datetime

# Nama file untuk menyimpan data
FILENAME = "data_absen.csv"

def inisialisasi_file():
    """Mengecek apakah file sudah ada. Jika belum, buat header."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Menulis judul kolom (Header)
            writer.writerow(["Nama", "Tanggal", "Jam", "Status"])
        print(f"[INFO] File {FILENAME} berhasil dibuat.")

def catat_kehadiran(nama):
    """Fungsi untuk menyimpan data ke CSV."""
    waktu_sekarang = datetime.now()
    tanggal = waktu_sekarang.strftime("%Y-%m-%d")
    jam = waktu_sekarang.strftime("%H:%M:%S")
    
    # Simpan ke file CSV
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, tanggal, jam, "Hadir"])
    
    print(f"✅ Berhasil! {nama} tercatat hadir pada {jam}.")

def main():
    inisialisasi_file()
    
    print("="*30)
    print("   SISTEM ABSENSI SEDERHANA   ")
    print("="*30)
    print("Ketik 'keluar' untuk menghentikan program.\n")

    while True:
        nama = input("Masukkan Nama Anda: ").strip()
        
        if nama.lower() == 'keluar':
            print("Program berhenti. Terima kasih.")
            break
        
        if nama:
            catat_kehadiran(nama)
        else:
            print("⚠️ Nama tidak boleh kosong!")
        
        print("-" * 20)

if __name__ == "__main__":
    main()
