/* Tüm sayfalarda çalışan arayüz davranışları:
   mobil menü · kaydırınca koyulaşan üst bar · bloklerın açılması        */
(function(){
  "use strict";

  /* ---------------------------------------------------------- mobil menü
     Menü paneli üst barın İÇİNDE ve position:absolute.
     backdrop-filter'lı bir atanın içinde position:fixed, ekrana göre değil
     o ataya göre hizalanır — o yüzden fixed kullanılmıyor. */
  var tog  = document.querySelector('.nav-toggle');
  var nav  = document.getElementById('nav');
  var head = document.getElementById('head');
  var GENIS = window.matchMedia('(min-width:1041px)');

  function esitle(){
    nav.hidden = !GENIS.matches;
    tog.setAttribute('aria-expanded', 'false');
  }
  function kapat(){
    if(GENIS.matches) return;
    nav.hidden = true;
    tog.setAttribute('aria-expanded', 'false');
  }

  if(tog && nav){
    tog.addEventListener('click', function(e){
      e.stopPropagation();
      var acik = nav.hidden;
      nav.hidden = !acik;
      tog.setAttribute('aria-expanded', String(acik));
    });
    nav.addEventListener('click', function(e){ if(e.target.closest('a')) kapat(); });
    document.addEventListener('click', function(e){
      if(!GENIS.matches && !nav.hidden && !e.target.closest('.site-head')) kapat();
    });
    document.addEventListener('keydown', function(e){ if(e.key === 'Escape') kapat(); });
    if(GENIS.addEventListener) GENIS.addEventListener('change', esitle);
    else window.addEventListener('resize', esitle);
    esitle();
  }

  /* ------------------------------------------------- kaydırınca üst bar */
  if(head){
    var son = null;
    var bakis = function(){
      var simdi = window.scrollY > 12;
      if(simdi !== son){ head.classList.toggle('is-stuck', simdi); son = simdi; }
    };
    window.addEventListener('scroll', bakis, {passive:true});
    bakis();
  }

  /* ------------------------------------------------------ blok açılması
     <head>'deki satır içi betik html'e .js-reveal ekler; burada yalnız
     görünür hale gelenlere .is-in konur. Betik yoksa her şey görünür. */
  var hedefler = document.querySelectorAll('.reveal');
  if(!hedefler.length) return;
  if(!('IntersectionObserver' in window) ||
     window.matchMedia('(prefers-reduced-motion:reduce)').matches){
    document.documentElement.classList.remove('js-reveal');
    return;
  }
  var gozcu = new IntersectionObserver(function(kayitlar){
    kayitlar.forEach(function(k){
      if(k.isIntersecting){ k.target.classList.add('is-in'); gozcu.unobserve(k.target); }
    });
  }, {rootMargin:'0px 0px -12% 0px', threshold:0.08});
  hedefler.forEach(function(el){ gozcu.observe(el); });
})();

/* --------------------------------------------------------------- lüks imleç
   Yalnız gerçek fare olan cihazlarda. Konum rAF içinde yumuşatılarak sürülür;
   hiçbir düzen özelliğine dokunmaz, sadece transform — 60fps kalır.            */
(function(){
  "use strict";
  var ince = window.matchMedia('(hover:hover) and (pointer:fine)');
  var sakin = window.matchMedia('(prefers-reduced-motion:reduce)');
  if(!ince.matches || sakin.matches) return;

  var nokta = document.createElement('div');
  nokta.className = 'cursor';
  nokta.setAttribute('aria-hidden', 'true');
  document.body.appendChild(nokta);

  var hx = innerWidth / 2, hy = innerHeight / 2, x = hx, y = hy, calisiyor = false;

  function dongu(){
    x += (hx - x) * 0.18;               /* yumuşatma */
    y += (hy - y) * 0.18;
    nokta.style.transform = 'translate3d(' + (x - 4.5) + 'px,' + (y - 4.5) + 'px,0)';
    if(Math.abs(hx - x) > .1 || Math.abs(hy - y) > .1) requestAnimationFrame(dongu);
    else calisiyor = false;
  }

  document.addEventListener('pointermove', function(e){
    hx = e.clientX; hy = e.clientY;
    if(!nokta.classList.contains('is-on')) nokta.classList.add('is-on');
    if(!calisiyor){ calisiyor = true; requestAnimationFrame(dongu); }
  }, {passive:true});

  document.addEventListener('pointerover', function(e){
    var t = e.target.closest && e.target.closest('a,button,.shot,.card,.chips li');
    nokta.classList.toggle('is-over', !!t);
  }, {passive:true});

  document.addEventListener('pointerleave', function(){ nokta.classList.remove('is-on'); });
  document.addEventListener('mouseleave', function(){ nokta.classList.remove('is-on'); });
})();
