<template>
    <div>
        <h1>{{ user.data.display }}</h1>
        <v-btn dark v-on:click="SignOut" style="margin-left: 1700px;">SignOut</v-btn>
    </div>
</template>

<script>
//import axios from 'axios';
import router from '../router';
import firebase from "firebase";
import { mapGetters } from "vuex";

export default {
    name: "Dashboard",
    data: () => ({

    }),
    computed: {
        ...mapGetters({
            user: "user"
        })
    },
    created() {
        this.checkLoggedIn();
    },
    methods: {
        checkLoggedIn() {
          if (!this.user.loggedIn) {
              router.push('/admin');
          }
          else {
              console.log(this.user);
          }
        },
        SignOut: function() {
            firebase.auth().signOut().then(() => {
                router.push('/admin');
            })
        }
    }
}
</script>