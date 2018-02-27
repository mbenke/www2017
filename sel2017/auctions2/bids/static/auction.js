function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
    $('#bid').click(function() {
        var price = $('#price').val();
        $.post('/ajax/bid/', {'price': price, 'csrfmiddlewaretoken': getCookie('csrftoken')}, function(data) {
            $('#current-price').text(data);
            if (parseInt(price) < parseInt(data)) {
                alert('Podbita cena mniejsza niż obecna.');
            }
        });
    });
});
