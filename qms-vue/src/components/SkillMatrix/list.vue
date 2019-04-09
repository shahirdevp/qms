<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">SKILL MATRIX</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn color="primary" ref="fileInput" @click.stop="drawer = !drawer">
            Add New
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
          <router-link :to="{ path: 'anual-training-plan/'+ props.item.id }" >{{ props.item.id }}</router-link>
        </td>
        <td class="text-xs-left"><router-link :to="{ path: 'anual-training-plan/'+ props.item.id }" >{{ props.item.topic }}</router-link></td>
        <td class="text-xs-left">{{ props.item.department_or_person }}</td>
        <td class="text-xs-left">{{ props.item.remarks }}</td>
        <td class="text-xs-left">{{ props.item.year }}</td>
        <td class="text-xs-left">{{ props.item.prepard_By }}</td>
        <td class="text-xs-left">{{ props.item.approved_By }}</td>
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
          <h3>Add ANNUAL TRAINING PLAN</h3>
          <br>
          <v-form ref="form" v-model="valid" id="emp" lazy-validation>

            <v-select :items="selectYears" v-model="year" :rules="yearRules" required label="Select Year" ></v-select>
            <v-select :items="selectMonth" v-model="month" :rules="monthRules" required  label="Select Month" ></v-select>

            <v-text-field v-model="topic" :counter="50" :rules="topicRules" label="Topic" required ></v-text-field>
            <v-text-field v-model="dep" :counter="50" :rules="depRules" label="Department / person" required ></v-text-field>

            <v-text-field v-model="remark" :counter="50" :rules="remarkRules" label="Remark" required ></v-text-field>
            <v-text-field v-model="legend" :counter="50" :rules="legendRules" label="Legend" required ></v-text-field>
            
            

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
        { text: "Topic", value: "topic" },
        { text: "Department / person", value: "department_or_person" },
        { text: "Remarks", value: "remarks" },
        { text: "Year", value: "year" },
        { text: "Prepard By", value: "prepard_By" },
        { text: "Approved By", value: "approved_By" },
      ],
      info: [],
      // add year
      selectYears:['2018','2019','2020','2021','2022','2023','2024','2025','2026'],
      selectMonth:['Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'],
      //  push to database
      valid: true,
      year:'',month:'', dep:'', topic:'', remark:'', legend:'',
      
      // form rules or validation
      
      yearRules: [v => !!v || "This field is required"],
      monthRules: [v => !!v || "This field is required"],
      topicRules: [v => !!v || "This field is required"],
      depRules: [v => !!v || "This field is required"],
      remarkRules: [v => !!v || "This field is required"],
      legendRules: [v => !!v || "This field is required"],
     
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
        .get("http://127.0.0.1:8000/api/v1/hr/anual_training")
        .then(function(response) {
          self.info = response.data;
        })
        .catch(function(error) {
          console.log(error);
        });
    },

    validate: function() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        var self = this;
          
          var mnth = this.month.toLowerCase().trim()
          axios({
              method: "post",
              url: "http://127.0.0.1:8000/api/v1/hr/anual_training",
              data: {
                year: this.year,
                topic: this.topic,
                department_or_person: this.dep,
                remarks: this.remark,
                legend: this.legend,
                mnth : '1',
                
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