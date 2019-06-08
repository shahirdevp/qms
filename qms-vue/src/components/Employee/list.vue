<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Employee Data</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn color="primary" ref="fileInput" @click.stop="drawer = !drawer">
            Add Employee
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

        <router-link :to="{ path: 'employee/'+ props.item.id }">
          <tr>
        <td class="text-xs-left">

            {{ props.item.employee_ID }}
        </td>
        <td class="text-xs-left">{{ props.item.name_of_the_Employee }}</td>
        <td class="text-xs-left">{{ props.item.position }}</td>
        <td class="text-xs-left">{{ props.item.date_of_join }}</td>
        <td class="text-xs-left">{{ props.item.qualification }}</td>
        </tr>
        </router-link>

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
          <h3>Add Employee</h3>
          <br>
          <v-form ref="form" v-model="valid" id="emp" lazy-validation>
            <v-text-field
              v-model="eid"
              :counter="20"
              :rules="eidRules"
              label="Employee Id"
              required
            ></v-text-field>

            <v-text-field
              v-model="ename"
              :counter="50"
              :rules="enameRules"
              label="Employee Name"
              required
            ></v-text-field>

            <v-dialog
              ref="dialogs"
              v-model="modal1"
              :return-value.sync="dob"
              persistent
              lazy
              full-width
              width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="dob"
                  label="Date Of Birth"
                  prepend-icon="event"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker v-model="dob" scrollable>
                <v-spacer></v-spacer>
                <v-btn flat color="primary" @click="modal1 = false">Cancel</v-btn>
                <v-btn flat color="primary" @click="$refs.dialogs.save(dob)">OK</v-btn>
              </v-date-picker>
            </v-dialog>

            <v-text-field v-model="frname" :counter="50" :rules="frnameRules" label="Fathers Name"></v-text-field>

            <v-text-field
              v-model="qlf"
              :counter="50"
              :rules="qlfRules"
              label="Qualification"
              required
            ></v-text-field>

            <v-text-field
              v-model="position"
              :counter="50"
              :rules="positionRules"
              label="Position"
              required
            ></v-text-field>
            <v-dialog
              ref="dialog"
              v-model="modal"
              :return-value.sync="doj"
              persistent
              lazy
              full-width
              width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="doj"
                  label="Date Of Join"
                  prepend-icon="event"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker v-model="doj" scrollable>
                <v-spacer></v-spacer>
                <v-btn flat color="primary" @click="modal = false">Cancel</v-btn>
                <v-btn flat color="primary" @click="$refs.dialog.save(doj)">OK</v-btn>
              </v-date-picker>
            </v-dialog>

            <template>
              <v-combobox
                v-model="language"
                :items="items"
                :search-input.sync="search"
                hide-selected
                label="Languages Know"
                multiple
                small-chips
              >
                <template v-slot:no-data>
                  <v-list-tile>
                    <v-list-tile-content>
                      <v-list-tile-title>
                        No results matching "
                        <strong>{{ search }}</strong>". Press
                        <kbd>enter</kbd> to create a new one
                      </v-list-tile-title>
                    </v-list-tile-content>
                  </v-list-tile>
                </template>
              </v-combobox>
            </template>

            <v-textarea v-model="addess" label="Address" :counter="300" required></v-textarea>

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
        { text: "ID", align: "left", value: "employee_ID" },
        { text: "Name", value: "name_of_the_Employee" },
        { text: "Position", value: "position" },
        { text: "DOJ", value: "date_of_join" },
        { text: "Qualification", value: "qualification" }
      ],
      tlist: [],

      // languages
      items: [
        "English",
        "Hindi",
        "Malayalam",
        "Kannada",
        "Tamil",
        "Telugu",
        "Urdu",
        " Gujarati",
        "Punjabi",
        "Assamese",
        "Odia",
        "Bengali",
        "Marathi"
      ],
      search: null,

      //  push to database
      valid: true,

      // date picker
      modal1: false,
      modal: false,

      dob: new Date().toISOString().substr(0, 10),
      doj: new Date().toISOString().substr(0, 10),

      eid: "",
      ename: "",
      frname: "",
      qlf: "",
      position: "",
      addess: "",
      language: "",

      // form rules or validation
      eidRules: [v => !!v || "Employee Id is required"],
      enameRules: [v => !!v || "Employee Name is required"],
      frnameRules: [v => !!v || "Employee Father name is required"],
      qlfRules: [v => !!v || "Qualification is required"],
      positionRules: [v => !!v || "Position is required"]
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
        .get(this.$apiUrl+"employee/")
        .then(function(response) {
          self.tlist = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },

    validate: function() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        var self = this;
        var newtxt = '';
        Object.keys(this.language).forEach(key => {
          newtxt += this.language[key]+', ';
        });
          axios({
              method: "post",
              url: this.$apiUrl+"employee/",
              data: {
                name_of_the_Employee: this.ename,
                address: this.addess,
                employee_ID: this.eid,
                fathers_name: this.frname,
                date_of_birth: this.dob,
                qualification: this.qlf,
                date_of_join: this.doj,
                languages_known: newtxt,
                position: this.position,
              }
            })
          .then(function(response) {
            self.getall()
            self.drawer = !self.drawer;
            swal({
              title: "Success",
              type: "success",
              text: "Successfully Employee data Added",
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