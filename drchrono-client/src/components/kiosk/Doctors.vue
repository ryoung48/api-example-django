<template>
    <v-list subheader>
        <v-subheader>{{title}}</v-subheader>
        <v-list-tile :disabled="disabled" v-for="(doctor, index) in doctors" :key="index" @click="action(doctor)">
            <v-list-tile-content>
                <v-list-tile-title> Dr. {{doctor.last_name}} ({{doctor.first_name}})</v-list-tile-title>
                <v-list-tile-sub-title>
                    <timer :start="doctor.time" :status="doctor.status"></timer>
                </v-list-tile-sub-title>
            </v-list-tile-content>
        </v-list-tile>
    </v-list>
</template>

<script>
import Timer from '@/components/timer'
export default {
    name: 'doctors',
    props: {
        doctors: Array,
        title: String,
        disabled: {
            type: Boolean,
            default: false
        },
        action: {
            type: Function,
            default: (d) => {}
        }
    },
    components: {
        'timer': Timer
    }
}
</script>
