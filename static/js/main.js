/* -- Ready function --*/
$(document).ready(function () {
    $('.collapsible').collapsible();
    $('select').material_select();
    $('.button-collapse').sideNav();
});

/* -- Slider activation -- */
$(document).ready(function(){
    $('.slider').slider();
  });


/* -- Flash Messages -- */
function flashed_messages() {
    $("#message").addClass("show");
    setTimeout(function () {
        $("#message").removeClass("show");
    }, 5000);
}