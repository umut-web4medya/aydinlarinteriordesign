# -*- coding: utf-8 -*-
"""Diller, bayraklar ve tüm görünen metinler.

⚠️ EN/DE metinleri Türkçe asıldan çevrildi; müşteri onayı bekliyor.
Türkçe metinler müşterinin kendi sözleridir, DEĞİŞTİRME.
"""

# --- bayraklar: dış istek yok, hepsi 3:2 kutuda ---------------------------
BAYRAK = {
    "tr": '<svg class="flag" viewBox="0 0 60 40" aria-hidden="true">'
          '<rect width="60" height="40" fill="#E30A17"/>'
          '<circle cx="22" cy="20" r="9.6" fill="#fff"/>'
          '<circle cx="25.8" cy="20" r="7.7" fill="#E30A17"/>'
          '<path fill="#fff" d="M42.40 20.00L38.75 21.27L38.67 25.14L36.33 22.05L32.63 23.17'
          'L34.84 20.00L32.63 16.83L36.33 17.95L38.67 14.86L38.75 18.73Z"/></svg>',

    "en": '<svg class="flag" viewBox="0 0 60 40" aria-hidden="true">'
          '<clipPath id="uj"><path d="M30 20V0h30v20h-30V40H30V20H0v-20h30z"/></clipPath>'
          '<rect width="60" height="40" fill="#012169"/>'
          '<path d="M0 0L60 40M60 0L0 40" stroke="#fff" stroke-width="8"/>'
          '<path d="M0 0L60 40M60 0L0 40" stroke="#C8102E" stroke-width="4.8" clip-path="url(#uj)"/>'
          '<path d="M30 0v40M0 20h60" stroke="#fff" stroke-width="13.3"/>'
          '<path d="M30 0v40M0 20h60" stroke="#C8102E" stroke-width="8"/></svg>',

    "de": '<svg class="flag" viewBox="0 0 60 40" aria-hidden="true">'
          '<rect width="60" height="13.34" fill="#111"/>'
          '<rect y="13.34" width="60" height="13.33" fill="#DD0000"/>'
          '<rect y="26.67" width="60" height="13.33" fill="#FFCE00"/></svg>',
}

REFERANSLAR = [
    (["Perde &amp; Ev Tekstili", "Curtains &amp; Home Textiles", "Gardinen &amp; Heimtextilien"],
     ["Poyraz Perde", "Emre Perde", "Model Perde", "Koza Perde", "Çizgi Perde",
      "Erva Perde", "Mevsim Perde", "Alis Perde", "BYM Perde", "Emart Perde"]),
    (["Konsept Home Mağaza", "Concept Home Stores", "Konzept-Home-Stores"],
     ["Valeria Home", "Glinza Home", "Velmora Home", "Home Project"]),
    (["Yeme &amp; İçme", "Food &amp; Beverage", "Gastronomie"],
     ["Komagene", "Tatlım Baklava", "Devran Döner"]),
    (["Ofis, Atölye &amp; Salon", "Office, Workshop &amp; Salon", "Büro, Werkstatt &amp; Salon"],
     ["Ayd Office", "Ayd Atölye", "Özeller Ofis", "Özgül Kuaför"]),
]

# --- sayfa adresleri ------------------------------------------------------
SLUG = {
    "tr": {"home": "", "services": "hizmetler", "projects": "projeler",
           "about": "hakkimizda", "contact": "iletisim"},
    "en": {"home": "", "services": "services", "projects": "projects",
           "about": "about", "contact": "contact"},
    "de": {"home": "", "services": "leistungen", "projects": "projekte",
           "about": "ueber-uns", "contact": "kontakt"},
}
KOK = {"tr": "", "en": "en/", "de": "de/"}
DIL_ADI = {"tr": "Türkçe", "en": "English", "de": "Deutsch"}

# --- metinler -------------------------------------------------------------
T = {
# ---------------------------------------------------------------- arayüz
"nav_home":      ("Anasayfa", "Home", "Startseite"),
"nav_services":  ("Hizmetler", "Services", "Leistungen"),
"nav_projects":  ("Projeler", "Projects", "Projekte"),
"nav_about":     ("Hakkımızda", "About", "Über uns"),
"nav_contact":   ("İletişim", "Contact", "Kontakt"),
"menu_open":     ("Menüyü aç", "Open menu", "Menü öffnen"),
"home_aria":     ("ana sayfa", "home", "Startseite"),
"logo_alt":      ("Aydınlar Interior Design logosu", "Aydınlar Interior Design logo",
                  "Aydınlar Interior Design Logo"),
"lang_label":    ("Dil", "Language", "Sprache"),
"carousel":      ("Tanıtım slaytları", "Intro slides", "Intro-Slides"),
"slide_nav":     ("Slayt gezinmesi", "Slide navigation", "Slide-Navigation"),
"prev":          ("Önceki slayt", "Previous slide", "Vorheriges Slide"),
"next":          ("Sonraki slayt", "Next slide", "Nächstes Slide"),
"img_label":     ("Görsel", "Image", "Bild"),
"proj_shot":     ("Proje görseli", "Project photo", "Projektfoto"),
"pages":         ("Sayfalar", "Pages", "Seiten"),
"project_mgr":   ("Proje Yetkilisi", "Project Manager", "Projektverantwortlicher"),

# ---------------------------------------------------------------- deste
"v1": ("Manifesto", "Manifesto", "Manifest"),
"v2": ("Konsept Mağaza", "Concept Store", "Konzeptladen"),
"v3": ("Anahtar Teslim", "Turnkey", "Schlüsselfertig"),
"v4": ("Üretim &amp; Uygulama", "Production &amp; Installation", "Produktion &amp; Montage"),
"v5": ("Referanslar", "References", "Referenzen"),

"p1_title":  ("Aydınlar Tasarım Manifestosu", "The Aydınlar Design Manifesto",
              "Das Aydınlar Design-Manifest"),
"p1_kicker": ("Tasarım Dili", "Design Language", "Designsprache"),
"manifesto": (
 "Her çizgide, her dokuda ve her detayda;<br>\n"
 "estetik ile fonksiyonun dengelendiği,<br>\n"
 "mekânın sadece tasarlanmadığı,<br>\n"
 "kimlik kazandığı bir yaklaşım.",
 "In every line, every texture and every detail;<br>\n"
 "an approach where aesthetics and function are balanced,<br>\n"
 "where a space is not merely designed<br>\n"
 "but given an identity.",
 "In jeder Linie, jeder Textur und jedem Detail;<br>\n"
 "ein Ansatz, in dem Ästhetik und Funktion im Gleichgewicht stehen,<br>\n"
 "in dem ein Raum nicht nur gestaltet wird,<br>\n"
 "sondern eine Identität erhält."),
"manifesto2": (
 "Bizim için tasarım;<br>\n"
 "görünenin ötesinde hissedilen,<br>\n"
 "zamansız ve özgün bir imzadır.",
 "For us, design is a signature —<br>\n"
 "timeless and singular —<br>\n"
 "felt beyond what is seen.",
 "Design ist für uns eine Signatur –<br>\n"
 "zeitlos und unverwechselbar –<br>\n"
 "spürbar über das Sichtbare hinaus."),

"p2_title":  ("Mimari Konsept Mağaza", "Architectural Concept Stores",
              "Architektonische Konzeptläden"),
"p2_kicker": ("Tüm Türkiye", "Across Türkiye", "Türkeiweit"),
"p2_body":   ("PLACEHOLDER — markanın mağaza konseptini nasıl kurguladığınızı anlatan giriş metni.",
              "PLACEHOLDER — the introduction describing how you build a brand's store concept.",
              "PLACEHOLDER — der Einstiegstext dazu, wie Sie das Ladenkonzept einer Marke aufbauen."),

"p3_title":  ("Mağaza Kurmak Artık Çok Kolay", "Opening a Store Just Got Easy",
              "Ein Geschäft zu eröffnen ist jetzt einfach"),
"p3_kicker": ("Anahtar Teslim", "Turnkey", "Schlüsselfertig"),
"p3_lead":   ("Hayalinizdeki perde ve halı mağazasını, anahtar teslim şekilde kuruyoruz.",
              "We build the curtain and carpet store you have in mind — turnkey, from start to finish.",
              "Wir bauen Ihr Wunschgeschäft für Gardinen und Teppiche – schlüsselfertig, von Anfang bis Ende."),
"c1": ("Uygun fiyat", "Fair pricing", "Faire Preise"),
"c2": ("Güvenilir hizmet", "Dependable service", "Verlässlicher Service"),
"c3": ("Modern tasarım showroomlar", "Modern showroom design", "Moderne Showroom-Gestaltung"),
"c4": ("%30 peşin, 12 ay taksit imkânı", "30% down payment, 12 monthly instalments",
       "30 % Anzahlung, 12 Monatsraten"),
"p3_close":  ("Siz sadece hayal edin, gerisini profesyonel ekibimiz halletsin.",
              "You just imagine it — our team takes care of the rest.",
              "Sie träumen davon – unser Team kümmert sich um den Rest."),

"p4_title":  ("Tasarım · Üretim · Uygulama", "Design · Production · Installation",
              "Design · Produktion · Montage"),
"p4_kicker": ("Tek Elden", "From One Source", "Alles aus einer Hand"),
"p4_body":   ("PLACEHOLDER — kendi üretiminizi ve sahadaki uygulama ekibinizi anlatan metin.",
              "PLACEHOLDER — the text about your own production and your on-site installation team.",
              "PLACEHOLDER — der Text über Ihre eigene Produktion und Ihr Montageteam vor Ort."),
"p4_link":   ("Üretim Sürecimiz", "Our Process", "Unser Ablauf"),

"p5_title":  ("Referanslarımız", "Our References", "Unsere Referenzen"),
"p5_kicker": ("21 Marka", "21 Brands", "21 Marken"),
"quote": ("Biz ne kadar kendimizi anlatmaya ya da ıspat etmeye çalışsak da "
          "referanslarımız bizi bizden daha iyi bilir ve anlatır.",
          "However much we try to describe or prove ourselves, our references "
          "know us better than we do — and tell it better.",
          "Wie sehr wir uns auch bemühen, uns zu beschreiben oder zu beweisen – "
          "unsere Referenzen kennen uns besser als wir selbst und erzählen es besser."),
"all_projects": ("Tüm Projeler", "All Projects", "Alle Projekte"),
"our_services": ("Hizmetlerimiz", "Our Services", "Unsere Leistungen"),

# ---------------------------------------------------------------- hizmetler
"svc_h1":   ("Mimari Konsept Mağaza", "Architectural Concept Stores",
             "Architektonische Konzeptläden"),
"svc_lede": ("Markanın kimliğini mağaza içinde kuran, tasarımdan üretime ve sahadaki "
             "uygulamaya kadar tek elden yürüyen bir hizmet.",
             "A single-source service that builds your brand's identity inside the store — "
             "from design through production to on-site installation.",
             "Eine Leistung aus einer Hand, die die Identität Ihrer Marke im Laden aufbaut – "
             "vom Entwurf über die Produktion bis zur Montage vor Ort."),
"svc_what": ("Ne Yapıyoruz", "What We Do", "Was wir tun"),
"svc_turnkey": ("Anahtar Teslim Proje", "Turnkey Projects", "Schlüsselfertige Projekte"),
"svc_process": ("Süreç", "Process", "Ablauf"),
"step1": ("Tasarım", "Design", "Entwurf"),
"step2": ("Üretim", "Production", "Produktion"),
"step3": ("Uygulama", "Installation", "Montage"),
"step1_b": ("PLACEHOLDER — tasarım aşamasında ne yaptığınızı anlatan kısa metin.",
            "PLACEHOLDER — a short text about what happens in the design stage.",
            "PLACEHOLDER — ein kurzer Text zur Entwurfsphase."),
"step2_b": ("PLACEHOLDER — üretim aşamasını anlatan kısa metin.",
            "PLACEHOLDER — a short text about the production stage.",
            "PLACEHOLDER — ein kurzer Text zur Produktionsphase."),
"step3_b": ("PLACEHOLDER — sahadaki uygulama ve teslim aşamasını anlatan kısa metin.",
            "PLACEHOLDER — a short text about on-site installation and handover.",
            "PLACEHOLDER — ein kurzer Text zu Montage und Übergabe vor Ort."),

# ---------------------------------------------------------------- projeler
"prj_h1":  ("Teslim Ettiğimiz İşler", "Work We Have Delivered", "Umgesetzte Projekte"),
"prj_refs": ("Referanslarımız · 21 Marka", "Our References · 21 Brands",
             "Unsere Referenzen · 21 Marken"),
"antalya_1": ("Aydınlar Interior Design Antalya projesinde, mekanın eski halinden yepyeni bir "
              "yaşam alanına dönüşümünü tamamladı. Baştan sona yenilenen bu projede, her detay "
              "titizlikle ele alındı ve ortaya modern, şık ve kullanışlı bir sonuç çıktı.",
              "In its Antalya project, Aydınlar Interior Design completed the transformation of "
              "the space from its former state into an entirely new living environment. Every "
              "detail of this full renovation was handled with care, resulting in a modern, "
              "elegant and practical space.",
              "Bei seinem Projekt in Antalya hat Aydınlar Interior Design die Verwandlung des "
              "Raumes von seinem früheren Zustand in eine völlig neue Wohnwelt abgeschlossen. "
              "Jedes Detail dieser Komplettsanierung wurde sorgfältig bearbeitet — das Ergebnis "
              "ist modern, elegant und funktional."),
"antalya_2": ("Estetik ve fonksiyonelliğin buluştuğu bu özel çalışma, modern tasarım anlayışını "
              "yaşam alanlarına en iyi şekilde yansıtıyor.",
              "Where aesthetics meets functionality, this project reflects a modern design "
              "approach in living spaces at its best.",
              "Diese besondere Arbeit, in der Ästhetik auf Funktionalität trifft, bringt modernes "
              "Designverständnis bestmöglich in Wohnräume."),

# ---------------------------------------------------------------- hakkımızda
"abt_company": ("Firma", "Company", "Unternehmen"),
"abt_brands":  ("21 Marka", "21 Brands", "21 Marken"),
"abt_brands_b": ("Perde ve ev tekstili mağazalarından yeme-içme zincirlerine ve ofislere kadar "
                 "teslim edilmiş projeler.",
                 "Projects delivered from curtain and home-textile stores to food chains and offices.",
                 "Umgesetzte Projekte – von Gardinen- und Heimtextilgeschäften bis zu "
                 "Gastronomieketten und Büros."),
"abt_note": ("PLACEHOLDER — kuruluş yılı, ekip ve atölye hakkındaki metni sen yazdığında buraya girecek.",
             "PLACEHOLDER — the text about founding year, team and workshop goes here.",
             "PLACEHOLDER — der Text zu Gründungsjahr, Team und Werkstatt kommt hierher."),
"firma_alt": ("Tüm Türkiye Mimari Konsept Mağaza · Anahtar Teslim Proje · Tasarım, Üretim, Uygulama",
              "Architectural concept stores across Türkiye · Turnkey projects · Design, production, installation",
              "Architektonische Konzeptläden türkeiweit · Schlüsselfertige Projekte · "
              "Entwurf, Produktion, Montage"),

# ---------------------------------------------------------------- iletişim
"ctc_h1":   ("Projenizi Konuşalım", "Let's Talk About Your Project",
             "Sprechen wir über Ihr Projekt"),
"ctc_lede": ("Mağaza konseptinizi konuşmak için proje yetkilimize doğrudan ulaşabilirsiniz.",
             "You can reach our project manager directly to discuss your store concept.",
             "Für Ihr Ladenkonzept erreichen Sie unseren Projektverantwortlichen direkt."),
"ctc_area": ("Çalışma Alanı", "Coverage", "Einsatzgebiet"),
"ctc_area_v": ("Tüm Türkiye", "Across Türkiye", "Türkeiweit"),
"ctc_note": ("PLACEHOLDER — adres, e-posta ve çalışma saatleri henüz yok. Bunları verdiğinde "
             "buraya eklenecek.",
             "PLACEHOLDER — address, e-mail and opening hours are not set yet.",
             "PLACEHOLDER — Adresse, E-Mail und Öffnungszeiten stehen noch aus."),

# ---------------------------------------------------------------- <head>
"desc_home": ("Aydınlar Premium Group İnşaat Ltd. Şti. — Tüm Türkiye mimari konsept mağaza, "
              "anahtar teslim proje; tasarım, üretim ve uygulama.",
              "Aydınlar Premium Group İnşaat Ltd. Şti. — architectural concept stores across "
              "Türkiye, turnkey projects; design, production and installation.",
              "Aydınlar Premium Group İnşaat Ltd. Şti. — architektonische Konzeptläden "
              "türkeiweit, schlüsselfertige Projekte; Entwurf, Produktion und Montage."),
"desc_svc":  ("Mimari konsept mağaza, anahtar teslim proje; tasarım, üretim ve uygulama.",
              "Architectural concept stores, turnkey projects; design, production and installation.",
              "Architektonische Konzeptläden, schlüsselfertige Projekte; Entwurf, Produktion und Montage."),
"desc_prj":  ("Teslim edilen konsept mağaza projeleri ve 21 marka referansı.",
              "Delivered concept store projects and 21 brand references.",
              "Umgesetzte Konzeptladen-Projekte und 21 Markenreferenzen."),
"desc_abt":  ("Tasarım manifestosu, firma bilgileri ve çalışma alanları.",
              "Design manifesto, company details and areas of work.",
              "Design-Manifest, Unternehmensangaben und Arbeitsbereiche."),
"desc_ctc":  ("İletişim: proje yetkilisi 0532 059 74 61.",
              "Contact: project manager +90 532 059 74 61.",
              "Kontakt: Projektverantwortlicher +90 532 059 74 61."),
}

IDX = {"tr": 0, "en": 1, "de": 2}


def t(key, lang):
    return T[key][IDX[lang]]
