<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">TRAINING REQUEST REGISTER</h3>
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
          <router-link :to="{ path: 'trining-request-register/'+ props.item.id }" >{{ props.item.id }}</router-link>
        </td>
        <td class="text-xs-left"><router-link :to="{ path: 'trining-request-register/'+ props.item.id }" >{{ props.item.training_Required }}</router-link></td>
        <td class="text-xs-left">{{ props.item.training_to }}</td>
        <td class="text-xs-left">{{ props.item.training_Suggested_by }}</td>
        <td class="text-xs-left">{{ props.item.reason_for_Training }}</td>
        <td class="text-xs-left">{{ props.item.date }}</td>
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
          <h3>Add TRAINING REQUEST REGISTER</h3>
          <br>
          <v-form ref="form" v-model="valid" id="emp" lazy-validation>

            <v-text-field v-model="trRequired" :counter="100" :rules="trRequiredRules" label="Training Required" required ></v-text-field>
            <v-text-field v-model="trTo" :counter="100" :rules="trToRules" label="Training To" required ></v-text-field>

            <v-text-field v-model="trSuggested" :counter="100"  :rules="trSuggestedRules" label="Training Suggested By" required ></v-text-field>
            <v-text-field v-model="trResoan" :counter="400" :rules="trResoanRules" label="Reason For Training" required ></v-text-field>
            
            <v-dialog ref="dialog" v-model="modal" :return-value.sync="trdate" persistent lazy full-width width="290px" >
              <template v-slot:activator="{ on }">
                <v-text-field v-model="trdate" label="Date Of Join" prepend-icon="event" readonly v-on="on" ></v-text-field>
              </template>
              <v-date-picker v-model="trdate" scrollable>
                <v-spacer></v-spacer>
                <v-btn flat color="primary" @click="modal = false">Cancel</v-btn>
                <v-btn flat color="primary" @click="$refs.dialog.save(trdate)">OK</v-btn>
              </v-date-picker>
            </v-dialog>
            
            <v-text-field v-model="trRemark" :counter="10" :rules="trRemarkRules" label="Remarks" required ></v-text-field>

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
        { text: "Training Required", value: "training_Required" },
        { text: "Training to", value: "training_to" },
        { text: "Training Suggested by", value: "training_Suggested_by" },
        { text: "Reason for Training", value: "reason_for_Training" },
        { text: "Date", value: "date" },
      ],
      info: [],

      //  push to database
      valid: true,
      modal: false,
      trdate: new Date().toISOString().substr(0, 10),

      trRequired:'',trTo:'',trSuggested:'',trResoan:'',trdate:'',trRemark:"",
      // form rules or validation
      trRequiredRules: [v => !!v || "This field is required"],
      trToRules: [v => !!v || "This field is required"],
      trSuggestedRules: [v => !!v || "This field is required"],
      trResoanRules: [v => !!v || "This field is required"],
      trdateRules: [v => !!v || "This field is required"],
      trRemarkRules: [v => !!v || "This field is required"],
     
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
        .get(this.$apiUrl+"training-request/")
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
              url: this.$apiUrl+"training-request/",
              data: {
                training_Required: this.trRequired,
                training_to: this.trTo,
                training_Suggested_by: this.trSuggested,
                reason_for_Training: this.trResoan,
                date: this.trdate,
                remarks: this.trRemark,
                prepared_By: 'admin user',
                approved_By: 'admin',
              }
            })
          .then(function( ) {
            self.getall()
            self.drawer = !self.drawer;
            swal({
              title: "Success",
              type: "success",
              text: "Successfully  Added",
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