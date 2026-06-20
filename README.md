# Kumpulan Program Python

## Deskripsi

Repository ini berisi dua program Python sederhana:

1. Sistem Absensi
2. Kalkulator IPK

Program dibuat menggunakan Python dasar dengan memanfaatkan fungsi, percabangan, perulangan, dan pengolahan file.

---

# Program 1 - Sistem Absensi

## Deskripsi

Program digunakan untuk mencatat kehadiran pengguna ke dalam file CSV secara otomatis dengan informasi:

* Nama
* Tanggal
* Jam
* Status Kehadiran

## Cara Menjalankan

```bash
python absensi.py
```

## Output

Data akan tersimpan pada file:

```text
data_absen.csv
```

Contoh:

```csv
Nama,Tanggal,Jam,Status
Budi,2026-06-20,08:30:15,Hadir
Andi,2026-06-20,08:35:20,Hadir
```

---

# Program 2 - Kalkulator IPK

## Deskripsi

Program digunakan untuk menghitung IPK berdasarkan nilai huruf yang diperoleh mahasiswa.

Konversi nilai:

| Nilai | Bobot |
| ----- | ----- |
| A     | 4     |
| B     | 3     |
| C     | 2     |
| D     | 1     |
| E     | 0     |

Program menerima daftar nilai kemudian menghitung rata-rata bobot untuk menghasilkan IPK.

## Cara Menjalankan

```bash
python kalkulator_ipk.py
```

## Contoh Kode

```python
mata_kuliah = ["A", "B", "C", "A"]
```

## Contoh Output

```text
IPK Anda: 3.25
```

## Algoritma

1. Membuat dictionary konversi nilai huruf ke bobot angka.
2. Menjumlahkan seluruh bobot nilai.
3. Membagi total bobot dengan jumlah mata kuliah.
4. Menampilkan hasil IPK.

---

# Library yang Digunakan

Program menggunakan library bawaan Python:

```python
csv
os
datetime
```

Tidak memerlukan instalasi package tambahan.

---

# Author

Kiel Manurung
