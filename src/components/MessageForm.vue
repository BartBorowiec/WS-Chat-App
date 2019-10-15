<template>
    <form v-on:submit="sendMessage">
        <input type="text" placeholder="Enter message">
        <button>Send ></button>
    </form>
</template>

<script>
import SendButton from './SendButton';

export default {
    methods: {
        sendMessage(e) {
            e.preventDefault();
            websocket.send(input.value);
        }
    }
}
</script>