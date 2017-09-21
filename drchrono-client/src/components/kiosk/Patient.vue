<template>
  <div>
    <v-card>
      <v-card-title primary-title>
        <div>
          <div class="headline">Patient Form: {{title}}</div>
          <span class="grey--text">Please fill out the information below to check-in. Thank you.</span>
        </div>
      </v-card-title>
      <v-layout row class="top generationParams">
        <v-flex xs3 class="space">
          <v-text-field required v-model="patient.first_name" label="First Name:" :rules="[firstNameRequired]"></v-text-field>
        </v-flex>
        <v-flex xs3 class="space">
          <v-text-field required v-model="patient.last_name" label="Last Name:" :rules="[lastNameRequired]"></v-text-field>
        </v-flex>
        <v-flex xs3 class="space">
          <v-text-field v-model="patient.ssn" label="SSN:" :rules="[ssnValidation]"></v-text-field>
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
          <v-text-field v-model="patient.zip_code" label="Zip Code:"></v-text-field>
        </v-flex>
      </v-layout>
      <v-layout row class="generationParams" v-if="verified">
        <v-flex xs3 class="space">
          <v-text-field v-model="patient.home_phone" label="Home Phone:" :rules="[homePhoneValidation]"></v-text-field>
        </v-flex>
        <v-flex xs3 class="space">
          <v-text-field v-model="patient.cell_phone" label="Cell Phone:" :rules="[cellPhoneValidation]"></v-text-field>
        </v-flex>
        <v-flex xs3 class="space">
          <v-text-field v-model="patient.email" label="Email:" :rules="[emailValidation]"></v-text-field>
        </v-flex>
      </v-layout>
      <v-layout row class="generationParams" v-if="verified">
        <v-flex xs3 class="space">
          <v-text-field v-model="patient.ethnicity" label="Ethnicity:"></v-text-field>
        </v-flex>
      </v-layout>
      <v-layout row class="bottom">
        <v-flex class="space">
          <v-btn secondary :loading="loading" :disabled="loading || validation" @click="submitAction()">{{submitText}}</v-btn>
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
        first_name: '',
        last_name: '',
        ssn: '',
        address: '',
        city: '',
        state: '',
        zip_code: '',
        email: '',
        home_phone: '',
        cell_phone: '',
        ethnicity: ''
      },
      verified: false,
      loading: false
    }
  },
  computed: {
    submitText: function() {
      return (!this.verified) ? 'Submit' : 'Finalize / Complete'
    },
    title: function() {
      return (this.doctor) ? `Dr. ${this.doctor.last_name}` : 'Generic'
    },
    validation: function() {
      return [this.ssnValidation, this.emailValidation, this.homePhoneValidation,
      this.cellPhoneValidation, this.firstNameRequired, this.lastNameRequired].some((f) => {
        return f() !== true
      })
    }
  },
  methods: {
    submitAction() {
      (!this.verified) ? this.verify() : this.finalize()
    },
    ssnValidation: function() {
      return /^\d{9}$|^$/.test(this.patient.ssn) || 'Invalid ssn.'
    },
    emailValidation: function() {
      return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$|^$/.test(this.patient.email) || 'Invalid email.'
    },
    homePhoneValidation: function() {
      return /^\d{3}-\d{3}-\d{4}$|^$/.test(this.patient.home_phone) || 'Invalid phone number.'
    },
    cellPhoneValidation: function() {
      return /^\d{3}-\d{3}-\d{4}$|^$/.test(this.patient.cell_phone) || 'Invalid phone number.'
    },
    firstNameRequired() {
      return this.patient.first_name !== '' || 'This field is required'
    },
    lastNameRequired() {
      return this.patient.last_name !== '' || 'This field is required'
    },
    verify() {
      this.loading = true
      chrono.verifyAppointment({
        ...{
          first_name: this.patient.first_name,
          last_name: this.patient.last_name,
          ssn: this.patient.ssn
        },
        ...(
          (this.doctor) ? { doctor_id: this.doctor.id } : {}
        )
      }).then((response) => {
        this.verified = response.status !== 'error'
        if (this.verified) {
          this.patient = { ...response.patient, ...{ appointment: response.appointment } }
        }
        this.action(response.status, response.message)
        this.loading = false
      })
    },
    finalize() {
      this.loading = true
      chrono.finalizeCheckin(this.patient).then((response) => {
        this.verified = response.status !== 'error'
        this.action(response.status, response.message)
        this.loading = false
        this.clear()
      })
    },
    clear() {
      this.patient = {
        first_name: '',
        last_name: '',
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
