# Analisis dan Prediksi Sentimen Teks dengan SVM

## Deskripsi Proyek:

Proyek ini bertujuan untuk melakukan analisis sentimen teks menggunakan metode Support Vector Machine (SVM) pada dataset [IndoNLU](https://github.com/indobenchmark/indonlu). Dataset ini berisi teks dengan label sentimen positif, negatif, dan netral. Tujuan utama proyek ini adalah mengembangkan model klasifikasi sentimen yang dapat memprediksi sentimen dari suatu teks, apakah tergolong sebagai teks yang positif, negatif, atau netral.

## Langkah-Langkah Proyek:

1. **Pemilihan Dataset:** Menggunakan dataset IndoNLU, yang berisi teks dan label sentimen untuk melatih dan menguji model.

2. **Pemrosesan Data:** Melakukan pemrosesan data, termasuk membaca dataset, memberikan nama kolom, dan memvisualisasikan distribusi variabel target untuk pemahaman awal.

3. **Analisis Data:** Melakukan analisis data, termasuk visualisasi panjang teks dan distribusi sentimen menggunakan grafik bar.

4. **Feature Engineering:** Menggunakan metode TF-IDF (Term Frequency-Inverse Document Frequency) untuk menghasilkan vektor fitur dari teks yang akan digunakan sebagai input model.

5. **Klasifikasi dengan SVM:** Menerapkan algoritma Support Vector Machine (SVM) dengan kernel linear untuk melakukan klasifikasi sentimen teks. Melakukan pelatihan model menggunakan data latih dan mengevaluasi performa model menggunakan data uji.

6. **Evaluasi Model:** Mengevaluasi model dengan metriks seperti precision, recall, F1-score, dan support untuk menganalisis kinerja model secara keseluruhan dan pada setiap kelas sentimen.

7. **Prediksi Sentimen:** Melakukan prediksi sentimen untuk beberapa contoh teks di luar dataset, untuk menunjukkan kemampuan model dalam memprediksi sentimen pada data baru.

## Hasil Proyek:
Proyek ini menghasilkan model klasifikasi sentimen teks menggunakan Support Vector Machine (SVM) dengan tingkat akurasi yang memadai. Performa model dievaluasi dengan menggunakan metriks yang mencakup precision, recall, F1-score, dan support. Model ini dapat digunakan untuk memprediksi sentimen dari teks baru dan dapat diterapkan dalam berbagai konteks, seperti analisis sentimen pada ulasan produk atau feedback pelanggan. Meskipun memiliki performa yang baik, proyek ini memberikan ruang untuk perbaikan lebih lanjut guna meningkatkan kinerja model terutama pada klasifikasi sentimen negatif.
