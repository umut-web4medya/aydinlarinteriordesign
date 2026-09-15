#!/usr/bin/env python3
"""
Aydınlar Interior Design — site derleyicisi (TR / EN / DE).

    python3 _src/build.py

Üst bar, alt bilgi, <head> ve tüm metinler tek yerde durur.
⛔ Üretilen .html dosyalarını ELLE DÜZENLEME — sonraki derlemede silinir.
Metinler: _src/diller.py   ·   Türkçe asıl içerik: _src/icerik.md
"""
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from diller import BAYRAK, REFERANSLAR, SLUG, KOK, DIL_ADI, t   # noqa: E402
from parcalar import btn, DESTE_SOL, DESTE_SAG, INSTAGRAM       # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "Aydınlar Interior Design"
FIRMA = "Aydınlar Premium Group İnşaat Ltd. Şti."
TEL_HREF = "+905320597461"
TEL_YAZI = "0532 059 74 61"
IG = "https://www.instagram.com/aydinlar.interior.design/"
YIL = "2026"
KOK_URL = "https://umut-web4medya.github.io/aydinlarinteriordesign/"
DILLER = ["tr", "en", "de"]
ANAHTARLAR = ["home", "services", "projects", "about", "contact"]


# ------------------------------------------------------------------ adresler
def dosya(lang, key):
    kok, slug = KOK[lang], SLUG[lang][key]
    return f"{kok}index.html" if key == "home" else f"{kok}{slug}/index.html"


def url(lang, key):
    kok, slug = KOK[lang], SLUG[lang][key]
    return kok if key == "home" else f"{kok}{slug}/"


def derinlik(yol):
    return yol.count("/")


def bag(su_an, lang, key):
    """su_an sayfasından, o dilin key sayfasına göreli bağlantı."""
    yukari = "../" * derinlik(dosya(*su_an))
    hedef = yukari + url(lang, key)
    return hedef or "./"


# ------------------------------------------------------------------ parçalar
def head(lang, key, baslik, aciklama):
    yol = dosya(lang, key)
    up = "../" * derinlik(yol)
    kendi = KOK_URL + url(lang, key)
    gorsel = KOK_URL + "images/slide-2.webp"
    yerel = {"tr": "tr_TR", "en": "en_GB", "de": "de_DE"}[lang]
    alt = "\n".join(
        f'<link rel="alternate" hreflang="{d}" href="{KOK_URL + url(d, key)}">'
        for d in DILLER
    )
    ogalt = "\n".join(
        f'<meta property="og:locale:alternate" content="{ {"tr":"tr_TR","en":"en_GB","de":"de_DE"}[d] }">'
        for d in DILLER if d != lang
    )
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{baslik}</title>
<meta name="description" content="{aciklama}">
<link rel="canonical" href="{kendi}">
{alt}
<link rel="alternate" hreflang="x-default" href="{KOK_URL + url('tr', key)}">
<link rel="icon" href="{up}images/favicon.ico" sizes="48x48">
<link rel="icon" href="{up}images/favicon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="{up}images/favicon-192.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{baslik}">
<meta property="og:description" content="{aciklama}">
<meta property="og:url" content="{kendi}">
<meta property="og:image" content="{gorsel}">
<meta property="og:image:width" content="1220">
<meta property="og:image:height" content="1207">
<meta property="og:image:alt" content="{t('alt2', lang)}">
<meta property="og:locale" content="{yerel}">
{ogalt}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{baslik}">
<meta name="twitter:description" content="{aciklama}">
<meta name="twitter:image" content="{gorsel}">
<meta name="theme-color" content="#f8f8f6">
<link rel="preload" as="font" type="font/woff2" href="{up}assets/fonts/bricolage-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="{up}assets/fonts/instrument-latin.woff2" crossorigin>
<link rel="stylesheet" href="{up}assets/site.css">
<script>document.documentElement.classList.add("js-reveal")</script>
<script type="application/ld+json">{sema(lang, key, baslik, aciklama, kendi, gorsel)}</script>
</head>
<body>"""


def sema(lang, key, baslik, aciklama, kendi, gorsel):
    """JSON-LD. Yalnız DOĞRULANMIŞ bilgiler: uydurma adres veya puan yok."""
    import json
    isletme = {
        "@type": "HomeAndConstructionBusiness",
        "@id": KOK_URL + "#isletme",
        "name": SITE,
        "legalName": FIRMA,
        "url": KOK_URL,
        "image": gorsel,
        "logo": KOK_URL + "images/favicon-192.png",
        "telephone": "+90 532 059 74 61",
        "description": t("desc_home", lang),
        "areaServed": {"@type": "Country", "name": "Türkiye"},
        "sameAs": [IG],
        "knowsAbout": [t("p2_title", lang), t("svc_turnkey", lang), t("p4_title", lang)],
        "makesOffer": {
            "@type": "Offer",
            "itemOffered": {"@type": "Service", "name": t("svc_turnkey", lang),
                            "description": t("p3_lead", lang)},
        },
    }
    graf = [isletme,
            {"@type": "WebSite", "@id": KOK_URL + "#site", "url": KOK_URL, "name": SITE,
             "inLanguage": lang, "publisher": {"@id": KOK_URL + "#isletme"}},
            {"@type": "WebPage", "@id": kendi + "#sayfa", "url": kendi, "name": baslik,
             "description": aciklama, "inLanguage": lang,
             "isPartOf": {"@id": KOK_URL + "#site"}, "about": {"@id": KOK_URL + "#isletme"}}]
    return json.dumps({"@context": "https://schema.org", "@graph": graf},
                      ensure_ascii=False, separators=(",", ":"))


def dil_secici(lang, key):
    ogeler = []
    for d in DILLER:
        aktif = d == lang
        sinif = ' class="is-on"' if aktif else ""
        simdiki = ' aria-current="true"' if aktif else ""
        ogeler.append(
            f'      <li><a{sinif} href="{bag((lang, key), d, key)}" '
            f'hreflang="{d}" lang="{d}" title="{DIL_ADI[d]}" '
            f'aria-label="{DIL_ADI[d]}"{simdiki}>'
            f'{BAYRAK[d]}</a></li>'
        )
    return ('  <ul class="lang" aria-label="' + t("lang_label", lang) + '">\n'
            + "\n".join(ogeler) + "\n  </ul>")


def header(lang, key):
    yol = dosya(lang, key)
    up = "../" * derinlik(yol)
    ogeler = []
    for k in ANAHTARLAR:
        cls = ' class="is-current"' if k == key else ""
        ogeler.append(f'    <li{cls}><a href="{bag((lang, key), lang, k)}">'
                      f'{t("nav_" + k, lang)}</a></li>')
    return f"""
<header class="site-head" id="head">
  <a class="brand" href="{bag((lang, key), lang, 'home')}" aria-label="{SITE} — {t('home_aria', lang)}">
    <img class="brand-logo" src="{up}images/aydinlar-logo-white.png" width="360" height="184"
         alt="{t('logo_alt', lang)}" decoding="async">
    <span>
      <span class="brand-name">Aydınlar</span>
      <span class="brand-sub">Interior Design</span>
    </span>
  </a>
  <ul class="nav" id="nav">
{chr(10).join(ogeler)}
  </ul>
{dil_secici(lang, key)}
  <a class="btn head-cta" href="tel:{TEL_HREF}">{TEL_YAZI}</a>
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="{t('menu_open', lang)}"><i></i></button>
</header>
"""


def footer(lang, key):
    links = "".join(f'<li><a href="{bag((lang, key), lang, k)}">{t("nav_" + k, lang)}</a></li>'
                    for k in ANAHTARLAR)
    return f"""
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h2>{SITE}</h2>
        <p>{FIRMA}<br>{t('firma_alt', lang)}</p>
      </div>
      <div>
        <h2>{t('pages', lang)}</h2>
        <ul>{links}</ul>
      </div>
      <div>
        <h2>{t('nav_contact', lang)}</h2>
        <ul>
          <li><a href="tel:{TEL_HREF}">{t('project_mgr', lang)} · {TEL_YAZI}</a></li>
          <li><a href="{IG}" target="_blank" rel="noopener">Instagram</a></li>
        </ul>
      </div>
    </div>
    <p class="foot-bottom">© {FIRMA} {YIL}</p>
  </div>
</footer>
"""


def sayfa_basi(kicker, h1, lede=""):
    l = f'\n      <p class="lede reveal">{lede}</p>' if lede else ""
    return (f'  <section class="page-hero">\n    <div class="wrap">\n'
            f'      <p class="eyebrow reveal">{kicker}</p>\n      <h1 class="reveal">{h1}</h1>{l}\n'
            f'    </div>\n  </section>\n')


def kapat(lang, key, deste=False):
    up = "../" * derinlik(dosya(lang, key))
    js = f'\n<script src="{up}assets/ui.js"></script>\n'
    if deste:
        js += f'<script src="{up}assets/deck.js"></script>\n'
    return js + "</body>\n</html>\n"


def kontrol_listesi(lang):
    return f"""        <ul class="check-list">
          <li>{t('c1', lang)}</li>
          <li>{t('c2', lang)}</li>
          <li>{t('c3', lang)}</li>
          <li class="is-highlight">{t('c4', lang)}</li>
        </ul>"""


def ref_bloklari(lang, sinif="ref-groups"):
    i = {"tr": 0, "en": 1, "de": 2}[lang]
    out = []
    for basliklar, isimler in REFERANSLAR:
        li = "".join(f"<li>{n}</li>" for n in isimler)
        out.append(f'          <div class="ref-group reveal">\n            <h3>{basliklar[i]}</h3>\n'
                   f'            <ul class="chips">{li}</ul>\n          </div>')
    return f'        <div class="{sinif}">\n' + "\n".join(out) + "\n        </div>"


# ------------------------------------------------------------------ anasayfa
def deste(lang):
    key = "home"
    up = "../" * derinlik(dosya(lang, key))
    dikey = [t(f"v{i}", lang) for i in range(1, 6)]
    olculer = "(max-width:980px) 100vw, 56vw"

    slaytlar = []
    for i in range(1, 6):
        aktif = " is-active" if i == 1 else ""
        gizli = "" if i == 1 else ' aria-hidden="true"'
        buyuk, kucuk = f"{up}images/slide-{i}.webp", f"{up}images/slide-{i}-sm.webp"
        setler = f"{kucuk} 760w, {buyuk} 1220w"
        olcu = f'sizes="{olculer}" width="1220" height="1229" decoding="async"'
        if i == 1:   # ilk kare hemen, kalanı deck.js yükler
            ana = (f'<img class="slide-bg" src="{buyuk}" srcset="{setler}" {olcu} '
                   f'alt="{t("alt1", lang)}" fetchpriority="high">')
            ysm = f'<img src="{buyuk}" srcset="{setler}" {olcu} alt="" aria-hidden="true">'
        else:
            ana = (f'<img class="slide-bg" data-src="{buyuk}" data-srcset="{setler}" {olcu} '
                   f'alt="{t(f"alt{i}", lang)}" loading="lazy">')
            ysm = (f'<img data-src="{buyuk}" data-srcset="{setler}" {olcu} alt="" '
                   f'aria-hidden="true" loading="lazy">')
        slaytlar.append(f"""  <article class="slide{aktif}" style="--i:{i}" aria-label="{i} / 5"{gizli}>
    <div class="bloom" aria-hidden="true">{ysm}</div>
    <div class="slide-media">{ana}</div>
    <div class="counter"><b>{i}</b><i>5</i></div>
    <p class="slide-vtitle"><span>{dikey[i-1]}</span></p>
  </article>""")

    def kutu(i, kicker, baslik, govde, eylemler="", ekstra=""):
        akt = " is-active" if i == 1 else ""
        hh = "h1" if i == 1 else "h2"     # sayfanın tek H1'i manifesto
        ey = f'\n        <div class="panel-actions">{eylemler}</div>' if eylemler else ""
        return f"""  <div class="panel{akt}" style="--i:{i}">
    <div class="frame"><div class="frame-inner">
      <div class="panel-scroll">
        <p class="panel-kicker">{kicker}</p>
        <{hh} class="panel-title">{baslik}</{hh}>
{govde}{ekstra}{ey}
      </div>
      <div class="scroll-hint"><b></b></div>
    </div></div>
  </div>"""

    kutular = [
        kutu(1, t("p1_kicker", lang), t("p1_title", lang),
             f"""        <div class="panel-body manifesto">
          <p>{t('manifesto', lang)}</p>
          <p>{t('manifesto2', lang)}</p>
          <p class="sig">{SITE}</p>
        </div>"""),
        kutu(2, t("p2_kicker", lang), t("p2_title", lang),
             f'        <div class="panel-body"><p>{t("p2_body", lang)}</p></div>',
             btn(t("our_services", lang), bag((lang, key), lang, "services"))),
        kutu(3, t("p3_kicker", lang), t("p3_title", lang),
             f'        <div class="panel-body"><p>{t("p3_lead", lang)}</p></div>',
             btn(f'{t("project_mgr", lang)} · {TEL_YAZI}', f"tel:{TEL_HREF}", "btn-accent"),
             "\n" + kontrol_listesi(lang)
             + f'\n        <p class="panel-close">{t("p3_close", lang)}</p>'),
        kutu(4, t("p4_kicker", lang), t("p4_title", lang),
             f'        <div class="panel-body"><p>{t("p4_body", lang)}</p></div>',
             btn(t("p4_link", lang), bag((lang, key), lang, "services"))),
        kutu(5, t("p5_kicker", lang), t("p5_title", lang),
             f'        <blockquote class="pull-quote">{t("quote", lang)}</blockquote>',
             btn(t("all_projects", lang), bag((lang, key), lang, "projects")),
             "\n" + ref_bloklari(lang)),
    ]

    return f"""<section class="hero" id="hero" aria-roledescription="carousel" aria-label="{t('carousel', lang)}">

{chr(10).join(slaytlar)}

{chr(10).join(kutular)}

  <nav class="hero-nav" aria-label="{t('slide_nav', lang)}">
    <button type="button" data-dir="-1" aria-label="{t('prev', lang)}">{DESTE_SOL}</button>
    <button type="button" data-dir="1" aria-label="{t('next', lang)}">{DESTE_SAG}</button>
    <span class="ayrac" aria-hidden="true"></span>
    <a class="sosyal" href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{INSTAGRAM}</a>
  </nav>

  <p class="hero-foot">© {FIRMA} {YIL}</p>
</section>"""


def sayfa_home(lang):
    return (head(lang, "home", f"{SITE} — {t('p2_title', lang)}", t("desc_home", lang))
            + header(lang, "home") + "\n<main>\n" + deste(lang) + "\n</main>\n"
            + kapat(lang, "home", deste=True))


# ------------------------------------------------------------------ hizmetler
def sayfa_services(lang):
    k = "services"
    g = sayfa_basi(t("nav_services", lang), t("svc_h1", lang), t("svc_lede", lang)) + f"""
  <div class="wrap">
    <section class="section">
      <h2 class="section-title reveal">{t('svc_what', lang)}</h2>
      <div class="cards">
        <article class="card reveal"><span class="mark"></span>
          <h3>{t('p2_title', lang)}</h3><p>{t('p2_body', lang)}</p></article>
        <article class="card reveal"><span class="mark"></span>
          <h3>{t('svc_turnkey', lang)}</h3><p>{t('p3_lead', lang)}</p></article>
        <article class="card reveal"><span class="mark"></span>
          <h3>{t('p4_title', lang)}</h3><p>{t('p4_body', lang)}</p></article>
      </div>
    </section>

    <section class="section">
      <div class="offer reveal">
        <h2>{t('p3_title', lang)}</h2>
        <p>{t('p3_lead', lang)}</p>
{kontrol_listesi(lang)}
        <p class="panel-close">{t('p3_close', lang)}</p>
        <div class="panel-actions">{btn(f'{t("project_mgr", lang)} · {TEL_YAZI}', f"tel:{TEL_HREF}", "btn-accent")}</div>
      </div>
    </section>

    <section class="section">
      <h2 class="section-title reveal">{t('svc_process', lang)}</h2>
      <ol class="steps">
        <li class="reveal"><h3>{t('step1', lang)}</h3><p>{t('step1_b', lang)}</p></li>
        <li class="reveal"><h3>{t('step2', lang)}</h3><p>{t('step2_b', lang)}</p></li>
        <li class="reveal"><h3>{t('step3', lang)}</h3><p>{t('step3_b', lang)}</p></li>
      </ol>
    </section>
  </div>
"""
    return (head(lang, k, f"{t('nav_services', lang)} — {SITE}", t("desc_svc", lang))
            + header(lang, k) + '\n<main class="page">\n' + g + "</main>\n"
            + footer(lang, k) + kapat(lang, k))


# ------------------------------------------------------------------ projeler
def sayfa_projects(lang):
    k = "projects"
    g = sayfa_basi(t("nav_projects", lang), t("prj_h1", lang)) + f"""
  <div class="wrap">
    <section class="section">
      <blockquote class="pull-quote reveal">{t('quote', lang)}</blockquote>
      <div class="proj">
        <div class="proj-shot reveal" data-label="{t('proj_shot', lang)}"></div>
        <div class="reveal">
          <p class="meta">Antalya</p>
          <h2>Poyraz Home</h2>
          <p>{t('antalya_1', lang)}</p>
          <p>{t('antalya_2', lang)}</p>
        </div>
      </div>
    </section>

    <section class="section">
      <h2 class="section-title reveal">{t('prj_refs', lang)}</h2>
{ref_bloklari(lang, 'ref-wall')}
    </section>
  </div>
"""
    return (head(lang, k, f"{t('nav_projects', lang)} — {SITE}", t("desc_prj", lang))
            + header(lang, k) + '\n<main class="page">\n' + g + "</main>\n"
            + footer(lang, k) + kapat(lang, k))


# ------------------------------------------------------------------ hakkımızda
def sayfa_about(lang):
    k = "about"
    g = sayfa_basi(t("nav_about", lang), t("p1_title", lang)) + f"""
  <div class="wrap">
    <section class="section">
      <div class="panel-body manifesto reveal" style="max-width:56ch">
        <p>{t('manifesto', lang)}</p>
        <p>{t('manifesto2', lang)}</p>
        <p class="sig">{SITE}</p>
      </div>
    </section>

    <section class="section">
      <h2 class="section-title reveal">{t('abt_company', lang)}</h2>
      <div class="cards">
        <article class="card reveal"><span class="mark"></span>
          <h3>{FIRMA}</h3><p>{t('firma_alt', lang)}</p></article>
        <article class="card reveal"><span class="mark"></span>
          <h3>{t('abt_brands', lang)}</h3>
          <p>{t('abt_brands_b', lang)}</p>
          {btn(t('all_projects', lang), bag((lang, k), lang, 'projects'), 'btn-quiet')}</article>
      </div>
      <p class="note reveal">{t('abt_note', lang)}</p>
    </section>
  </div>
"""
    return (head(lang, k, f"{t('nav_about', lang)} — {SITE}", t("desc_abt", lang))
            + header(lang, k) + '\n<main class="page">\n' + g + "</main>\n"
            + footer(lang, k) + kapat(lang, k))


# ------------------------------------------------------------------ iletişim
def sayfa_contact(lang):
    k = "contact"
    g = sayfa_basi(t("nav_contact", lang), t("ctc_h1", lang), t("ctc_lede", lang)) + f"""
  <div class="wrap">
    <section class="section">
      <div class="contact">
        <div class="contact-card reveal">
          <p class="ck-label">{t('project_mgr', lang)}</p>
          <a href="tel:{TEL_HREF}">{TEL_YAZI}</a>
        </div>
        <div class="contact-card reveal">
          <p class="ck-label">Instagram</p>
          <a href="{IG}" target="_blank" rel="noopener">@aydinlar.interior.design</a>
        </div>
        <div class="contact-card reveal">
          <p class="ck-label">{t('abt_company', lang)}</p>
          <p>{FIRMA}</p>
        </div>
        <div class="contact-card reveal">
          <p class="ck-label">{t('ctc_area', lang)}</p>
          <p>{t('ctc_area_v', lang)}</p>
        </div>
      </div>
      <p class="note reveal">{t('ctc_note', lang)}</p>
    </section>
  </div>
"""
    return (head(lang, k, f"{t('nav_contact', lang)} — {SITE}", t("desc_ctc", lang))
            + header(lang, k) + '\n<main class="page">\n' + g + "</main>\n"
            + footer(lang, k) + kapat(lang, k))


URETICI = {"home": sayfa_home, "services": sayfa_services, "projects": sayfa_projects,
           "about": sayfa_about, "contact": sayfa_contact}


def main():
    n = 0
    for lang in DILLER:
        for key in ANAHTARLAR:
            yol = ROOT / dosya(lang, key)
            yol.parent.mkdir(parents=True, exist_ok=True)
            html = URETICI[key](lang)
            yol.write_text(html, encoding="utf-8")
            print(f"  {dosya(lang, key):28s} {len(html):>7,} bayt")
            n += 1
    import seo_uret
    seo_uret.uret()
    print(f"Derlendi — {n} sayfa.")


if __name__ == "__main__":
    main()
