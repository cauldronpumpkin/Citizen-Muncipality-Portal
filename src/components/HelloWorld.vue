<template>
  <div class="hello"> <br> <br> <br> <br> <br> <br> <br>
    <v-btn @click="InsertFunc" dark> Citizen </v-btn> <br> <br> <br>
    <v-btn @click="ShowFunc" dark> Municipality </v-btn>
  </div>
</template>

<script>
import router from '../router'
export default {
  name: 'HelloWorld',
  methods: {
    InsertFunc: function() {
      router.push('/insert');
    },
    ShowFunc: function() {
      router.push('/show')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
