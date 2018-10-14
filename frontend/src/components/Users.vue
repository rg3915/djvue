<template>
  <b-table striped hover :items="users"></b-table>
</template>

<script>

import axios from 'axios'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data () {
    return {
      headers: [
        { text: 'Username', value: 'username' },
        { text: 'E-mail', value: 'email' }
      ],
      users: []
    }
  },
  created () {
    axios.get('http://localhost:8000/api/user/json/')
    .then(result => {
      console.log(result)
      this.users = result.data.data
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
