import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import Vuetify from 'vuetify'
import vuetify from './plugins/vuetify';
import 'vuetify/dist/vuetify.min.css'
import axios from 'axios'
import VueSession from 'vue-session'
import VueGoogleCharts from 'vue-google-charts'
import * as firebase from "firebase"
 
Vue.use(VueGoogleCharts)

Vue.use(VueSession)

Vue.use(Vuetify)


Vue.config.productionTip = false
const base = axios.create({
  baseURL: 'http://localhost:8000'
})

var firebaseConfig = {
  apiKey: "AIzaSyA12scKkPCY16hLwGSZAJivqsOB-9pEHmg",
  authDomain: "disease-f22d1.firebaseapp.com",
  databaseURL: "https://disease-f22d1.firebaseio.com",
  projectId: "disease-f22d1",
  storageBucket: "disease-f22d1.appspot.com",
  messagingSenderId: "870376153294",
  appId: "1:870376153294:web:a2f7a3b1cf96305487309f",
  measurementId: "G-Q5HKWP2RX6"
};

firebase.initializeApp(firebaseConfig);
firebase.auth().onAuthStateChanged(user => {
  store.dispatch("fetchUser", user);
});

Vue.prototype.$http = base
new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
