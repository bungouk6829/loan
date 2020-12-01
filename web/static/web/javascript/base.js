$(document).ready(function(){
  $('.main_menu>li').hover(function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','#528afa');
    $(this).find('ul').slideDown(100);
    $(this).find('ul').css('display','flex');
  },function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
    $(this).find('ul').slideUp(100);
  });
  $('.sub_menu>ul>li').hover(function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','#528afa');
  },function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
  });
  $('#header_section > div.mobile_toggle_menu_btn > img').click(function(){
    $('.mobile_menu>li').find('ul').hide();
    $('.mobile_menu').toggle(200);
  });
  $('.mobile_menu>li').click(function(){
    $('.mobile_menu>li').find('ul').hide();
    $(this).find('ul').toggle(100);
  });
});
