<template>
  <div>
      <appointments v-if="authorized"></appointments>
      <doctor-login v-if="!authorized"></doctor-login>
  </div>
</template>

<script>
import chrono from '../api/chrono'
import Appointments from '@/components/doctor/appointments'
import DoctorLogin from '@/components/doctor/authForm'
export default {
  name: 'doctorManager',
  components: {
    'appointments': Appointments,
    'doctor-login': DoctorLogin
  },
  data() {
    return {
      authorized: false
    }
  },
  mounted() {
    this.checkAuth()
  },
  methods: {
    checkAuth() {
      chrono.loggedIn().then((response) => {
        this.authorized = response
      })
    }
  }
}
</script>
