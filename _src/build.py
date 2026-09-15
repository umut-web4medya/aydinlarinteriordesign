#!/usr/bin/env python3
"""
Aydınlar Interior Design — site derleyicisi.

    python3 _src/build.py

Üst bar, alt bilgi ve <head> tek yerde durur; sayfalar buradan üretilir.
⛔ Üretilen .html dosyalarını ELLE DÜZENLEME — bir sonraki derlemede silinir.
Görünen metinler için _src/icerik.md dosyasına bak.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "Aydınlar Interior Design"
FIRMA = "Aydınlar Premium Group İnşaat Ltd. Şti."
TEL_HREF = "+905320597461"
TEL_YAZI = "0532 059 74 61"
IG = "https://www.instagram.com/aydinlar.interior.design/"
YIL = "2026"

NAV = [
    ("",           "Anasayfa"),
    ("hizmetler",  "Hizmetler"),
    ("projeler",   "Projeler"),
    ("hakkimizda", "Hakkımızda"),
    ("iletisim",   "İletişim"),
]


def head(up, title, desc, extra_css=""):
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{up}images/favicon.ico" sizes="48x48">
<link rel="icon" href="{up}images/favicon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="{up}images/favicon-192.png">
<meta property="og:title" content="{title}">
<meta property="og:type" content="website">
<meta property="og:locale" content="tr_TR">
<link rel="stylesheet" href="{up}assets/site.css">{extra_css}
</head>
<body>"""


def header(up, current):
    items = []
    for slug, label in NAV:
        href = (up or "./") if slug == "" else f"{up}{slug}/"
        cls = ' class="is-current"' if slug == current else ""
        items.append(f'    <li{cls}><a href="{href}">{label}</a></li>')
    return f"""
<header class="site-head">
  <a class="brand" href="{up or "./"}" aria-label="{SITE} — ana sayfa">
    <img class="brand-logo" src="{up}images/aydinlar-logo-white.png" width="360" height="184"
         alt="{SITE} logosu" decoding="async">
    <span>
      <span class="brand-name">Aydınlar</span>
      <span class="brand-sub">Interior Design</span>
    </span>
  </a>
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="Menüyü aç"><i></i></button>
  <ul class="nav" id="nav">
{chr(10).join(items)}
  </ul>
  <a class="head-cta" href="tel:{TEL_HREF}">{TEL_YAZI}</a>
</header>
"""


def footer(up):
    links = "".join(
        f'<li><a href="{(up or "./") if s == "" else f"{up}{s}/"}">{l}</a></li>'
        for s, l in NAV
    )
    return f"""
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h4>Aydınlar Interior Design</h4>
        <p>{FIRMA}<br>Tüm Türkiye Mimari Konsept Mağaza<br>Anahtar Teslim Proje</p>
      </div>
      <div>
        <h4>Sayfalar</h4>
        <ul>{links}</ul>
      </div>
      <div>
        <h4>İletişim</h4>
        <ul>
          <li><a href="tel:{TEL_HREF}">Proje Yetkilisi · {TEL_YAZI}</a></li>
          <li><a href="{IG}" target="_blank" rel="noopener">Instagram</a></li>
        </ul>
      </div>
    </div>
    <p class="foot-bottom">© {FIRMA} {YIL}</p>
  </div>
</footer>
"""


def page_head(kicker, h1, lede=""):
    lede_html = f'\n      <p class="lede">{lede}</p>' if lede else ""
    return f"""  <div class="page-head">
    <div class="wrap">
      <p class="kicker">{kicker}</p>
      <h1>{h1}</h1>{lede_html}
    </div>
  </div>
"""


# ---------------------------------------------------------------- sayfalar
def sayfa_anasayfa():
    hero = (ROOT / "_src" / "_hero.html").read_text(encoding="utf-8")
    return (
        head("", f"{SITE} — Mimari Konsept Mağaza ve Anahtar Teslim Proje",
             f"{FIRMA} — Tüm Türkiye mimari konsept mağaza, anahtar teslim proje; "
             "tasarım, üretim ve uygulama.")
        + header("", "")
        + "\n<main>\n" + hero + "\n</main>\n"
        + '\n<script src="assets/nav.js"></script>\n<script src="assets/deck.js"></script>\n'
        + "</body>\n</html>\n"
    )


def sayfa_hizmetler():
    body = page_head(
        "Hizmetler", "Mimari Konsept Mağaza",
        "Markanın kimliğini mağaza içinde kuran, tasarımdan üretime ve sahadaki "
        "uygulamaya kadar tek elden yürüyen bir hizmet."
    ) + f"""
  <div class="wrap">
    <section class="section">
      <h2 class="section-title">Ne Yapıyoruz</h2>
      <div class="svc-grid">
        <article class="svc">
          <span class="svc-mark"></span>
          <h3>Mimari Konsept Mağaza</h3>
          <p>PLACEHOLDER — markanın mağaza konseptini nasıl kurguladığınızı anlatan metin.</p>
        </article>
        <article class="svc">
          <span class="svc-mark"></span>
          <h3>Anahtar Teslim Proje</h3>
          <p>Hayalinizdeki perde ve halı mağazasını, anahtar teslim şekilde kuruyoruz.</p>
        </article>
        <article class="svc">
          <span class="svc-mark"></span>
          <h3>Tasarım · Üretim · Uygulama</h3>
          <p>PLACEHOLDER — kendi üretiminizi ve sahadaki uygulama ekibinizi anlatan metin.</p>
        </article>
      </div>
    </section>

    <section class="section">
      <div class="offer">
        <h2>Mağaza Kurmak Artık Çok Kolay</h2>
        <p>Hayalinizdeki perde ve halı mağazasını, anahtar teslim şekilde kuruyoruz.</p>
        <ul class="check-list">
          <li>Uygun fiyat</li>
          <li>Güvenilir hizmet</li>
          <li>Modern tasarım showroomlar</li>
          <li class="is-highlight">%30 peşin, 12 ay taksit imkânı</li>
        </ul>
        <p class="panel-close">Siz sadece hayal edin, gerisini profesyonel ekibimiz halletsin.</p>
        <a class="panel-link" href="tel:{TEL_HREF}">Proje Yetkilisi · {TEL_YAZI}</a>
      </div>
    </section>

    <section class="section">
      <h2 class="section-title">Süreç</h2>
      <ol class="steps">
        <li>
          <h3>Tasarım</h3>
          <p>PLACEHOLDER — tasarım aşamasında ne yaptığınızı anlatan kısa metin.</p>
        </li>
        <li>
          <h3>Üretim</h3>
          <p>PLACEHOLDER — üretim aşamasını anlatan kısa metin.</p>
        </li>
        <li>
          <h3>Uygulama</h3>
          <p>PLACEHOLDER — sahadaki uygulama ve teslim aşamasını anlatan kısa metin.</p>
        </li>
      </ol>
    </section>
  </div>
"""
    return (
        head("../", f"Hizmetler — {SITE}",
             "Mimari konsept mağaza, anahtar teslim proje; tasarım, üretim ve uygulama.")
        + header("../", "hizmetler") + "\n<main class=\"page\">\n" + body + "</main>\n"
        + footer("../") + '\n<script src="../assets/nav.js"></script>\n</body>\n</html>\n'
    )


REFERANSLAR = [
    ("Perde &amp; Ev Tekstili", ["Poyraz Perde", "Emre Perde", "Model Perde", "Koza Perde",
                                 "Çizgi Perde", "Erva Perde", "Mevsim Perde", "Alis Perde",
                                 "BYM Perde", "Emart Perde"]),
    ("Konsept Home Mağaza",     ["Valeria Home", "Glinza Home", "Velmora Home", "Home Project"]),
    ("Yeme &amp; İçme",         ["Komagene", "Tatlım Baklava", "Devran Döner"]),
    ("Ofis, Atölye &amp; Salon", ["Ayd Office", "Ayd Atölye", "Özeller Ofis", "Özgül Kuaför"]),
]


def ref_wall():
    out = []
    for baslik, isimler in REFERANSLAR:
        li = "".join(f"<li>{i}</li>" for i in isimler)
        out.append(f'      <div class="ref-group">\n        <h4>{baslik}</h4>\n'
                   f'        <ul>{li}</ul>\n      </div>')
    return "\n".join(out)


def sayfa_projeler():
    body = page_head("Projeler", "Teslim Ettiğimiz İşler") + f"""
  <div class="wrap">
    <section class="section">
      <blockquote class="pull-quote">
        Biz ne kadar kendimizi anlatmaya ya da ıspat etmeye çalışsak da
        referanslarımız bizi bizden daha iyi bilir ve anlatır.
      </blockquote>
      <div class="proj">
        <div class="proj-shot" data-label="Proje görseli"></div>
        <div>
          <p class="meta">Antalya</p>
          <h3>Poyraz Home</h3>
          <p>Aydınlar Interior Design Antalya projesinde, mekanın eski halinden yepyeni bir
             yaşam alanına dönüşümünü tamamladı. Baştan sona yenilenen bu projede, her detay
             titizlikle ele alındı ve ortaya modern, şık ve kullanışlı bir sonuç çıktı.</p>
          <p>Estetik ve fonksiyonelliğin buluştuğu bu özel çalışma, modern tasarım anlayışını
             yaşam alanlarına en iyi şekilde yansıtıyor.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <h2 class="section-title">Referanslarımız · 21 Marka</h2>
      <div class="ref-wall">
{ref_wall()}
      </div>
    </section>
  </div>
"""
    return (
        head("../", f"Projeler — {SITE}",
             "Aydınlar Interior Design'ın teslim ettiği konsept mağaza projeleri ve 21 marka referansı.")
        + header("../", "projeler") + "\n<main class=\"page\">\n" + body + "</main>\n"
        + footer("../") + '\n<script src="../assets/nav.js"></script>\n</body>\n</html>\n'
    )


def sayfa_hakkimizda():
    body = page_head("Hakkımızda", "Aydınlar Tasarım Manifestosu") + f"""
  <div class="wrap">
    <section class="section">
      <div class="panel-body manifesto" style="font-size:clamp(16px,1.35vw,21px);max-width:60ch">
        <p>Her çizgide, her dokuda ve her detayda;<br>
           estetik ile fonksiyonun dengelendiği,<br>
           mekânın sadece tasarlanmadığı,<br>
           kimlik kazandığı bir yaklaşım.</p>
        <p>Bizim için tasarım;<br>
           görünenin ötesinde hissedilen,<br>
           zamansız ve özgün bir imzadır.</p>
        <p class="sig">Aydınlar Interior Design</p>
      </div>
    </section>

    <section class="section">
      <h2 class="section-title">Firma</h2>
      <div class="svc-grid">
        <article class="svc">
          <span class="svc-mark"></span>
          <h3>{FIRMA}</h3>
          <p>Tüm Türkiye Mimari Konsept Mağaza · Anahtar Teslim Proje ·
             Tasarım, Üretim, Uygulama</p>
        </article>
        <article class="svc">
          <span class="svc-mark"></span>
          <h3>21 Marka</h3>
          <p>Perde ve ev tekstili mağazalarından yeme-içme zincirlerine ve ofislere kadar
             teslim edilmiş projeler. <a class="panel-link" href="../projeler/">Projeler</a></p>
        </article>
      </div>
      <p class="note">PLACEHOLDER — kuruluş yılı, ekip ve atölye hakkındaki metni sen
        yazdığında buraya girecek.</p>
    </section>
  </div>
"""
    return (
        head("../", f"Hakkımızda — {SITE}",
             f"{FIRMA} — tasarım manifestosu, firma bilgileri ve çalışma alanları.")
        + header("../", "hakkimizda") + "\n<main class=\"page\">\n" + body + "</main>\n"
        + footer("../") + '\n<script src="../assets/nav.js"></script>\n</body>\n</html>\n'
    )


def sayfa_iletisim():
    body = page_head(
        "İletişim", "Projenizi Konuşalım",
        "Mağaza konseptinizi konuşmak için proje yetkilimize doğrudan ulaşabilirsiniz."
    ) + f"""
  <div class="wrap">
    <section class="section">
      <div class="contact">
        <div class="contact-card">
          <h3>Proje Yetkilisi</h3>
          <a href="tel:{TEL_HREF}">{TEL_YAZI}</a>
        </div>
        <div class="contact-card">
          <h3>Instagram</h3>
          <a href="{IG}" target="_blank" rel="noopener">@aydinlar.interior.design</a>
        </div>
        <div class="contact-card">
          <h3>Firma</h3>
          <p>{FIRMA}</p>
        </div>
        <div class="contact-card">
          <h3>Çalışma Alanı</h3>
          <p>Tüm Türkiye</p>
        </div>
      </div>
      <p class="note">PLACEHOLDER — adres, e-posta ve çalışma saatleri henüz yok.
        Bunları verdiğinde buraya eklenecek. İletişim formu istersen ayrıca konuşalım:
        statik sitede form için bir form servisi gerekir.</p>
    </section>
  </div>
"""
    return (
        head("../", f"İletişim — {SITE}",
             f"{FIRMA} iletişim: proje yetkilisi {TEL_YAZI}.")
        + header("../", "iletisim") + "\n<main class=\"page\">\n" + body + "</main>\n"
        + footer("../") + '\n<script src="../assets/nav.js"></script>\n</body>\n</html>\n'
    )


SAYFALAR = {
    "index.html":            sayfa_anasayfa,
    "hizmetler/index.html":  sayfa_hizmetler,
    "projeler/index.html":   sayfa_projeler,
    "hakkimizda/index.html": sayfa_hakkimizda,
    "iletisim/index.html":   sayfa_iletisim,
}


def main():
    for yol, uret in SAYFALAR.items():
        hedef = ROOT / yol
        hedef.parent.mkdir(parents=True, exist_ok=True)
        html = uret()
        hedef.write_text(html, encoding="utf-8")
        print(f"  {yol:24s} {len(html):>7,} bayt")
    print("Derlendi.")


if __name__ == "__main__":
    main()
