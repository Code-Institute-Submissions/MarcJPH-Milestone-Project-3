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

function confirm_delete() {
    var confirmation = confirm("Are you sure to want to delete this activity?");
    if (confirmation) {
        window.location.href = "{{ url_for('delete_activity', activity_id=places._id) }}";
        alert("The activity has been deleted");
    }
    else {
        alert("The activity was not deleted");
    }
}