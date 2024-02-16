<h1 align="center">Sistem Rekomendasi Buku</h1>
<p align="center">
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/05dfa0cf-1b9a-4d63-a855-4f77f2582c5e" width="800">
</p>

## Project Overview

Sistem rekomendasi buku merupakan sistem yang merekomendasikan buku kepada pengguna. Sistem rekomendasi yang dibuat ini berdasarkan dengan preferensi kesukaan pengguna pada masa lalu, rating dari buku yang ada, dan berdasarkan preferensi pengguna lain untuk merekomendasikan buku yang mungkin disukai oleh pengguna. Dengan adanya sistem rekomendasi ini akan bermanfaat untuk meningkatkan keuntungan dari pembelian barang yang berupa buku atau juga bisa diterapkan pada perpustakaan agar pengguna mendapatkan rekomendasi buku yang sesuai dengan minatnya sehingga dapat menentukan pilihan dan dapat meningkatkan minat baca pengguna. 
 
## Business Understanding

### Problem Statements

- Bagaimana cara merekomendasikan buku yang mirip dengan buku yang disukai pengguna di masa lalu?
- Bagaimana cara merekomendasikan buku yang mungkin disukai pengguna berdasarkan preferensi pengguna lain?

### Goals

- Menghasilkan sejumlah rekomendasi buku yang mirip dengan buku yang disukai pengguna di masa lalu dengan teknik algoritma Content Based Filtering.
- Menghasilkan sejumlah rekomendasi buku yang belum pernah dibaca sebelumnya dan mungkin disukai pengguna berdasarkan preferensi pengguna lain dengan teknik algoritma Collaborative Filtering.


### Solution Statements

Solusi yang dibuat yaitu dengan menggunakan 2 algoritma sistem rekomendasi pada Machine Learning. Adapun kedua algoritma tersebut yaitu:

- Content Based Filtering 

  Content Based Filtering mempelajari profil minat pengguna baru berdasarkan data dari objek yang telah dinilai pengguna. Algoritma ini bekerja dengan menyarankan konten/item serupa yang pernah disukai di masa lalu atau sedang dilihat di masa kini kepada pengguna. Semakin banyak informasi yang diberikan pengguna, semakin baik akurasi sistem rekomendasi. Algortima ini akan digunakan untuk merekomendasikan buku yang akan dibaca berdasarkan buku lain yang pernah dibaca pengguna di masa lalu.
    
- Collaborative Filtering

  Collaborative Filtering bergantung pada pendapat komunitas pengguna. Algoritma ini tidak memerlukan atribut untuk setiap itemnya seperti pada sistem berbasis konten (Content Based Filtering). Algoritma ini digunakan untuk merekomendasikan buku kepada pengguna berdasarkan nilai rating buku tertinggi.


## Data Understanding

Dataset yang digunakan pada proyek ini adalah dataset Book Recommendation Dataset yang didapat dari situs [Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset). Pada dataset ini terdapat 3 berkas beformat csv yaitu: Books, Ratings, dan Users. Dari ketiga berkas tersebut akan dibuat variabel untuk memuat berbagai fitur didalamnya.


## Exploratory Data Analysis - Univariate Analysis

Variabel-variabel pada Book Recommendation Dataset adalah sebagai berikut:

1. **Variabel Books**

   Merupakan informasi seputar buku yang didalamnya terdapat fitur: judul buku, penulis buku, tahun publikasi buku, dan penerbit.

   Tabel 1. Informasi pada variabel Books:

   | Column              | Non-Null Count  | Dtype  |
   |---------------------|-----------------|--------|
   | ISBN                | 271360 non-null | object |
   | Book-Title          | 271360 non-null | object |
   | Book-Author         | 271359 non-null | object |
   | Year-Of-Publication | 271360 non-null | object |
   | Publisher           | 271358 non-null | object |
   | Image-URL-S         | 271360 non-null | object |
   | Image-URL-M         | 271360 non-null | object |
   | Image-URL-L         | 271357 non-null | object |

   Berdasarkan Tabel 1, dapat diketahui bahwa variabel Books memiliki kurang lebih 271.359 entri. Terdapat 8 fitur, yaitu:

   - ISBN (International Standard Book Number) adalah kode pengidentifikasian buku.
   - Book-Title merupakan judul buku.
   - Book-Author merupakan nama dari penulis buku.
   - Year-Of-Publication merupakan tahun publikasi buku.
   - Publisher merupakan pihak yang menerbitkan buku.
   - Image-URL-S merupakan tautan dalam skala kecil (small).
   - Image-URL-M merupakan tautan dalam skala sedang (medium).
   - Image-URL-L merupakan tautan dalam skala besar (large).

2. **Variabel Ratings**

   Berisi informasi penilaian terhadap buku. Penilaian (Book-Rating) bersifat eksplisit, dinyatakan dalam skala 1-10 (semakin tinggi nilai menunjukkan apresiasi yang lebih tinggi), atau implisit, yang dinyatakan dengan 0.

   Tabel 2. Informasi pada variabel Ratings:

   | Column      | Non-Null Count   | Dtype  |
   |-------------|------------------|--------|
   | User-ID     | 1149780 non-null | int64  |
   | ISBN        | 1149780 non-null | object |
   | Book-Rating | 1149780 non-null | int64  |

   Berdasarkan Tabel 2, dapat diketahui bahwa variabel Ratings memiliki banyak entri yaitu 1.149.780 entri. Terdapat 3 fitur, yaitu:

   - User-ID merupakan identitas pengguna.
   - ISBN merupakan kode pengidentifikasian buku.
   - Book-Rating metupakan informasi penilaian buku .

   Tabel 3. Distribusi rating pada variabel Ratings:

   |       | User-ID        | Book-Rating    |
   |-------|----------------|----------------|
   | count | 1149780.000000 | 1149780.000000 |
   | mean  | 140386.395126	 | 2.866950       |
   | std   | 80562.277719	  | 3.854184       |
   | min   | 2.000000	      | 0.000000       |
   | 25%   | 70345.000000   | 0.000000       |
   | 50%   | 141010.000000	 | 0.000000       |
   | 75%   | 211028.000000	 | 7.000000       |
   | max   | 278854.000000	 | 10.000000      |

   Berdasarkan Tabel 3, dapat diketahui bahwa nilai maksimum Book-Rating adalah 10 dan nilai minimumnya adalah 0.
   
3. **Variabel Users**
   
   Berisi informasi seputar data pengguna yang didalamnya terdapat fitur: ID user, lokasi, dan umur.
   
   Tabel 4. Informasi pada variabel Users:
   
   | Column   | Non-Null Count  | Dtype  |
   |----------|-----------------|--------|
   | User-ID  | 278858 non-null | int64  |
   | Location | 278858 non-null | object |
   | Age      | 168096 non-null | float  |
   
Variabel yang akan di eksplorasi pada proyek ini adalah variabel Books dan Ratings. Sedangkan, variabel Users hanya digunakan untuk melihat bagaimana profil pengguna saja.


## Data Preprocessing

Dapat dilihat sebelumnya pada bagian Exploratory Data Analysis - Univariate Analysis bahwa sangat banyak entri pada masing-masing variabel, contohnya pada Variabel Ratings memiliki hingga 1.149.780 entri, dengan banyaknya entri akan memakan banyak penggunaan backend RAM gratis pada platform Google Colab, sehingga entri pada masing-masing variabel akan dikurangi menjadi 50.000 entri saja. Kemudian melakukan proses penggabungan data berkas berdasarkan fitur-fitur yang memiliki keterkaitan. Langkah selanjutnya adalah menghapus fitur pada variabel Books yaitu: Image-URL-S, Image-URL-M, dan Image-URL-L. Karena ketiga fitur tersebut tidak akan digunakan dan tidak memiliki pengaruh terhadap perekomendasian buku.


## Data Preparation Model Content Based Filtering

1. Mengatasi Missing Value

   Tabel 5. Missing value setelah proses penggabungan

   | Column              |      |
   |---------------------|------|
   | User-ID             | 0    |
   | ISBN                | 0    |
   | Book-Rating         | 0    |
   | Book-Title          | 5287 |
   | Book-Author         | 5287 |
   | Year-Of-Publication | 5287 |
   | Publisher           | 5287 |

   Berdasarkan Tabel 5, dapat diketahui terdapat 5.287 missing value pada fitur Book-Title (judul buku), Book-Author (penulis), Year-Of-Publication (tahun publikasi buku), dan Publisher (penerbit). Maka data yang memiliki missing value ini akan dihapus agar pembuatan model akan menjadi lebih baik dan dapat meningkatkan performa model.

2. Menghapus data duplikat
   Menghapus data duplikat perlu dilakukan karena hanya akan digunakan data unik untuk dimasukkan ke dalam proses pemodelan. Oleh karena itu, perlu menghapus data yang duplikat. Dalam hal ini, fitur ISBN yang duplikat akan dibuang.
    
3. Langkah selanjutnya adalah melakukan konversi data series menjadi list untuk kemudian membuat dictionary untuk menentukan pasangan key-value pada data yang telah dikonversi menjadi list sebelumnya.

## Modeling and Result

### A. Model Development dengan Content Based Filtering

   Adapun langkah-langkah yang digunakan dalam pengembangan model dengan Content Based Filtering yaitu:

   1. **TF-IDF Vectorizer**

      Pada tahap ini, membangun sistem rekomendasi sederhana berdasarkan judul buku yang tersedia menggunakan TF-IDF Vectorizer, selanjutnya melakukan fit pada judul buku dan ditransformasikan kedalam bentuk matriks yang kemudian menghasilkan vektor tf-idf dalam bentuk matriks.
   
   2. **Cosine Similarity**

      Pada tahap ini akan menghitung derajat kesamaan (similarity degree) antar judul buku dengan teknik Cosine Similarity, selanjutnya melihat matriks kesamaan setiap judul buku dengan menampilkan judul buku dalam 10 sampel kolom (axis=1) dan 10 sampel baris (axis=0) yang dapat dilihat pada Gambar 1.
   
      ![Cosine Similarity](https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/20e428e0-3c99-41cb-b7d2-442fc73874c6)
   
      Gambar 1. Matriks Cosine Similarity
   
      Berdasarkan Gambar 1, dapat diketahui angka yang memiliki nilai lebih dari 0 atau mendekati 1 mengindikasikan kemiripan judul buku. Dalam hal ini judul buku pada baris Y (vertikal) memiliki kemiripan dengan judul buku pada kolom X (horizontal). Sehingga, buku **The Fiancee and Other Stories (Penguin Classics)** terindikasi mirip dengan buku **James Herriot's Cat Stories**.

   3. **Mendapatkan Rekomendasi**
   
      Pada tahap ini akan menghasilkan sejumlah buku yang akan direkomendasikan kepada pengguna dengan keluaran sistem rekomendasi buku berupa Top-N Recommendation, oleh karena itu sistem akan memberikan sejumlah rekomendasi buku pada pengguna. Sebagai contoh, pengguna X pernah membaca buku yang berjudul **The Fiancee and Other Stories (Penguin Classics)**. Kemudian, saat pengguna tersebut berencana untuk membaca buku lain, sistem akan merekomendasikan buku lain yang memiliki kemiripan dengan buku yang sebelumnya pernah dibaca oleh pengguna. Rekomendasi kedua buku ini berdasarkan kesamaan yang dihitung dengan Cosine Similarity pada tahap sebelumnya.
      
Setelah dilakukan tahapan-tahapan tersebut, dilakukan uji coba dengan menghasilkan Top-N Recommendation pada model Content Based Filtering. Pada kasus kali ini, dilakukan uji coba untuk mencari judul buku yang mirip dengan buku yang berjudul **Waking Up Screaming: Haunting Tales of Terror**. Hasil rekomendasi buku dapat dilihat pada Tabel 6.

Tabel 6. Hasil rekomendasi buku Content Based Filtering

| No.| Books Title                                 | Books Author     | Year | Publisher             |
|----|---------------------------------------------|------------------|------|-----------------------|
| 1  | The Haunting                                | Paul Doherty	    | 1998	| Headline              |
| 2  | Waking Beauty                               |	Paul Witcover	   | 1997	| Harpercollins         |   
| 3  | Tales of Terror and the Supernatural        |	Wilkie Collins   |	1972	| Dover Publications    |
| 4  | Magic Terror: Seven Tales                   |	Peter Straub     |	2001	| Fawcett Books         |
| 5  | A Winter Haunting	                          | Dan Simmons      |	2002	| HarperTorch           |
| 6  | Haunting Rachel	                            | KAY HOOPER       |	1999	| Bantam                |
| 7  | CHRISTOPHER PIKE'S TALES OF TERROR #2       |	Christopher Pike	| 1998	| Simon Pulse           |
| 8  | The Haunting of Hill House                  |	Shirley Jackson  |	1984	| Penguin Books         |
| 9  | Great Tales of Terror (A Watermill Classic) |	Edgar Allan Poe  |	1993 |	Troll  Communications |
| 10 | Tales Of Passion Tales Of Woe	              | Sandra Gulland   |	1999 |	Touchstone            |

Berdasarkan Tabel 6, dapat diketahui bahwa dari 10 buku yang direkomendasikan memiliki kemiripan dengan buku yang berjudul **Waking Up Screaming: Haunting Tales of Terror**.
        
        
### B. Model Development dengan Collaborative Filtering

   Adapun langkah-langkah yang digunakan dalam pengembangan model dengan Collaborative Filtering yaitu:

   1. **Data Preparation Model Collaborative Filtering**
   
      Tahap pertama dalam melakukan persiapan sebelum melakukan pemodelan adalah melakukan persiapan data Ratings untuk menyandikan (encode) fitur User-ID dan ISBN kedalam indeks integer, kemudian memetakan User-ID dan ISBN ke dataframe yang berkaitan, dan terakhir mengecek beberapa hal dalam data seperti jumlah user, jumlah buku, dan mengubah nilai rating menjadi float.

   2. **Membagi Data untuk Training dan Validasi**
   
      Sebelum melakukan pelatihan model tahapan yang harus diselesaikan yaitu mengacak data Ratings terlebih dahulu agar pendistribusiannya menjadi random, kemudian dilanjutkan dengan memetakan (mapping) data user dan buku menjadi satu value terlebih dahulu, lalu membuat rating dalam skala 0 sampai 1 agar mudah dalam melakukan proses training, agar nantinya data akan siap untuk dimasukkan ke dalam model, dan terakhir melakukan split data untuk membagi data menjadi 80% data latih dan 20% data validasi.

   3. **Proses Training**
   
      Pada tahap ini, model menghitung skor kecocokan antara pengguna dan buku dengan teknik embedding menggunakan class RecommenderNet. Pertama, melakukan proses embedding terhadap data user dan buku. Selanjutnya, melakukan operasi perkalian dot product antara embedding user dan buku. Selain itu, juga menambahkan bias untuk setiap user dan buku. Skor kecocokan ditetapkan dalam skala [0,1] dengan fungsi aktivasi sigmoid. Selanjutnya, melakukan proses compile terhadap model. Model ini menggunakan Binary Crossentropy untuk menghitung loss function, Adam (Adaptive Moment Estimation) sebagai optimizer dengan parameter learning rate sebesar 0.001, dan Root Mean Squared Error (RMSE) sebagai metrics evaluation.
      
Setelah dilakukan tahapan-tahapan tersebut, dilakukan uji coba dengan menghasilkan Top-N Recommendation buku pada model Collaborative Filtering. Untuk mendapatkan rekomendasi buku, pertama mengambil sampel user secara acak dan mendefinisikan variabel unreaded_Books yang merupakan daftar buku yang belum pernah dibaca oleh pengguna, unreaded_Books inilah yang akan menjadi buku yang direkomendasikan kepada pengguna. Sebelumnya, pengguna telah memberi rating pada beberapa buku yang telah mereka baca. Rating ini digunakan untuk membuat rekomendasi buku yang mungkin cocok untuk pengguna. Buku yang akan direkomendasikan tentulah buku yang belum pernah dibaca oleh pengguna. Hasil rekomendasi buku dapat dilihat pada Gambar 2.

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/3cbe0954-06ee-4206-89a8-9ccfea55ac4c" width="500">
</p>

Gambar 2. Hasil rekomendasi buku Collaborative Filtering

Berdasarkan Gambar 2 merupakan rekomendasi untuk user dengan id 7134. Dari output tersebut, dapat melakukan perbandingan antara Buku dengan rating tinggi dari user: 7134 dan Top 10 rekomendasi buku untuk user: 7134.
   

## Evaluasi

### A. Evaluasi Content Based Filtering

Adapun langkah yang digunakan untuk mendapatkan rekomendasi yaitu dengan menggunakan Top-N Recommendation untuk mengambil k dengan nilai similarity terbesar pada index matriks yang diberikan. Langkah pertama yaitu mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan yang kemudian dataframe akan diubah menjadi numpy, dengan menggunakan argpartition di ambil sejumlah nilai k tertinggi dari similarity, dalam kasus ini digunakan dataframe Cosine Similarity. Kemudian, mengambil data dari bobot (tingkat kesamaan) tertinggi ke terendah, kemudian menghapus judul buku agar nantinya output data judul buku yang dicari tidak muncul pada daftar rekomendasi buku.

Berdasarkan hasil rekomendasi buku dengan model Content Based Filtering yang dapat dilihat pada Tabel 6, dapat diketahui dari 10 buku yang direkomendasikan, terdapat 9 buku yang relevan, jadi dapat disimpulkan precision pada sistem ini sebesar 90% yang mengacu pada persamaan berikut:

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/48ee34c9-638e-4dd0-92b6-04999392d334" width="300">
</p>

Gambar 3. Persamaan Recommender System Precision


### B. Evaluasi Collaborative Filtering

Adapun metrik evaluasi yang digunakan pada model Collaborative Filtering adalah Root Mean Squared Error (RMSE). Metode pengukuran ini berfungsi sebagai perkiraan nilai yang diamati dengan mengukur perbedaan nilai prediksi model. Root Mean Squared Error adalah hasil dari akar kuadrat dari Mean Squared Error. Keakuratan metode estimasi kesalahan pengukuran diwakili oleh nilai RMSE yang kecil. Semakin kecil (mendekati 0) nilai RMSE maka hasil prediksi akan semakin akurat. Persamaan metrik RMSE ditunjukkan pada gambar berikut:

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/9e738ca0-5da5-4a25-9037-aee1cf035e4a" width="300">
</p>

Gambar 4. Persamaan metrik RMSE

Berdasarkan Gambar 4, keterangan yang ada pada persamaan RMSE yaitu:

    n => Jumlah data
    i => Urutan Data
    y => Nilai hasil observasi
    ŷ => Nilai hasil prediksi

Melihat visualisasi proses training plot metrik evaluasi RMSE dengan matplotlib.

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/f604f3e5-af88-4637-903f-2d562de9f9f5" width="400">
</p>

Gambar 5. Visualisasi plot metrik evaluasi RMSE

Dapat diketahui proses training model cukup smooth pada 20 epochs. Dari proses ini, diperoleh nilai error akhir sebesar sekitar 0.12 dan error pada data validasi sekitar 0.23. Nilai tersebut cukup bagus untuk sebuah sistem rekomendasi.


## Kesimpulan

Sistem rekomendasi yang dibuat pada proyek ini untuk dapat merekomendasikan buku kepada pengguna dengan menggunakan dua pendekatan model algortima. Model pertama yaitu, Content Based Filtering yang bertujuan untuk menghasilkan sejumlah rekomendasi buku yang mirip dengan buku yang disukai pengguna di masa lalu. Dan model kedua yaitu, Collaborative Filtering yang bertujuan untuk menghasilkan sejumlah rekomendasi buku yang belum pernah dibaca sebelumnya yang mungkin akan disukai pengguna berdasarkan preferensi pengguna lain. Pengembangan kedua pendekatan model pada proyek ini untuk menghasilkan sistem rekomendasi buku telah memiliki tingkat akurasi perekomendasian dengan cukup baik. Namun tidak menutup kemungkinan, model yang telah dibuat pada proyek ini dapat dikembangkan lagi dengan lebih baik untuk mendapatkan tingkat akurasi yang lebih baik dan dapat lebih meminimalkan error.
