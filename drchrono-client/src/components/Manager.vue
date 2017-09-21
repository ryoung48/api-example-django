<template>
  <div>
      <appointments v-if="authorized"></appointments>
      <auth-form v-if="!authorized"></auth-form>
  </div>
</template>

<script>
import chrono from '../api/chrono'
import Appointments from '@/components/doctor/appointments'
import AuthForm from '@/components/doctor/authForm'
export default {
  name: 'manager',
  components: {
    'appointments': Appointments,
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
