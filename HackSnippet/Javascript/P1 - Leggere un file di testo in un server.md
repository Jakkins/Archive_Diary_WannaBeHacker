

## XMLHttpRequest

- onreadystatechange
- readyState
  - readyState is a property of xmlhttp
  - there are 5 types (2013)
    - 0 = req has not been sent
    - 1 = connection with the server established
    - 2 = req received by the server
    - 3 = server is processing the req
    - 4 = req finished to be processed and res is ready
- responseText
- open
- send


## Short answer

```javascript
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       // Action to be performed when the document is read;
       console.log(xmlreq.responseText)
    }
};
xhttp.open("GET", "filename", true);
xhttp.send();
```

## Long answer

[source](https://www.youtube.com/watch?v=4LyXm-4AGUw)

```javascript
let xmlreq
// if the window support XMLHttpRequest
if(window.XMLHttpRequest) {
   xmlreq = new XMLHttpRequest()
}
else {
  // IE 4 or 5... Ancient History...
  xmlreq = new ActiveXObject("Microsoft.XMLHTTP")
}

// if there is any change at all, fire this function
xmlreq.onreadystatechange = function() {
  if(xmlreq.readyState == 4) {
    // use the ID of a div
    document.getElementById('resultDiv').innerHTML = xmlreq.responseText;
  }
  
  // method, file url, asynchronous
  xmlreq.open("GET", "text.txt", true)
  xmlreq.send()
  
}
```
