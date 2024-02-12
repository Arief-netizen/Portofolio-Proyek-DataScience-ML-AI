import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title='Jumlah Pesanan', page_icon='images/favicon.ico')

# Membaca dataset
all_data = pd.read_csv('dataset/all_data.csv')

all_data['order_purchase_timestamp'] = pd.to_datetime(all_data['order_purchase_timestamp'])

# Membuat kolom 'month' dan 'year' yang berisi informasi bulan dan tahun dari setiap tanggal pembelian
all_data['month'] = all_data['order_purchase_timestamp'].dt.to_period('M')
all_data['year'] = all_data['order_purchase_timestamp'].dt.year

# Mengelompokkan DataFrame berdasarkan kolom 'month' dan 'year'
all_data_date = all_data.groupby(by=['month', 'year']).order_id.nunique().reset_index()

st.header('**Jumlah Pesanan Per Bulan**')

# Melakukan visualisasi jumlah pesanan per bulan
all_data_date['formatted_month'] = all_data_date['month'].dt.strftime('%b-%Y')   # mengubah format bulan

fig, ax = plt.subplots(figsize=(10, 6))
all_data_date.plot(kind='bar', x='formatted_month', y='order_id', legend=False, color='#87CEFA', edgecolor='black', ax=ax)

plt.title('Jumlah Pesanan per Bulan', fontsize=16, fontweight='bold')
plt.xlabel('Bulan', fontsize=14, fontweight='bold')
plt.ylabel('Jumlah Pesanan', fontsize=14, fontweight='bold')

for index, value in enumerate(all_data_date['order_id']):
    plt.text(index, value + 0.1, str(value), ha='center', va='bottom', fontsize=9)

st.pyplot(fig)

st.header('**Explanatory Analysis**')
st.subheader('**Pada bulan apa terjadi peningkatan pembelian tertinggi oleh pelanggan dan apa yang mungkin menyebabkan hal itu dapat terjadi?**')
st.markdown('Berdasarkan hasil grafik Jumlah Pesanan per Bulan, diketahui pembelian terbanyak terjadi pada tanggal 24 November 2017. Hal ini menunjukkan bahwa ada suatu momen atau peristiwa yang menyebabkan peningkatan penjualan pada periode tersebut.')
st.markdown('Berdasarkan informasi tersebut dapat dilakukan peningkatan promosi untuk produk-produk yang berkaitan dengan momen atau peristiwa tersebut. Hal ini dapat dilakukan dengan berbagai cara, seperti memasang iklan di media massa, mempromosikan produk melalui media sosial, atau mengadakan event khusus untuk mempromosikan produk.')

st.caption('Copyright ©AriefBaihaqy 2023')