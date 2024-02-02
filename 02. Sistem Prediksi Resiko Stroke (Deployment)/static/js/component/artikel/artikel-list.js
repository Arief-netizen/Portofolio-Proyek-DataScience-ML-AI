// import "./artikel-item.js";

class ArtikelList extends HTMLElement {
  set artikels(artikelData) {
    this._artikel_list = artikelData;
    this.render();
  }
  render() {
    this.innerHTML = "";
    this._artikel_list.forEach((artikel) => {
      const artikelItemElement = document.createElement("artikel-item");
      artikelItemElement.artikel = artikel;
      artikelItemElement.className = "col-lg-3 col-md-6 col-sm-12 mb-4";
      this.appendChild(artikelItemElement);
    });
  }
}
customElements.define("artikel-list", ArtikelList);
