$( document ).ready(function() {

$(".pendingrecommendation-table > tbody > tr").click(function() {
    window.location.href = $(this).attr('href');
});

});

