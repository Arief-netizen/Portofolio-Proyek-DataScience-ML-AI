class AppBar extends HTMLElement {
  connectedCallback() {
    this.render();
  }
  render() {
    this.innerHTML = `
    <nav class="navbar navbar-expand-lg sticky-top navbar-light" id="navbar">
      <span class="navbar-brand nav-logo" style="color: #041562" 
        >Healthcare</span
      >
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#collapsibleNavbar"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="collapsibleNavbar" >
        <ul class="navbar-nav"  style="text-align:right">
          <li class="nav-item">
            <a
              id="nav-beranda"
              class="nav-link active"
              href="/"
              >Beranda</a
            >
          </li>
          <li class="nav-item">
            <a
              href="/predict"
              id="nav-input"
              class="nav-link active"
              
              >Cek Kesehatan</a
            >
          </li>
          <li class="nav-item">
            <a
              id="nav-artikel"
              class="nav-link active"
              
              href="/article"
              >Artikel Kesehatan</a
            >
          </li>
          <li class="nav-item">
            <a
              id="nav-tentang-kami"
              class="nav-link active"
              href="/about"
              >Tentang Kami</a
            >
          </li>
        </ul>
      </div>
    </nav>`;
  }
}
customElements.define("app-bar", AppBar);
