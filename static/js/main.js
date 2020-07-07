$(document).ready(function () {
    $('.collapsible').collapsible();
    $('select').material_select();
    $(".button-collapse").sideNav();
    $('.carousel.carousel-slider').carousel({ fullWidth: true });
  });


/* -- Flash Messages -- */
function flashed_messages() {
	$("#message").addClass("show");
    setTimeout(function () {
        $("#message").removeClass("show");
    }, 5000);
}