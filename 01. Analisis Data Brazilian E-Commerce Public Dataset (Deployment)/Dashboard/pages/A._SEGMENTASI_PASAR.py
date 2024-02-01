import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title='Segmentasi Pasar', page_icon='images/favicon.ico')

# Membaca dataset
all_data = pd.read_csv('dataset/all_data.csv')

# Visualisasi segmentasi pasar tertinggi
most_customers = all_data.groupby(by='customer_city').agg({'customer_id': 'nunique'}).sort_values(by='customer_id', ascending=False)
most_customers = most_customers.reset_index()

st.header('**Segmentasi Pasar Berdasarkan Jumlah Pelanggan per Kota**')

sns.set(style='whitegrid', palette='pastel')

# Plot bar untuk analisis segmentasi pasar tertinggi
fig, ax = plt.subplots(figsize=(10, 6))
barplot = sns.barplot(x='customer_id', y='customer_city', 
                      data=most_customers.head(10), palette='viridis')

for p in barplot.patches:
    barplot.annotate(f'{p.get_width():.0f}', (p.get_width(), p.get_y() + p.get_height() / 2),
                     ha='left', va='center', color='black', fontsize=10, fontweight='bold')

# Menambahkan judul dan label sumbu
plt.title('Top 10 Segmentasi Pasar', fontsize=16, fontweight='bold')
plt.xlabel('Jumlah Pelanggan', fontsize=14, fontweight='bold')
plt.ylabel('Kota', fontsize=14, fontweight='bold')

# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)

st.header('**Explanatory Analysis**')
st.subheader('**Bagaimana segmentasi pasar berdasarkan wilayah geografis?**')
st.markdown('Berdasarkan hasil grafik Segmentasi Pelanggan, Sao Paulo adalah kota dengan jumlah pelanggan terbanyak, diikuti oleh Rio de Janeiro dan Belo Horizonte.')
st.markdown('Tingginya jumlah pelanggan di ketiga wilayah tersebut menunjukkan potensi yang besar untuk pengembangan bisnis atau peningkatan pelayanan. Hal ini dapat dilakukan dengan berbagai cara, seperti meningkatkan strategi promosi, pemasaran yang lebih intensif, atau menyediakan layanan khusus.')
st.markdown('Sedangkan wilayah lain dengan jumlah pelanggan yang masih sedikit dapat dilakukan peningkatan promosi di wilayah tersebut. Hal ini dapat dilakukan dengan memasang iklan di media massa lokal, mempromosikan produk melalui media sosial lokal, atau mengadakan event khusus di wilayah tersebut.')

st.caption('Copyright ©AriefBaihaqy 2023')