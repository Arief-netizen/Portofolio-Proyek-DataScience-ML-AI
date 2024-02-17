<h1 align="center">Predictive Analytics Harga Sewa Rumah</h1>
<p align="center">
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/03834802-5fdb-42c0-b5b3-e0e29cbb505b" width="600">
</p>

## Domain Proyek

### Latar Belakang

Rumah merupakan kebutuhan primer bagi manusia. Setiap orang tentu punya rumah ideal yang mereka impikan. Apalagi dengan semakin lengkapnya fasilitas yang ditawarkan oleh developer properti seperti luas rumah, jumlah kamar tidur, jumlah kamar mandi, dll. Tentunya dengan kriteria yang ditawarkan tersebut mempengaruhi terhadap nilai harga sewa rumah. 

Kurangnya media informasi menyulitkan dalam mendapatkan informasi harga sewa rumah. Sehingga diperlukan model untuk dapat memprediksi harga sewa rumah untuk mempermudah dalam bertransaksi. 

Bagi calon konsumen tentunya sangat konservatif mengenai harga dan tipe rumah yang diinginkan. Sehingga dibutuhkan model prediksi yang bisa digunakan untuk mengetahui kisaran harga sewa rumah yang diinginkan konsumen sesuai kriteria tipe rumah yang ada. Sedangkan bagi penjual model prediksi ini diharapkan bisa membantu penjual rumah yang kesulitan untuk menentukan harga rumah dengan harga yang berada di pasaran dan bisa mendapatkan keuntungan bagi penjual.
  
 
## Business Understanding

### Problem Statements

- Fitur apa yang paling berpengaruh terhadap harga sewa rumah?
- Berapakah harga pasar sewa rumah dengan karakteristik atau fitur yang tertentu?

### Goals

- Mengetahui fitur yang paling berkorelasi dengan harga sewa rumah
- Membuat model machine learning yang dapat memprediksi harga sewa rumah seakurat mungkin berdasarkan fitur-fitur yang ada

### Solution statements

- Melakukan Exploratory Data Analysis deskripsi variabel terhadap dataset, melihat apakah terdapat missing value dan outliers dengan menganalisa visualisasi dataset dan mengetahui fitur yang paling berkolerasi terhadap harga sewa rumah. 
- Menggunakan 3 algoritma berbeda untuk membandingkan algoritma yang memiliki tingkat error paling kecil yang kemudian menjadi algoritma rekomendasi untuk digunakan sebagai prediksi harga sewa rumah, adapun ketiga algoritma tersebut adalah:

    - K-Nearest Neighbor Algorithm yang menggunakan kesamaan fitur untuk memprediksi nilai dari setiap data yang baru.
    - Random Forest yang menggunakan rata-rata prediksi seluruh pohon dalam model ensemble untuk dijadikan prediksi akhirnya. 
    - Boosting Algorithm yang bertujuan untuk meningkatkan performa atau akurasi prediksi dengan menggabungkan beberapa model sederhana dan dianggap lemah sehingga membentuk suatu model yang kuat.


## Data Understanding

Dataset yang digunakan pada proyek ini adalah dataset House Rent Prediction Dataset yang didapat dari situs [Kaggle](https://www.kaggle.com/datasets/iamsouravbanerjee/house-rent-prediction-dataset). Dalam Dataset ini memiliki 4.746 rumah/apartemen/rumah susun yang tersedia untuk disewakan dengan berbagai karakteristik yang berbeda. Karakteristik yang dimaksud disini adalah fitur non-numerik seperti Floor, Area Type, Area Locality, City, Furnishing Status, Tenant Preferred, dan  Point of Contact, serta fitur numerik seperti BHK, Rent, Size, dan Bathroom. Kesebelas fitur ini merupakan fitur yang akan digunakan dalam menemukan pola dan data.


## Exploratory Data Analysis - Deskripsi Variabel

Berdasarkan informasi dari [Kaggle](https://www.kaggle.com/datasets/iamsouravbanerjee/house-rent-prediction-dataset), variabel-variabel pada House Rent Prediction Dataset adalah sebagai berikut:

- BHK: Jumlah kamar tidur (bedrooms), aula (hall), dapur (kitchen).
- Rent: Harga sewa rumah/apartemen/rumah susun.
- Size: Ukuran (ft<sup>2</sup>) rumah/apartemen/rumah susun.
- Floor: Letak lantai dan jumlah total lantai rumah/apartemen/rumah susun (contoh: lantai ground dari 2, 3 dari 5, dll.)
- Area Type: Ukuran rumah/apartemen/rumah susun dengan kategori Super Area, Area Karpet atau Area Bangunan.
- Area Locality: Letak lokasi rumah/apartemen/rumah susun.
- City: Kota letak rumah/apartemen/rumah susun berada.
- Furnishing Status: Status perabotan rumah/apartemen/rumah susun dengan kategori Furnished (berperabot), Semi-Furnished (sedikit perabotan), dan Unfurnished (tidak memiliki perabotan).
- Tenant Preferred: Jenis penyewa yang diutamakan oleh pemilik.
- Bathroom: Jumlah kamar mandi.
- Point of Contact: Siapa yang harus dihubungi untuk informasi lebih lanjut tentang rumah/apartemen/rumah susun.


Tabel 1. Informasi pada dataset:

| Column            | Non-Null Count | Dtype  |
|-------------------|----------------|--------|
| Posted On         | 4746 non-null  | object |
| BHK               | 4746 non-null  | int64  |
| Rent              | 4746 non-null  | int64  |
| Size              | 4746 non-null  | int64  |
| Floor             | 4746 non-null  | object |
| Area Type         | 4746 non-null  | object |
| Area Locality     | 4746 non-null  | object |
| City              | 4746 non-null  | object |
| Furnishing Status | 4746 non-null  | object |
| Tenant Preferred  | 4746 non-null  | object |
| Bathroom          | 4746 non-null  | int64  |
| Point of Contact  | 4746 non-null  | object |

Pada Tabel 1 dapat disimpulkan bahwa:
-	Terdapat 4 kolom numerik dengan tipe data int64, yaitu: BHK, Rent, Size, dan Bathroom.
-	Terdapat 8 kolom categorical dengan tipe object, yaitu: Posted On, Floor, Area Type, Area Locality, City, Furnishing Status, Tenant Preferred, dan  Point of Contact.

Tabel 2. Deskripsi statistik data:

|       |         BHK |         Rent |        Size |    Bathroom |
|-------|-------------|--------------|-------------|-------------| 
| count | 4746.000000 | 4.746000e+03 | 4746.000000 | 4746.000000 |
| mean  |    2.083860 | 3.499345e+04 |  967.490729 |    1.965866 |
| std   |    0.832256 | 7.810641e+04 |  634.202328 |    0.884532 |
| min   |    1.000000 | 1.200000e+03 |   10.000000 |    1.000000 |
| 25%   |    2.000000 | 1.000000e+04 |  550.000000 |    1.000000 |
| 50%   |    2.000000 | 1.600000e+04 |  850.000000 |    2.000000 |
| 75%   |    3.000000 | 3.300000e+04 | 1200.000000 |    2.000000 |
| max   |    6.000000 | 3.500000e+06 | 8000.000000 |   10.000000 |

Berdasarkan Tabel 2, terdapat informasi statistik pada masing-masing kolom, antara lain:

- Count  adalah jumlah sampel pada data.
- Mean adalah nilai rata-rata.
- Std adalah standar deviasi.
- Min yaitu nilai minimum setiap kolom. 
- 25% adalah kuartil pertama. Kuartil adalah nilai yang menandai batas interval dalam empat bagian sebaran yang sama. 
- 50% adalah kuartil kedua, atau biasa juga disebut median (nilai tengah).
- 75% adalah kuartil ketiga.
- Max adalah nilai maksimum.

Dapat diketahui tidak ada nilai 0 pada nilai minimum, sehingga dapat dikatakan tidak ada missing value pada dataset.


## Exploratory Data Analysis - Menangani Outliers

Terdapat beberapa outliers pada dataset, seperti contoh pada Fitur Size yang divisualisasikan dengan boxplot yang dapat dilihat pada Gambar 1.

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/cab08717-2e88-452a-b8f9-3f1e3e2067b0" width="500">
</p>

Gambar 1. Outliers Fitur Size.

Dalam menangani outliers digunakan metode IQR dengan membuat batas bawah dan batas atas dengan persamaan:

Batas bawah = Q1 - 1.5 * IQR
Batas atas  = Q3 + 1.5 * IQR

Hasil penanganan outliers dengan metode IQR dapat dilihat pada Gambar 2:

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/88a4a1d0-e047-4c14-afaa-e6e0008e81ed" width="500">
</p>

Gambar 2. Hasil penanganan outliers Fitur Size.


## Exploratory Data Analysis - Univariate Analysis

Tabel 3. Sample pada fitur Area Type:

| Area Type   | BHK  | Rent | Size | Bathroom |
|-------------|------|------|------|----------|
| Built Area  |    2 |    2 |    2 |        2 |
| Carpet Area | 1799 | 1799 | 1799 |     1799 |
| Super Area  | 2330 | 2330 | 2330 |     2330 |

Dari Tabel 3, pada fitur Area Type, jumlah sample pada baris Built Area hanya memliki 2 sample, maka sample Built Area akan dihapus karena memiliki sample yang terlalu sedikit.

Tabel 4. Uunique length pada masing-masing fitur:

| Feature           | Unique Length |
|-------------------|---------------|
| Floor             |           332 |
| Area Type         |             2 |
| Area Locality     |          1971 |
| City              |             6 | 
| Furnishing Status |             3 |
| Tenant Preferred  |             3 |

Berdasarkan Tabel 4, Dapat dilihat pada output diatas bahwa fitur Floor dan Area Locality memiliki nilai unique length yang terlalu tinggi jika dibandingkan dengan fitur lainnya. Maka kedua fitur ini akan dihapus.

### Categorical Features

**Fitur Area Type**
<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/47c120cc-a594-4f0b-b0fd-4b0f7759a484" width="500">
</p>

Gambar 3. Fitur Area Type.

Berdasarkan Gambar 3. Terdapat 2 kategori pada fitur Area Type, secara berurutan dari yang paling banyak yaitu: Super Area, lalu Carpet Area. Dari data persentase dapat disimpulkan bahwa lebih dari 50% sampel merupakan rumah tipe grade tinggi, yaitu Super Area.

**Fitur City**

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/6ce49301-fa71-4af4-982e-80e10f6bc1f0" width="500">
</p>

Gambar 4. Fitur City.

Berdasarkan Gambar 4. Urutan kategori letak rumah/apartemen/rumah susun di kota yang paling sedikit ke yang paling banyak adalah Kolkata-Delhi-Mumbai-Hyderabad-Chenmai-Bangalore. Dari grafik diatas dapat disimpulkan bahwa sebagian besar letak rumah/apartemen/rumah susun dari yang paling banyak berada pada kota Bangalore, Chennai, dan Hyderadab.

**Fitur Furnishing Status**

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/eb54de00-72c8-4e57-83c1-a67ed5638306" width="500">
</p>

Gambar 5. Fitur Furnishing Status.

Berdasarkan Gambar 5. Fitur Furnishing Status terdiri dari 3 kategori dari yang paling sedikit ke yang paling banyak, yaitu: Furnished (memiliki perabotan), Unfurnished (tidak ada perabotan), Semi-Furnished (memiliki sebagian perabotan). Dapat disimpulkan bahwa rumah/apartemen/rumah susun yang tersedia lebih banyak yang memiliki sebagian perabotan dan tidak ada perabotan.

### Numerical Features

Histogram pada masing-masing numerical features dapat dilihat pada Gambar 6:

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/d431df67-4ae3-42a2-8cc2-4001ba3df1f9" width="800">
</p>

Gambar 6. Univariate numerical features.

Berdasarkan Gambar 6. Didapatkan informasi sebagai berikut:

Fitur BHK:
- Rumah/apartemen/rumah susun memiliki 1 hingga 3 kamar tidur, aula, dan dapur, namun sebagian besar memiliki 2 kamar tidur, aula, dan dapur.

Fitur Rent:
- Peningkatan harga sewa rumah sebanding dengan penurunan jumlah sampel. Dapat dilihat jelas dari histogram 'Rent' yang grafiknya mengalami penurunan seiring dengan semakin banyaknya jumlah sampel (sumbu x).
- Rentang harga sewa rumah hingga sekitar $65000.

- Harga rumah yang banyak disewa sekitar bernilai dibawah $18000.

Fitur Size:
- Rumah/apartemen/rumah susun memiliki ukuran dibawah 2100 (ft<sup>2</sup>), namun sebagian besar memiliki ukuran diantara 500 (ft<sup>2</sup>) hingga 1200 (ft<sup>2</sup>).

Fitur Bathroom:
- Rumah/apartemen/rumah susun memiliki 1 hingga 3 kamar mandi, namun sebagian besar memiliki 2 kamar mandi.

## Exploratory Data Analysis - Multivariate Analysis

### Categorical Features

Rata-rata sewa rumah/apartemen/rumah susun terhadap masing-masing fitur untuk mengetahui pengaruh fitur kategori terhadap sewa rumah/apartemen/rumah susun:

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/6d9157bc-5ee9-4de0-8676-6c9863332a1d" width="600">
</p>

Gambar 7. Multivariate categorical features.

Berdasarkan Gambar 7. Dapat disimpulkan bahwa:

- Pada fitur Area Type, rata-rata sewa berada antara \$15007 hingga \$23714. Tipe grade tertinggi yaitu Super Area memiliki sewa yang rendah jika dibandingkan dengan sewa tipe grade dibawahnya yaitu Carpet Area. Dalam hal ini fitur Area Type memiliki pengaruh yang kecil.
- Pada fitur City, rata-rata sewa berada antara \$10987 hingga \$36662. Kota Bangalore, Chennai, dan hyderabad memiliki sewa yang rendah jika dibandingkan dengan sewa kota Mumbai. Dalam hal ini fitur City memiliki pangaruh yang cukup besar.
- Pada fitur Furnishing Status, rata-rata sewa berada antara \$15989 hingga \$24250. rumah/apartemen/rumah susun Semi-Furnished dan Unfurnished memiliki sewa yang rendah jika dibandingkan dengan sewa rumah/apartemen/rumah susun yang Furnished. Dalam hal ini fitur Furnishing Status memiliki pengaruh yang cukup besar.
- Pada Fitur Tenant Preferred, rata-rata sewa berada antara \$17384 hingga \$24004. Dari grafik dapat dilihat bahawa Family memiliki sewa yang paling tinggi dibandingkan dengan yang lain. Dalam hal ini fitur Tenant Preferred memiliki pengaruh yang cukup lumayan besar.

### Numerical Features

Kolerasi antar fitur numerical dapat dilihat pada Gambar 8:

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/edfbb290-1741-4671-b2af-6b930e33312f" width="600">
</p>

Gambar 8. Multivariate numerical features.

Berdasarkan Gambar 8. Koefisien korelasi berkisar antara -1 dan +1. Ia mengukur kekuatan hubungan antara dua variabel serta arahnya (positif atau negatif). Mengenai kekuatan hubungan antar variabel, semakin dekat nilainya ke 1 atau -1, korelasinya semakin kuat. Sedangkan, semakin dekat nilainya ke 0, korelasinya semakin lemah. Dapat dilihat kolerasi pada Fitur BHK, Size, dan Bathroom berkolerasi dengan fitur Rent dengan cukup baik. Sementara itu, fitur 'Price Per Square Feet' memiliki korelasi yang kecil (0.29). Sehingga, fitur tersebut akan di-drop.

## Data Preparation

1. Encoding Fitur Kategori

    Proses encoding fitur categorical menggunakan teknik one-hot-encoding dalam penerapannya untuk mendapatkan fitur baru yang sesuai sehingga dapat mewakili variabel categorical. Dalam hal ini terdapat fitur categorical yaitu: Area Type, City, Furnishing Status, dan Tenant Preferred yang kemudian akan diubah menjadi numerical features.

2. Train-Test-Split

    Melakukan pembagian dataset menjadi data latih (train) dan data uji (test) dengan mempertahankan sebagian data yang ada untuk menguji seberapa baik generalisasi model terhadap data baru. Pembagian data dilakukan sebelum proses transformasi data, sehingga dapat mengurangi potensi kebocoran data (data leakage). Dalam hal ini jumlah data sebesar 4.129 akan dibagi dengan rasio 75:25 menjadi 3.096 data latih dan 1.033 data uji.

3. Standarisasi

    Untuk menghindari kebocoran informasi pada data uji, teknik StandardScaler dari library Scikitlearn digunakan dalam tahapan transformasi data numerical. Proses standarisasi mengubah nilai rata-rata (mean) menjadi 0 dan nilai standar deviasi menjadi 1.

## Modeling

Dalam mengembangkan model machine learning pada proyek ini digunakan 3 algoritma, yang kemudian akan dievaluasi performa dari masing-masing algoritma dan menentukan salah satu algoritma yang memiliki hasil terbaik dan dengan nilai error yang paling kecil. Ketiga algoritma yang akan digunakan, antara lain:

-	K-Nearest Neighbor (KNN)

    Pada algortima ini menggunakan kesamaan fitur untuk memprediksi nilai dari setiap data yang baru. KNN bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat. Dalam pemilihan k harus hati-hati karena apabila memilih k yang terlalu rendah, maka akan menghasilkan model yang overfit dan hasil dari prediksinya akan memiliki varians yang tinggi. Dan jika memilih k yang terlalu tinggi, maka akan menghasilkan model yang underfitt dan hasil dari prediksinya akan memiliki bias yang tinggi. Kelebihan dari algoritma KNN ini relatif sederhana dibandingkan dengan algoritma lain, mudah dipahami dan digunakan. Algoritma KNN memiliki kekurangan jika dihadapkan pada jumlah fitur atau dimensi besar yang biasa disebut curse of dimensionality. Dalam melakukan pemodelan pada proyek ini didapatkan hasil akurasi data latih sebesar 0.516 atau 51%. Adapun parameter dan nilai yang digunakan dalam melakukan pemodelan pada algoritma ini yaitu:
    
    - n_neighbors = 8
      
      Parameter n_neighbors digunakan untuk menentukan jumlah tetangga terdekat (dengan k adalah sebuah angka positif).

-	Random Forest 

    Algoritma Random Forest adalah salah satu algoritma supervised learning. Algoritma ini disusun dari banyak algoritma pohon (decision tree) yang pembagian data dan fiturnya dipilih secara acak. Kelebihan dari algoritma Random Forest adalah algoritma ini sering digunakan karena cukup sederhana tetapi memiliki stabilitas yang mumpuni, dan algoritma ini termasuk kedalam kategori ensemble (group) learning yang merupakan model prediksi yang terdiri dari beberapa model dan bekerja secara bersama-sama, sehingga tingkat keberhasilan akan lebih tinggi dibanding model yang bekerja sendirian. Algoritma Random Forest ini memiliki kekurangan dalam menentukan nilai parameternya harus benar-benar tepat untuk data. Dalam melakukan pemodelan pada proyek ini didapatkan hasil akurasi data latih sebesar 0.982 atau 98%. Adapun parameter dan nilai yang digunakan dalam melakukan pemodelan pada algoritma ini yaitu:
    
    - n_estimators = 50 
      
      Parameter n_estimators digunakan untuk menentukan jumlah pohon di forest.
      
    - max_depth = 8
    
      Parameter max_depth digunakan untuk menentukan kedalaman atau panjang pohon. Merupakan ukuran seberapa banyak pohon dapat membelah (splitting) untuk membagi setiap node kedalam jumlah pengamatan yang diinginkan.
      
    - random_state = 33
    
      Parameter random_state digunakan untuk mengontrol random number generator yang digunakan.
      
    - n_jobs = -1 
      
      Parameter n_jobs digunakan untuk menentukan jumlah job (pekerjaan) yang digunakan secara paralel. Merupakan komponen untuk mengontrol thread atau proses yang berjalan secara paralel.

-	Boosting Algorithm

    Boosting juga merupakan metode ensemble learning, perbedaannya dengan model Random Forest adalah model dilatih secara berurutan atau dalam proses yang iteratif. Algoritma yang menggunaakn teknik boosting bertugas memperbaiki kesalahan dari model pertama yang telah dibuat. Kelebihan dari algoritma ini adalah algoritma ini berfungsi untuk meningkatkan performa atau akurasi prediksi dengan cara menggabungkan beberapa model sederhana dan dianggap lemah sehingga membentuk suatu model yang kuat. Dalam melakukan pemodelan pada proyek ini didapatkan hasil akurasi data latih sebesar 0.848 atau 84%. Adapun parameter dan nilai yang digunakan dalam melakukan pemodelan pada algoritma ini yaitu:
    
    - learning_rate = 0.1
      
      Bobot yang diterapkan pada setiap regressor di masing-masing proses iterasi boosting.
      
    - n_estimators = 150
      
      Parameter n_estimators digunakan untuk memperkuat kontribusi pada setiap regresor.
      
    - random_state = 55
      
      Parameter random_state digunakan untuk mengontrol random number generator yang digunakan.
      
Sehingga dalam pembuatan model machine learning pada proyek ini performa terbaik ditunjukkan oleh algoritma Random Forest yang memiliki hasil score sebesar 0.982 atau 98%.


## Evaluation

Metrik yang digunakan pada prediksi ini adalah MSE atau Mean Squared Error yang menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi. MSE didefinisikan dalam persamaan yang dapat dilihat pada Gambar 9:

<p>
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/3689ac98-5381-436e-bd8b-ccd6888df4ec" width="300">
</p>

Gambar 9. Persamaan MSE.

Berdasarkan Gambar 9. Keterangan yang ada dalam persamaan MSE yaitu:

N = jumlah dataset

yi = nilai sebenarnya

y_pred = nilai prediksi

- Tabel 5. Hasil evaluasi MSE pada data latih dan data test adalah sebagai berikut:
    
  |          | train        | test         |
  |----------|--------------|--------------| 
  | KNN      | 60847.512857 | 93295.599863 |
  | RF       |   678.321111 |  3338.271112 |
  | Boosting | 22478.006109	| 29291.066335 |

- Hasil evaluasi plot metrik MSE dengan bar chart dapat dilihat pada Gambar 10:

    <p>
      <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/41df8c44-b008-4835-a391-17103b81cc34" width="450">
    </p>
    
    Gambar 10. Plot metrik MSE.

    Berdasarkan Gambar 10. Terlihat bahwa algoritma model Random Forest (RF) memiliki hasil yang paling baik dibandingkan dengan algoritma model Boosting dan KNN. Hal ini ditunjukkan karena hasil pengujian model Random Forest memiliki nilai error terkecil dibandingkan dengan dua algoritma lainnya yang memiliki angka error yang besar diatas 20.000.

- Tabel 6. Prediksi dari data uji untuk melakukan pengujian:

    | y_true | prediksi_KNN | prediksi_RF | prediksi_Boosting |
    |--------|--------------|-------------|-------------------| 
    |  14000 |      18250.0	|     14075.2 |           15554.1 |

    Terlihat pada Tabel 6, bahwa prediksi dengan algoritma Random Forest (RF) memiliki performa paling baik, dapat dilihat nilai pada kolom "prediksi_RF" memberikan nilai yang paling mendekati dengan nilai pada kolom "y_true".
