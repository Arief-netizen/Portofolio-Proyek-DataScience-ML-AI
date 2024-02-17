# Sistem Deteksi Masker Real-time (Website Deployment)

## Deskripsi Proyek:

Proyek ini merupakan implementasi sistem deteksi masker pada gambar wajah manusia dengan menggunakan teknik Transfer Learning dari pre-trained model InceptionV3. Dataset yang digunakan adalah [Face Mask Detection](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection) yang berisi gambar-gambar wajah manusia dengan kategori menggunakan masker, salah menggunakan masker, dan tidak menggunakan masker. Proyek ini melibatkan tahap-tahap seperti memuat dataset, parsing anotasi, data preprocessing, pengembangan model menggunakan Transfer Learning, pelatihan model, evaluasi performa model, penyimpanan model untuk keperluan deployment, dan integrasi model ke website.

## Langkah-Langkah Proyek:

1. **Impor Library dan Dependencies:** Tahap awal melibatkan impor library yang dibutuhkan, seperti TensorFlow, OpenCV, dan sebagainya.

2. **Memuat Dataset dan Parsing Anotasi:** Dataset Face Mask Detection terdiri dari dua folder, yaitu "images" dan "annotations". Anotasi dalam format XML digunakan untuk mendapatkan informasi lokasi bounding box dan label kategori untuk setiap gambar.

3. **Data Preprocessing:** Melibatkan cropping dan resize gambar wajah berdasarkan bounding box, serta konversi label kategori menjadi representasi kategorikal. Pemetaan label kategori juga disimpan untuk keperluan prediksi setelah model dilatih.

4. **Model Development:** Memanfaatkan Transfer Learning dari pre-trained model InceptionV3 untuk mendeteksi masker. Menambahkan lapisan tambahan untuk menyesuaikan model dengan tugas deteksi masker. Melakukan kompilasi model dan pelatihan dengan data latih.

5. **Training Model:** Melibatkan normalisasi data dan pembagian dataset menjadi data latih dan data uji. Model dilatih menggunakan data latih untuk mengenali kategori masker pada gambar wajah.

6. **Evaluasi Model:** Menampilkan grafik accuracy dan loss selama pelatihan model. Model dievaluasi dengan data uji untuk mengukur performa.

7. **Penyimpanan Model:** Model yang telah dilatih dan pemetaan label kategori disimpan untuk tahap deployment.

8. **Deployment dan Prediksi Real-time:** Model dan pemetaan label kategori digunakan untuk membuat aplikasi website deteksi masker real-time. Pengguna dapat melakukan deteksi masker secara real-time, dan aplikasi dapat memberikan hasil deteksi masker pada wajah pengguna.

## Hasil Proyek:

<p align="center">
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/afc03673-6e15-49f3-8d1c-ce536e3c58d7" width="700">
  <img src="https://github.com/Arief-netizen/Portofolio-Proyek-DataScience-ML-AI/assets/56224972/558ca468-d03b-406e-b4c6-3a4fc258df4a" width="700">
</p>

Proyek ini menghasilkan sebuah sistem deteksi masker yang dapat digunakan untuk mendeteksi apakah seseorang menggunakan masker dengan benar, salah menggunakan masker, atau tidak menggunakan masker sama sekali. Model yang dikembangkan memiliki tingkat akurasi yang baik, yaitu sekitar 97% pada data validasi, dan loss pada data validasi sekitar 0.3.

Dengan demikian, meskipun proyek ini telah mencapai tingkat akurasi yang baik, penyempurnaan pada penanganan kondisi gelap dapat menjadi fokus untuk meningkatkan daya tanggap dan kehandalan sistem deteksi masker secara keseluruhan.  Penyempurnaan lebih lanjut dapat dilakukan dengan pemilihan dataset yang mencakup berbagai kondisi pencahayaan, termasuk kondisi gelap, dapat menjadi langkah yang lebih proaktif dalam melatih model agar lebih toleran terhadap variasi pencahayaan. Pengumpulan data tambahan yang mencakup situasi gelap atau kondisi pencahayaan yang ekstrem juga dapat memperkaya kapabilitas model deteksi masker ini.

### Setup Local

1. Buka folder project Sistem Deteksi Masker dengan text editor.

2. Buka terminal pada text editor dan install dependencies yang terletak di file requirements.txt dengan command:
    ```bash
    pip install -r requirements.txt
    ```

3. Lalu jalankan aplikasi pada terminal dengan command:
    ```bash
    flask run
    ```

4. Jalankan http://127.0.0.1:5000 pada browser.
