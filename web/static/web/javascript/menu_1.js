$(document).ready(function(){
  function change_color(selector){
    $(selector).css('color', 'white');
    $(selector).css('background', '#2a4ed4');
    $(selector).css('border-radius', '5px');
    $(selector).css('opacity', '0.7');
  }

  href = window.location.href.replace("http://kbu6829.pythonanywhere.com/","");

  if (href == "company"){
    selector = '#content_menu > ul > a:nth-child(1) > li'
    change_color(selector);
  }
  else if (href == "history"){
    selector = '#content_menu > ul > a:nth-child(2) > li'
    change_color(selector);
  }
  else if (href == "organization"){
    selector = '#content_menu > ul > a:nth-child(3) > li'
    change_color(selector);
  }
  else if (href == "management"){
    selector = '#content_menu > ul > a:nth-child(4) > li'
    change_color(selector);
  }
  else if (href == "map"){
    selector = '#content_menu > ul > a:nth-child(5) > li'
    change_color(selector);
  }
});
