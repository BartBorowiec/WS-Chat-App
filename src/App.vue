<template>
    <h1>Welcome to ChatApp!</h1>
</template>

<script>
var websocket = new WebSocket('ws://localhost:8765');

// var form = document.querySelector('form');
// var input = document.querySelector('#message');

// form.addEventListener('submit', function(e) {
//     e.preventDefault();

//     websocket.send(input.value);
// })

websocket.onmessage = function(event) {
    console.log(event)
}
websocket.onopen = function(event) {
    console.log('hello');
    websocket.send('hello server');
}

</script>

<style lang="scss">
    body {
        background-color: aqua;
    }
    h1 {
        text-align: center;
        font-family: 'Roboto', Arial, sans-serif;
    }
</style>