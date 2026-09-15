(function(){
  var hero   = document.getElementById('hero');
  if(!hero) return;                                   /* iç sayfalarda deste yok */
  var slides = Array.prototype.slice.call(hero.querySelectorAll('.slide'));
  var panels = Array.prototype.slice.call(hero.querySelectorAll('.panel'));
  var imgs   = slides.map(function(sl){ return sl.querySelectorAll('img[data-src]'); });
  var index  = 0, locked = false;

  /* görseller: ilk kare HTML'de yüklenir, kalanlar gerektiğinde */
  function gorseliYukle(liste){
    if(!liste) return;
    Array.prototype.forEach.call(liste, function(img){
      if(!img.dataset.src) return;
      if(img.dataset.srcset) img.srcset = img.dataset.srcset;
      img.src = img.dataset.src;
      delete img.dataset.src;
      delete img.dataset.srcset;
    });
  }
  var SPEED  = 1100;                                  /* CSS'teki --kup-sure ile aynı */
  var girisT = null;                                  /* içeriğin yükselme animasyonu */
  var DECK   = window.matchMedia('(min-width:981px)');

  /* küp derinliği = kutunun genişliği; yoksa dönüş yamuk görünür */
  function sizeCube(){
    if(!DECK.matches) return;
    var w = panels[0].getBoundingClientRect().width;
    if(w) hero.style.setProperty('--cw', Math.round(w) + 'px');
  }

  function park(el, deg){                             /* geçişsiz konumlandır */
    el.classList.add('no-anim');
    el.style.setProperty('--a', deg + 'deg');
    el.style.setProperty('--sh', '.85');              /* yan yüz karanlıkta başlar */
    void el.offsetWidth;                              /* reflow: açı uygulansın */
    el.classList.remove('no-anim');
  }

  function show(next, dir){
    if(!DECK.matches || locked) return;
    var n = slides.length;
    next = ((next % n) + n) % n;
    if(next === index) return;
    if(!dir) dir = (next === (index + 1) % n) ? 1 : (next === (index - 1 + n) % n ? -1 : (next > index ? 1 : -1));

    gorseliYukle(imgs[next]);                         /* hedefin karesi hazır olsun */

    var geri = dir < 0;

    /* görsel tarafı: giden kare üstte kalıp perde gibi çekilir */
    var eski = slides[index];
    eski.classList.remove('is-active');
    eski.classList.toggle('geri', geri);
    eski.classList.add('is-leaving');
    eski.setAttribute('aria-hidden','true');

    /* kutu tarafı: küp 90° döner */
    var out = panels[index], inc = panels[next];
    clearTimeout(girisT);
    panels.forEach(function(p){ p.classList.remove('is-entering'); });
    out.classList.remove('is-active');
    out.classList.add('is-leaving');
    out.style.setProperty('--a', (dir > 0 ? -90 : 90) + 'deg');
    out.style.setProperty('--sh','.85');              /* dönüp giden yüz kararır */

    park(inc, dir > 0 ? 90 : -90);                    /* reflow burada: animasyonlar baştan başlar */
    inc.style.setProperty('--a','0deg');
    inc.style.setProperty('--sh','0');                /* öne gelen yüz aydınlanır */
    inc.classList.toggle('geri', geri);
    inc.classList.add('is-active', 'is-entering');
    girisT = setTimeout(function(){ inc.classList.remove('is-entering'); }, 1800);

    hero.classList.remove('is-turning');
    void hero.offsetWidth;
    hero.classList.add('is-turning');                 /* küpün geri çekilip öne gelmesi */

    index = next;
    slides[index].classList.add('is-active');
    slides[index].removeAttribute('aria-hidden');
    if(history.replaceState) history.replaceState(null,'','#slayt-'+(index+1));

    locked = true;
    setTimeout(function(){
      out.classList.remove('is-leaving');
      park(out, 90);
      eski.classList.add('park');                     /* gizliyken konumunu geçişsiz sıfırla */
      eski.classList.remove('is-leaving');
      void eski.offsetWidth;
      eski.classList.remove('park');
      hero.classList.remove('is-turning');
      locked = false;
    }, SPEED);
  }

  hero.querySelectorAll('.hero-nav button').forEach(function(b){
    var d = Number(b.dataset.dir);
    b.addEventListener('click', function(){ show(index + d, d); });
  });

  /* tekerlek: sayfa kaymaz, deste döner.
     Kutu kendi içinde kayabiliyorsa önce ona hakkını ver. */
  hero.addEventListener('wheel', function(e){
    if(!DECK.matches) return;
    var box = e.target.closest ? e.target.closest('.panel-scroll') : null;
    if(box && box.scrollHeight > box.clientHeight + 2){
      var atTop = box.scrollTop <= 0;
      var atEnd = box.scrollTop + box.clientHeight >= box.scrollHeight - 1;
      if((e.deltaY < 0 && !atTop) || (e.deltaY > 0 && !atEnd)) return;
    }
    e.preventDefault();
    if(locked || Math.abs(e.deltaY) < 6) return;
    var d = e.deltaY > 0 ? 1 : -1;
    show(index + d, d);
  }, {passive:false});

  document.addEventListener('keydown', function(e){
    if(!DECK.matches) return;
    if(e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === 'PageDown'){ e.preventDefault(); show(index+1, 1); }
    else if(e.key === 'ArrowLeft' || e.key === 'ArrowUp' || e.key === 'PageUp'){ e.preventDefault(); show(index-1, -1); }
  });

  var y0=null, x0=null;
  hero.addEventListener('touchstart', function(e){ y0=e.touches[0].clientY; x0=e.touches[0].clientX; }, {passive:true});
  hero.addEventListener('touchend', function(e){
    if(!DECK.matches || y0===null) return;
    var dy=y0-e.changedTouches[0].clientY, dx=x0-e.changedTouches[0].clientX;
    var d = Math.abs(dx) > Math.abs(dy) ? dx : dy;
    if(Math.abs(d) > 45){ var s = d > 0 ? 1 : -1; show(index + s, s); }
    y0=x0=null;
  }, {passive:true});

  /* kaydırma göstergesi: yalnız taşan metinde görünür */
  hero.querySelectorAll('.panel-scroll').forEach(function(box){
    var hint = box.parentNode.querySelector('.scroll-hint');
    var dot  = hint && hint.querySelector('b');
    if(!dot) return;
    function sync(){
      var max = box.scrollHeight - box.clientHeight;
      hint.classList.toggle('is-on', max > 4);
      dot.style.top = (max > 4 ? (box.scrollTop / max) * 100 : 0) + '%';
    }
    box.addEventListener('scroll', sync);
    window.addEventListener('resize', sync);
    sync();
  });

  /* sayfa oturduktan sonra kalan kareleri sessizce indir */
  function kalanlariYukle(){ imgs.forEach(gorseliYukle); }
  if(document.readyState === 'complete') setTimeout(kalanlariYukle, 800);
  else window.addEventListener('load', function(){ setTimeout(kalanlariYukle, 800); });

  /* ilk kurulum */
  panels.forEach(function(el, i){
    if(i !== 0){ el.style.setProperty('--a','90deg'); el.style.setProperty('--sh','.85'); }
  });
  panels[0].style.setProperty('--a','0deg');
  panels[0].style.setProperty('--sh','0');
  sizeCube();
  window.addEventListener('resize', sizeCube);
  if(DECK.addEventListener) DECK.addEventListener('change', sizeCube);

  /* mobil: deste yok; kareler ekrana girerken perde gibi açılır.
     İlk kare CSS animasyonuyla açılır (site.css), burada yalnız açık işaretlenir. */
  if(!DECK.matches && 'IntersectionObserver' in window &&
     !window.matchMedia('(prefers-reduced-motion:reduce)').matches){
    var gozcu = new IntersectionObserver(function(kayitlar){
      kayitlar.forEach(function(k){
        if(k.isIntersecting){ k.target.classList.add('is-in'); gozcu.unobserve(k.target); }
      });
    }, {rootMargin:'0px 0px -8% 0px', threshold:0.05});
    hero.querySelectorAll('.slide-media').forEach(function(el){
      if(el.closest('.slide') === slides[0]) el.classList.add('is-in');
      else gozcu.observe(el);
    });
    hero.classList.add('medya-gozcu');
  }

  var m = /^#slayt-(\d+)$/.exec(location.hash);
  if(m && slides[m[1]-1]) show(Number(m[1]) - 1, 1);
})();
