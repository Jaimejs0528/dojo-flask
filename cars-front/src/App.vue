<template>
    <div id="app">
        <Navbar></Navbar>
        <router-view/>
    </div>
</template>

<script>
    import Navbar from "./components/Navbar";

    export default {
        components: {Navbar}
    }
</script>

<style>
    @import url('https://fonts.googleapis.com/css?family=Ubuntu&display=swap');

    #app {
        font-family: 'Ubuntu', sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c3e50;
        margin-top: 60px;
    }

    .toast-fail-response {
        border: 1px dashed #f44336 !important;
        background-color: #ef9a9a !important;
        border-radius: 30px !important;
        color: #000 !important;
    }

    .toast-success-response {
        border: 1px dashed #4caf50 !important;
        background-color: #a5d6a7 !important;
        border-radius: 30px !important;
        color: #000 !important;
    }
</style>
