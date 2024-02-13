<h1 align="center">Predictive Analytics Harga Berlian</h1>
<p align="center">
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/03834802-5fdb-42c0-b5b3-e0e29cbb505b" width="600">
</p>
 
## Business Understanding

### Problem Statements

- Dari berbagai fitur yang tersedia, manakah fitur yang memiliki dampak paling signifikan terhadap harga berlian?
- Berapakah nilai pasar harga berlian dengan spesifikasi atau atribut tertentu?

### Goals

- Mengidentifikasi fitur yang memiliki korelasi terkuat dengan harga berlian.
- Mengembangkan model machine learning yang mampu memperkirakan harga berlian dengan tingkat akurasi yang tinggi berdasarkan berbagai fitur yang tersedia.

### Solution statements

- Melakukan Exploratory Data Analysis deskripsi variabel terhadap dataset, melihat apakah terdapat missing value dan outliers dengan menganalisa visualisasi dataset dan mengetahui fitur yang paling berkolerasi terhadap harga berlian. 
- Menggunakan 3 algoritma berbeda untuk membandingkan algoritma yang memiliki tingkat error terkecil dengan metrik Mean Squared Error (MSE) yang kemudian menjadi algoritma rekomendasi untuk digunakan sebagai prediksi harga berlian, adapun ketiga algoritma tersebut adalah:

    - K-Nearest Neighbor Algorithm yang menggunakan kesamaan fitur untuk memprediksi nilai dari setiap data yang baru.
    - Random Forest yang menggunakan rata-rata prediksi seluruh pohon dalam model ensemble untuk dijadikan prediksi akhirnya. 
    - Boosting Algorithm yang bertujuan untuk meningkatkan performa atau akurasi prediksi dengan menggabungkan beberapa model sederhana dan dianggap lemah sehingga membentuk suatu model yang kuat.


## Data Understanding

Dataset yang digunakan pada proyek ini adalah dataset *Diamonds* yang didapat dari situs [Kaggle](https://www.kaggle.com/datasets/shivam2503/diamonds). Dalam dataset ini berisi harga dan atribut lainnya dari hampir 54.000 berlian.


## Exploratory Data Analysis - Deskripsi Variabel

Berdasarkan informasi dari [Kaggle](https://www.kaggle.com/datasets/shivam2503/diamonds), variabel-variabel pada dataset Diamonds adalah sebagai berikut:

- price: adalah harga dalam dolar Amerika Serikat ($), fitur ini merupakan fitur target pada proyek ini.
- carat: merepresentasikan bobot (weight) dari diamonds (0.2-5.01), digunakan sebagai ukuran dari batu permata dan perhiasan.
- cut: merepresentasikan kualitas pemotongan diamonds (Fair, Good, Very Good, Premium, and Ideal).
- color: merepresentasikan warna, dari J (paling buruk) ke D (yang terbaik).
- clarity: merepresentasikan seberapa jernih diamonds (I1 (paling buruk), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (terbaik))
- x: merepresentasikan panjang diamonds dalam mm (0-10.74).
- y: merepresentasikan lebar diamonds dalam mm (0-58.9).
- z: merepresentasikan kedalaman diamonds dalam mm (0-31.8).
- depth: merepresentasikan z/mean(x, y) = 2 * z/(x + y) (43-79).
- table: merepresentasikan lebar bagian atas berlian relatif terhadap titik terlebar 43-95).


Tabel 1. Informasi pada dataset:

| Column  | Non-Null Count | Dtype   |
|---------|----------------|---------|
| carat   | 53940 non-null | float64 |
| cut     | 53940 non-null | object  |
| color   | 53940 non-null | object  |
| clarity | 53940 non-null | object  |
| depth   | 53940 non-null | float64 |
| table   | 53940 non-null | float64 |
| price   | 53940 non-null | int64   |
| x       | 53940 non-null | float64 |
| y       | 53940 non-null | float64 |
| z       | 53940 non-null | float64 |

Pada Tabel 1 dapat disimpulkan bahwa:
Dari output diatas terlihat bahwa:

- Terdapat 3 kolom/fitur dengan tipe object, yaitu: cut, color, dan clarity. Fitur ini merupakan categorical features (fitur non-numerik).
- Terdapat 6 fitur numerik dengan tipe data float64 yaitu: carat, depth, table, x, y, dan z. Ini merupakan fitur numerik yang merupakan hasil pengukuran secara fisik.
- Terdapat 1 fitur numerik dengan tipe data int64, yaitu: price. fitur ini merupakan fitur target.

Tabel 2. Deskripsi statistik data:

|       |        carat |        depth |        table |        price |            x |            y |            z |
|-------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| count | 53940.000000 | 53940.000000 | 53940.000000 | 53940.000000 | 53940.000000 | 53940.000000 | 53940.000000 |
| mean  |     0.797940 |    61.749405 |    57.457184 |  3932.799722 |     5.731157 |     5.734526 |     3.538734 |
| std   |     0.474011 |     1.432621	|     2.234491 |  3989.439738 |     1.121761 |     1.142135 |     0.705699 |
| min   |     0.200000 |    43.000000 |    43.000000 |   326.000000 |     0.000000 |     0.000000 |     0.000000 |
| 25%   |     0.400000 |    61.000000 |    56.000000 |   950.000000 |     4.710000 |     4.720000 |     2.910000 |
| 50%   |     0.700000 |    61.800000 |    57.000000 |  2401.000000 |     5.700000 |     5.710000 |     3.530000 |
| 75%   |     1.040000 |    62.500000 |    59.000000 |  5324.250000 |     6.540000 |     6.540000 |     4.040000 |
| max   |     5.010000 |    79.000000 |    95.000000 | 18823.000000 |    10.740000 |    58.900000 |    31.800000 |

Berdasarkan Tabel 2, terdapat informasi statistik pada masing-masing kolom, antara lain:

- Count  adalah jumlah sampel pada data.
- Mean adalah nilai rata-rata.
- Std adalah standar deviasi.
- Min yaitu nilai minimum setiap kolom. 
- 25% adalah kuartil pertama. Kuartil adalah nilai yang menandai batas interval dalam empat bagian sebaran yang sama. 
- 50% adalah kuartil kedua, atau biasa juga disebut median (nilai tengah).
- 75% adalah kuartil ketiga.
- Max adalah nilai maksimum.

Dapat diketahui, nilai minimum untuk kolom x, y, dan z adalah 0. x, y, dan z adalah ukuran panjang, lebar, dan kedalaman diamonds sehingga tidak mungkin ada diamonds dengan dimensi x, y, atau z bernilai 0. Hal ini bisa jadi merupakan data yang tidak valid atau missing value.

## Exploratory Data Analysis - Menangani Missing Value

Seperti yang dijelaskan sebelumnya, x, y, dan z adalah ukuran panjang, lebar, dan kedalaman diamonds sehingga tidak mungkin ada diamonds dengan dimensi bernilai 0. Maka dari itu penanganan missing value dilakukan dengan menghapus sample data ukuran panjang (x), lebar (y), dan kedalaman (z) diamonds yang memiliki nilai 0. 

## Exploratory Data Analysis - Menangani Outliers

Terdapat beberapa outliers pada dataset, seperti contoh pada fitur carat dan fitur depth yang divisualisasikan dengan boxplot yang dapat dilihat pada Gambar 1 dan Gambar 2.

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/308acfe5-e602-4746-9d75-0835f47d02ea" width="500">
</p>

Gambar 1. Outliers fitur carat.

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/8a438c78-4ef6-48f0-93d1-62a94eaf918f" width="500">
</p>

Gambar 2. Outliers fitur depth.

Dalam menangani outliers digunakan metode IQR dengan membuat batas bawah dan batas atas dengan persamaan:

Batas bawah = Q1 - 1.5 * IQR
Batas atas  = Q3 + 1.5 * IQR

Hasil penanganan outliers dengan metode IQR dapat dilihat pada Gambar 3 dan Gambar 4:

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/44241d99-2dce-4603-825a-fd452ed5900e" width="500">
</p>

Gambar 3. Hasil penanganan outliers fitur carat.

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/76369a40-a664-46c6-8376-1a798e0353a8" width="500">
</p>

Gambar 4. Hasil penanganan outliers fitur depth.


## Exploratory Data Analysis - Univariate Analysis

Pada tahap ini membagi fitur pada dataset menjadi dua bagian:
- Numerical features = price, carat, depth, table, x, y, z.
- Categorical features = cut, color, clarity.

  
### Categorical Features

**Fitur cut**
<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/1e2d2429-b9d7-457e-ab20-3ed6c252a3d5" width="500">
</p>

Gambar 5. Fitur cut.

Berdasarkan Gambar 5. Terdapat 5 kategori pada fitur Cut, secara berurutan dari jumlahnya yang paling banyak yaitu: Ideal, Premium, Very Good, Good, dan Fair. Dari data persentase dapat disimpulkan bahwa lebih dari 60% sampel merupakan diamonds tipe grade tinggi, yaitu grade Ideal dan Premium.

**Fitur color**

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/ca091bf3-f34b-4c99-86f5-50661086bf23" width="500">
</p>

Gambar 6. Fitur color.

Pada bagian Exploratory Data Analysis - Deskripsi Variabel sebelumnya didapatkan informasi bahwa kualitas warna dari yang paling buruk ke yang paling bagus adalah J, I, H, G, F, E, dan D. Maka berdasarkan Gambar 6. Dapat disimpulkan bahwa sebagian besar grade berada pada grade menengah, yaitu G, F, E.

**Fitur clarity**

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/70441ee1-b5ff-47ca-a50b-966e23aeb31c" width="500">
</p>

Gambar 7. Fitur clarity.

Dari penjelasan pada bagian Exploratory Data Analysis - Deskripsi Variabel sebelumnya, dapat diketahui bahwa fitur clarity terbagi menjadi 8 kategori, dimulai dari yang paling buruk hingga yang paling baik kualitasnya adalah I1, SI2, SI1, VS2, VS1, VVS2, VVS1, dan IF. Maka berdasarkan Gambar 7. Dapat disimpulkan bahwa sebagian besar fitur merupakan grade rendah, yaitu SI1, SI2, dan VS2.

### Numerical Features

Histogram pada masing-masing numerical features dapat dilihat pada Gambar 8:

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/364974ef-10ae-4bb4-94d1-88904311e4c3" width="800">
</p>

Gambar 8. Univariate numerical features.

Berdasarkan Gambar 8. Dari histogram "price" yang merupakan target fitur, diperoleh beberapa informasi, antara lain:

- Peningkatan harga diamonds sebanding dengan penurunan jumlah sampel. Dilihat jelas dari histogram "price" yang grafiknya mengalami penurunan seiring dengan semakin banyaknya jumlah sampel (sumbu x).
- Rentang harga diamonds cukup tinggi yaitu dari skala ratusan dolar Amerika hingga sekitar \$11800.

- Setengah harga berlian bernilai dibawah \$2500.
- Distribusi harga miring ke kanan (right-skewed). Hal ini akan berimplikasi pada model.


## Exploratory Data Analysis - Multivariate Analysis

### Categorical Features

Rata-rata harga berlian terhadap masing-masing fitur untuk mengetahui pengaruh fitur kategori terhadap harga berlian:

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/575e06ed-a878-40f5-9ad0-33dcde98f4c1" width="600">
</p>

Gambar 9. Multivariate categorical features.

Dengan mengamati rata-rata harga relatif terhadap fitur kategori berdasarkan Gambar 9. Dapat diketahui informasi sebagai berikut:

- Pada fitur cut, rata-rata harga cenderung mirip. Rentangnya berada antara \$3500 hingga \$4500. Grade tertinggi yaitu grade Ideal memiliki harga rata-rata terendah diantara grade lainnya. Sehingga, fitur cut memiliki pengaruh atau dampak yang kecil terhadap rata-rata harga.
- Pada fitur color, semakin rendah grade warna, harga diamonds justru semakin tinggi harga. Dari sini dapat disimpulkan bahwa warna memiliki pengaruh yang rendah terhadap harga.
- Pada fitur clarity, secara umum, diamond dengan grade lebih rendah memiliki harga yang lebih tinggi. Hal ini berarti bahwa fitur clarity memiliki pengaruh yang rendah terhadap harga.

Berdasarkan hal tersebut, dapat diketahui bahwa fitur kategori memiliki pengaruh yang rendah terhadap harga berlian.


### Numerical Features

**Melihat hubungan antar fitur numerik dengan pairplot**

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/08459b3e-7bec-4c81-a50c-3b75903c7611" width="700">
</p>

Gambar 10. Numerical features pairplot.

Berdasarkan Gambar 10. Pada pola sebaran data grafik pairplot, terlihat fitur carat, x, y, dan z memiliki korelasi yang tinggi dengan fitur price. Sedangkan kedua fitur lainnya yaitu depth dan table terlihat memiliki korelasi yang lemah karena sebarannya tidak membentuk pola.

**Melihat korelasi antar fitur numerik dengan correlation matrix**

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/691694c0-5c5a-4f27-917d-0c4a3f80df5d" width="600">
</p>

Gambar 11. Numerical features correlation matrix.

Berdasarkan Gambar 11. Fitur carat, x, y, dan z memiliki skor korelasi yang besar (di atas 0.9) dengan fitur target price. Artinya, fitur price berkorelasi tinggi dengan keempat fitur tersebut. Sementara itu, fitur depth memiliki korelasi yang sangat kecil (0.01). Sehingga, fitur tersebut akan dihapus.

## Data Preparation

Pada tahap ini dilakukan proses transformasi pada data sehingga menjadi bentuk yang cocok untuk proses pemodelan.

1. Encoding Fitur Kategori

    Menggunakan teknik one-hot-encoding untuk melakukan proses encoding dengan fitur get_dummies sehingga variabel kategori berubah menjadi variabel numerik.

2. Reduksi Dimensi dengan PCA
   
    Mereduksi jumlah fitur dengan tetap mempertahankan informasi pada data menggunakan Principal Component Analysis (PCA).

    <p>
      <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/7770a327-6658-4f60-bd1a-4741433320de" width="500">
    </p>

    Gambar 12. Pairplot fitur x, y, z.

    Berdasarkan Gambar 12. Ketiga fitur ukuran diamonds dalam kolom x, y, dan z memiliki korelasi yang tinggi. Hal ini karena ketiga fitur ini memiliki informasi yang sama, yaitu ukuran diamonds.

    PCA digunakan karena variabel dalam data memiliki korelasi yang tinggi. Korelasi tinggi ini menunjukkan data yang berulang atau redundant, maka dari itu teknik PCA digunakan untuk mereduksi variabel asli menjadi sejumlah kecil variabel baru yang tidak berkorelasi linier, disebut komponen utama (PC).
   
4. Train-Test-Split

    Melakukan pembagian dataset menjadi data latih (train) dan data uji (test) dengan mempertahankan sebagian data yang ada untuk menguji seberapa baik generalisasi model terhadap data baru. Pembagian data dilakukan sebelum proses transformasi data, sehingga dapat mengurangi potensi kebocoran data (data leakage). Dalam hal ini jumlah data sebesar 4.7524 akan dibagi dengan rasio 90:10 menjadi 4.2771 data latih dan 4.753 data uji.

5. Standarisasi

    Untuk menghindari kebocoran informasi pada data uji, teknik StandardScaler dari library Scikitlearn digunakan dalam tahapan transformasi data numerical. Proses standarisasi mengubah nilai rata-rata (mean) menjadi 0 dan nilai standar deviasi menjadi 1.

## Modeling

Dalam mengembangkan model machine learning pada proyek ini digunakan 3 algoritma, yang kemudian akan dievaluasi performa dari masing-masing algoritma dan menentukan salah satu algoritma yang memiliki hasil terbaik dan dengan nilai error yang paling kecil menggunakan metrik MSE. Ketiga algoritma yang akan digunakan, antara lain:

-	K-Nearest Neighbor (KNN)

    Pada algortima ini menggunakan kesamaan fitur untuk memprediksi nilai dari setiap data yang baru. KNN bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat. Dalam pemilihan k harus hati-hati karena apabila memilih k yang terlalu rendah, maka akan menghasilkan model yang overfit dan hasil dari prediksinya akan memiliki varians yang tinggi. Dan jika memilih k yang terlalu tinggi, maka akan menghasilkan model yang underfitt dan hasil dari prediksinya akan memiliki bias yang tinggi. Kelebihan dari algoritma KNN ini relatif sederhana dibandingkan dengan algoritma lain, mudah dipahami dan digunakan. Algoritma KNN memiliki kekurangan jika dihadapkan pada jumlah fitur atau dimensi besar yang biasa disebut curse of dimensionality. Dalam melakukan pemodelan pada proyek ini didapatkan hasil akurasi data latih sebesar 0.972 atau 97%. Adapun parameter dan nilai yang digunakan dalam melakukan pemodelan pada algoritma ini yaitu:
    
    - n_neighbors = 10
      
      Parameter n_neighbors digunakan untuk menentukan jumlah tetangga terdekat (dengan k adalah sebuah angka positif).

-	Random Forest 

    Algoritma Random Forest adalah salah satu algoritma supervised learning. Algoritma ini disusun dari banyak algoritma pohon (decision tree) yang pembagian data dan fiturnya dipilih secara acak. Kelebihan dari algoritma Random Forest adalah algoritma ini sering digunakan karena cukup sederhana tetapi memiliki stabilitas yang mumpuni, dan algoritma ini termasuk kedalam kategori ensemble (group) learning yang merupakan model prediksi yang terdiri dari beberapa model dan bekerja secara bersama-sama, sehingga tingkat keberhasilan akan lebih tinggi dibanding model yang bekerja sendirian. Algoritma Random Forest ini memiliki kekurangan dalam menentukan nilai parameternya harus benar-benar tepat untuk data. Dalam melakukan pemodelan pada proyek ini didapatkan hasil akurasi data latih sebesar 0.987 atau 98%. Adapun parameter dan nilai yang digunakan dalam melakukan pemodelan pada algoritma ini yaitu:
    
    - n_estimators = 50 
      
      Parameter n_estimators digunakan untuk menentukan jumlah pohon di forest.
      
    - max_depth = 16
    
      Parameter max_depth digunakan untuk menentukan kedalaman atau panjang pohon. Merupakan ukuran seberapa banyak pohon dapat membelah (splitting) untuk membagi setiap node kedalam jumlah pengamatan yang diinginkan.
      
    - random_state = 55
    
      Parameter random_state digunakan untuk mengontrol random number generator yang digunakan.
      
    - n_jobs = -1 
      
      Parameter n_jobs digunakan untuk menentukan jumlah job (pekerjaan) yang digunakan secara paralel. Merupakan komponen untuk mengontrol thread atau proses yang berjalan secara paralel.

-	Boosting Algorithm

    Boosting juga merupakan metode ensemble learning, perbedaannya dengan model Random Forest adalah model dilatih secara berurutan atau dalam proses yang iteratif. Algoritma yang menggunaakn teknik boosting bertugas memperbaiki kesalahan dari model pertama yang telah dibuat. Kelebihan dari algoritma ini adalah algoritma ini berfungsi untuk meningkatkan performa atau akurasi prediksi dengan cara menggabungkan beberapa model sederhana dan dianggap lemah sehingga membentuk suatu model yang kuat. Dalam melakukan pemodelan pada proyek ini didapatkan hasil akurasi data latih sebesar 0.964 atau 96%. Adapun parameter dan nilai yang digunakan dalam melakukan pemodelan pada algoritma ini yaitu:
    
    - learning_rate = 0.05
      
      Bobot yang diterapkan pada setiap regressor di masing-masing proses iterasi boosting.
      
    - random_state = 55
      
      Parameter random_state digunakan untuk mengontrol random number generator yang digunakan.
      
Sehingga dalam pembuatan model machine learning pada proyek ini score terbaik ditunjukkan oleh algoritma Random Forest yang memiliki hasil akurasi sebesar 0.999 atau 99%.


## Evaluation

Metrik yang digunakan pada prediksi ini adalah MSE atau Mean Squared Error yang menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi. MSE didefinisikan dalam persamaan yang dapat dilihat pada Gambar 9:

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/bf7ad560-ff59-4004-9a73-7f1e1775b9fb" width="300">
</p>

Gambar 13. Persamaan MSE.

Berdasarkan Gambar 13. Keterangan yang ada dalam persamaan MSE yaitu:

N = jumlah dataset

yi = nilai sebenarnya

y_pred = nilai prediksi

- Tabel 5. Hasil evaluasi MSE pada data latih dan data test adalah sebagai berikut:
    
  |          |      train |        test |
  |----------|------------|-------------| 
  | KNN      |  71.394561 |   95.296801 |
  | RF       |   0.129931 |    0.502556 |
  | Boosting | 266.088836	| 239.1362665 |

- Hasil evaluasi plot metrik MSE dengan bar chart dapat dilihat pada Gambar 14:

    <p>
      <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/4cb8493f-5977-4d07-ad67-dd523f515b11" height="300" >
    </p>
    
    Gambar 14. Plot metrik MSE.

    Berdasarkan Gambar 14. Terlihat bahwa algoritma model Random Forest (RF) memiliki hasil yang paling baik dibandingkan dengan algoritma model KNN dan Boosting. Hal ini ditunjukkan karena hasil pengujian model Random Forest memiliki nilai error terkecil dibandingkan dengan dua algoritma KNN yang memiliki angka error diatas 50, dan algoritma Boosting yang memiliki angka error diatas 200.

- Tabel 6. Prediksi dari data uji untuk melakukan pengujian:

    | y_true | prediksi_KNN | prediksi_RF | prediksi_Boosting |
    |--------|--------------|-------------|-------------------| 
    |   2930 |       2929.8	|      2930.1 |            3663.0 |

    Terlihat pada Tabel 6, bahwa prediksi dengan algoritma Random Forest (RF) memiliki performa paling baik, dapat dilihat nilai pada kolom "prediksi_RF" memberikan nilai yang paling mendekati dengan nilai pada kolom "y_true".
