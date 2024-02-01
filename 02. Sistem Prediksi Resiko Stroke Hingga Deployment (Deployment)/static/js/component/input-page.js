class InputPage extends HTMLElement {
  connectedCallback() {
    this.render();
  }
  render() {
    this.innerHTML = `
    <div class="section" style="text-align: center">
    <img 
      class="rounded-circle img-input-page"
      src="./static/img/icon_layanan_cek_kesehatan.png"
    />
    <p id="subtitle">Cek Kesehatanmu</p>
    <p class="subtitle-description">
      Diagnosa sekarang, dan hindari risikonya
    </p>
    <form
      id = "formCekKesehatan"
      method="post"
      action="/result"
      class="mt-5"
      style="text-align: start"
      
      
    >
      <div class="row">
        <div class="col-lg-6 col-md-12 col-sm-12">
          <div class="form-group">
            <label for="gender">Apa jenis kelamin anda?</label>
            <select class="form-control" id="gender" name="gender" required>
              <option value="1">Laki-laki</option>
              <option value="0">Perempuan</option>
            </select>
          </div>
          <div class="form-group">
            <label for="age">Berapa usia anda saat ini?</label>
            <input
              type="number"
              class="form-control"
              id="age"
              placeholder="Masukkan usia anda saat ini"
              name="age"
              required
            />
          </div>
          <div class="form-group">
            <label for="age"
              >Apakah anda memiliki riwayat tekanan darah tinggi?</label
            >
            <select
              class="form-control"
              id="hypertension"
              name="hypertension"
              required
            >
              <option value="1">Ya</option>
              <option value="0">Tidak</option>
            </select>
          </div>
          <div class="form-group">
            <label for="age"
              >Apakah anda memiliki riwayat penyakit jantung?</label
            >
            <select
              class="form-control"
              id="heart_disease"
              name="heart_disease"
              required
            >
              <option value="1">Ya</option>
              <option value="0">Tidak</option>
            </select>
          </div>
          <div class="form-group">
            <label for="age">Apakah anda sudah menikah?</label>
            <select
              class="form-control"
              id="ever_married"
              name="ever_married"
              required
            >
              <option value="1">Sudah</option>
              <option value="0">Belum</option>
            </select>
          </div>
        </div>
        <div class="col-lg-6 col-md-12 col-sm-12">
          <div class="form-group">
            <label>Apa pekerjaan anda saat ini?</label>
            <select class="form-control" id="work_type" name="work_type" required>
              <option value="0">PNS</option>
              <option value="2">Swasta</option>
              <option value="3">Wiraswasta</option>
              <option value="1">Tidak Bekerja</option>
              <option value="4">Pelajar</option>
            </select>
          </div>
          <div class="form-group">
            <label>Pada lingkungan mana anda tinggal?</label>
            <select
              class="form-control"
              id="Residence_type"
              name="Residence_type"
              required
            >
              <option value="0">Pedesaan</option>
              <option value="1">Perkotaan</option>
            </select>
          </div>
          <div class="form-group">
            <label for="avg_glucose_level"
              >Berapa rata-rata kadar glukosa dalam darah anda?</label
            >
            <input
              type="number"
              step="0.01"
              class="form-control"
              id="avg_glucose_level"
              placeholder="Masukkan kadar glukosa dalam darah anda"
              name="avg_glucose_level"
              required
            />
          </div>
          <div class="form-group">
            <label for="avg_glucose_level"
              >Berapa massa indeks tubuh anda?</label
            >
            <input
              type="number"
              step="0.01"
              class="form-control"
              id="bmi"
              placeholder="Masukkan massa indeks tubuh anda"
              name="bmi"
              required
            />
          </div>
          <div class="form-group">
            <label>Apakah anda seorang perokok?</label>
            <select
              class="form-control"
              id="smoking_status"
              name="smoking_status"
              required
            >
              <option value="3">Aktif Merokok</option>
              <option value="1">Pernah Merokok (sudah berhenti)</option>
              <option value="2">Tidak Pernah Merokok</option>
            </select>
          </div>
        </div>
      </div>
      <button id="cekKesehatanSubmit" type="submit" class="mt-3" style="width: 100%">Kirim</button>
    </form>
  </div>

        `;
  }
}
customElements.define("input-page", InputPage);
