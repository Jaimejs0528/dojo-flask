<template>
    <div class="home">
        <div class="content-text">
            <h1 class="title">Encuentra tu coche</h1>
            <h4>Tienda de carros online</h4>
            <hr>
            <p class="flow-text">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia, quidem quod? Architecto
                atque dolorum earum esse expedita magnam maiores neque nostrum officiis quae.
            </p>

            <button @click="redirectCars" class="btn main-button">Compra un coche</button>
            <button @click="redirectCar" class="btn main-button">Agrega un coche</button>
        </div>
        <Footer></Footer>
    </div>
</template>


<script>
    import Footer from "../components/Footer";

    export default {
        name: "Home",
        components: {Footer},
        methods: {
            redirectCars: function () {
                this.$router.push('/cars')

            },
            redirectCar: function () {
                this.$router.push('/car')
            }
        }
    }
</script>


<style scoped>
    .home {
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 100vw;
        height: calc(100vh - 60px) !important;
        background-image: url("../assets/header.jpg");
        background-color: black;
        background-size: cover;
        background-repeat: no-repeat;
    }

    .content-text {
        margin-top: -10% !important;
        width: 60% !important;
        margin-left: 10% !important;
    }

    .flow-text {
        width: 60% !important;
        font-weight: 100;
    }

    .main-button {
        border: 1px dashed #f44336;
        border-radius: 30px !important;
        background-color: #ef9a9a !important;
        color: black !important;
        transition: all 0.5s ease;
    }

    .main-button:hover {
        background-color: white !important;
        color: #f44336 !important;
    }
</style>
