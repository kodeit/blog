$(document).ready(function() {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    /* Reference: Django Ajax docs */
    $('.comments').on("click", '.cmt_del_bnt', function() {
        var id = $(this).attr('data-id');
        if(confirm("Are you sure you want to delete this comment?")){
            var request = $.ajax({
                type: "POST",
                url: "/comments/delete/"+id,
                data: {'id': id, },
             });
            request.done(function(data) {
                if(data['success'] == 1) {
                    $('#comment-div-' + id).remove();
                    if (data['count'] == 0) {
                        $('#no-comments').show();
                    } else {
                        $('#no-comments').hide();
                    }
                } else {
                    alert("You don't have permission to delete this comment");
                }
            });
            request.fail(function(jqXHR, status, error) {
                alert("Failed to delete the comment", status)
            });
        }
    });

    /* Add new comment */

    $('.cmt_add-frm').submit(function(e) {
        e.preventDefault();
        var form = $(this);
        var data =  new FormData(form.get(0));

        var request = $.ajax({
            url: "/comments/create/",
            type: "POST",
            data: data,
            cache: false,
            processData: false,
            contentType: false,
        });
        request.done(function(json) {
            if (json['success'] == 0) {
                errors = ""
                for (var err in json['error']){
                    errors += "" + err + ": " + json['error'][err] + "\n"
                }
                alert(errors)
            } else {
                html = "<div id='comment-div-" +
                        json['id'] + "'>" +
                        json['html'] +
                       "</div>"
                $('.comments').prepend(html);
                $('textarea#id_comment').val(" ");
                $('#no-comments').hide()
            }
        });
        request.fail(function(jqXHR, status, error) {
           alert("Failed to create the comment", status)
        });
    });

})  /* End document ready */
