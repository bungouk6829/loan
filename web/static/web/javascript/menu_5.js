$(document).ready(function(){
  function change_color(selector){
    $(selector).css('color', 'white');
    $(selector).css('background', '#2a4ed4');
    $(selector).css('border-radius', '5px');
    $(selector).css('opacity', '0.7');
  }
  selector = '#content_menu > ul > a:nth-child(1) > li'
  change_color(selector);

// 이미지를 magnific popup image viewer에 연결시킴
  $('.mg-link').magnificPopup({
    type: 'image',
    closeOnContentClick: true
  });
  
});
