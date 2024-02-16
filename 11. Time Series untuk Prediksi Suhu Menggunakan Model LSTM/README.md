# Time Series untuk Prediksi Suhu Menggunakan Model LSTM

## Deskripsi Proyek:

Proyek ini bertujuan untuk mengembangkan model Time Series menggunakan arsitektur Long Short-Term Memory (LSTM) dengan tujuan melakukan prediksi suhu udara di Delhi. Data yang digunakan berasal dari dataset [Delhi Weather Data](https://www.kaggle.com/datasets/mahirkukreja/delhi-weather-data), yang mencakup informasi suhu udara dalam rentang waktu tertentu. Proyek ini melibatkan langkah-langkah seperti eksplorasi data, preprocessing, pembagian data, pembangunan model LSTM, pelatihan model, dan evaluasi performa model.

## Langkah-Langkah Proyek:

**1. Import Library dan Mengunduh Dataset:** Proyek dimulai dengan mengimpor library yang diperlukan dan memuat dataset Delhi Weather Data.

**2. Eksplorasi Data:** Melakukan eksplorasi data untuk memahami struktur dan karakteristiknya. Hal ini mencakup melihat jumlah baris dan kolom, menampilkan beberapa data teratas dan terbawah, serta memeriksa informasi dan keberadaan nilai yang kosong.

**3. Preprocessing Data:** Langkah ini melibatkan preprocessing data seperti mengubah format tanggal, normalisasi data suhu, dan menampilkan plot time series untuk melihat karakteristiknya.

**4. Pembagian Data dan Data Preparation:** Data dibagi menjadi data pelatihan dan data uji untuk melatih dan menguji model. Selain itu, fungsi windowed_dataset dibuat untuk mengubah data menjadi format yang dapat diterima oleh model.

**5. Pelatihan Model LSTM:** Membangun model LSTM menggunakan TensorFlow dan Keras. Model ini dilatih menggunakan data pelatihan dengan memperhatikan metrik Mean Absolute Error (MAE). Selama proses pelatihan, penggunaan callback digunakan untuk memberhentikan pelatihan jika MAE sudah mencapai nilai target.

**6. Evaluasi Model:** Model dievaluasi dengan memplot grafik loss dan MAE pada data pelatihan dan data uji. Dengan menggunakan MAE sebagai metrik, dapat diketahui sejauh mana model dapat memprediksi suhu udara dengan akurat.

## Hasil Proyek:

![Plot Loss dan MAE](https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/bbecc318-f933-48cc-86b4-6c67b7221436)

Pada plot Loss, terlihat bahwa nilai Loss pada training set terus menurun hingga mencapai nilai yang relatif stabil. Hal ini menunjukkan bahwa model sudah mampu belajar dengan baik dari data training. Sedangkan pada plot MAE, terlihat bahwa nilai MAE pada training set juga terus menurun hingga mencapai nilai yang relatif stabil. Hal ini menunjukkan bahwa model sudah mampu memprediksi nilai suhu udara dengan cukup akurat.

Pada plot MAE, terlihat bahwa nilai MAE cenderung stabil di sekitar 10%. Nilai MAE sebesar 10% dapat dikatakan cukup baik untuk proyek Time Series dengan dataset yang relatif kecil. Hal ini menunjukkan bahwa model sudah mampu memprediksi nilai suhu udara di Delhi dengan cukup akurat.

Model Time Series LSTM yang dikembangkan mampu memberikan prediksi suhu udara yang cukup akurat berdasarkan hasil plot metrik training dan test (Loss dan MAE). Grafik Loss dan MAE menunjukkan bahwa model telah belajar dengan baik dan memberikan performa yang cukup baik. Dengan demikian, proyek ini dapat memberikan kontribusi dalam pengembangan model prediksi suhu udara menggunakan pendekatan Time Series dengan LSTM.
