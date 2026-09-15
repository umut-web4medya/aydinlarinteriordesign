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

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "Aydınlar Interior Design"
FIRMA = "Aydınlar Premium Group İnşaat Ltd. Şti."
TEL_HREF = "+905320597461"
TEL_YAZI = "0532 059 74 61"
IG = "https://www.instagram.com/aydinlar.interior.design/"
YIL = "2026"
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
    alt = "\n".join(
        f'<link rel="alternate" hreflang="{d}" href="{bag((lang, key), d, key)}">'
        for d in DILLER
    )
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{baslik}</title>
<meta name="description" content="{aciklama}">
<link rel="icon" href="{up}images/favicon.ico" sizes="48x48">
<link rel="icon" href="{up}images/favicon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="{up}images/favicon-192.png">
<meta property="og:title" content="{baslik}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{ {'tr': 'tr_TR', 'en': 'en_GB', 'de': 'de_DE'}[lang] }">
{alt}
<link rel="alternate" hreflang="x-default" href="{bag((lang, key), 'tr', key)}">
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body>"""


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
<header class="site-head">
  <a class="brand" href="{bag((lang, key), lang, 'home')}" aria-label="{SITE} — {t('home_aria', lang)}">
    <img class="brand-logo" src="{up}images/aydinlar-logo-white.png" width="360" height="184"
         alt="{t('logo_alt', lang)}" decoding="async">
    <span>
      <span class="brand-name">Aydınlar</span>
      <span class="brand-sub">Interior Design</span>
    </span>
  </a>
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="{t('menu_open', lang)}"><i></i></button>
  <ul class="nav" id="nav">
{chr(10).join(ogeler)}
  </ul>
{dil_secici(lang, key)}
  <a class="head-cta" href="tel:{TEL_HREF}">{TEL_YAZI}</a>
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
        <h4>{SITE}</h4>
        <p>{FIRMA}<br>{t('firma_alt', lang)}</p>
      </div>
      <div>
        <h4>{t('pages', lang)}</h4>
        <ul>{links}</ul>
      </div>
      <div>
        <h4>{t('nav_contact', lang)}</h4>
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
    l = f'\n      <p class="lede">{lede}</p>' if lede else ""
    return (f'  <div class="page-head">\n    <div class="wrap">\n'
            f'      <p class="kicker">{kicker}</p>\n      <h1>{h1}</h1>{l}\n'
            f'    </div>\n  </div>\n')


def kapat(lang, key, deste=False):
    up = "../" * derinlik(dosya(lang, key))
    js = f'\n<script src="{up}assets/nav.js"></script>\n'
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
        out.append(f'          <div class="ref-group">\n            <h4>{basliklar[i]}</h4>\n'
                   f'            <ul>{li}</ul>\n          </div>')
    return f'        <div class="{sinif}">\n' + "\n".join(out) + "\n        </div>"


# ------------------------------------------------------------------ anasayfa
def deste(lang):
    key = "home"
    up = "../" * derinlik(dosya(lang, key))
    dikey = [t(f"v{i}", lang) for i in range(1, 6)]
    slaytlar = []
    for i in range(1, 6):
        aktif = " is-active" if i == 1 else ""
        gizli = "" if i == 1 else ' aria-hidden="true"'
        buyuk, kucuk = f"{up}images/slide-{i}.webp", f"{up}images/slide-{i}-sm.webp"
        setler = f'{kucuk} 760w, {buyuk} 1220w'
        olculer = '(max-width:980px) 100vw, 55vw'
        if i == 1:      # ilk kare hemen yüklenir
            gorsel = (f'<img class="slide-bg" src="{buyuk}" srcset="{setler}" sizes="{olculer}" '
                      f'alt="{t("alt1", lang)}" width="1220" height="1229" fetchpriority="high" decoding="async">')
        else:           # kalanlar boşta kalınca — deck.js yükler
            gorsel = (f'<img class="slide-bg" data-src="{buyuk}" data-srcset="{setler}" sizes="{olculer}" '
                      f'alt="{t(f"alt{i}", lang)}" width="1220" height="1229" loading="lazy" decoding="async">')
        slaytlar.append(f"""  <article class="slide{aktif}" style="--i:{i}" aria-label="{i} / 5"{gizli}>
    <div class="slide-media">{gorsel}</div>
    <div class="counter"><b>{i}</b><i>5</i></div>
    <h2 class="slide-vtitle"><span>{dikey[i-1]}</span></h2>
  </article>""")

    kutular = [
f"""  <div class="panel is-active" style="--i:1">
    <div class="frame"><div class="frame-inner">
      <div class="panel-scroll">
        <h3 class="panel-title">{t('p1_title', lang)}</h3>
        <p class="panel-kicker">{t('p1_kicker', lang)}</p>
        <div class="panel-body manifesto">
          <p>{t('manifesto', lang)}</p>
          <p>{t('manifesto2', lang)}</p>
          <p class="sig">{SITE}</p>
        </div>
      </div>
      <div class="scroll-hint"><b></b></div>
    </div></div>
  </div>""",
f"""  <div class="panel" style="--i:2">
    <div class="frame"><div class="frame-inner">
      <div class="panel-scroll">
        <h3 class="panel-title">{t('p2_title', lang)}</h3>
        <p class="panel-kicker">{t('p2_kicker', lang)}</p>
        <div class="panel-body"><p>{t('p2_body', lang)}</p></div>
        <a class="panel-link" href="{bag((lang, key), lang, 'services')}">{t('our_services', lang)}</a>
      </div>
      <div class="scroll-hint"><b></b></div>
    </div></div>
  </div>""",
f"""  <div class="panel" style="--i:3">
    <div class="frame"><div class="frame-inner">
      <div class="panel-scroll">
        <h3 class="panel-title">{t('p3_title', lang)}</h3>
        <p class="panel-kicker">{t('p3_kicker', lang)}</p>
        <div class="panel-body"><p>{t('p3_lead', lang)}</p></div>
{kontrol_listesi(lang)}
        <p class="panel-close">{t('p3_close', lang)}</p>
        <a class="panel-link" href="tel:{TEL_HREF}">{t('project_mgr', lang)}</a>
      </div>
      <div class="scroll-hint"><b></b></div>
    </div></div>
  </div>""",
f"""  <div class="panel" style="--i:4">
    <div class="frame"><div class="frame-inner">
      <div class="panel-scroll">
        <h3 class="panel-title">{t('p4_title', lang)}</h3>
        <p class="panel-kicker">{t('p4_kicker', lang)}</p>
        <div class="panel-body"><p>{t('p4_body', lang)}</p></div>
        <a class="panel-link" href="{bag((lang, key), lang, 'services')}">{t('p4_link', lang)}</a>
      </div>
      <div class="scroll-hint"><b></b></div>
    </div></div>
  </div>""",
f"""  <div class="panel" style="--i:5">
    <div class="frame"><div class="frame-inner">
      <div class="panel-scroll">
        <h3 class="panel-title">{t('p5_title', lang)}</h3>
        <p class="panel-kicker">{t('p5_kicker', lang)}</p>
        <blockquote class="pull-quote">{t('quote', lang)}</blockquote>
{ref_bloklari(lang)}
        <a class="panel-link" href="{bag((lang, key), lang, 'projects')}">{t('all_projects', lang)}</a>
      </div>
      <div class="scroll-hint"><b></b></div>
    </div></div>
  </div>"""]

    return f"""<section class="hero" id="hero" aria-roledescription="carousel" aria-label="{t('carousel', lang)}">

{chr(10).join(slaytlar)}

{chr(10).join(kutular)}

  <nav class="hero-nav" aria-label="{t('slide_nav', lang)}">
    <button type="button" data-dir="-1" aria-label="{t('prev', lang)}">
      <svg viewBox="0 0 120 20" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="square" aria-hidden="true">
        <path class="shaft" d="M119 10H4"/><path d="M4 10l9-7.5M4 10l9 7.5"/>
      </svg>
    </button>
    <button type="button" data-dir="1" aria-label="{t('next', lang)}">
      <svg viewBox="0 0 120 20" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="square" aria-hidden="true">
        <path class="shaft" d="M1 10h115"/><path d="M116 10l-9-7.5M116 10l-9 7.5"/>
      </svg>
    </button>
  </nav>

  <div class="side-social">
    <a href="{IG}" target="_blank" rel="noopener">Instagram</a>
  </div>

  <p class="hero-foot">© {FIRMA} {YIL}</p>
  <a class="hero-phone" href="tel:{TEL_HREF}">{t('project_mgr', lang)} · {TEL_YAZI}</a>
</section>"""


def sayfa_home(lang):
    return (head(lang, "home", f"{SITE} — {t('p2_title', lang)}", t("desc_home", lang))
            + header(lang, "home") + "\n<main>\n" + deste(lang) + "\n</main>\n"
            + kapat(lang, "home", deste=True))


def sayfa_services(lang):
    k = "services"
    g = sayfa_basi(t("nav_services", lang), t("svc_h1", lang), t("svc_lede", lang)) + f"""
  <div class="wrap">
    <section class="section">
      <h2 class="section-title">{t('svc_what', lang)}</h2>
      <div class="svc-grid">
        <article class="svc"><span class="svc-mark"></span>
          <h3>{t('p2_title', lang)}</h3><p>{t('p2_body', lang)}</p></article>
        <article class="svc"><span class="svc-mark"></span>
          <h3>{t('svc_turnkey', lang)}</h3><p>{t('p3_lead', lang)}</p></article>
        <article class="svc"><span class="svc-mark"></span>
          <h3>{t('p4_title', lang)}</h3><p>{t('p4_body', lang)}</p></article>
      </div>
    </section>

    <section class="section">
      <div class="offer">
        <h2>{t('p3_title', lang)}</h2>
        <p>{t('p3_lead', lang)}</p>
{kontrol_listesi(lang)}
        <p class="panel-close">{t('p3_close', lang)}</p>
        <a class="panel-link" href="tel:{TEL_HREF}">{t('project_mgr', lang)} · {TEL_YAZI}</a>
      </div>
    </section>

    <section class="section">
      <h2 class="section-title">{t('svc_process', lang)}</h2>
      <ol class="steps">
        <li><h3>{t('step1', lang)}</h3><p>{t('step1_b', lang)}</p></li>
        <li><h3>{t('step2', lang)}</h3><p>{t('step2_b', lang)}</p></li>
        <li><h3>{t('step3', lang)}</h3><p>{t('step3_b', lang)}</p></li>
      </ol>
    </section>
  </div>
"""
    return (head(lang, k, f"{t('nav_services', lang)} — {SITE}", t("desc_svc", lang))
            + header(lang, k) + '\n<main class="page">\n' + g + "</main>\n"
            + footer(lang, k) + kapat(lang, k))


def sayfa_projects(lang):
    k = "projects"
    g = sayfa_basi(t("nav_projects", lang), t("prj_h1", lang)) + f"""
  <div class="wrap">
    <section class="section">
      <blockquote class="pull-quote">{t('quote', lang)}</blockquote>
      <div class="proj">
        <div class="proj-shot" data-label="{t('proj_shot', lang)}"></div>
        <div>
          <p class="meta">Antalya</p>
          <h3>Poyraz Home</h3>
          <p>{t('antalya_1', lang)}</p>
          <p>{t('antalya_2', lang)}</p>
        </div>
      </div>
    </section>

    <section class="section">
      <h2 class="section-title">{t('prj_refs', lang)}</h2>
{ref_bloklari(lang, 'ref-wall')}
    </section>
  </div>
"""
    return (head(lang, k, f"{t('nav_projects', lang)} — {SITE}", t("desc_prj", lang))
            + header(lang, k) + '\n<main class="page">\n' + g + "</main>\n"
            + footer(lang, k) + kapat(lang, k))


def sayfa_about(lang):
    k = "about"
    g = sayfa_basi(t("nav_about", lang), t("p1_title", lang)) + f"""
  <div class="wrap">
    <section class="section">
      <div class="panel-body manifesto about-manifesto">
        <p>{t('manifesto', lang)}</p>
        <p>{t('manifesto2', lang)}</p>
        <p class="sig">{SITE}</p>
      </div>
    </section>

    <section class="section">
      <h2 class="section-title">{t('abt_company', lang)}</h2>
      <div class="svc-grid">
        <article class="svc"><span class="svc-mark"></span>
          <h3>{FIRMA}</h3><p>{t('firma_alt', lang)}</p></article>
        <article class="svc"><span class="svc-mark"></span>
          <h3>{t('abt_brands', lang)}</h3>
          <p>{t('abt_brands_b', lang)}</p>
          <a class="panel-link" href="{bag((lang, k), lang, 'projects')}">{t('all_projects', lang)}</a></article>
      </div>
      <p class="note">{t('abt_note', lang)}</p>
    </section>
  </div>
"""
    return (head(lang, k, f"{t('nav_about', lang)} — {SITE}", t("desc_abt", lang))
            + header(lang, k) + '\n<main class="page">\n' + g + "</main>\n"
            + footer(lang, k) + kapat(lang, k))


def sayfa_contact(lang):
    k = "contact"
    g = sayfa_basi(t("nav_contact", lang), t("ctc_h1", lang), t("ctc_lede", lang)) + f"""
  <div class="wrap">
    <section class="section">
      <div class="contact">
        <div class="contact-card">
          <h3>{t('project_mgr', lang)}</h3>
          <a href="tel:{TEL_HREF}">{TEL_YAZI}</a>
        </div>
        <div class="contact-card">
          <h3>Instagram</h3>
          <a href="{IG}" target="_blank" rel="noopener">@aydinlar.interior.design</a>
        </div>
        <div class="contact-card">
          <h3>{t('abt_company', lang)}</h3>
          <p>{FIRMA}</p>
        </div>
        <div class="contact-card">
          <h3>{t('ctc_area', lang)}</h3>
          <p>{t('ctc_area_v', lang)}</p>
        </div>
      </div>
      <p class="note">{t('ctc_note', lang)}</p>
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
    print(f"Derlendi — {n} sayfa.")


if __name__ == "__main__":
    main()
