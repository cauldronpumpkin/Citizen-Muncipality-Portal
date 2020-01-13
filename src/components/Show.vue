<template>
    <div>
      <GChart
      v-if="show == 1"
      type="ColumnChart"
      :data="chartData"
      :options="chartOptions"
      /> <br> <br> <br> <br>
      <v-text-field label="Enter Locality" v-model="Locality" style="margin-left: 800px;width: 300px;" id="id1"></v-text-field>
      <v-btn dark v-on:click="test">Show</v-btn> <br> <br>
      <v-btn dark v-on:click="reset">Reset</v-btn>
    </div>
</template>

<script>
import { GChart } from 'vue-google-charts'
import db from '../Fire'
export default {
    name: 'Show',

    components: {
        GChart
    },

    data () {
    return {
      array: [],
      show: 0,
      Locality: "",
      Locality_Select: ['Kharghar', 'Dadar', 'Thane', 'Malabar Hills'],
      chartData: [
        ['Locality', 'Dengue', 'Malaria', 'Aids'],
        [this.Locality, 0, 0, 0],
      ],
      chartOptions: {
        chart: {
          title: 'Company Performance',
          subtitle: 'Sales, Expenses, and Profit: 2014-2017',
          }
        },
      }
    },
    updated() {
      this.chartData[1][0] = this.Locality;
      this.chartData[1][1] = this.array.filter((data) => {
          return (data.locality.toLowerCase() == this.Locality.toLowerCase() && data.ailment.toLowerCase() == "dengue");
      }).length;
      this.chartData[1][2] = this.array.filter((data) => {
          return (data.locality.toLowerCase() == this.Locality.toLowerCase() && data.ailment.toLowerCase() == "malaria");
      }).length;
      this.chartData[1][3] = this.array.filter((data) => {
          return (data.locality.toLowerCase() == this.Locality.toLowerCase() && data.ailment.toLowerCase() == "aids");
      }).length;
    },

    created() {
      db.collection('Model').get().then((snapshot) => {
        snapshot.docs.forEach(doc => {
         this.array.push(doc.data());
        })
      })
    },
    methods: {
      test: function() {
        this.show = 1;
      },
      reset: function() {
        window.location.reload();
      }
    }
}
</script>

<style scoped>

</style>