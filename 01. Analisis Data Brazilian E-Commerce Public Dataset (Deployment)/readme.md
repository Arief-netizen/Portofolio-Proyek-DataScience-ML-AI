# Analisis Data Brazilian E-Commerce Public Dataset
![Cover-Brazilian-Ecommerce](https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/aff85630-41be-4ad4-ac08-5c4b19e6dae2)

**Tujuan Proyek:**
Proyek ini bertujuan untuk melakukan analisis mendalam terhadap [Brazilian E-Commerce Public Dataset on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) hingga website deployment menggunakan streamlit. Data ini mencakup informasi seputar pelanggan, produk, pesanan, pembayaran, dan lokasi geografis. Analisis ini dimaksudkan untuk memberikan wawasan yang berharga dalam mendukung pengambilan keputusan bisnis.

## Pertanyaan Bisnis

1. **Segmentasi Pasar Berdasarkan Wilayah Geografis:**
   - Mengidentifikasi kota-kota dengan jumlah pelanggan terbanyak.
   - Memberikan wawasan terhadap potensi pengembangan bisnis di wilayah-wilayah tertentu.

2. **Kategori Barang yang Paling Sering Dibeli dan Solusi terhadap Kategori Produk yang Paling Jarang Dibeli:**
   - Menganalisis kategori produk dengan penjualan tertinggi dan terendah.
   - Menyajikan solusi atau strategi untuk meningkatkan penjualan kategori produk yang kurang diminati.

3. **Peningkatan Pembelian Tertinggi pada Bulan Tertentu:**
   - Mengidentifikasi bulan dengan peningkatan pembelian tertinggi.
   - Menyelidiki faktor-faktor atau peristiwa yang mungkin menyebabkan peningkatan tersebut.

4. **Tipe Pembayaran yang Paling Sering Digunakan dan Peningkatan Layanan Transaksi:**
   - Menganalisis tipe pembayaran yang paling sering digunakan oleh pelanggan.
   - Memberikan rekomendasi untuk meningkatkan layanan transaksi, khususnya terkait dengan penggunaan kartu kredit.

## Library dan Data Wrangling

Proyek ini menggunakan beberapa library seperti pandas, matplotlib, seaborn, dan lainnya. Data awal diunduh dari [Brazilian E-Commerce Public Dataset on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) kemudian dilakukan beberapa proses seperti data wrangling untuk membersihkan data, menangani missing values, dan menggabungkan beberapa dataset yang saling berkaitan.

## Exploratory Data Analysis (EDA)

Pada tahap EDA, dilakukan analisis statistik dan visualisasi data untuk memahami pola, tren, dan wawasan yang dapat diperoleh dari dataset. Beberapa analisis mencakup:

- Segmentasi pasar berdasarkan wilayah geografis.
- Kategori barang yang paling sering dibeli.
- Jumlah pesanan per bulan dan tahun.
- Tipe pembayaran yang paling sering digunakan.

## Data Cleaning

Tahap data cleaning dilakukan untuk menangani missing values, kesalahan tipe data, dan data duplikat. Data yang telah dibersihkan kemudian digabungkan untuk memudahkan analisis lebih lanjut.

## Melakukan Merge Data

Data yang telah dibersihkan digabungkan untuk membentuk dataset yang lengkap.

## Visualisasi Data

Visualisasi data dilakukan untuk memberikan gambaran yang lebih jelas terkait pertanyaan bisnis yang diajukan. Beberapa visualisasi yang dilakukan antara lain:

- Segmentasi pasar berdasarkan kota.
- Penjualan pada kategori produk.
- Jumlah pesanan per bulan.
- Tipe pembayaran yang sering digunakan.

## Explanatory Analysis

### **Segmentasi Pasar Berdasarkan Wilayah Geografis:**
![Segmentasi-Pasar](https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/c6d130d9-2bbf-40e1-b98c-3952430146aa)

Berdasarkan hasil analisis, dapat disimpulkan bahwa Sao Paulo adalah kota dengan jumlah pelanggan terbanyak, diikuti oleh Rio de Janeiro dan Belo Horizonte. Untuk mengoptimalkan potensi pasar, disarankan untuk:

- Meningkatkan strategi pemasaran di wilayah-wilayah dengan pertumbuhan pelanggan yang potensial.
- Menyesuaikan stok produk dan layanan berdasarkan preferensi pelanggan di setiap wilayah.
- Membangun kemitraan lokal dan berkolaborasi dengan bisnis setempat untuk memperluas jangkauan.

### **Kategori Barang yang Paling Sering Dibeli dan Solusi terhadap Kategori Produk yang Paling Jarang Dibeli:**
![Penjualan-Kategori-Produk](https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/3edfe53c-1b49-46c4-b09b-321587542aa5)

Berdasarkan analisis, Bed, Bath, Table adalah kategori produk dengan penjualan tertinggi, sementara kategori Security and Service adalah yang paling sedikit dibeli. Solusi yang dapat diimplementasikan melibatkan:

- Peningkatan promosi dan pemasaran untuk produk kategori yang kurang diminati.
- Penawaran diskon atau bundel produk untuk meningkatkan daya tarik.
- Melakukan riset pasar lebih lanjut untuk memahami preferensi pelanggan di kategori tersebut.

### **Peningkatan Pembelian Tertinggi pada Bulan Tertentu:**
![Jumlah-Pesanan](https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/728d44a1-1e97-4129-804e-aedeabee7a3b)

Dari analisis, diketahui bahwa terjadi peningkatan pembelian tertinggi pada bulan November 2017. Faktor yang mungkin menyebabkan peningkatan ini antara lain:

- Penawaran promo khusus selama musim liburan atau peristiwa penjualan besar.
- Program loyalitas atau hadiah khusus untuk pelanggan selama periode tersebut.
- Keberhasilan kampanye pemasaran atau iklan yang diluncurkan pada bulan tersebut.

Berdasarkan informasi tersebut dapat dilakukan peningkatan promosi untuk produk-produk yang berkaitan dengan momen atau peristiwa tersebut. Hal ini dapat dilakukan dengan berbagai cara, seperti memasang iklan di media massa, mempromosikan produk melalui media sosial, atau mengadakan event khusus untuk mempromosikan produk.

### **Tipe Pembayaran yang Paling Sering Digunakan dan Peningkatan Layanan Transaksi:**
![Tipe-Pembayaran](https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/40532622-64f2-4e0f-89e4-4c8d55b3485f)

Dari hasil analisis, diketahui bahwa penggunaan kartu kredit mendominasi tipe pembayaran. Untuk meningkatkan layanan transaksi:

- Memperluas pilihan kartu kredit yang dapat diterima.
- Memudahkan proses otorisasi kartu kredit.
- Kolaborasi dengan mitra keuangan untuk memberikan insentif khusus bagi pengguna kartu kredit.

Hasil explanatory analysis ini memberikan pemahaman mendalam tentang perilaku pelanggan dan peluang pengembangan bisnis yang dapat dioptimalkan.

Proyek ini memberikan pandangan menyeluruh terhadap Brazilian E-Commerce Public Dataset dan memberikan dasar untuk pengambilan keputusan bisnis yang lebih baik. Seluruh kode dan analisis dapat ditemukan dalam file notebook [Analisis Data Brazilian E-Commerce Public Dataset.ipynb](https://colab.research.google.com/drive/1UHxlt5_OE1BSqRmJTsWcp9nVWyRI2G9T).


## Setup Environment Dashboard Analisis Data Brazilian E-Commerce
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```

## Menjalankan Dashboard Streamlit App
```
cd Dashboard
streamlit run DASHBOARD.py
```
