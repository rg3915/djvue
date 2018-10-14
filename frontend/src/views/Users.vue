<template>
  <div>
    <b-table striped hover :items="users"></b-table>
  </div>
</template>

<script>

export default {
  data () {
    return {
    }
  },
  methods: {
  },
  computed: {
    users () {
      return this.$store.state.users
    }
  }
}
</script>