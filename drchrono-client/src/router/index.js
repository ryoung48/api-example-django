import Vue from 'vue'
import Router from 'vue-router'
import Kiosk from '@/components/Kiosk'
import DoctorLogin from '@/components/doctor/DoctorLogin'
import DoctorManager from '@/components/DoctorManager'

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
      component: DoctorLogin
    },
    {
      path: '/manager',
      name: 'Manager',
      component: DoctorManager
    },
    {
      path: '*',
      redirect: '/kiosk'
    }
  ]
})
