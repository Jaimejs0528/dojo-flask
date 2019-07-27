import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

import 'materialize-css/dist/css/materialize.css'
import 'materialize-css/dist/js/materialize.js'
import Router from "vue-router";

Vue.config.productionTip = false
Vue.prototype.$http = axios

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
