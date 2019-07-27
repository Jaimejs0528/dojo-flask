<template>
    <div>
        <div class="add-container">
            <div class="left-side">
                <h4>Agrega un carro</h4>
                <hr>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque maiores nostrum quia sint
                    voluptate. Accusamus autem debitis ducimus eveniet fugiat harum maxime modi, obcaecati odio
                    quaerat
                    qui rem sint sit!
                </p>

                <h4>Nosotros lo vendemos</h4>
                <hr>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi autem consectetur deserunt,
                    dolor
                    eaque incidunt itaque maiores nam nesciunt pariatur placeat porro possimus quisquam quo
                    repudiandae
                    sed totam ullam vel.
                </p>
            </div>
            <div class="center-side"></div>
            <div class="right-side">
                <form @submit="sendCar" class="form-container center-align" id="carForm">
                    <h4>Ingresa los datos</h4>
                    <hr class="form-separator">
                    <div class="row">
                        <div class="input-field col s12 l6">
                            <input v-model="brand" id="brand" name="brand" type="text" class="validate"
                                   required minlength="2" maxlength="20">
                            <label for="brand">Marca</label>
                            <span class="helper-text" data-error="valor no válido" data-success="correcto"></span>

                        </div>

                        <div class="input-field col s12 l6">
                            <input v-model="model" id="model" name="model" type="text" class="validate"
                                   required minlength="1" maxlength="50">
                            <label for="model">Modelo</label>
                            <span class="helper-text" data-error="valor no válido" data-success="correcto"></span>
                        </div>
                    </div>

                    <div class="row">
                        <div class="input-field col s12 l6">
                            <input v-model="price" id="price" name="price" type="number" class="validate"
                                   required min="0">
                            <label for="price">Precio</label>
                            <span class="helper-text" data-error="valor no válido" data-success="correcto"></span>
                        </div>

                        <div class="input-field col s12 l6">
                            <input v-model="year" id="year" name="year" type="number" class="validate"
                                   required min="1800" max="2020">
                            <label for="year">Año</label>
                            <span class="helper-text" data-error="valor no válido" data-success="correcto"></span>
                        </div>
                    </div>

                    <div class="row">
                        <div class="input-field col s12">
                            <input v-model="image" id="image" name="image" type="text" class="validate"
                                   required minlength="10" maxlength="200">
                            <label for="image">Imagen</label>
                            <span class="helper-text" data-error="valor no válido" data-success="correcto"></span>
                        </div>
                    </div>

                    <div v-if="responseStatus" class="form-response">
                        <p :class="[responseStatus ? 'success-message' : 'fail-message']">{{responseMessage}}</p>
                    </div>

                    <div class="center-align">
                        <button class="btn main-button" type="submit">Enviar</button>
                    </div>
                </form>
            </div>
        </div>
        <Footer></Footer>
    </div>
</template>

<script>
    import Footer from "../components/Footer";

    const baseUrl = 'http://localhost:5000/car';
    const responseSuccessMessage = "Operación exitosa";
    const responseFailMessage = "Operación fallida";

    export default {
        name: "AddCar",
        components: {Footer},
        data() {
            return {
                responseStatus: null,
                responseMessage: "",
                brand: "",
                model: "",
                image: "",
                year: null,
                price: null
            }
        },
        methods: {
            sendCar: function (e) {
                e.preventDefault();

                if (this.checkForm()) {
                    const data = this.buildData();
                    this.$http.post(baseUrl, data)
                        .then((response) => {
                            this.responseStatus = response.data.success;
                            this.responseMessage = this.responseStatus ? responseSuccessMessage : responseFailMessage;
                            this.resetForm();
                        }).catch((error) => {
                        this.responseStatus = false;
                        this.responseMessage = responseFailMessage;
                    });
                }
            },
            checkForm: function () {
                this.errors = [];

                if (!this.brand) {
                    this.errors.push("La marca es requerida");
                }
                if (!this.model) {
                    this.errors.push("El modelo es requerido");
                }
                if (!this.year) {
                    this.errors.push("El año es requerido");
                }
                if (!this.price) {
                    this.errors.push("El precio es requerido");
                }
                if (!this.image) {
                    this.errors.push("La imagen es requerida");
                }

                if (!this.errors.length) {
                    return true;
                }
            },
            buildData() {
                return {
                    "brand": this.brand,
                    "model": this.model,
                    "image": this.image,
                    "year": this.year,
                    "price": this.price
                };
            },
            resetForm() {
                if (this.responseStatus) {
                    this.brand = "";
                    this.model = "";
                    this.image = "";
                    this.year = null;
                    this.price = null;
                }
                setTimeout(() => {
                    this.responseStatus = null;
                    this.responseMessage = "";
                }, 3000);
            }
        }
    }
</script>

<style scoped>
    .add-container {
        width: 70vw;
        margin-left: 15vw;
        height: 80vh;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
    }

    .left-side {
        flex: 40%;
    }

    .center-side {
        flex: 10%;
    }

    .right-side {
        flex: 50%;
    }

    .form-container {
        margin-top: 20px !important;
        border: 1px dashed gray;
        border-radius: 30px;
        text-align: center;
        padding: 10px 20px 10px 20px !important;
    }

    .form-container .row {
        margin: 0 !important;
        padding: 0 !important;
    }

    .form-separator {
        margin-bottom: 20px !important;
    }

    .success-message {
        color: #4caf50 !important;
    }

    .fail-message {
        color: #f44336 !important;
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
