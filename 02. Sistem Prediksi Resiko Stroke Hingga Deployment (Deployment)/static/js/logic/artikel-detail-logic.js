// import artikelData from "../component/artikel/artikel-data.js";
src="{{ url_for('static', filename='js/component/artikel/artikel-data.js') }}"
const renderDetailArtikel = (artikelItem) => {
  const artikelDetail = document.querySelector("artikel-detail");
  artikelDetail.artikel = artikelItem;
};
const searchArtikelByTitle = (title) => {
  let selected = {};
  for (let artikel of artikelData) {
    if (artikel.judul.toLocaleLowerCase() == title.toLocaleLowerCase()) {
      selected = artikel;
    }
  }
  return selected;
};

document.addEventListener("DOMContentLoaded", (e) => {
  let param = window.location.search.split("=");
  let title = param[1].replaceAll("%20", " ");
  console.log("title = " + title);
  console.log(searchArtikelByTitle(title));

  renderDetailArtikel(searchArtikelByTitle(title));
});
