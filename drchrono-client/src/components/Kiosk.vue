<template>
  <div>
    <v-layout row wrap class="content">
      <v-flex>
        <h1>Check-in Kiosk</h1>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs4 offset-xs4>
        <v-card>
          <doctors :doctors="doctors.checked_in" title="Doctors Available" :action="selectDoctor"></doctors>
          <v-divider></v-divider>
          <doctors v-if="!selectedDoctor" :doctors="doctors.checked_out" title="Doctors Unavailable" :disabled="true"></doctors>
        </v-card>
        <patient v-if="selectedDoctor" :doctor="selectedDoctor" :action="sendAlert" :close="unSelectDoctor"></patient>
        <v-alert :success="alertType === 'success'" :error="alertType === 'error'" :info="alertType === 'info'" :value="alert" transition="scale-transition">
          {{alertMsg}}
        </v-alert>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import chrono from '../api/chrono'
import Doctors from '@/components/kiosk/doctors'
import Patient from '@/components/kiosk/patient'
export default {
  name: 'kiosk',
  components: {
    'doctors': Doctors,
    'patient': Patient
  },
  data() {
    return {
      doctors: { checked_in: [], checked_out: [] },
      selectedDoctor: undefined,
      alert: false,
      alertMsg: '',
      alertType: 'error',
      loggedIn: chrono.loggedIn
    }
  },
  mounted() {
    this.getDoctors()
    setInterval(this.getDoctors, 1000 * 300)
  },
  methods: {
    getDoctors() {
      chrono.doctors().then((response) => {
        this.doctors = response
      })
    },
    selectDoctor(doctor) {
      this.selectedDoctor = doctor
    },
    unSelectDoctor() {
      this.selectedDoctor = undefined
    },
    sendAlert(type, msg) {
      this.alertType = type
      this.alertMsg = msg
      this.alert = true
      setTimeout(() => {
        this.alert = false
      }, 1000 * 5)
    }
  }
}
</script>
