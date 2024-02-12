import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title='Tipe Pembayaran', page_icon='images/favicon.ico')

# Membaca dataset
all_data = pd.read_csv('dataset/all_data.csv')

st.header('**Frekuensi Tipe Pembayaran**')

# Melakukan visualisasi tipe pembayaran yang sering dilakukan
sns.set(style='whitegrid', palette='muted')

plt.figure(figsize=(10, 6))
barplot = sns.barplot(x=all_data['payment_type'].value_counts().index,
                      y=all_data['payment_type'].value_counts(),
                      palette='viridis')

for p in barplot.patches:
    barplot.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='center', xytext=(0, 10), textcoords='offset points',
                     fontsize=10, color='black', fontweight='bold')

plt.title('Frekuensi Tipe Pembayaran', fontsize=16, fontweight='bold')
plt.xlabel('Tipe Pembayaran', fontsize=14, fontweight='bold')
plt.ylabel('Jumlah Penggunaan', fontsize=14, fontweight='bold')

st.pyplot(plt)

st.header('**Explanatory Analysis**')
st.subheader('**Tipe pembayaran apa yang paling sering atau disukai oleh pelanggan saat melakukan transaksi dan bagaimana peningkatan layanan tersebut agar pelanggan lebih nyaman dalam melakukan transaksi?**')
st.markdown('Dari informasi yang didapatkan pada grafik Tipe Pembayaran, terlihat bahwa penggunaan kartu kredit sebagai metode pembayaran mendominasi. Oleh karena itu, penyediaan fasilitas yang memudahkan pembayaran dengan kartu kredit dapat ditingkatkan, seperti:')
st.markdown('''
            - Menawarkan berbagai pilihan kartu kredit yang dapat diterima, termasuk kartu kredit dari berbagai bank dan lembaga keuangan.
            - Mempermudah proses otorisasi kartu kredit.
            - Perusahaan dapat bekerja sama dengan berbagai bank dan lembaga keuangan untuk memberikan diskon atau promo khusus bagi pelanggan yang menggunakan kartu kredit dari mitra tersebut.
            ''')

st.caption('Copyright ©AriefBaihaqy 2023')