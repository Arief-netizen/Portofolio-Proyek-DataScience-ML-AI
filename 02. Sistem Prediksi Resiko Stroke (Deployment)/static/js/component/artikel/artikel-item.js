class ArtikelItem extends HTMLElement {
  set artikel(artikelItem) {
    this._artikel = artikelItem;
    this.render();
  }

  render() {
    this.innerHTML = `
        <div class="card item-artikel">
            <img
            style="height:250px"
            class="card-img-top"
            alt="gambar"
            src="${this._artikel.img_url}"
            />
            <div class="card-body">
            <p class="card-title" style="color: #0e0e0e">
            ${this._artikel.judul}
            </p>
            <p class="card-description">${this._artikel.tanggal_terbit}</p>
            <a style="text-decoration:none;"id="link-detail-artikel" href="/article_detail?judul=${this._artikel.judul}" style="text-align: end">Selengkapnya</a>
            </div>
        </div>`;
  }
}

customElements.define("artikel-item", ArtikelItem);
