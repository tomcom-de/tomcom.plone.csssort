$(document).ready(function() {

    $("#sortable").sortable();

    $(".css-save").click(function(event) {
        event.preventDefault();

        elements=$('.sort-index')

        for (var i = 0; i <= elements.length; i++) {

            $(elements[i]).attr('value',i);
        }

        $("#save-css-form").submit()
    });

    $(".remove").click(function(event) {
        check = confirm('Really?');
        if (check == false) {
            return false;
        }
    });

    $('.tool-tip').tooltip();

});