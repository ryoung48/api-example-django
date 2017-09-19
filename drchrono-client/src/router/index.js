import Vue from 'vue'
import Router from 'vue-router'
import Kiosk from '@/components/Kiosk'
import Login from '@/components/doctor/Login'
import Appointments from '@/components/doctor/Appointments'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/kiosk',
      name: 'Kiosk',
      component: Kiosk
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/appointments',
      name: 'Appointments',
      component: Appointments
    },
    {
      path: '*',
      redirect: '/kiosk'
    }
  ]
})
