// import artikelData from "../component/artikel/artikel-data.js";

const searchArtikelByKeyword = (keyword) => {
  let filtered = [];
  for (let artikel of artikelData) {
    if (
      artikel.judul.toLocaleLowerCase().includes(keyword.toLocaleLowerCase())
    ) {
      filtered.push(artikel);
    }
  }
  return filtered;
};
const renderArtikel = (allArtikel) => {
  const artikelList = document.querySelector("artikel-list");
  artikelList.artikels = allArtikel;
  console.log(artikelList.artikels);
};
const showResponseMessage = (message = "Data gagal dimuat") => {
  alert(message);
};

const searchInput = document.getElementById("search-keyword");
const searchButton = document.getElementById("searchArtikelButton");

document.addEventListener("DOMContentLoaded", () => {
  if (searchInput.value == "" || searchInput == null) {
    renderArtikel(artikelData);
  }

  searchButton.addEventListener("click", (e) => {
    const keyword = searchInput.value;
    if (keyword != "") {
      const selectedArtikel = searchArtikelByKeyword(keyword);
      if (selectedArtikel.length < 1) {
        showResponseMessage("Data tidak ditemukan");
      } else {
        renderArtikel(selectedArtikel);
      }
    } else if (keyword === "") {
      renderArtikel(artikelData);
    }
    e.preventDefault();
  });

  console.log(artikelData);
});
