import streamlit as st

# Menetapkan konfigurasi halaman
st.set_page_config(page_title='Data Analysis', page_icon='images/favicon.ico')

st.header('**Project Details**')
st.subheader('**Analisis Data Brazilian E-Commerce Public Dataset**')
st.markdown('Dataset: [kaggle.com/BrazilianE-CommercePublicDataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)')
st.image('images/BrazilianEcommerce.png')
st.markdown('Brazilian E-Commerce Public Dataset berisi informasi 100 ribu pesanan dari tahun 2016 hingga 2018 yang dilakukan diberbagai pasar di Brazil. Berbagai fitur memungkinkan untuk melihat suatu pesanan dari berbagai sektor: mulai dari status pesanan, harga, pembayaran, kinerja pengiriman hingga lokasi pelanggan, atribut produk, dan ulasan dari pelanggan.')

st.subheader('Pertanyaan Bisnis')

st.markdown('<style>a { text-decoration: none; }</style>', unsafe_allow_html=True)

st.markdown('1. Bagaimana segmentasi pasar berdasarkan wilayah geografis? [**(HASIL)**](http://localhost:8501/A._SEGMENTASI_PASAR)')
st.markdown('2. Kategori barang apa\nyang paling sering dibeli oleh pelanggan, dan bagaimana solusi terhadap kategori produk yang paling jarang dibeli? [**(HASIL)**](http://localhost:8501/B._KATEGORI_PRODUK)')
st.markdown('3. Pada bulan apa terjadi peningkatan pembelian tertinggi oleh pelanggan dan apa yang mungkin menyebabkan hal itu dapat terjadi? [**(HASIL)**](http://localhost:8501/C._JUMLAH_PESANAN)')
st.markdown('4. Tipe pembayaran apa yang paling sering atau disukai oleh pelanggan saat melakukan transaksi dan bagaimana peningkatan layanan tersebut agar pelanggan lebih nyaman dalam melakukan transaksi? [**(HASIL)**](http://localhost:8501/D._TIPE_PEMBAYARAN)')
st.markdown('Tautan Proyek Analisis Data: [Klik disini!](https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/blob/41de63bd8189edbac38d8e98836b8f469e856d00/01.%20Analisis%20Data%20Brazilian%20E-Commerce%20Public%20Dataset%20(Deployment)/Notebook/Analisis%20Data%20Brazilian%20E-Commerce%20Public%20Dataset.ipynb)')

st.caption('Copyright ©AriefBaihaqy 2023')
