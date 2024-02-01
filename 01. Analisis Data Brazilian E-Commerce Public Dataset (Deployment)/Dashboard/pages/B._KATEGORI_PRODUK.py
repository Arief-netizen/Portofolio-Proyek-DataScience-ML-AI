import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.set_page_config(page_title='Kategori Produk', page_icon='images/favicon.ico')

# Membaca dataset
all_data = pd.read_csv('dataset/all_data.csv')

# Menampilkan jumlah penjualan per kategori produk
category = (all_data.groupby(by='product_category_name_english_x')['product_id']
               .count()
               .reset_index()
               .rename(columns={'product_category_name_english_x': 'category', 'product_id': 'orders'}))

# Melakukan visualisasi penjualan kategori produk tertinggi dan terendah
category_sorted = category.sort_values(by='orders', ascending=False)

st.header('**Penjualan Teratas dan Terendah Berdasarkan Kategori Produk**')

# Memilih 5 kategori produk teratas dan terbawah
top_categories = category_sorted.head(5)
bottom_categories = category_sorted.tail(5)
sns.set(style='whitegrid', palette='pastel')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6.5))

# Plot kategori penjualan teratas
sns.barplot(x='orders', y='category', data=top_categories, 
            ax=ax1, palette='viridis')
ax1.set_title('Top 5 Kategori Produk dengan Penjualan Tertinggi', fontsize=14, fontweight='bold')
ax1.set_xlabel('Jumlah Penjualan', fontsize=12, fontweight='bold')
ax1.set_ylabel('Kategori', fontsize=12, fontweight='bold')
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Plot kategori penjualan terendah
sns.barplot(x='orders', y='category', data=bottom_categories, ax=ax2, 
            order=bottom_categories['category'][::-1], palette='viridis')
ax2.set_title('Top 5 Kategori Produk dengan Penjualan Terendah', fontsize=14, fontweight='bold')
ax2.set_xlabel('Jumlah Penjualan', fontsize=12, fontweight='bold')
ax2.set_ylabel('Kategori', fontsize=12, fontweight='bold')
ax2.grid(axis='x', linestyle='--', alpha=0.7)

for ax in [ax1, ax2]:
    for p in ax.patches:
        ax.annotate(f'{p.get_width():.0f}', (p.get_width(), p.get_y() + p.get_height() / 2),
                    ha='left', va='center', color='black', fontsize=10, fontweight='bold')

plt.subplots_adjust(hspace=0.6)

st.pyplot(fig)

st.header('**Explanatory Analysis**')
st.subheader('**Kategori barang apa yang paling sering dibeli oleh pelanggan, dan bagaimana solusi terhadap kategori produk yang paling jarang dibeli?**')
st.markdown('Berdasarkan visualisasi grafik diatas, dapat diketahui bahwa Bed, Bath, Table merupakan kategori produk yang paling banyak dibeli, sedangkan kategori produk Security and Service adalah kategori yang paling sedikit dibeli. Hal ini menunjukkan bahwa pelanggan lebih tertarik untuk membeli produk-produk yang berkaitan dengan kebutuhan sehari-hari, seperti perlengkapan tidur, perlengkapan mandi, dan perlengkapan rumah tangga.')
st.markdown('Berdasarkan informasi ini, solusi yang dapat dilakukan adalah:')
st.markdown('''
            - Meningkatkan promosi untuk produk-produk di kategori Security and Services. Hal ini dapat dilakukan dengan berbagai cara, seperti memasang iklan di media massa, mempromosikan produk melalui media sosial, atau mengadakan event khusus untuk mempromosikan produk.
            - Melakukan riset pasar untuk mengetahui kebutuhan pelanggan di kategori Security and Services. Hal ini dapat dilakukan dengan melakukan survei kepada pelanggan, mengadakan focus group discussion, atau menganalisis data penjualan.
            - Menawarkan produk-produk di kategori Security and Services dengan harga yang lebih kompetitif. Hal ini dapat menarik minat pelanggan untuk membeli produk-produk di kategori tersebut.
            ''')

st.caption('Copyright ©AriefBaihaqy 2023')