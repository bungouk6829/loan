$(document).ready(function(){
  function change_color(selector){
    $(selector).css('color', 'white');
    $(selector).css('background', '#b74aff');
    $(selector).css('border-radius', '5px');
    $(selector).css('opacity', '0.7');
  }

  href = window.location.href.replace("http://xn--620b86bm2f81gduat3p7lmnlx.com/","");

  if (href == "investor"){
    selector = '#content_menu > ul > a:nth-child(1) > li'
    change_color(selector);
  }
});
