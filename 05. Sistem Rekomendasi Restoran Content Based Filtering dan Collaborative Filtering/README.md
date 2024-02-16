<h1 align="center">Sistem Rekomendasi Restoran</h1>
<p align="center">
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/ee1d6db4-fdc8-476b-8e29-bb090de351f4" width="800">
</p>

## Project Overview

Sistem rekomendasi restoran adalah solusi berbasis teknologi yang bertujuan memberikan rekomendasi restoran kepada pengguna berdasarkan preferensi kuliner mereka, pengalaman makan sebelumnya, dan juga preferensi pengguna lain dengan selera serupa. Dengan menggunakan data historis pengguna, ulasan restoran, dan preferensi kuliner, sistem ini dirancang untuk memberikan rekomendasi yang personal dan relevan kepada pengguna.
 
## Business Understanding

### Problem Statements

- Bagaimana dapat memberikan rekomendasi restoran yang serupa dengan pilihan kuliner yang disukai oleh pengguna berdasarkan pengalaman makan sebelumnya?
- Bagaimana sistem dapat merekomendasikan restoran yang mungkin disukai oleh pengguna berdasarkan preferensi kuliner dari pengguna lain yang memiliki selera serupa?

### Goals

- Menghasilkan rekomendasi restoran yang serupa dengan pengalaman makan sebelumnya pengguna dengan menggunakan teknik algoritma Content Based Filtering.
- Menghasilkan rekomendasi restoran yang belum pernah dikunjungi sebelumnya dan mungkin disukai pengguna berdasarkan preferensi kuliner dari pengguna lain yang memiliki selera serupa dengan menggunakan teknik algoritma Collaborative Filtering.


### Solution Statements

Solusi yang dibuat yaitu dengan menggunakan 2 algoritma sistem rekomendasi pada Machine Learning. Adapun kedua algoritma tersebut yaitu:

- Content Based Filtering

Content Based Filtering akan menganalisis preferensi kuliner pengguna berdasarkan data dari restoran yang pernah dikunjungi atau dinilai sebelumnya. Algoritma ini akan merekomendasikan restoran dengan menu atau gaya kuliner yang mirip dengan yang disukai pengguna di masa lalu atau sedang diminati saat ini.

- Collaborative Filtering

Collaborative Filtering bergantung pada preferensi kuliner komunitas pengguna. Algoritma ini tidak memerlukan atribut spesifik untuk setiap restoran, melainkan merekomendasikan tempat makan berdasarkan penilaian tertinggi dari pengguna lain dengan selera serupa.


## Data Understanding

Dataset yang digunakan pada proyek ini adalah dataset Restaurant & Consumer Data yang didapat dari situs [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/232/restaurant+consumer+data). Pada dataset ini terdapat 9 berkas beformat csv. Berdasarkan hal tersebut akan dibagi menjadi 3 kategori, yaitu Restaurant, Consumers, dan User-Item-Rating. Kemudian akan dibuat variabel untuk memuat berbagai fitur didalamnya.


## Exploratory Data Analysis - Univariate Analysis

Variabel-variabel pada Book Restaurant & Consumer Data adalah sebagai berikut:

1. **Variabel Accepts**

   Merupakan jenis pembayaran yang diterima pada restoran tertentu.

   Tabel 1. Informasi pada variabel Accepts.

   | Column   | Non-Null Count | Dtype  |
   |----------|----------------|--------|
   | placeID  | 1314 non-null  | int64  |
   | Rpayment | 1314 non-null  | object |

   Berdasarkan Tabel 1, dapat diketahui bahwa variabel Accepts memiliki 1.314 entri. Variabel Accepts ini termasuk ke dalam kategori data Restaurant. Terdapat 2 fitur pada variabel Accepts, yaitu 'placeID' dan 'Rpayment'. 'PlaceID' merupakan ID restoran, sedangkan 'Rpayment' merupakan jenis pembayaran yang digunakan pada restoran.

2. **Variabel Cuisine**

   Berisi informasi jenis masakan yang tersedia di restoran.

   Tabel 2. Informasi pada variabel Cuisine.

   | Column   | Non-Null Count | Dtype  |
   |----------|----------------|--------|
   | placeID  | 916 non-null   | int64  |
   | Rcuisine | 916 non-null   | object |

   Berdasarkan Tabel 2, variabel Cuisine ini termasuk ke dalam kategori data Restaurant. Terdapat 2 fitur pada variabel Cuisine, yaitu 'placeID' dan 'Rcuisine'. 'PlaceID' merupakan ID restoran, sedangkan 'Rcuisine' merupakan jenis masakan yang tersedia pada restoran. Data jenis masakan ini akan digunakan untuk memprediksi top-N rekomendasi bagi pengguna.

3. **Variabel Profile**

   Profile pengguna terkadang diperlukan untuk memahami pola preferensi terhadap suatu item. Pada variabel Profile ini didapatkan berbagai fitur mulai dari 'marital_status', 'birth_year', 'smoker', 'religion', 'budget', dan lain-lain.
   
   Pada pengembangan model dengan content-based filtering, data yang dibutuhkan nantinya adalah nama restoran dan jenis masakan. Dengan ini akan dihitung kesamaan (similarity) nama restoran dan jenis masakan kemudian membuat rekomendasi berdasarkan kesamaan ini.
   
4. **Variabel Rating**

   Berisi informasi penilaian terhadap restoran.

   Tabel 3. Fitur pada variabel Rating.

   | userID | placeID | rating | food_rating | service_rating |
   |--------|---------|--------|-------------|----------------|
   | U1077  | 135085  | 2      | 2           | 2              |
   | U1077  | 135038  | 2      | 2           | 1              |
   | U1077  | 132825  | 2      | 2           | 2              |
   | U1077  | 135038  | 1      | 2           | 2              |
   | U1068  | 135104  | 1      | 1           | 2              |

   Berdasarkan Tabel 3, dapat diketahui bahwa data variabel Rating terdiri dari 5 fitur dengan tiga kategori rating. Fitur-fitur tersebut antara lain:

   - userID merupakan ID pengguna.
   - placeID merupakan ID restoran.
   - rating merupakan data penilaian untuk restoran.
   - food_rating merupakan data penilaian untuk makanan atau masakan di restoran tersebut.
   - service_rating merupakan data penilaian layanan restoran tersebut.

   Tabel 4. Distribusi rating pada data.

   |       | placeID       | rating      | food_rating | service_rating |
   |-------|---------------|-------------|-------------|----------------|
   | count | 1161.000000   | 1161.000000 | 1161.000000 | 1161.000000    |
   | mean  | 134192.041344 | 1.199828    | 1.215332    | 1.090439       |
   | std   | 1100.916275	 | 0.773282    | 0.792294    | 0.790844       |
   | min   | 132560.000000 | 0.000000    | 0.000000    | 0.000000       |
   | 25%   | 132856.000000 | 1.000000    | 1.000000    | 0.000000       |
   | 50%   | 135030.000000 | 1.000000    | 1.000000    | 1.000000       |
   | 75%   | 135059.000000 | 2.000000    | 2.000000    | 2.000000       |
   | max   | 135109.000000 | 2.000000    | 2.000000    | 2.000000       |

   Berdasarkan Tabel 4, dapat diketahui bahwa nilai maksimum rating adalah 2 dan nilai minimumnya adalah 0. Artinya, skala rating berkisar antara 0 hingga 2.  


## Data Preprocessing

Pada bagian Data Understanding sebelumnya terdapat 9 berkas beformat csv, yang kemudian akan dibagi menjadi 3 kategori, yaitu Restaurant, Consumers, dan User-Item-Rating. Pada tahap ini, seluruh data pada kategori Restaurant akan digabungkan. Sehingga fitur 'placeID' yang unik digunakan sebagai acuan dalam penggabungan ini. Setelab proses penggabungan didapatkan sebanyak 1.331 entri data.

## Data Preparation Model Content Based Filtering

**1. Mengatasi Missing Value**

   Tabel 5. Missing value setelah proses penggabungan.

   | Column      |     |
   |-------------|-----|
   | User-ID     | 0   |
   | placeID     | 0   |
   | rating      | 0   |
   | food_rating | 0   |
   | name        | 0   |
   | Rcuisine    | 288 |

   Berdasarkan Tabel 5, terdapat 288 missing value pada fitur 'Rcuisine' (jenis masakan). 288 dari 1.331 merupakan jumlah yang signifikan. Sebenarnya sayang jika data missing value ini dilakukan drop. Namun, tidak dapat diidentifikasi nama masakan yang tidak memiliki data 'Rcuisine' ini termasuk ke dalam jenis masakan mana. Oleh karena itu, akan dilakukan fungsi drop pada missing value ini.

**2. Menyamakan Jenis Masakan**
   
   Sebelum masuk tahap akhir (pemodelan), perlu untuk menyamakan nama masakan. Terkadang, masakan yang sama memiliki nama atau kategori yang berbeda. Jika dibiarkan, hal ini bisa menyebabkan bias pada data.

   Diantara semua jenis masakan pada data, ada satu yang menarik, yaitu jenis masakan bernama Game dari restoran KFC. Restoran KFC memiliki dua jenis masakan yang berbeda, yaitu Game dan American. Dalam sistem rekomendasi yang akan dikembangkan, penting untuk memastikan satu restoran mewakili satu jenis masakan. Tujuannya supaya tidak terjadi dobel atau rangkap jenis dalam satu restoran. Sehingga, sistem dapat merekomendasikan resto berdasarkan jenis masakannya. Dalam hal ini, KFC lebih cocok disebut sebagai restoran dengan jenis masakan American. Jadi, perlu mengganti jenis Game dengan American.  

**3. Menghapus data duplikat**
   
   Menghapus data duplikat perlu dilakukan karena hanya akan digunakan data unik untuk dimasukkan ke dalam proses pemodelan. Oleh karena itu, perlu menghapus data yang duplikat. Dalam hal ini, fitur 'placeID' yang duplikat akan dibuang.
   
**4. Konversi data series menjadi list**
   
   Langkah selanjutnya adalah melakukan konversi data series menjadi list untuk kemudian membuat dictionary untuk menentukan pasangan key-value pada data yang telah dikonversi menjadi list sebelumnya.

## Modeling and Result

### A. Model Development dengan Content Based Filtering

   Adapun langkah-langkah yang digunakan dalam pengembangan model dengan Content Based Filtering yaitu:

   1. **TF-IDF Vectorizer**

      Pada tahap ini, membangun sistem rekomendasi berdasarkan jenis masakan yang tersedia menggunakan TF-IDF Vectorizer untuk menemukan representasi fitur penting dari setiap jenis masakan, selanjutnya melakukan fit pada jenis masakan dan ditransformasikan kedalam bentuk matriks yang kemudian menghasilkan vektor tf-idf dalam bentuk matriks.
   
   2. **Cosine Similarity**

      Pada tahap ini akan menghitung derajat kesamaan (similarity degree) antar restoran dengan teknik Cosine Similarity, selanjutnya melihat matriks kesamaan setiap restoran dengan menampilkan restoran dalam 5 sampel kolom (axis=1) dan 10 sampel baris (axis=0) yang dapat dilihat pada Gambar 1.
   
      ![Cosine Similarity](https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/aaca99e1-bd82-4fbd-899c-f890975af00b)
   
      Gambar 1. Matriks Cosine Similarity
   
      Berdasarkan Gambar 1, dapat diketahui angka yang memiliki nilai 1.0 mengindikasikan bahwa restoran pada kolom X (horizontal) memiliki kesamaan dengan restoran pada baris Y (vertikal). Sebagai contoh, resto **Hamburguesas La perica** dan resto **carnitas_mata** teridentifikasi mirip (similar) dengan resto **tacos abi**.

      Dengan data kesamaan (similarity) restoran yang diperoleh sebelumnya, selanjutnya akan dilakukan rekomendasi daftar resto yang mirip (similar) dengan resto yang sebelumnya pernah dikunjungi pelanggan.
      
   3. **Mendapatkan Rekomendasi**
   
      Pada tahap ini akan menghasilkan sejumlah restoran yang akan direkomendasikan kepada pengguna dengan keluaran sistem rekomendasi restoran berupa Top-N Recommendation. Sebagai contoh seperti matriks sebelumnya, pengguna X pernah memesan makanan dari resto **tacos abi**. Kemudian, saat pengguna tersebut berencana untuk memesan makanan di restoran lain, sistem akan merekomendasikan resto **Hamburguesas La perica** dan resto **carnitas_mata**. Rekomendasi kedua restoran ini berdasarkan kesamaan yang dihitung dengan cosine similarity pada tahap sebelumnya.
      
Setelah dilakukan tahapan-tahapan tersebut, dilakukan uji coba dengan menghasilkan Top-N Recommendation pada model Content Based Filtering. Pada kasus kali ini, dilakukan uji coba untuk mencari restoran yang mirip dengan jenis masakan pada restoran KFC. Hasil rekomendasi restoran dapat dilihat pada Tabel 6.

Tabel 6. Hasil rekomendasi restoran Content Based Filtering.

| No.| resto_name         | cuisine       |
|----|--------------------|---------------|
| 1  | VIPS               | American	    |
| 2  | tacos los volcanes |	American	    | 
| 3  | Pizzeria Julios    |	American      |
| 4  | Sirlone	          |	International |
| 5  | McDonalds Centro	  | American      |

Berdasarkan Tabel 6, sistem telah berhasil memberikan rekomendasi 5 nama restoran yang mirip dengan KFC dengan kategori American dan kategori International.
        
### B. Model Development dengan Collaborative Filtering

   Adapun langkah-langkah yang digunakan dalam pengembangan model dengan Collaborative Filtering yaitu:

   1. **Data Preparation Model Collaborative Filtering**
   
      Berikut adalah hal-hal yang telah dilakukan pada tahap ini:

      - Menyandikan (encode) fitur 'user' dan 'placeID' kedalam indeks integer.
      - Memetakan 'userID' dan 'placeID' ke dataframe yang berkaitan.
      - Mengecek beberapa hal dalam data seperti jumlah user, jumlah resto, kemudian mengubah nilai rating menjadi float.

   2. **Membagi Data untuk Training dan Validasi**
   
      Sebelum melakukan pelatihan model tahapan yang harus diselesaikan yaitu mengacak data Ratings terlebih dahulu agar pendistribusiannya menjadi random, kemudian dilanjutkan dengan membagi data train dan validasi dengan komposisi 80:20. Namun sebelumnya, perlu memetakan (mapping) data user dan resto menjadi satu value terlebih dahulu. Lalu, membuat rating dalam skala 0 sampai 1 agar mudah dalam melakukan proses training.

   3. **Proses Training**
   
      Pada tahap ini, model menghitung skor kecocokan antara pengguna dan resto dengan teknik embedding. Pertama, dilakukan proses embedding terhadap data user dan resto. Selanjutnya, melakukan operasi perkalian dot product antara embedding user dan resto. Selain itu, menambahkan bias untuk setiap user dan resto. Skor kecocokan ditetapkan dalam skala [0,1] dengan fungsi aktivasi sigmoid. Model ini menggunakan Binary Crossentropy untuk menghitung loss function, Adam (Adaptive Moment Estimation) sebagai optimizer, dan root mean squared error (RMSE) sebagai metrics evaluation.
      
Setelah dilakukan tahapan-tahapan tersebut, dilakukan uji coba untuk menghasilkan rekomendasi restoran kepada pengguna. Untuk mendapatkan rekomendasi resto, perlu diambil sampel user secara acak dan mendefinisikan variabel resto_not_visited yang merupakan daftar resto yang belum pernah dikunjungi oleh pengguna. Daftar resto yang belum pernah dikunjungi oleh pengguna inilah yang akan menjadi resto yang direkomendasikan. Sebelumnya, pengguna telah memberi rating pada beberapa resto yang telah mereka kunjungi. Maka dari itu rating tersebut digunakan untuk membuat rekomendasi restoran yang mungkin cocok untuk pengguna. Restoran yang akan direkomendasikan adalah restoran yang belum pernah dikunjungi oleh pengguna. Oleh karena itu, perlu membuat variabel "resto_not_visited" sebagai daftar restoran untuk direkomendasikan pada pengguna. Hasil rekomendasi restoran dapat dilihat pada Gambar 2.

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/e142ab49-4310-474d-91c5-bfb4fb2923b7" width="400">
</p>

Gambar 2. Hasil rekomendasi restoran Collaborative Filtering

Berdasarkan Gambar 2 merupakan rekomendasi untuk user dengan ID U1034. Dari output tersebut, dapat dibandingkan antara Resto dengan rating tinggi dari user: U1034 dan Top 10 rekomendasi resto untuk user: U1034.

Beberapa rekomendasi restoran menyediakan jenis/kategori masakan yang sesuai dengan rating user. Diperoleh 3 rekomendasi resto dengan kategori Mexican, 1 rekomendasi resto dengan kategori Pizzeria yang sama dengan kategori Italian, rekomendasi resto dengan 1 kategori Japanese yang mirip dengan kategori Seafood, karena kategori Japanese pada umumnya meyediakan hidangan seafood, lalu 1 kategori American yang merupakan resto KFC yang menyediakan sajian fast food.
   
Sehingga dapat diketahui dari hasil tersebut bahwa model melakukan prediksi dengan cukup sesuai.


## Evaluasi

### A. Evaluasi Content Based Filtering

Adapun langkah yang digunakan untuk mendapatkan rekomendasi yaitu dengan menggunakan Top-N Recommendation untuk mengambil k dengan nilai similarity terbesar pada index matriks yang diberikan. Langkah pertama yaitu mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan yang kemudian dataframe akan diubah menjadi numpy, dengan menggunakan argpartition di ambil sejumlah nilai k tertinggi dari similarity, dalam kasus ini digunakan dataframe Cosine Similarity. Kemudian, mengambil data dari bobot (tingkat kesamaan) tertinggi ke terendah, kemudian menghapus nama restoran agar nantinya output data nama restoran yang dicari tidak muncul pada daftar rekomendasi restoran.

### B. Evaluasi Collaborative Filtering

Adapun metrik evaluasi yang digunakan pada model Collaborative Filtering adalah Root Mean Squared Error (RMSE). Metode pengukuran ini berfungsi sebagai perkiraan nilai yang diamati dengan mengukur perbedaan nilai prediksi model. Root Mean Squared Error adalah hasil dari akar kuadrat dari Mean Squared Error. Keakuratan metode estimasi kesalahan pengukuran diwakili oleh nilai RMSE yang kecil. Semakin kecil (mendekati 0) nilai RMSE maka hasil prediksi akan semakin akurat. Persamaan metrik RMSE ditunjukkan pada gambar berikut:

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/55912666-1989-425f-9243-2c20043f0b9b" width="200">
</p>

Gambar 3. Persamaan metrik RMSE

Berdasarkan Gambar 3, keterangan yang ada pada persamaan RMSE yaitu:

    n => Jumlah data
    i => Urutan Data
    y => Nilai hasil observasi
    ŷ => Nilai hasil prediksi

Melihat visualisasi proses training plot metrik evaluasi RMSE dengan matplotlib.

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/36970f06-c9ce-4339-8215-eb27e8571798" width="400">
</p>

Gambar 4. Visualisasi plot metrik evaluasi RMSE

Dapat diketahui proses training model cukup smooth dan model konvergen pada epochs sekitar 100. Dari proses ini, diperoleh nilai error akhir sekitar 0.20, dan error pada data validasi sekitar 0.35. Nilai tersebut cukup bagus untuk sebuah sistem rekomendasi.

## Kesimpulan

Sistem rekomendasi yang dirancang dalam proyek ini bertujuan untuk memberikan rekomendasi restoran kepada pengguna melalui dua pendekatan model algoritma yang berbeda. Pendekatan pertama menggunakan Content Based Filtering, dengan tujuan menghasilkan rekomendasi restoran yang mirip dengan tempat makan yang disukai pengguna di masa lalu. Pendekatan kedua, Collaborative Filtering, bertujuan memberikan rekomendasi restoran yang belum pernah dikunjungi sebelumnya, berpotensi disukai oleh pengguna berdasarkan preferensi kuliner pengguna lain. Pengembangan kedua pendekatan model dalam proyek ini menunjukkan tingkat akurasi rekomendasi yang memadai. Meskipun demikian, masih terdapat peluang untuk mengembangkan model dengan lebih baik, meningkatkan tingkat akurasi, dan mengurangi tingkat kesalahan rekomendasi.
