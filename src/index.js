var websocket = new WebSocket('ws://localhost:8765');

var form = document.querySelector('form');
var input = document.querySelector('#message');

form.addEventListener('submit', function(e) {
    e.preventDefault();

    websocket.send(input.value);
})

websocket.onmessage = function(event) {
    console.log(event);
}