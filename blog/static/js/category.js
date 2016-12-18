$(document).ready(function(){
    $('#mbtn').click(function(e) {
        $('#cat-modal').modal('show');
    });

    $('#name-group').click(function(){
        $('#name-group').removeClass("has-error");
    });

    $('#description-group').click(function(){
        $('#description-group').removeClass("has-error");
    });

    $("#cat-form").submit(function(event){
        event.preventDefault();
        var form = $(this);
        var data =  new FormData(form.get(0));

        var request = $.ajax({
            url: $('.addcat').attr('action'),
            type: "POST",
            data: data,
            cache: false,
            processData: false,
            contentType: false,
        });

        request.done(function(json) {
            $('#id_category').append($('<option>', {
                value:json['id'],
                text:json['name']
            }));
            $('#cat-modal').modal('hide');
        });

        request.fail(function(jqXHR, status, error) {
            $.each(jqXHR.responseJSON, function(i, err) {
               $('#'+i+'-group').addClass('has-error');
               $('#'+i+'-group').append('<div class="help-block">' + err + '</div>');
            });
        });
    });
});

