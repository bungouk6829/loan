$(document).ready(function(){
// 메뉴 마우스 호버 글씨색 바뀜
// $('#content_menu > ul > a > li').hover(function(){
//   $(this).css('transition','.1s ease');
//   $(this).css('color','#528afa');
// },function(){
//   $(this).css('transition','.1s ease');
//   $(this).css('color','#4d4d4d;');
// });
// 현재페이지의 메뉴칸만 색이 바뀜
  function change_color(selector){
    $(selector).css('color', 'white');
    $(selector).css('background', '#2a4ed4');
    $(selector).css('border-radius', '5px');
    $(selector).css('opacity', '0.7');
  }

  selector = '#content_menu > ul > a:nth-child(1) > li'
  change_color(selector);

});
