<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">HR Requirement Register</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn color="primary" ref="fileInput" @click.stop="drawer = !drawer">
            Add Hr
            <v-icon right>add</v-icon>
          </v-btn>
        </div>
      </v-flex>
    </v-layout>
    
    <v-data-table
      :headers="headers"
      :items="tlist"
      class="elevation-1"
      :rows-per-page-items="[10,20,50]"
    >
      <template v-slot:items="props">
        <td class="text-xs-left">
          <router-link :to="{ path: 'hr-detail/'+ props.item.id }">{{ props.item.hr_required_deg }}</router-link>
        </td>
        <td class="text-xs-left">{{ props.item.requestedby }}</td>
        <td class="text-xs-left">{{ props.item.reson_new_hire }}</td>
        <td class="text-xs-left">{{ props.item.remarks }}</td>
        <td class="text-xs-left">{{ props.item.preparedBy }}</td>
        <td class="text-xs-left">{{ props.item.arrovedBy }}</td>
        <td class="text-xs-left">{{ props.item.createdOn }}</td>
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
          <h3>Add HR Requirement Register</h3>
          <br>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="hrd"
              :counter="100"
              :rules="hrdRules"
              label="HR Required for Designation"
              required
            ></v-text-field>
            <v-text-field
              v-model="reason"
              :counter="400"
              :rules="reasonRules"
              label="Reason for New Hiring"
              required
            ></v-text-field>
            <v-text-field
              v-model="requiested"
              :counter="50"
              :rules="requiestedRules"
              label="Requested By"
              required
            ></v-text-field>
            <v-text-field v-model="remark" :counter="400" label="Remarks" required></v-text-field>

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
        {
          text: "HR Required for Designation",
          align: "left",
          sortable: false,
          value: "hr_required_deg"
        },
        { text: "Requestedby", value: "requestedby" },
        { text: "Reason for New Hiring	", value: "reson_new_hire" },
        { text: "Remarks", value: "remarks" },
        { text: "PREPARED BY", value: "preparedBy" },
        { text: "APPROVED BY", value: "arrovedBy" },
        { text: "Created Date", value: "createdOn" }
      ],
      tlist: [],

      //  push to database
      valid: true,
      // form items
      hrd: "",
      reason: "",
      requiested: "",
      remark: "",
      // form rules or validation
      hrdRules: [
        v => !!v || "HR Required for Designation is required",
        v =>
          (v && v.length <= 100) ||
          "HR Required for Designation must be less than 100 characters"
      ],
      reasonRules: [
        v => !!v || "Reason for New Hiring is required",
        v =>
          (v && v.length <= 400) ||
          "Reason for New Hiring must be less than 100 characters"
      ],
      requiestedRules: [
        v => !!v || "Requested By is required",
        v =>
          (v && v.length <= 50) ||
          "Requested By must be less than 100 characters"
      ]
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
        .get(this.$apiUrl+"hr/")
        .then(function(response) {
          self.tlist = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },

    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        var self = this;
        axios
          .post(this.$apiUrl+"hr/", {
            hr_required_deg: this.hrd,
            requestedby: this.reason,
            reson_new_hire: this.reason,
            remarks: this.remark,
            preparedBy: "sdf",
            arrovedBy: "sd"
          })
          .then(function(response) {
            console.log(response);
            // self.$refs.fileInput.click();
            self.drawer = !self.drawer;
            self.getall();
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
</style>
