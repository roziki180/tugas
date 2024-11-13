# Program untuk menghitung rata-rata nilai ujian siswa

def hitung_rata_rata(nilai_list):
    if len(nilai_list) == 0:
        return 0
    return sum(nilai_list) / len(nilai_list)

def main():
    nilai_siswa = []
    
    while True:
        try:
            # Meminta pengguna untuk memasukkan nilai
            nilai = input("Masukkan nilai ujian siswa (atau ketik 'selesai' untuk menghitung rata-rata): ")
            
            if nilai.lower() == 'selesai':
                break
            
            # Mengkonversi input menjadi angka
            nilai = float(nilai)
            nilai_siswa.append(nilai)
        
        except ValueError:
            print("Input tidak valid. Harap masukkan angka atau ketik 'selesai'.")

    # Menghitung dan menampilkan rata-rata
    rata_rata = hitung_rata_rata(nilai_siswa)
    print(f"Rata-rata nilai ujian siswa adalah: {rata_rata:.2f}")

if __name__ == "__main__":
    main()