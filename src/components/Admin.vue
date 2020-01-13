<template>
    <div>
        <v-card class="InsertCard" >
            <v-card dark style="margin-top: -30px;height: 26px;"><h3 style="font-family: sans-serif;"> Enter Credentials </h3></v-card><br>
             <v-form
                ref="form"
                v-model="valid"
                :lazy-validation="lazy"
            >
                <v-text-field
                    class="InsertText"
                    label="Username"
                    v-model="user"
                    single-line
                    :counter = "30"
                    maxlength = "30"
                    required
                    :rules="nameRules"
                    solo
                ></v-text-field>
                <v-text-field
                    class="InsertText"
                    label="Password"
                    type="password"
                    v-model="pass"
                    single-line
                    :counter = "30"
                    maxlength = "30"
                    required
                    :rules="passRules"
                    solo
                ></v-text-field>
                <v-btn @click="Submit" class="InsertButton" dark> Submit </v-btn>
             </v-form>
        </v-card>
    </div>
</template>

<script>
//import axios from 'axios';
import router from '../router';
import firebase from "firebase";
//import { mapGetters } from "vuex";

export default {
    data: () => ({
        user: "",
        pass: "",
        valid: true,
        nameRules: [
            v => !!v || 'User is required',
            v => (v && v.length <= 30) || 'Name must be less than 10 characters',
        ],
        passRules: [
            v => !!v || 'Password is required',
            v => (v && v.length <= 30) || 'Name must be less than 10 characters',
        ],
    }),
    methods: {
      Submit () {
       firebase
        .auth()
        .signInWithEmailAndPassword(this.user, this.pass)
        .then(data => {
            console.log(data);
            router.push('/dashboard');
        })
        .catch(err => {
          this.error = err.message;
        });
      }    
    }    
}
</script>

<style scoped>
    .InsertCard {
        width: 400px;
        height: 260px;
        padding: 30px 1px;
        margin-top: 150px;
        margin-left: 750px;
    }
    .InsertText {
        width: 300px;
        margin-left: 50px;
    }
    .InsertButton {
        margin-left: 212px;
    }
</style>