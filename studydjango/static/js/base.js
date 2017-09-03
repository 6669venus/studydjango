function baseInit() {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
}

function setMyIp(toSpan) {
    $.getJSON('//api.ipify.org?format=jsonp&callback=?', function(data) {
        toSpan.text(data.ip);
    });
    //return "Ok " + ip;
    // var res = $.ajax({
    //     url: '//api.ipify.org?format=jsonp&callback=',
    //     async: false
    // }).responseText;

    // console.log("'" + res + "'");
    // return res;
    
}
