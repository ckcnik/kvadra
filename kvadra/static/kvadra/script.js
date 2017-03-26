$(document).ready(function() {

    $('#form-send-text button').on('click', function() {

        var form = $(this).parents('form');
        $.ajax({
            type: form.attr('method'),
            url: form.attr('action'),
            data: form.serialize(),
            dataType: 'json',

            success: function (response) {
                form.find('textarea').val('');
                alert("Saved");
            },
            error: function (response) {
                var errors = JSON.parse(response.responseText);
                alert(errors.text[0]);
            }
        });
        return false;
    });
});
