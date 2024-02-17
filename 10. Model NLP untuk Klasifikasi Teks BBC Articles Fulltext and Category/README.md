# Model NLP untuk Klasifikasi Teks BBC Articles Fulltext and Category

## Deskripsi Proyek:

Proyek ini bertujuan untuk mengembangkan model Natural Language Processing (NLP) menggunakan Deep Learning, khususnya Convolutional Neural Network (CNN) dan Long Short-Term Memory (LSTM) untuk mengklasifikasikan teks artikel dari BBC berdasarkan kategori atau topiknya. Dataset yang digunakan adalah [BBC Articles Fulltext and Category](https://www.kaggle.com/datasets/yufengdev/bbc-fulltext-and-category), yang berisi artikel dari berbagai kategori seperti bisnis, hiburan, politik, olahraga, dan teknologi.

## Langkah-Langkah Proyek:

1. **Import Library dan Mengunduh Dataset:** Proyek dimulai dengan mengimpor library yang diperlukan dan memuat dataset BBC Articles Fulltext and Category.

2. **Persiapan Data:** Data teks dari dataset BBC diolah dan dibersihkan dengan menghapus stopwords dan melakukan tokenisasi. Selanjutnya, data dipisahkan menjadi data pelatihan dan data validasi.

3. **One-Hot Encoding dan Pembagian Dataset:** Kategori teks diubah menjadi representasi biner dengan one-hot encoding. Selanjutnya, dataset dibagi menjadi data pelatihan dan data validasi dengan proporsi 80:20.

4. **Tokenisasi dan Padding:** Teks dibuat menjadi sekuens kata-kata menggunakan tokenizer, dan kemudian dilakukan padding agar memiliki panjang yang seragam.

5. **Pembangunan Model:** Model klasifikasi teks dibangun menggunakan arsitektur deep learning yang terdiri dari lapisan-lapisan seperti Embedding, Conv1D, MaxPooling1D, LSTM, dan Dense. Model ini dirancang untuk mengklasifikasikan teks ke dalam salah satu dari enam kategori yang ada.

6. **Pelatihan dan Evaluasi Model:** Model dilatih menggunakan data pelatihan dan dievaluasi menggunakan data validasi. Proses ini dilakukan selama beberapa epoch, dan akurasi serta loss model dievaluasi.

7. **Plotting Performa Model:** Performa model dievaluasi dengan memplot grafik akurasi dan loss pada data pelatihan dan validasi selama proses pelatihan.

## Hasil Proyek:

![Plot Accuracy and Loss](https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/d249f453-5476-4934-ad26-64afaf7c4390)

Berdasarkan hasil plot akurasi dan loss model, akurasi pelatihan dan validasi meningkat secara signifikan, mencapai nilai target 80% pada epoch ke-35. Sementara itu loss pelatihan dan validasi juga menurun secara signifikan.

Selain itu gap antara kurva akurasi pelatihan dan validasi cukup kecil, yaitu sekitar 1%. Hal ini menunjukkan bahwa model tidak mengalami overfitting yang signifikan.

Secara keseluruhan, model NLP yang dilatih memiliki kinerja yang baik. Namun, masih ada potensi untuk meningkatkan akurasi dengan menggunakan lebih banyak data pelatihan atau dengan penyesuaian model.

Dengan demikian, proyek ini memberikan kontribusi dalam pengembangan model NLP untuk klasifikasi teks, yang dapat diterapkan dalam berbagai konteks seperti analisis berita, pengelompokan dokumen, dan aplikasi pengelolaan konten.
