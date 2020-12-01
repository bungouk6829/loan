$(document).ready(function(){
  function change_color(selector){
    $(selector).css('color', 'white');
    $(selector).css('background', '#2a4ed4');
    $(selector).css('border-radius', '5px');
    $(selector).css('opacity', '0.7');
  }
  selector = '#content_menu > ul > a:nth-child(1) > li'
  change_color(selector);

});
