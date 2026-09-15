# -*- coding: utf-8 -*-
"""Tekrar eden küçük işaretleme parçaları — ikonlar ve düğmeler."""

OK_SAG = ('<svg class="arw" viewBox="0 0 16 16" fill="none" stroke="currentColor" '
          'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
          '<path d="M2 8h12M9.5 3.5L14 8l-4.5 4.5"/></svg>')

DESTE_SOL = ('<svg viewBox="0 0 20 14" fill="none" stroke="currentColor" stroke-width="1.5" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M19 7H1M1 7l5.5-5M1 7l5.5 5"/></svg>')

DESTE_SAG = ('<svg viewBox="0 0 20 14" fill="none" stroke="currentColor" stroke-width="1.5" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M1 7h18M18.5 7L13 2M18.5 7L13 12"/></svg>')

INSTAGRAM = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
             'aria-hidden="true"><rect x="2.8" y="2.8" width="18.4" height="18.4" rx="5.4"/>'
             '<circle cx="12" cy="12" r="4.1"/>'
             '<circle cx="17.4" cy="6.6" r="1.25" fill="currentColor" stroke="none"/></svg>')


def btn(metin, href, tur="", ok=True):
    """Cam düğme. tur: '' | 'btn-accent' | 'btn-quiet'"""
    sinif = ("btn " + tur).strip()
    return f'<a class="{sinif}" href="{href}">{metin}{OK_SAG if ok else ""}</a>'
