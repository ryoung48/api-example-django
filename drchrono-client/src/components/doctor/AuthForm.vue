<template>
    <v-layout row>
        <v-flex xs4 offset-xs4>
            <v-card>
                <v-card-title primary-title>
                    <div>
                        <div class="headline">Doctor Login Form</div>
                        <span class="grey--text">Please fill out your credentials below.</span>
                    </div>
                </v-card-title>
                <v-layout row class="bottom">
                    <v-flex class="space">
                        <v-btn secondary large :href="login">Login with drchrono</v-btn>
                    </v-flex>
                </v-layout>
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>
import chrono from '../../api/chrono'
export default {
    name: 'authForm',
    data() {
        return {
            'login': chrono.login
        }
    }
}
</script>
