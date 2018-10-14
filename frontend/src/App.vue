<template>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
</template>

<script>

import Hello from './components/Hello.vue'
import Navbar from './components/Navbar.vue'

export default {
  name: 'app',
  components: {
    Hello,
    Navbar
  },
  created () {
    this.$store.dispatch('getUsers')
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /*margin-top: 60px;*/
}
</style>
