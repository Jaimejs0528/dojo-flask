<template>
    <div class="car-list-container">
        <div class="row">
            <div v-for="car in cars" v-if="!car.sold" class="col s12 l4">
                <div class="car-container">
                    <div class="car-image">
                        <img v-bind:src="car.image" class="car-image" alt="car image">
                    </div>
                    <div class="car-info">
                        <span class="span-feature left">{{car.brand}}</span>
                        <span class="span-feature">{{car.model}}</span>
                        <span class="span-feature right">{{car.year}}</span>
                    </div>
                    <div class="car-footer">
                        <p class="left car-price">$ {{car.price}}</p>
                        <button @click="buyCar(car)" class="right btn main-button">Comprar</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import * as M from 'materialize-css/dist/js/materialize.js'

    const getAllCarsUrl = 'http://localhost:5000/cars';
    const updateCarUrl = 'http://localhost:5000/car';
    const responseSuccessMessage = "Operación exitosa";
    const responseFailMessage = "Operación fallida";

    export default {
        name: "CarList",
        data() {
            return {
                cars: [],
                success: false
            }
        },
        mounted() {
            this.updateCarsList();
        },
        methods: {
            buyCar: function (car) {
                car.sold = true;
                this.$http.put(updateCarUrl, car)
                    .then((response) => {
                        this.showResponseMessage(response.data.success);
                        this.updateCarsList();
                    }).catch((error) => {
                    console.log(error);
                });
            },
            updateCarsList: function () {
                this.$http.get(getAllCarsUrl)
                    .then((response) => {
                        this.cars = response.data.data;
                    }).catch((error) => {
                    console.log(error);
                });
            },
            showResponseMessage: function (success) {
                if (success) {
                    M.toast({
                        html: responseSuccessMessage,
                        classes: 'toast-success-response'
                    });
                } else {
                    M.toast({
                        html: responseFailMessage,
                        classes: 'toast-fail-response'
                    });
                }
            }
        }
    }
</script>


<style scoped>
    .car-list-container {
        width: 90vw;
        margin-left: 5vw;
        margin-top: 100px !important;
    }

    .car-container {
        border: 1px dashed gray;
        padding: 20px 20px 20px 20px !important;
    }

    .car-image {
        width: 100% !important;
        height: 250px !important;
        max-height: 300px !important;
    }

    .car-info {
        margin-top: 10px !important;
        margin-bottom: 10px !important;
    }

    .span-feature {
        display: inline-block;
        padding: 5px 10px 5px 10px !important;
        border: 1px dashed blue;
        border-radius: 30px !important;
    }

    .car-info-text > b {
        font-size: 36px !important;
        font-weight: 100 !important;
    }


    .car-price {
        margin-top: -0px !important;
        font-size: 28px !important;
        font-weight: bold;

    }

    .car-footer {
        margin: 0 auto !important;
        padding: 0 !important;
        height: 30px !important;
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
