import Vue from 'vue'
import Router from 'vue-router'
import Kiosk from '@/components/Kiosk'
import Gated from '@/components/gated/Gated'
import Manager from '@/components/manager'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/gate',
      name: 'Gate',
      component: Gated
    },
    {
      path: '/kiosk',
      name: 'Kiosk',
      component: Kiosk
    },
    {
      path: '/doctors',
      name: 'Manager',
      component: Manager
    },
    {
      path: '*',
      redirect: '/gate'
    }
  ]
})
