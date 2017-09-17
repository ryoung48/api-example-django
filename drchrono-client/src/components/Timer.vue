<template>
    <div class="upper">
        {{status}} <span class="lower">for ::</span>
         {{days}} Day{{(days !== 1) ? "s" : ""}} : 
         {{hours}} Hour{{(hours !== 1) ? "s" : ""}} : 
         {{minutes}} Minute{{(minutes !== 1) ? "s" : ""}} : 
         {{seconds}} Second{{(seconds !== 1) ? "s" : ""}}
    </div>
</template>

<script>
export default {
    name: 'timer',
    props: {
        status: String,
        start: String
    },
    data() {
        return {
            elapsed: 0
        }
    },
    mounted() {
        this.timeDiff()
        setInterval(this.timeDiff, 1000)
    },
    methods: {
        timeDiff() {
            this.elapsed = new Date() - new Date(this.start)
        }
    },
    computed: {
        seconds: function() {
            return Math.trunc((this.elapsed / 1000)) % 60
        },
        minutes: function() {
            return Math.trunc((this.elapsed / 1000 / 60)) % 60
        },
        hours: function() {
            return Math.trunc((this.elapsed / 1000 / 60 / 60)) % 24
        },
        days: function() {
            return Math.trunc(this.elapsed / 1000 / 60 / 60 / 24)
        }
    }
}
</script>

<style scoped>
.upper {
  text-transform: capitalize;
}
.lower {
    text-transform: lowercase;
}
</style>
