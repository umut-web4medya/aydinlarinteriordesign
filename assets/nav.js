/* Üst bar — tüm sayfalarda. Mobilde menü aç/kapa, masaüstünde her zaman açık. */
(function(){
  var tog = document.querySelector('.nav-toggle');
  var nav = document.getElementById('nav');
  if(!tog || !nav) return;
  var WIDE = window.matchMedia('(min-width:981px)');

  function sync(){ nav.hidden = !WIDE.matches; tog.setAttribute('aria-expanded','false'); }
  tog.addEventListener('click', function(){
    var open = nav.hidden;
    nav.hidden = !open;
    tog.setAttribute('aria-expanded', String(open));
  });
  if(WIDE.addEventListener) WIDE.addEventListener('change', sync);
  else window.addEventListener('resize', sync);
  sync();
})();
