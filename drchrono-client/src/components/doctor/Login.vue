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
                        <v-btn secondary large :href="login">Login with DrChrono</v-btn>
                    </v-flex>
                </v-layout>
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>
import chrono from '../../api/chrono'
export default {
    name: 'login',
    data() {
        return {
            first: '',
            last: '',
            login: chrono.login
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
