# jshint

[jshint.com](http://jshint.com)

```
$ npm install -g jshint
/usr/local/bin/jshint -> /usr/local/lib/node_modules/jshint/bin/jshint
jshint@2.9.4 /usr/local/lib/node_modules/jshint
```

# Użycie

```
$ cat foo1.js
$(document).ready(function() {
$("body h1:first").text('welcome')
})
$ jshint foo1.js
foo1.js: line 2, col 35, Missing semicolon.
foo1.js: line 3, col 3, Missing semicolon.

2 errors
$ cat foo2.js
$(document).ready(function() {
    $("body h1:first").text('welcome');
    });
$ jshint foo2.js
```

# `--show-non-errors`

```
$ jshint --show-non-errors foo2.js

foo2.js :
	Implied globals:
			$: 1,2
			document: 1
```

# `.jshintrc`

```
$ emacs .jshintrc
$ cat .jshintrc
{
 "browser": true,
  "jquery" : true
}
$ jshint --show-non-errors foo2.js
$ jshint --show-non-errors foo2.js && echo $?
  0
```

# HTML

```
✗ jshint jquery2.html
jquery2.html: line 1, col 1, Expected an identifier and instead saw '<'.
jquery2.html: line 1, col 2, Expected an operator and instead saw '!'.
jquery2.html: line 1, col 2, Expected an assignment or function call and instead saw an expression.
jquery2.html: line 1, col 3, Missing semicolon.
jquery2.html: line 1, col 3, Expected an assignment or function call and instead saw an expression.
jquery2.html: line 1, col 10, Missing semicolon.
jquery2.html: line 2, col 1, Expected an identifier and instead saw '<'.
jquery2.html: line 2, col 1, Unrecoverable syntax error. (13% scanned).

8 errors
```

# --extract

```
$ jshint --extract=auto jquery2.html
jquery2.html: line 11, col 35, Missing semicolon.
jquery2.html: line 12, col 3, Missing semicolon.

2 errors
$ cat jquery2.html
<!doctype html>
<meta charset="utf-8">
<html>
<body>
<h1 id="h1-1">h1</h1>
</body>
<script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<p id="ip"></p>
<script>
$(document).ready(function() {
$("body h1:first").text('welcome')
})
</script>
</html>
```
