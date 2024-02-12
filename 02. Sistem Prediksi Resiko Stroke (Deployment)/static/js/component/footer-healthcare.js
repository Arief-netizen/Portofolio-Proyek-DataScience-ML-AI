class FooterHealthcare extends HTMLElement {
  connectedCallback() {
    this.render();
  }
  render() {
    this.innerHTML = `
    <div class="inner-footer">
    <div class="d-md-flex flex-md-row text-white">
      <div class="sub-section-footer">
        <span class="logo-white">Healthcare</span>
        <p class="pb-3 pt-2"><i class="fa-sharp fa-solid fa-location-dot"></i> Surabaya, Indonesia</p>
      </div>
      <div class="sub-section-footer" >
        <p class="pb-2 pt-2" style="font-weight: 700">LAYANAN KAMI</p>
        <p class="pb-2"><a style="text-decoration:none;"class="text-white"href="/">Beranda</a></p>
        <p class="pb-2"><a style="text-decoration:none;"class="text-white"href="/predict">Cek Kesehatan</a></p>
        <p class="pb-2"><a style="text-decoration:none;"class="text-white"href="/article">Artikel Kesehatan</a></p>
        <p class="pb-2"><a style="text-decoration:none;"class="text-white"href="/about">Tentang Kami</a></p>
      </div>
      <div class="sub-section-footer" >
        <p class="pb-2 pt-2" style="font-weight: 700">HUBUNGI KAMI</p>
        <p class="pb-2"><a style="text-decoration:none;" class="text-white"href="mailto:ariefbaihaqy.19006@gmail.com"> Imam Arief Al Baihaqy</a></p>
        <p class="pb-2"><a style="text-decoration:none;" class="text-white"href="mailto:syiidahasnaa30@gmail.com"> Rosyiidah Hasnaa</a></p>
        <p class="pb-2"><a style="text-decoration:none;" class="text-white"href="mailto:newtsnew@gmail.com"> Nikolas Edo</a></p>
        <p class="pb-2"><a style="text-decoration:none;" class="text-white"href="mailto:erinnurfa52@gmail.com"> Erin Nur Fatimah</a></p>
      </div>
    </div>
    </div>
    
    <hr>
    <p class="text-white text-center pt-3">Copyright &#169; 2023 - Healthcare. All Right Reserved</p>
      `;
  }
}
customElements.define("footer-healthcare", FooterHealthcare);
