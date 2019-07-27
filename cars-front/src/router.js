import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import ListCars from "./views/ListCars";
import AddCar from "./views/AddCar";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/cars',
      name: 'cars',
      component: ListCars
    },
    {
      path: '/car',
      name: 'car',
      component: AddCar
    }
  ]
})
