$(document).ready(function(){
  function change_color(selector){
    $(selector).css('color', 'white');
    $(selector).css('background', '#b74aff');
    $(selector).css('border-radius', '5px');
    $(selector).css('opacity', '0.7');
  }
  selector = '#content_menu > ul > a:nth-child(2) > li'
  change_color(selector);

});
