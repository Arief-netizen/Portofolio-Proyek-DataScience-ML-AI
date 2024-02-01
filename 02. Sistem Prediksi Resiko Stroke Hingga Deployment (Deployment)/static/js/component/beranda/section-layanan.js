class SectionLayanan extends HTMLElement {
  connectedCallback() {
    this.render();
  }
  render() {
    this.innerHTML = ` 
      <div class="section layanan">
        <div class="d-lg-flex flex-lg-row">
          <div class="sub-section">
            <img src="./static/img/vector3.png" alt="gambar1" />
          </div>
          <div class="sub-section" style="text-align: center">
            <span id="subtitle">Layanan Kami</span>
            <div class="row">
              <div class="col-lg-6 col-md-6 col-sm-12 mt-3 mb-3">
                <div class="card item-layanan">
                  <div class="card-body">
                    <img
                      class="card-img rounded-circle"
                      alt="gambar"
                      src="./static/img/icon_layanan_cek_kesehatan.png"
                    />
                    <p class="card-title">Cek Kesehatan</p>
                    <p class="card-description">
                      Cek kesehatan akan membantu anda untuk mengetahui bagaimana tingkat
                      kemungkinan anda terserang penyakit stroke.
                    </p>
                    <a style="text-decoration:none;" class="text-white" href="/predict"><button class="card-button">Mulai Cek</button></a>
                  </div>
                </div>
              </div>
              <div class="col-lg-6 col-md-6 col-sm-12 mt-3 mb-3">
                <div class="card item-layanan">
                  <div class="card-body">
                    <img
                      class="card-img rounded-circle"
                      alt="gambar"
                      src="./static/img/article_icon.jpg"
                    />
                    <p class="card-title">Artikel Kesehatan</p>
                    <p class="card-description">
                      Artikel kesehatan akan dapat membantu anda untuk mendapatkan informasi
                      seputar stroke dan informasi kesehatan lainnya.
                    </p>
                    <a style="text-decoration:none;" class="text-white" href="/article"><button class="card-button">Baca Artikel</button></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
  }
}
customElements.define("section-layanan", SectionLayanan);
