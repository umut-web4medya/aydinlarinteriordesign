# -*- coding: utf-8 -*-
"""sitemap.xml ve robots.txt üretir. build.py her derlemede çağırır.

⚠️ robots.txt yalnız alan adının KÖKÜNDE geçerlidir. Site şu an
github.io'nun alt yolunda durduğu için bu dosya arama motorlarınca
okunmaz; özel alan adına geçince devreye girer. Sitemap her yolda çalışır.
"""


def uret():
    from build import DILLER, ANAHTARLAR, url, KOK_URL, ROOT

    satirlar = ['<?xml version="1.0" encoding="UTF-8"?>',
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
                '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for lang in DILLER:
        for key in ANAHTARLAR:
            if key == "home" and lang == "tr":
                oncelik = "1.0"
            elif key == "home":
                oncelik = "0.8"
            else:
                oncelik = "0.6"
            satirlar.append('  <url>')
            satirlar.append(f'    <loc>{KOK_URL + url(lang, key)}</loc>')
            for d in DILLER:
                satirlar.append('    <xhtml:link rel="alternate" '
                                f'hreflang="{d}" href="{KOK_URL + url(d, key)}"/>')
            satirlar.append('    <xhtml:link rel="alternate" '
                            f'hreflang="x-default" href="{KOK_URL + url("tr", key)}"/>')
            satirlar.append('    <changefreq>monthly</changefreq>')
            satirlar.append(f'    <priority>{oncelik}</priority>')
            satirlar.append('  </url>')
    satirlar.append('</urlset>')
    (ROOT / 'sitemap.xml').write_text('\n'.join(satirlar) + '\n', encoding='utf-8')

    (ROOT / 'robots.txt').write_text(
        '# Aydınlar Interior Design\n'
        'User-agent: *\n'
        'Allow: /\n\n'
        f'Sitemap: {KOK_URL}sitemap.xml\n',
        encoding='utf-8')
    print(f'  sitemap.xml ({len(DILLER) * len(ANAHTARLAR)} adres) + robots.txt')
