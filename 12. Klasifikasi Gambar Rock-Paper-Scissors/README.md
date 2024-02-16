# Klasifikasi Gambar Rock-Paper-Scissors

## Deskripsi Proyek:

Proyek ini merupakan implementasi klasifikasi gambar untuk mengenali tiga kategori utama, yaitu batu (rock), kertas (paper), dan gunting (scissors) menggunakan model Convolutional Neural Network (CNN). Data yang digunakan merupakan dataset [Rock-Paper-Scissors Images](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors), yang memuat gambar-gambar tangan yang membentuk batu, kertas, dan gunting. Proyek ini melibatkan tahap-tahap seperti pengunduhan dataset, pemisahan data, augmentasi gambar, pembangunan model CNN, pelatihan model, evaluasi performa model, serta uji coba dengan gambar input diluar dataset.

## Langkah-Langkah Proyek:

1. **Install Package dan Import Library:** Tahap awal melibatkan instalasi package dan impor library yang diperlukan, termasuk TensorFlow, matplotlib, dan splitfolders untuk pemisahan data.

2. **Mengunduh dan Memisahkan Dataset:** Memuat dataset Rock-Paper-Scissors Images. Data kemudian dipisahkan menjadi data training dan data validation.

3. **Eksplorasi Data:** Melihat beberapa contoh gambar dari masing-masing kategori (rock, paper, scissors) untuk memastikan dataset telah diunduh dan terbagi dengan benar.

4. **Augmentasi Data Gambar:** Implementasi ImageDataGenerator digunakan untuk melakukan augmentasi data pada data training dan data validation. Ini melibatkan proses seperti zoom, rotasi, dan horizontal flip untuk meningkatkan variasi data.

5. **Membangun Model Convolutional Neural Network (CNN):** Arsitektur model CNN sederhana dibangun dengan menggunakan beberapa layer Conv2D, MaxPooling2D, Flatten, Dense, dan Dropout. Model ini dirancang untuk dapat mengenali pola pada gambar batu, kertas, dan gunting.

6. **Melakukan Training Model:** Model CNN dilatih menggunakan data training dengan metrik loss function 'categorical_crossentropy' dan optimizer RMSprop. Callback EarlyStopping juga digunakan untuk mencegah overfitting.

7. **Evaluasi dan Visualisasi Performa Model:** Melihat hasil dari grafik akurasi dan loss pada data training dan data validation. Mengetahui performa model pada kedua set data tersebut.

8. **Menguji Model dengan Gambar Input:** Melakukan input data asing yang tidak dikenali dataset berupa gambar-gambar tangan yang membentuk batu, kertas, dan gunting untuk melihat kemampuan model dalam memprediksi kategori gambar tersebut.

## Hasil Proyek:

![Plot Training and Validation](https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/24566ea1-0985-40a0-9332-30e68aee8ff9)

Model klasifikasi gambar rock-paper-scissors yang telah dilatih berhasil mencapai tingkat akurasi yang tinggi, yaitu sekitar 99% pada data training dan 98% pada data validation. Grafik loss menunjukkan penurunan yang konsisten, dan penggunaan callback EarlyStopping berhasil mencegah overfitting.

Penggunaan ImageDataGenerator untuk augmentasi data memberikan variasi tambahan pada dataset, yang membantu model untuk belajar dengan lebih baik. Selain itu, uji coba dengan gambar input yang tidak dikenali oleh model juga menunjukkan bahwa model dapat memprediksi kategori gambar dengan tepat.

Secara keseluruhan, model klasifikasi rock paper scissors yang dilatih dapat dikatakan telah berhasil. Model tersebut dapat memprediksi dengan akurasi yang tinggi dan tidak mengalami overfitting.
