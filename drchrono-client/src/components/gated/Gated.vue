<template>
  <div>
      <kiosk v-if="authorized"></kiosk>
      <auth-form v-if="!authorized"></auth-form>
  </div>
</template>

<script>
import chrono from '../../api/chrono'
import Kiosk from '@/components/Kiosk'
import AuthForm from '@/components/doctor/authForm'
export default {
  name: 'manager',
  components: {
    'kiosk': Kiosk,
    'auth-form': AuthForm
  },
  mounted() {
    this.checkAuth()
  },
  computed: {
    authorized: function() {
      return this.$store.getters.authorized
    }
  },
  methods: {
    checkAuth() {
      chrono.loggedIn().then((response) => {
        this.$store.commit('setAuthorized', response)
      })
    }
  }
}
</script>
