$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
    });
    $(document).ready(function () {
        $('select').formSelect();
    });
});

// function confirm_delete(){
//     var confirm_delete = confirm("Are you sure to want to delete this activity?");
//     if(confirm_delete){
//         window.location.href = "/delete_activity/<activity_id>";
//     }
// }