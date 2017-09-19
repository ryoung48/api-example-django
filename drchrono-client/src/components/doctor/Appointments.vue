<template>
  <div>
    <v-layout row wrap class="content">
      <v-flex>
        <h1>Appointments</h1>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs4 offset-xs4>
        <v-card>
          <v-layout>
            <v-flex xs5 class="top">
              <v-select :items="doctorNames" v-model="doctor" item-value="value" overflow></v-select>
            </v-flex>
            <v-flex xs5 class="top">
              <v-btn primary @click="updateStatus()">{{statusText}}</v-btn>
            </v-flex>
          </v-layout>
          <v-divider v-if="arrived"></v-divider>
          <v-list subheader v-if="arrived">
            <v-subheader>Arrived</v-subheader>
            <v-list-tile v-for="(appointment, index) in appointments.arrived" :key="index" @click="visit(appointment.id)">
              <v-list-tile-content>
                <v-list-tile-title>{{appointment.patient.first}} {{appointment.patient.last}}: {{appointment.reason}}</v-list-tile-title>
                <v-list-tile-sub-title>
                  <timer :start="appointment.arrival_date" :status="appointment.status"></timer>
                </v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
          <v-divider v-if="confirmed"></v-divider>
          <v-list subheader v-if="confirmed">
            <v-subheader>Confirmed</v-subheader>
            <v-list-tile v-for="(appointment, index) in appointments.confirmed" :key="index">
              <v-list-tile-content>
                <v-list-tile-title>{{appointment.patient.first}} {{appointment.patient.last}}: {{appointment.reason}}</v-list-tile-title>
                <v-list-tile-sub-title>
                  Scheduled at: {{appointment.scheduled_date}}
                </v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
          <v-divider v-if="finished"></v-divider>
          <v-list subheader v-if="finished">
            <v-subheader>Finished | Average wait-time: {{(appointments.avg_wait / 60).toFixed(2)}} minutes</v-subheader>
            <v-list-tile v-for="(appointment, index) in appointments.finished" :key="index">
              <v-list-tile-content>
                <v-list-tile-title>{{appointment.patient.first}} {{appointment.patient.last}}: {{appointment.reason}}</v-list-tile-title>
                <v-list-tile-sub-title>
                  Waited {{(appointment.wait_time / 60).toFixed(2)}} minutes
                </v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import chrono from '../../api/chrono'
import Timer from '@/components/timer'
export default {
  name: 'appointments',
  components: {
    'timer': Timer
  },
  data() {
    return {
      doctors: [],
      doctor: undefined,
      appointments: { arrived: [], confirmed: [], finished: [], avg_wait: -1 }
    }
  },
  mounted() {
    this.getDoctors()
    setInterval(this.getDoctors, 1000 * 300)
  },
  computed: {
    doctorNames: function() {
      return this.doctors.map((d, i) => {
        return { text: d.first + ' ' + d.last, value: d }
      })
    },
    toggleStatus: function() {
      return (this.doctor && this.doctor.status_code === 'O') ? 'I' : 'O'
    },
    statusText: function() {
      return (this.doctor && this.doctor.status_code === 'O') ? 'Login' : 'Logout'
    },
    arrived: function() {
      return this.appointments.arrived && this.appointments.arrived.length > 0
    },
    confirmed: function() {
      return this.appointments.confirmed && this.appointments.confirmed.length > 0
    },
    finished: function() {
      return this.appointments.finished && this.appointments.finished.length > 0
    }
  },
  methods: {
    getAppointments() {
      (this.doctor) && chrono.getAppointments(this.doctor.id).then((response) => {
        this.appointments = response
      })
    },
    getDoctors() {
      chrono.doctors().then((response) => {
        this.doctors = [...response.checked_in, ...response.checked_out]
        if (!this.doctor) {
           let pick = Math.floor(Math.random() * this.doctors.length)
           this.doctor = this.doctors[pick]
           this.getAppointments()
        }
      })
    },
    visit(id) {
      chrono.visit({appointment_id: id}).then((response) => {
        this.getAppointments()
      })
    },
    updateStatus() {
      chrono.updateDoctorStatus({
        doctor_id: this.doctor.id,
        status: this.toggleStatus
        }).then((response) => {
          this.doctor.status = response.status
          this.doctor.status_code = response.status_code
      })
    }
  },
  watch: {
    doctor: function() {
      this.getAppointments()
    }
  }
}
</script>

<style scoped>
.top {
  margin-top: 15px;
  margin-left: 15px;
}
</style>
