<template>
  <div>
    <section class="full-pag-wrap">
      <v-container grid-list-lg>
        <v-layout row wrap align-center justify-center fill-height>
          <v-flex xs12 md6 lg6>
            <div class="center-box">
              <img src="../../assets/reg.png" class="responsive-img">
            </div>
          </v-flex>

          <v-flex xs12 md6 lg6>
            <div class="center">
             
              <v-form ref="form" class id="emp" lazy-validation>
                <v-container>
                    <v-flex xs12 sm10 md10>
                    <h1 class="text-center reg-title">Register Organization</h1>
                    </v-flex>
                    <v-layout row wrap>
                        <v-flex xs12 sm10 md10>
                            <v-text-field 
                                label="Company name" 
                                outline
                                v-model="formation.comapeny"
                                :rules="rules.comapeny"
                                required
                            ></v-text-field>
                        </v-flex>
                        <v-flex xs12 sm10 md10>
                            <v-text-field 
                            label="Website Url" 
                            outline
                            v-model="formation.url"
                            :rules="rules.url"
                            required
                            type="url"
                            placeholder="http://example.com"
                            ></v-text-field>
                        </v-flex>
                        
                        <v-flex xs12 sm10 md10>
                            <div class="">
                                <v-btn large :disabled="!valid"  @click="login" block dark color="green darken-3" >submit</v-btn>
                            </div>
                        </v-flex>
                  </v-layout>
                </v-container>
              </v-form>
              
            </div>
            
          </v-flex>
        </v-layout>
      </v-container>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import swal from "sweetalert2";
import router from "../../router";
import jsonfile from "jsonfile";
import jfile from '../../../student.json';
    export default {
 data: () => ({
    formation: {},
    valid: true,
    loading: false,
    rules: {
      comapeny: [
        v => !!v || "Company name is required",
        v =>/^[a-z0-9_]+$/.test(v) ||
          "A Company name can only contain letters and digits"
      ],
      url: [
        v => !!v || "Url is required",
        
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
          url: this.$apiUrl+"organization/cformation/",
          data: {
            CmpName: this.formation.comapeny,
            app_domain: this.formation.url
          }
        })
          .then(res => {
           console.log(res.data)
           this.saveTest(res.data)
            // router.push("");
          })
          .catch(e => {

            this.loading = false;
            swal({
              type: "warning",
              title: "Error",
              text: "Something when to wrong. Please try again",
              showConfirmButton: false,
              showCloseButton: false,
              timer: 3000
            });
            console.log(e.data)
          });
      }
    },
    saveTest(respond){
      
       
        axios.post('http://5ineprojects.com/json-create/register.php',{
         register:respond,
        },
        )
        .then(res => {
          router.push("policy-settep");
        })
        .catch(err => {
          alert('error')
          console.error(err); 
        })

     
        
    }
  }
    };
</script>

<style scoped>
.center-box {
  position: relative;
  height: calc(100vh - 86px);
}
.center-box img {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  margin: auto;
}
>>>.v-text-field.v-text-field--enclosed .v-text-field__details {
    margin-bottom: 2px;
    height: 0;
}
>>>.theme--light.v-text-field--outline > .v-input__control > .v-input__slot {
    border: 1px solid rgba(105, 101, 101, 0.54);
}
>>>.theme--light.v-text-field--outline > .v-input__control > .v-input__slot:hover{
    border: 1px solid rgba(0,0,0,0.87) !important;
}
.text-center{
    text-align: center;
}
.reg-title{
    padding: 15px 0px;
}
</style>
