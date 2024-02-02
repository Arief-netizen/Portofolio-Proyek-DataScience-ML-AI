# Analisis Data Brazilian E-Commerce

Proyek ini bertujuan untuk menganalisis dataset [Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) hingga dilakukan deployment berbasis website menggunakan streamlit. Dataset ini mencakup berbagai informasi terkait transaksi e-commerce di Brazil, termasuk informasi pelanggan, produk, pesanan, pembayaran, dan lokasi geografis. Berikut adalah beberapa pertanyaan bisnis yang dijawab melalui analisis data:

1. **Segmentasi Pasar Berdasarkan Wilayah Geografis**: Analisis dilakukan untuk memahami distribusi pelanggan berdasarkan kota-kota di Brazil dan mengidentifikasi area dengan potensi pasar yang tinggi.

2. **Kategori Barang yang Paling Sering Dibeli**: Analisis difokuskan pada kategori produk yang paling sering dibeli oleh pelanggan, serta memberikan solusi terhadap kategori produk yang jarang dibeli.

3. **Tren Pembelian Berdasarkan Bulan**: Analisis dilakukan untuk mengidentifikasi bulan mana yang mengalami peningkatan pembelian tertinggi oleh pelanggan dan faktor-faktor apa yang mungkin mempengaruhi peningkatan tersebut.

4. **Preferensi Tipe Pembayaran Pelanggan**: Melalui analisis ini, dicari tahu tipe pembayaran apa yang paling sering atau disukai oleh pelanggan saat melakukan transaksi, serta bagaimana meningkatkan layanan pembayaran agar pelanggan merasa lebih nyaman.

Proyek ini melibatkan langkah-langkah seperti melakukan proses data wrangling untuk membersihkan dan mempersiapkan data, menjalankan Exploratory Data Analysis (EDA) untuk memahami pola-pola dalam dataset, dan menyajikan temuan melalui visualisasi data serta penjelasan terperinci.

Untuk informasi lebih lanjut, Anda dapat mengunjungi notebook Colab yang terlampir dalam proyek ini atau melihat dataset asli di [Kaggle Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

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
