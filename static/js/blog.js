$(function() {
    $("#backLink").click(function(event) {
        event.preventDefault();
        history.back(1);
    });
});