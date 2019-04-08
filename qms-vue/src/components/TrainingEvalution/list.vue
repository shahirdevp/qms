<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name"> Training Evaluation Record		</h3>
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
        <td class="text-xs-left"> <router-link :to="{ path: 'training-evalution-record/'+ props.item.id }" >{{ props.item.id }}</router-link> </td>
        <td class="text-xs-left"><router-link :to="{ path: 'training-evalution-record/'+ props.item.id }" >{{ props.item.trg_no }}</router-link></td>
        <td class="text-xs-left">{{ props.item.training_topic }}</td>
        <td class="text-xs-left">{{ props.item.date_of_trainig }}</td>
        <td class="text-xs-left">{{ props.item.faculty }}</td>
        <td class="text-xs-left">{{ props.item.venue }}</td>
        <td class="text-xs-left">{{ props.item.evaluation_criteria }}</td>
        <td class="text-xs-left">{{ props.item.evaluated_By }}</td>
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

            
            <v-text-field v-model="trg_no" :counter="50" tupe="number" :rules="trg_noRules" label="Trg No" required ></v-text-field>
            <v-text-field v-model="trainingTopic" :counter="50" :rules="trainingTopicRules" label="Training Topic" required ></v-text-field>
            <v-text-field v-model="faculty" :counter="50" :rules="facultyRules" label="Faculty Name" required ></v-text-field>

            <v-dialog
              ref="dialog"
              v-model="modal"
              :return-value.sync="dot"
              persistent
              lazy
              full-width
              width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="dot"
                  label="Date Of Training"
                  prepend-icon="event"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker v-model="dot" scrollable>
                <v-spacer></v-spacer>
                <v-btn flat color="primary" @click="modal = false">Cancel</v-btn>
                <v-btn flat color="primary" @click="$refs.dialog.save(dot)">OK</v-btn>
              </v-date-picker>
            </v-dialog>

            <v-text-field v-model="venue" :counter="50" :rules="venueRules" label="Venue" required ></v-text-field>
            <v-text-field v-model="nop" :counter="50" :rules="nopRules" label="Name of the Participant" required ></v-text-field>
            <v-text-field v-model="score" :counter="50" tupe="number" :rules="scoreRules" label="Enter Score" required ></v-text-field>
            <v-text-field v-model="evl" :counter="300" :rules="evlRules" label="Evalution Criteria" required ></v-text-field>
            <v-text-field v-model="eot" :counter="200" :rules="eotRules" label="Effectiveness of Training" required ></v-text-field>
            <v-text-field v-model="evaluate" :counter="50" :rules="evaluateRules" label="Evaluated By" required ></v-text-field>
            
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
        { text: "Trg No", value: "trg_no" },
        { text: "Training Topic", value: "training_topic" },
        { text: "Date Of Training", value: "date_of_trainig" },
        { text: "Faculty", value: "faculty" },
        { text: "Venue", value: "venue" },
        { text: "Evaluation criteria", value: "evaluation_criteria" },
        { text: "Evaluatd By", value: "evaluated_By" },
      ],
      info: [],
     
      //  push to database
      valid: true,
      modal: false,
      dot: new Date().toISOString().substr(0, 10),
      trg_no:'', trainingTopic:'', faculty:'', venue:'', nop:'', score:'', evl:'', eot: '', evaluate:'',
      
      // form rules or validation
      trg_noRules:[v => !!v || "This field is required"],
      trainingTopicRules:[v => !!v || "This field is required"],
      facultyRules:[v => !!v || "This field is required"],
      venueRules:[v => !!v || "This field is required"],
      nopRules:[v => !!v || "This field is required"],
      scoreRules:[v => !!v || "This field is required"],
      evlRules:[v => !!v || "This field is required"],
      eotRules:[v => !!v || "This field is required"],
      evaluateRules:[v => !!v || "This field is required"],
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
        .get(this.$apiUrl+"training-evalution/")
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
          axios({
              method: "post",
              url: this.$apiUrl+"training-evalution/",
              data: {
                trg_no: self.trg_no ,  
                training_topic: self.trainingTopic , 
                date_of_trainig: self.dot , 
                faculty: self.faculty ,  
                venue: self.venue ,  
                name_of_participant : self.nop ,  
                score: self.score , 
                evaluation_criteria: self.evl , 
                Effectiveness_of_Training: self.eot , 
                evaluated_By: self.evaluate , 
              }
            })
          .then(function(response) {
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