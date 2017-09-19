<template>
  <div>
    <v-card>
      <v-card-title primary-title>
        <div>
          <div class="headline">Patient Form: Dr. {{doctor.last}}</div>
          <span class="grey--text">Please fill out the information below to check-in. Thank you.</span>
        </div>
      </v-card-title>
      <v-layout row class="top generationParams">
        <v-flex xs3 class="space">
          <v-text-field v-model="patient.first" label="First Name:"></v-text-field>
        </v-flex>
        <v-flex xs3 class="space">
          <v-text-field v-model="patient.last" label="Last Name:"></v-text-field>
        </v-flex>
        <v-flex xs3 class="space">
          <v-text-field v-model="patient.ssn" label="SSN:"></v-text-field>
        </v-flex>
      </v-layout>
      <v-layout row class="generationParams" v-if="verified">
        <v-flex xs3 class="space">
          <v-text-field v-model="patient.city" label="City:"></v-text-field>
        </v-flex>
        <v-flex xs3 class="space">
          <v-text-field v-model="patient.state" label="State:"></v-text-field>
        </v-flex>
        <v-flex xs3 class="space">
          <v-text-field v-model="patient.ethnicity" label="Ethnicity:"></v-text-field>
        </v-flex>
      </v-layout>
      <v-layout row class="bottom">
        <v-flex class="space">
          <v-btn secondary :loading="loading" :disabled="loading" @click="submitAction()">{{submitText}}</v-btn>
        </v-flex>
        <v-flex class="space">
          <v-btn secondary @click="clear()">Close</v-btn>
        </v-flex>
      </v-layout>
    </v-card>
  </div>
</template>

<script>
import chrono from '../../api/chrono'
export default {
  name: 'patient',
  props: {
    doctor: Object,
    action: Function,
    close: Function
  },
  data() {
    return {
      patient: {
        first: '',
        last: '',
        ssn: '',
        city: '',
        state: '',
        ethnicity: ''
      },
      verified: false,
      loading: false
    }
  },
  computed: {
    submitText: function() {
      return (!this.verified) ? 'Submit' : 'Finalize / Complete'
    }
  },
  methods: {
    submitAction() {
      (!this.verified) ? this.verify() : this.finalize()
    },
    verify() {
      this.loading = true
      chrono.verifyAppointment({
        first: this.patient.first,
        last: this.patient.last,
        ssn: this.patient.ssn,
        doctor_id: this.doctor.id
      }).then((response) => {
        this.verified = response.status !== 'error'
        if (this.verified) {
          this.patient = {...response.patient, ...{appointment: response.appointment}}
        }
        this.action(response.status, response.message)
        this.loading = false
      })
    },
    finalize() {
      this.loading = true
      chrono.finalizeCheckin({
        city: this.patient.city,
        state: this.patient.state,
        ethnicity: this.patient.ethnicity,
        appointment: this.patient.appointment
      }).then((response) => {
        this.verified = response.status !== 'error'
        this.action(response.status, response.message)
        this.loading = false
        this.clear()
      })
    },
    clear() {
      this.patient = {
        first: '',
        last: '',
        ssn: '',
        city: '',
        state: '',
        ethnicity: ''
      }
      this.verified = false
      this.close()
    }
  }
}
</script>

<style scoped>
.generationParams {
  margin-left: 15px;
}

.top {
  margin-top: 15px;
}

.bottom {
  padding-bottom: 10px;
  margin-left: 5px;
}

.space {
  margin-right: 15px;
}
</style>
