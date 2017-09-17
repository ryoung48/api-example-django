import Vue from 'vue'
import Router from 'vue-router'
import Kiosk from '@/components/Kiosk'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Kiosk',
      component: Kiosk
    }
  ]
})
