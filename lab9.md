# Zaliczeniowe Zadanie Laboratoryjne 3

* Należy zmodernizować wyniki zadania drugiego przerabiając serwer na RESTowy.
* Klient powinien być statycznym HTML + CSS + JS (może być serwowany przez django)
* Po załadowaniu HTML, klient powinien rozpocząć pobieranie danych z serwera. Do momentu pobrania danych klient powinien wyświetlać informacje pobrane w poprzedniej sesji przechowywane po stronie przeglądarki
* Klient powinien komunikować się z serwisem RESTowym
* Komunikacja powinna odbywać się przy wykorzystaniu JSONa
* Należy obsługiwać błędy po obu stronach
* Można wykorzystać dodatkową bibliotekę JS
* Trzeba obsłużyć odczyt i edycję (GET/POST)

# Laboratorium 9
* XmlHttpRequest
* Ajax i CSRF
* LocalStorage


# httpbin.org

Np.

```
$ curl http://httpbin.org/ip
{
  "origin": "193.0.96.15"
}
```

```
$ curl http://httpbin.org/get\?key\=value 
{
  "args": {
    "key": "value"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/7.43.0"
  }, 
  "origin": "193.0.96.15", 
  "url": "http://httpbin.org/get?key=value"
}

```

# Modyfikacja dokumentu przez jQuery

```
<!doctype html>
<meta charset="utf-8">
<html>
<body>
<h1>h1</h1>
</body>
<script type="text/javascript" charset="utf8"
src="https://code.jquery.com/jquery-3.2.1.min.js"></script>

<script>
$(document).ready(function() {
$("body h1:first").text('welcome')
})
</script>
</html>
``` 

[learn.jquery.com](https://learn.jquery.com/)

# Konsola JavaScript

```
$("h1:first").text("hello")
```

```
$.ajax({
  url: "http://httpbin.org/ip",
  success: function( result ) {
   console.log( result);
  }
});
```

[learn.jquery.com/ajax/](https://learn.jquery.com/ajax/)

# Wskazywanie elementów

Zamiast `document.getElementById('id')`

wystarczy `$(selektor CSS)` np.

```
$('#table1)

$('.inactive-user').hide()
```

# Lepsza identyfikacja

```
<!doctype html>
<meta charset="utf-8">
<html>
<body>
<h1 id="h1-1">h1</h1>
</body>
<script type="text/javascript" charset="utf8"
src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<p id="ip"></p>
<script>
$(document).ready(function() {
$("#h1-1").text('welcome')
})
</script>
</html>
```

# Jeszcze AJAX
```
$.ajax({ url: "http://httpbin.org/ip" })
  .done(function(json){ 
           $("#ip").text(json.origin);
	 })
   .fail(function(xhr, status, error) {
	     alert( "Error!" );
	     console.log( "Error: " + errorThrown );
	     console.log( "Status: " + status );
	     console.dir( xhr );
  	 })
   .always(function( xhr, status ) { alert( "Done." ); });
```


# AJAX i  CSRF

[Dokumentacja](https://docs.djangoproject.com/en/1.11/ref/csrf/#setting-the-token-on-the-ajax-request)

Używając jQuery, umoieścić w template:

```
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	    xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }}});
```

# LocalStorage

[Dokumentacja](https://developer.mozilla.org/en/docs/Web/API/Window/localStorage)

* odczyt wartości 

```
localStorage.foo
localStorage['foo']
localStorage.getItem('foo')
```

ustawianie wartości

```
localStorage.setItem('foo', 42);
localStorage['foo'] = 42;
localStorage.foo = 42
```

* usuwanie

```
localStorage.removeItem('foo');
localStorage.clear();
```

# Zdarzenia

[Demo](https://mdn.github.io/dom-examples/web-storage/)

```
window.addEventListener('storage', function(e) {
  document.querySelector('.my-key').textContent = e.key;
  document.querySelector('.my-old').textContent = e.oldValue;
  document.querySelector('.my-new').textContent = e.newValue;
  document.querySelector('.my-url').textContent = e.url;
  document.querySelector('.my-storage').textContent = e.storageArea;
});
```
