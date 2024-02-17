<h1 align="center">Capstone Project SIB Dicoding - Sistem Prediksi Resiko Stroke</h1>
<p align="center"> 
   <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/8667243a-0651-4a81-a561-3a902c95c602" height="300">
</p>

### Anggota Tim
- Imam Arief Al Baihaqy (Machine Learning Developer)
- Rosyiidah Hasnaa (Front End Developer)
- Erin Nur Fatimah (Machine Learning Developer)
- Nikolas Edo (Front End Developer)

## Detail Proyek
**Learning Path:** Pengembang Machine Learning dan Front-End Web

**Tema yang dipilih:** Solusi Terkait Kesehatan dan Kesejahteraan Lingkungan

**Judul Proyek:** Sistem Prediksi Penyakit Stroke Berbasis Machine Learning

**Project Overview:** Project ini bertujuan untuk mengembangkan sebuah sistem prediksi resiko stroke menggunakan input data kesehatan dari pengguna. Sistem ini akan membantu dalam mengidentifikasi individu yang memiliki resiko tinggi terkena stroke, sehingga dapat dilakukan intervensi atau tindakan pencegahan yang tepat. Dataset yang digunakan yaitu [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset). Dataset ini berisi informasi tentang pasien, seperti jenis kelamin, usia, riwayat hipertensi, riwayat penyakit jantung, status perkawinan, jenis pekerjaan, lingkungan tempat tinggal, kadar glukosa darah rata-rata, indeks massa tubuh (BMI), status merokok, dan keterangan stroke.

## Proses yang Dilakukan:

1. **Data Loading:** Melakukan impor library dan memuat Stroke Prediction Dataset .

2. **EDA - Deskripsi Variabel:** Melakukan deskripsi variabel untuk memahami atribut-atribut pada dataset.

3. **EDA - Menangani Missing Value dan Outliers:** Menangani missing value pada fitur BMI dengan mengganti nilai NaN dengan nilai rata-rata BMI. Kemudian, menangani outliers pada fitur BMI dengan menggunakan metode IQR.

4. **EDA - Univariate Analysis:** Melakukan analisis terhadap masing-masing fitur kategori dan numerik pada dataset untuk memahami distribusi data.

5. **EDA - Multivariate Analysis:** Melakukan analisis terhadap hubungan antar fitur pada dataset.

6. **Data Preparation:** Menghapus fitur 'id' yang tidak diperlukan, menghapus sampel 'Other' pada fitur 'gender', encoding fitur kategori menjadi numerik, menangani ketidakseimbangan data pada fitur target 'stroke' menggunakan SMOTE, serta melakukan pembagian dataset menjadi data latih dan data uji.

7. **Standarisasi:** Melakukan standarisasi fitur-fitur numerik menggunakan StandardScaler.

8. **Model Development:** Mengembangkan model Machine Learning menggunakan 3 algoritma, yaitu K-Nearest Neighbor, Decision Tree, dan Random Forest. Evaluasi performa model menggunakan F1 score.

9. **Evaluasi Model:** Memilih algoritma dengan performa terbaik berdasarkan F1 score pada data uji.

10. **Menyimpan Model:** Menyimpan model terbaik, yaitu Random Forest, dalam format pickle untuk digunakan dalam proses website deployment.

## Hasil Proyek:

- Halaman Cek Kesehatan
<p align="center">
   <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/f9af3903-8499-45a7-8d35-d774668fa609" height="778")>
</p>

- Hasil Cek Kesehatan
<p align="center">
   <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/f3567921-f9ff-4433-925d-bc1cf6c0d80c" height="750")>
</p>

- Metrik Evaluasi F1 Score
<p align="center">
   <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/277b497b-eb9b-4481-972e-9904ace046c4" height="300")>
</p>

Proyek ini berhasil mengembangkan sistem prediksi resiko stroke dengan menggunakan Random Forest sebagai model utama. Model ini memiliki akurasi yang baik dalam memprediksi resiko stroke berdasarkan data kesehatan pasien, dengan akurasi pada data latih sebesar 99%, dan data uji sebesar 96%.

|                    | train	  | test     |
|--------------------|----------|----------|
| K-Nearest Neighbor | 0.983539 | 0.951646 |
| Decision Tree      | 0.982253 | 0.928498 |
| Random Forest      | 0.999871 | 0.963477 |

### Setup Local

1. Buka folder proyek Sistem Prediksi Resiko Stroke dengan text editor.

2. Buka terminal pada text editor dan install dependencies yang terletak di file requirements.txt dengan command:
    ```bash
    pip install -r requirements.txt
    ```

3. Lalu jalankan aplikasi pada terminal dengan command:
    ```bash
    flask run
    ```

4. Jalankan http://127.0.0.1:5000 pada browser.
