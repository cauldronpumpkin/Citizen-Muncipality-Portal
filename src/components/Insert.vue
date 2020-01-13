<template>
    <div>
        <v-card class="InsertCard" >
            <v-card dark style="margin-top: -30px;height: 26px;"><h3 style="font-family: sans-serif;"> Enter Details of Your Ailment </h3></v-card><br>
             <v-form
                ref="form"
                v-model="valid"
                :lazy-validation="lazy"
            >
                <v-text-field
                    class="InsertText"
                    label="Email"
                    v-model="email"
                    single-line
                    :counter = "40"
                    maxlength = "40"
                    required
                    :rules="emailRules"
                    solo
                ></v-text-field>
                <v-text-field
                    class="InsertText"
                    label="Disease"
                    v-model="disease"
                    single-line
                    :counter = "20"
                    maxlength = "20"
                    required
                    :rules="nameRules"
                    solo
                ></v-text-field>
                <v-text-field
                    class="InsertText"
                    label="Locality"
                    v-model="locality"
                    single-line
                    :counter = "20"
                    maxlength = "20"
                    required
                    :rules="nameRules"
                    solo
                ></v-text-field>
                <v-btn @click="Submit" class="InsertButton" dark> Submit </v-btn>
             </v-form>
        </v-card>
    </div>
</template>

<script>
// import axios from 'axios';
// import router from '../router';
import db from '../Fire';

export default {
    data: () => ({
        email: "",
        disease: "",
        locality: "",
        Locality_Select: ['Kharghar', 'Dadar', 'Thane', 'Malabar Hills'],
        valid: true,
        emailRules: [
            v => !!v || 'E-mail is required',
            v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
        ],
        nameRules: [
            v => !!v || 'Name is required',
            v => (v && v.length <= 10) || 'Name must be less than 10 characters',
        ],
    }),
    methods: {
      Submit () {
        if (this.$refs.form.validate()) {
            this.loading = true;
            const instance = {
                email: this.email,
                ailment: this.disease,
                locality: this.locality
            }
            db.collection('Model').add(instance).then(() => {
                alert('Added to DataBase');
            })
        }
      }
    }
}
</script>

<style scoped>
    .InsertCard {
        width: 400px;
        height: 330px;
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