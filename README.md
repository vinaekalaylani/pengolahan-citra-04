# Pengolahan Citra - Session 4

Repository ini digunakan untuk memenuhi tugas mata kuliah **Pengolahan Citra (Sesi 4)**. Tugas ini terdiri dari dua bagian utama, yaitu Tugas Teori dan Tugas Praktik.

## 📝 Detail Tugas

### 1. Tugas Teori (PDF)
Menjawab pertanyaan-pertanyaan berikut dan dikumpulkan dalam format file **PDF**:
1. Apa perbedaan antara *scaling* dan *zoom*? Apakah keduanya sama?
2. Mengapa rotasi bisa menyebabkan kehilangan informasi pada citra?
3. Bagaimana cara memilih metode interpolasi yang tepat untuk aplikasi tertentu?

### 2. Tugas Praktik (Python Script)
Membuat script Python yang kompatibel dengan Google Colab untuk melakukan transformasi citra dengan ketentuan:
1. **Translasi Citra**: Menggeser citra ke arah tertentu.
2. **Rotasi Citra**: Memutar citra dengan sudut 45°, 90°, 180°.
3. **Scaling Citra**: Memperbesar dan memperkecil citra dengan menggunakan jenis interpolasi yang relevan (`INTER_LINEAR` dan `INTER_AREA`).
4. **Flipping Citra**: Membalikkan citra secara horizontal (`flipCode = 1`) dan vertikal (`flipCode = 0`).

---

## 📂 Struktur Repository Yang Diharapkan

Sesuai instruksi, repository ini harus berisi 2 file utama untuk dinilai:
- `image_transformations.py`: Script code Python untuk transformasi citra (Tugas Praktik).
- `[Nama File Teori].pdf`: File dokumen mandiri yang berisi jawaban dari pertanyaan di atas (Tugas Teori) *(Jangan lupa untuk Anda tambahkan ke repo ini ya!)*.

## 🚀 Cara Menjalankan Script Praktik
Mengingat script ini dirancang khusus untuk kompatibilitas Google Colab (`google.colab.patches` dll):
1. Buka [Google Colab](https://colab.research.google.com/).
2. Buat notebook baru.
3. Salin/Paste seluruh kode dari `image_transformations.py` ke dalam satu cell di Colab dan sesuaikan.
4. Run/Jalankan cell tersebut (`Shift + Enter`). Colab akan memunculkan tombol **Upload** untuk mengunggah gambar Anda terlebih dahulu sebelum program memulai proses transformasi.
