<template>
  <div>
    <v-layout row wrap class="content">
      <v-flex>
        <h1>Check-in Kiosk</h1>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs6 offset-xs3>
        <v-card v-if="!doctorUnknown">
          <doctors :doctors="doctors.checked_in" title="Doctors Available" :action="selectDoctor"></doctors>
          <v-divider></v-divider>
          <doctors v-if="!selectedDoctor" :doctors="doctors.checked_out" title="Doctors Unavailable" :disabled="true"></doctors>
          <v-btn v-if="!selectedDoctor" secondary @click="setUnknown()">I don't know who my doctor is</v-btn>
        </v-card>
        <patient v-if="selectedDoctor || doctorUnknown" :doctor="selectedDoctor" :action="sendAlert" :close="unSelectDoctor"></patient>
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
      doctorUnknown: false,
      alert: false,
      alertMsg: '',
      alertType: 'error'
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
      this.doctorUnknown = false
    },
    setUnknown() {
      this.doctorUnknown = true
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
