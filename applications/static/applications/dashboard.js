$( document ).ready(function() {

$(".pendingrecommendation-table > tbody > tr").click(function() {
    window.location.href = $(this).attr('href');
});

 $("#request-changes").on("hide.bs.collapse", function(){
    $(".btn-request-changes").html('<span class="glyphicon glyphicon-collapse-down"></span> Request Changes');
  });
  $("#request-changes").on("show.bs.collapse", function(){
    $(".btn-request-changes").html('<span class="glyphicon glyphicon-collapse-up"></span> Request Changes');
  });
});

