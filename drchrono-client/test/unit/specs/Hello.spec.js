import Vue from 'vue'
import Kiosk from '@/components/Kiosk'

describe('Kiosk.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(Kiosk)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.Kiosk h1').textContent)
      .to.equal('Check-in Kiosk')
  })
})
