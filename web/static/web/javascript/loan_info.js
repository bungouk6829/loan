$(document).ready(function(){
  function change_color(selector){
    $(selector).css('color', 'white');
    $(selector).css('background', '#b74aff');
    $(selector).css('border-radius', '5px');
    $(selector).css('opacity', '0.7');
  }

  href = window.location.href.replace("http://127.0.0.1:8000/","");

  if (href == "worker"){
    selector = '#content_menu > ul > a:nth-child(1) > li'
    change_color(selector);
  }

  else if (href == "business"){
    selector = '#content_menu > ul > a:nth-child(2) > li'
    change_color(selector);
  }

  else if (href == "woman"){
    selector = '#content_menu > ul > a:nth-child(3) > li'
    change_color(selector);
  }

  else if (href == "jobless"){
    selector = '#content_menu > ul > a:nth-child(4) > li'
    change_color(selector);
  }

  else if (href == "cosmetic"){
    selector = '#content_menu > ul > a:nth-child(5) > li'
    change_color(selector);
  }

  else if (href == "estate"){
    selector = '#content_menu > ul > a:nth-child(1) > li'
    change_color(selector);
  }

  else if (href == "gold"){
    selector = '#content_menu > ul > a:nth-child(2) > li'
    change_color(selector);
  }

  else if (href == "leisure"){
    selector = '#content_menu > ul > a:nth-child(3) > li'
    change_color(selector);
  }

  else if (href == "car"){
    selector = '#content_menu > ul > a:nth-child(4) > li'
    change_color(selector);
  }

  else if (href == "motor"){
    selector = '#content_menu > ul > a:nth-child(5) > li'
    change_color(selector);
  }
});
