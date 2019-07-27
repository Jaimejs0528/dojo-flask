<template>
    <div class="navbar-container">
        <nav>
            <div class="nav-wrapper">
                <a href="#" class="brand-logo">
                    <img src="../assets/icon.png" alt="icon">
                </a>
                <ul id="nav-mobile" class="right hide-on-med-and-down nav-list">
                    <li><router-link class="router-link" to="/">Inicio</router-link></li>
                    <li><router-link class="router-link" to="/cars">Comprar</router-link></li>
                    <li><router-link class="router-link" to="/car">Agregar</router-link></li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>
    export default {
        name: "Navbar"
    }
</script>

<style scoped>
    nav{
        background-color: transparent !important;
    }

    .navbar-container{
        top: 0;
        position: fixed !important;
        width: 100vw !important;
        background-color: white !important;
    }

    .nav-wrapper{
        border: 1px solid gray;
        color: black
    }

    .nav-list{
        width: 40vw !important;
        margin-right: 40px !important;
    }

    .nav-list li{
        width: 33% !important;
    }

    .router-link{
        color: black !important;
        text-align: center !important;
    }

    .brand-logo{
        margin-left: 40px !important;
        padding: 10px !important;;
    }

    .brand-logo img{
        height: 50px !important;
        width: 50px !important;
    }
</style>
