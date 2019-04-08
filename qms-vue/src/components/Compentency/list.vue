<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Compentency Matrix</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn color="primary" ref="fileInput" @click.stop="drawer = !drawer">
            Add Compentency
            <v-icon right>add</v-icon>
          </v-btn>
        </div>
      </v-flex>
    </v-layout>

    <v-data-table
      :headers="headers"
      :items="info"
      class="elevation-1"
      :rows-per-page-items="[10,20,50]"
    >
      <template v-slot:items="props">
        <td class="text-xs-left">
          <router-link :to="{ path: 'compentency-matrix/'+ props.item.id }" >{{ props.item.id }}</router-link>
        </td>
        <td class="text-xs-left"><router-link :to="{ path: 'compentency-matrix/'+ props.item.id }" >{{ props.item.position }}</router-link></td>
        <td class="text-xs-left">{{ props.item.education_Background }}</td>
        <td class="text-xs-left">{{ props.item.experience }}</td>
        <td class="text-xs-left">{{ props.item.competency_Requirement }}</td>
      </template>
    </v-data-table>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
      right
      width="650"
      class="form-drawer elevation-0"
    >
      <div class="post-form-container">
        <div class="post-form">
          <!-- post form -->
          <h3>Add Compentency Matrix</h3>
          <br>
          <v-form ref="form" v-model="valid" id="emp" lazy-validation>

            <v-text-field v-model="position" :counter="50" :rules="positionRules" label="Position" required ></v-text-field>
            <v-text-field v-model="eduBackg" :counter="50" :rules="eduBackgRules" label="Education Background" required ></v-text-field>
            <v-text-field v-model="exp" :counter="10" type="number" :rules="expRules" label="Experience" required ></v-text-field>
            <v-text-field v-model="competency" :counter="50" :rules="competencyRules" label="Competency Requirement" required ></v-text-field>

            

            <v-btn :disabled="!valid" color="success" @click="validate">Submit</v-btn>
            <v-btn color="error" @click="reset">Reset Form</v-btn>
            <v-btn color="warning" @click.stop="drawer = !drawer">Cancel</v-btn>
          </v-form>
        </div>
      </div>
    </v-navigation-drawer>
  </div>

  <!-- 
    # Fetch hr lis - api - http://localhost:8000/api/v1/hr/
    #add new post - component - addPost
  -->
</template>

			
<script>
import axios from "axios";
import swal from "sweetalert2";
import router from "../../router";

export default {
  data() {
    return {
      drawer: null,
      // table ist
      headers: [
        { text: "ID", align: "left", value: "id" },
        { text: "Position", value: "position" },
        { text: "Education Background", value: "education_Background" },
        { text: "Experience", value: "experience" },
        { text: "Competency Requirement", value: "competency_Requirement" }
      ],
      info: [],

      //  push to database
      valid: true,
      position:'',eduBackg:'',exp:'',competency:'',
      
      // form rules or validation
      positionRules: [v => !!v || "This field is required"],
      eduBackgRules: [v => !!v || "This field is required"],
      expRules: [v => !!v || "This field is required"],
      competencyRules: [v => !!v || "This field is required"],
     
    };
  },

  mounted() {
    this.getall();
  },

  methods: {
    // fetch all hr list
    getall() {
      var self = this;
      axios
        .get("http://127.0.0.1:8000/api/v1/hr/completency")
        .then(function(response) {
          self.info = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },

    validate: function() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        var self = this;
        
          axios({
              method: "post",
              url: "http://127.0.0.1:8000/api/v1/hr/completency",
              data: {
                position: this.position,
                education_Background: this.eduBackg,
                experience: this.exp,
                competency_Requirement: this.competency,
              }
            })
          .then(function(response) {
            self.getall()
            self.drawer = !self.drawer;
            swal({
              title: "Success",
              type: "success",
              text: "Successfully completency Matrix Added",
              showConfirmButton: false,
              showCloseButton: false,
              timer: 3000
            });
          })
          .catch(function(error) {
            console.log(error);
          });
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    }
  }
};
</script>


<style scoped>
.post-form-container {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: auto;
}
.post-form-container .post-form {
  position: absolute;
  width: 100%;
  height: 100%;
  padding: 30px 25px;
}
.v-input__prepend-outer {
  display: none !important;
}
</style>

<style >
#emp .v-input__prepend-outer {
  display: none !important;
}
</style>