<template>
  <v-app>
    <v-toolbar dark>
      <v-toolbar-title>drchrono</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn v-for="(link, title, index) in dynLinks" :key="index" :to="link" flat>{{title}}</v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </main>
    <v-footer></v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      links: {
        Kiosk: 'kiosk/'
      }
    }
  },
  computed: {
    dynLinks: function() {
      return {
        ...this.links,
        ...(
          (!this.$store.getters.locked) ? {Doctors: 'doctors/'} : {}
        )
      }
    }
  }
}
</script>

<style lang="stylus">
  @import './stylus/main';
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  .content {
    text-align: center;
    margin: auto;
  }
</style>
