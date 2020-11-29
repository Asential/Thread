document.addEventListener('DOMContentLoaded', function() {
    $(".reply_btn").click(function () {
        $(this).parent().children('.reply-form').show();
        $(this).hide();
    });
    $(".cancel_btn").click(function(){
        $(this).parent().hide();
        $(this).parent().parent().children('.reply_btn').show();
      });
});