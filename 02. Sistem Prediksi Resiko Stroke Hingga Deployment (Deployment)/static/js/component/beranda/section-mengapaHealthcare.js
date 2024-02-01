class SectionMengapaHealthcare extends HTMLElement {
  connectedCallback() {
    this.render();
  }
  render() {
    this.innerHTML = `
      <div class="section">
        <div class="d-lg-flex flex-lg-row">
          <div class="sub-section mt-5">
            <span class="" id="subtitle">Mengapa Helathcare Hadir?</span>
            <p class="description">
              Serangan stroke menjadi nomor dua dalam penyakit pembunuh menurut
              WHO pada tahun 2021. Data statistik menunjukkan bahwa satu dari
              empat orang dewasa mengalami serangan ini. Hal ini disebabkan oleh
              beberapa penyakit bawaan seperti riwayat tekanan darah tinggi,
              kolesterol, obesitas, dan riwayat bawaan stroke pada keluarga
              penderita. Oleh karena itu, health care hadir sebagai solusi.
            </p>
          </div>
          <div class="sub-section" style="text-align: center">
            <img src="./static/img/vector2.png" alt="gambar1" />
          </div>
        </div>
      </div>
    `;
  }
}
customElements.define("section-mengapahealthcare", SectionMengapaHealthcare);
