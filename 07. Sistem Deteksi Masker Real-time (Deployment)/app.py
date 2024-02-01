# Impor library
from flask import Flask, render_template, Response
import cv2
import pickle
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__, template_folder='Front-End', static_folder='Front-End')

# Mendefinisikan rute halaman website
@app.route('/')

@app.route('/Beranda')
def index():
    return render_template('index.html')

@app.route("/About")
def about():
    return render_template("about.html")

@app.route('/Deteksi-Masker')
def predict():
    return render_template('deteksi-masker.html')

# Memuat model yang telah dilakukan pelatihan
model = load_model('Notebook/training.h5')

# Membaca data kategorikal yang telah diubah menjadi label prediksi
with open('Notebook/label_prediksi.pkl', 'rb') as pf:
    label_prediksi = pickle.load(pf)
    
# Mengimpor Haar Cascade Classifier untuk mendeteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.samples.findFile(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'))

# Warna teks hasil prediksi dan teks akurasi    
colors = {0: (0, 0, 255), 1: (0, 255, 0), 2: (0, 255, 255)}

# Fungsi untuk menghasilkan frame berikutnya
def generate_frames():
    camera = cv2.VideoCapture(0)   # akses webcam camera
    while True:
        ret, frame = camera.read()
        if not ret:
            break

        # Melakukan deteksi wajah dalam frame dengan detektor wajah
        frame = cv2.flip(frame, 1)   # mirroring gambar
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in faces:
            
            # Preprocessing 
            roi = frame[y : y+h, x : x+w]   # memotong / cropping wajah dari frame menggunakan region of interest (ROI)
            img = cv2.resize(roi, (100, 100))   # resize gambar menjadi 100x100 piksel
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # mengubah warna ke RGB
            img = img / 255.   # normalisasi piksel gambar
            img = np.expand_dims(img, axis=0)   # memperluas dimensi gambar
            
            # Prediksi
            scores = model.predict(img)
            target = np.argmax(scores, axis=1)[0]
            
            # Membuat kotak pembatas dan hasil prediksi
            cv2.rectangle(img=frame, pt1=(x, y), pt2=(x+w, y+h), color=colors[target], thickness=4)
            
            # Untuk menampilkan teks hasil prediksi
            text = "{}".format(label_prediksi[target])
            text_width, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
            cv2.putText(frame, text, (x + (w - text_width) // 2, y-50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[target], 2)
            
            # Untuk menampilkan teks akurasi prediksi
            accuracy = scores[0][target] * 100
            text_accuracy = "Akurasi: {:.2f}%".format(accuracy)
            text_accuracy_width, _ = cv2.getTextSize(text_accuracy, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
            cv2.putText(frame, text_accuracy, (x + (w - text_accuracy_width) // 2, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[target], 2)

        # Mengubah frame menjadi format .jpg agar dapat dihasilkan dalam bentuk data bytes
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        # Menghasilkan frame sebagai output untuk dikirimkan sebagai respons streaming pada aplikasi Flask
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    camera.release()
    
# Menentukan rute yang akan menghasilkan stream video real time
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
