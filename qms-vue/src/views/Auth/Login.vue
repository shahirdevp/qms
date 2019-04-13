<template>
  <div>
    <v-layout row align-center justify-center fill-height class="bac-img">
      <v-flex xs12 md5 sm5>
        <div class="img-card white--text">
          <v-card-text>
            <h1 class="display-2 font-weight-light white--text">Your Space To Be Social</h1>
            <br>
            <p
              class="body-2"
            >Thanks for provide the vuetify material theme , I want to know your project will have github link? (convenient different developer make a pull request)</p>
          </v-card-text>
        </div>
      </v-flex>

      <v-flex xs12 md7 sm7>
        <div class="form-card">
          <v-card-text>
            
            <div row>
              <v-flex xs12 md10 offset-md>
                <div class="logoset">
                  <v-icon dark color="green darken-3 headline" style="margin-right:10px">dashboard</v-icon>
                  <span class="headline mb20">QMS Application</span>
                </div>
           
                <div class="form-set">
                  <v-layout
                row
                fill-height
                justify-center
                align-center
                v-if="loading"
              >
                <v-progress-circular
                  :size="50"
                  color="primary"
                  indeterminate
                />
              </v-layout>
                  <v-form v-else ref="form" v-model="valid" lazy-validation>
                    <v-text-field
                      v-model="credentials.username"
                      :counter="70"
                      label="username"
                      :rules="rules.username"
                      maxlength="70"
                      required
                      
                    ></v-text-field>
                    <v-text-field
                      type="password"
                      v-model="credentials.password"
                      :counter="20"
                      label="password"
                      :rules="rules.password"
                      maxlength="20"
                      required
                      
                    ></v-text-field>
                    <div>
                      <v-btn flat class="float-rigt" left>Forgot Password?</v-btn>
                      <v-checkbox
                        
                        label="Remember Me"
                        required
                        
                        class="m0"
                      ></v-checkbox>
                    </div>
                    <div class="mt25">
                      <v-btn 
                      block 
                      dark 
                      color="green darken-3" 
                      :disabled="!valid"
                      @click="login">submit</v-btn>
                    </div>
                  </v-form>
                </div>
              </v-flex>
            </div>
          </v-card-text>
        </div>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>

import axios from "axios";
import swal from "sweetalert2";
import router from "../../router";
export default {
  name: "Auth",
  data: () => ({
    credentials: {},
    valid: true,
    loading: false,
    rules: {
      username: [
        v => !!v || "Username is required",
        v =>
          (v && v.length > 3) ||
          "A username must be more than 3 characters long",
        v =>
          /^[a-z0-9_]+$/.test(v) ||
          "A username can only contain letters and digits"
      ],
      password: [
        v => !!v || "Password is required",
        v =>
          (v && v.length > 5) || "The password must be longer than 5 characters"
      ]
    }
  }),
  methods: {
    login() {
      // checking if the input is valid
      if (this.$refs.form.validate()) {
        this.loading = true;
        axios({
          method: "post",
          url: this.$apiUrl+"auth/",
          data: {
            username: this.credentials.username,
            password: this.credentials.password
          }
        })
          .then(res => {
            this.$session.start();
            this.$session.set("token", res.data.token);
            router.push("/dashboard");
          })
          .catch(e => {

            this.loading = false;
            swal({
              type: "warning",
              title: "Error",
              text: "Wrong username or password",
              showConfirmButton: false,
              showCloseButton: false,
              timer: 3000
            });
            // console.log(res.data)
          });
      }
    }
  }
};
</script>




<style scoped>
.theme--dark.v-btn.v-btn--disabled:not(.v-btn--icon):not(.v-btn--flat):not(.v-btn--outline) {

    background-color: rgba(117, 117, 117, 0.82) !important;

}
.fillheight {
  min-height: 100vh;
}
.bac-img {
  background: #4d6e69 url("../../assets/cam.jpg");
  background-size: cover;
  background-blend-mode: overlay;
}
.form-card {
  background: #fff;
  padding: 105px;
  height: 100vh;
}
.float-rigt {
  float: right;
}
.m0 {
  margin: 0px;
}
.m0 .v-input__slot {
  margin-top: 5px;
}
.logoset {
  padding: 0 0 25px 0;
}
.img-card {
  padding: 0 50px;
}
.mt25 {
  margin-top: 25px;
}
.v-btn--disabled{
    background-color: #988e8e !important;
    color: #000;
}
</style>

