# Analisis dan Prediksi Sentimen Teks dengan Deep Learning pada Data IndoNLU

## Deskripsi Proyek:

Proyek ini bertujuan untuk melakukan analisis dan prediksi sentimen teks menggunakan pendekatan Deep Learning pada dataset [IndoNLU](https://github.com/indobenchmark/indonlu). Dataset ini memuat teks beserta label sentimen (positif, negatif, netral). Dalam proyek ini, model Deep Learning, khususnya BERT (Bidirectional Encoder Representations from Transformers), digunakan untuk melatih dan menguji kemampuan model dalam mengenali dan mengklasifikasikan sentimen dari teks bahasa Indonesia.

## Langkah-Langkah Proyek:

1. **Memuat dan Inisialisasi Model Pre-trained:** Proyek dimulai dengan memuat model BERT bahasa Indonesia yang telah dilatih sebelumnya. Tokenizer dan konfigurasi model juga diinisialisasi untuk proses berikutnya.

2. **Persiapan Dataset Analisis Sentimen:** Membagi dataset menjadi set pelatihan, validasi, dan pengujian. Tokenizer digunakan untuk mengonversi teks ke dalam subwords, dan dataset dipersiapkan untuk digunakan pada model.

3. **Pengujian pada Contoh Kalimat:** Sebuah contoh kalimat diuji pada model untuk mengevaluasi kemampuan model dalam memprediksi sentimen. Proses ini memberikan gambaran awal tentang performa model.

4. **Fine Tuning dan Evaluasi:** Model dilatih dengan dataset pelatihan, dan kemudian dievaluasi pada dataset validasi untuk mengukur performa. Proses ini dilakukan sejumlah epoch untuk meningkatkan akurasi model.

5. **Evaluasi pada Data Pengujian:** Model yang telah dilatih dievaluasi pada dataset pengujian untuk mengukur kemampuan generalisasi dan performa keseluruhan model pada data baru.

6. **Prediksi Sentimen:** Model digunakan untuk memprediksi sentimen pada beberapa contoh teks di luar dataset, memperlihatkan kemampuan model dalam situasi penggunaan nyata.

## Hasil Proyek:

Proyek ini menghasilkan model Deep Learning berbasis BERT yang mampu melakukan analisis dan prediksi sentimen pada teks bahasa Indonesia. Performa model dievaluasi menggunakan metriks seperti loss, akurasi, precision, recall, dan F1-score. Model ini dapat digunakan untuk memprediksi sentimen pada teks baru dan dapat diterapkan dalam berbagai konteks, seperti analisis sentimen pada ulasan produk, komentar, atau feedback pengguna. Meskipun model sudah memberikan hasil yang baik, proyek ini memberikan potensi untuk pengembangan lebih lanjut guna meningkatkan kinerja dan menghadapi variasi yang lebih kompleks dalam data teks bahasa Indonesia.
