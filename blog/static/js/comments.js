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

    $('.cmt_del_bnt').click(function(e) {
        e.preventDefault();
        var id = $(this).attr('data-id');

        if(confirm("Are you sure you want to delete this comment?")){
              $.ajax({
              type: "POST",
              url: $('.cmt_del-frm').attr('action'),
              data: {'id': id, },
              success: function(data){
                    if(data['success'] == 1) {
                          $('#comment-div-' + id).remove()
                          if (data['count'] == 0) {
                                $('#no-comments').show()
                          }
                          else {
                                $('#no-comments').hide()
                          }
                    }
                    else {
                          alert("You don't have permission to delete this comment")
                    }
              }
          });
        }
    });
})

