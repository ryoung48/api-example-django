<template>
  <div>
    <v-layout row wrap class="content">
      <v-flex>
        <h1>Appointments</h1>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs6 offset-xs3>
        <v-card>
          <v-card-title primary-title>
            <div>
              <div class="headline">
                {{doctor.first_name}} {{doctor.last_name}}:
                <span>
                  <v-btn secondary @click="toggleLock()">{{lockButton}} Kiosk</v-btn>
                </span>
                <span>
                  <v-btn secondary :href="logout">Logout</v-btn>
                </span>
                <span>
                  <v-progress-circular indeterminate class="indigo--text" v-show="loading"></v-progress-circular>
                </span>
              </div>
            </div>
          </v-card-title>
          <v-divider v-if="arrived"></v-divider>
          <v-list subheader v-if="arrived">
            <v-subheader>Arrived</v-subheader>
            <v-list-tile v-for="(appointment, index) in appointments.arrived" :key="index" @click="visit(appointment.id)">
              <v-list-tile-content>
                <v-list-tile-title>{{appointment.patient.first_name}} {{appointment.patient.last_name}}: {{appointment.reason}}</v-list-tile-title>
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
                <v-list-tile-title>{{appointment.patient.first_name}} {{appointment.patient.last_name}}: {{appointment.reason}}</v-list-tile-title>
                <v-list-tile-sub-title>
                  Scheduled at: {{appointment.scheduled_time}}
                </v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
          <v-divider v-if="session"></v-divider>
          <v-list subheader v-if="session">
            <v-subheader>In Session</v-subheader>
            <v-list-tile v-for="(appointment, index) in appointments.session" :key="index">
              <v-list-tile-content>
                <v-list-tile-title>{{appointment.patient.first_name}} {{appointment.patient.last_name}}: {{appointment.reason}}</v-list-tile-title>
                <v-list-tile-sub-title>
                  Waited {{(appointment.wait_time / 60).toFixed(2)}} minutes
                </v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
          <v-divider v-if="finished"></v-divider>
          <v-list subheader v-if="finished">
            <v-subheader>Finished | Average wait-time: {{(appointments.avg_wait / 60).toFixed(2)}} minutes</v-subheader>
            <v-list-tile v-for="(appointment, index) in appointments.finished" :key="index">
              <v-list-tile-content>
                <v-list-tile-title>{{appointment.patient.first_name}} {{appointment.patient.last_name}}: {{appointment.reason}}</v-list-tile-title>
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
      appointments: {
        arrived: [],
        confirmed: [],
        finished: [],
        session: [],
        avg_wait: -1,
        doctor: {
          id: -1,
          first_name: '',
          last_name: '',
          status: '',
          status_code: ''
        }
      },
      alert: false,
      alertMsg: '',
      loading: false,
      logout: chrono.logout
    }
  },
  mounted() {
    this.getAppointments()
  },
  computed: {
    toggleStatus: function() {
      return (this.doctor && this.doctor.status_code === 'O') ? 'I' : 'O'
    },
    statusText: function() {
      return (this.doctor && this.doctor.status_code === 'O') ? 'Check-in' : 'Check-out'
    },
    arrived: function() {
      return this.appointments.arrived && this.appointments.arrived.length > 0
    },
    confirmed: function() {
      return this.appointments.confirmed && this.appointments.confirmed.length > 0
    },
    finished: function() {
      return this.appointments.finished && this.appointments.finished.length > 0
    },
    session: function() {
      return this.appointments.session && this.appointments.session.length > 0
    },
    doctor: function() {
      return this.appointments.doctor
    },
    locked: function() {
      return this.$store.getters.locked
    },
    lockButton: function() {
      return (this.$store.getters.locked) ? 'Unlock' : 'Lock'
    }
  },
  methods: {
    getAppointments() {
      chrono.getAppointments().then((response) => {
        this.appointments = response
        this.loading = false
      })
    },
    visit(id) {
      this.loading = true
      chrono.visit({ appointment_id: id }).then((response) => {
        this.getAppointments()
      })
    },
    toggleLock() {
      this.$store.commit('setLock', !this.locked)
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
