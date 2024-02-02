class ArtikelDetail extends HTMLElement {
  set artikel(artikel) {
    this._artikel = artikel;
    this.render();
  }

  render() {
    this.innerHTML = `
    <div class="section" id="#demo">
   
    <p class="artikel-title">
      ${this._artikel.judul}
    </p>
    <p class="artikel-subtitle">
      <i class="fa-solid fa-user" style="color: #041562"></i> ${
        this._artikel.penulis + ", " + this._artikel.tanggal_terbit
      }
    </p>
    <img
      src="${this._artikel.img_url}"
      alt="Gambar artikel"
      style="width: 100%;"
      
    />
    <p class="description">
      ${this._artikel.deskripsi}
    </p>
    <p class="description">
      Sumber :
      <a
        href="${this._artikel.sumber}"
        >${this._artikel.sumber}</a
      >
    </p>
    <p id="demo"></p>
  </div>
      `;
  }
}
customElements.define("artikel-detail", ArtikelDetail);
