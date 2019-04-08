<template>
  <div id="empd">
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Employee Data</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <div :class="{dn : !dn}">
            <v-btn color="info" ref="fileInput" @click.stop="dn = !dn">
              Edit
              <v-icon right>edit</v-icon>
            </v-btn>
            <v-btn color="red" dark ref="fileInput" @click="deleteData()">
              Delete
              <v-icon right>delete</v-icon>
            </v-btn>
          </div>

          <div :class="{dn : dn}">
            <v-btn color="warning" ref="fileInput" @click.stop="dn = !dn">
              Cancel
              <v-icon right>close</v-icon>
            </v-btn>

            <v-btn color="success" ref="fileInput" @click="validate()">
              Save
              <v-icon right>check</v-icon>
            </v-btn>
          </div>
        </div>
      </v-flex>
    </v-layout>

    <!-- Details -->
    <v-card style="margin:15px;padding:15px" :class="{ dn: !dn }">
      <v-layout row wrap>
        <v-flex xs12>
          <div class="c-title">{{ detail.name_of_the_Employee }}</div>
          <div class="c-right-date">HR/F/01 Rev: 00 Date: {{ detail.created_On }}</div>
        </v-flex>
        <v-layout class="text-content" row wrap>
          <v-flex xs6>
            <div class="c-ul">
              <div class="c-list">
                <div class="c-list-lable">Employee ID</div>
                <div class="c-list-content">{{ detail.employee_ID }}</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">Employee Name</div>
                <div class="c-list-content">{{ detail.name_of_the_Employee }}</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">Position</div>
                <div class="c-list-content">{{ detail.position }}</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">Qualification</div>
                <div class="c-list-content">{{ detail.qualification }}</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>
            </div>
          </v-flex>

          <v-flex xs6>
            <div class="c-ul">
              <div class="c-list">
                <div class="c-list-lable">Date Of Birth</div>
                <div class="c-list-content">{{ detail.date_of_birth }}</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">Date Of Join</div>
                <div class="c-list-content">{{ detail.date_of_join }}</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">Languages Know</div>
                <div class="c-list-content">{{ detail.languages_known }}</div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">Address</div>
                <div class="c-list-content">
                  <div class="c-list-content-con">{{ detail.address }}</div>
                </div>
                <div class="c-list-action text-xs-center">
                  <v-btn flat icon color="primary" small>
                    <v-icon>edit</v-icon>
                  </v-btn>
                </div>
              </div>
            </div>
          </v-flex>
        </v-layout>
      </v-layout>
    </v-card>

    <!-- Details -->
    <v-card style="margin:15px;padding:15px" :class="{ dn: dn }">
      <v-layout row wrap>
        <v-flex xs12>
          <div class="c-title">{{ detail.name_of_the_Employee }}</div>
          <div class="c-right-date">HR/F/01 Rev: 00 Date: {{ detail.created_On }}</div>
        </v-flex>
           <v-form ref="form" class="block" v-model="valid"  lazy-validation>
          <v-layout class="text-content" row wrap>
            <v-flex xs6>
              <div class="form-box">
                <v-text-field
                  v-model="detail.employee_ID"
                  :counter="20"
                  :rules="eidRules"
                  label="Employee Id"
                  required
                ></v-text-field>

                <v-text-field
                  v-model="detail.name_of_the_Employee"
                  :counter="50"
                  :rules="enameRules"
                  label="Employee Name"
                  required
                ></v-text-field>

                <v-dialog
                  ref="dialogs"
                  v-model="modal"
                  persistent
                  :return-value.sync="doj"
                  lazy
                  full-width
                  width="290px"
                >
                  <template v-slot:activator="{ on }">
                    <v-text-field
                      v-model="detail.date_of_birth"
                      label="Date Of Birth"
                      prepend-icon="event"
                      readonly
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker v-model="detail.date_of_birth" scrollable>
                    <v-spacer></v-spacer>
                    <v-btn flat color="primary" @click="modal1 = false">Cancel</v-btn>
                    <v-btn flat color="primary" @click="$refs.dialogs.save(detail.date_of_birth)">OK</v-btn>
                  </v-date-picker>
                </v-dialog>

                <v-text-field
                  v-model="detail.fathers_name"
                  :counter="50"
                  :rules="frnameRules"
                  label="Fathers Name"
                ></v-text-field>

                <v-text-field
                  v-model="detail.qualification"
                  :counter="50"
                  :rules="qlfRules"
                  label="Qualification"
                  required
                ></v-text-field>
              </div>
            </v-flex>

            <v-flex xs6>
              <div class="form-box">
                <v-text-field
                  v-model="detail.position"
                  :counter="50"
                  :rules="positionRules"
                  label="Position"
                  required
                ></v-text-field>
                <v-dialog
                  ref="dialog"
                  v-model="modal"
                  :return-value.sync="detail.date_of_join"
                  persistent
                  lazy
                  full-width
                  width="290px"
                >
                  <template v-slot:activator="{ on }">
                    <v-text-field
                      v-model="detail.date_of_join"
                      label="Date Of Join"
                      prepend-icon="event"
                      readonly
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker v-model="detail.date_of_join" scrollable>
                    <v-spacer></v-spacer>
                    <v-btn flat color="primary" @click="modal = false">Cancel</v-btn>
                    <v-btn flat color="primary" @click="$refs.dialog.save(detail.date_of_join)">OK</v-btn>
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
                <v-textarea v-model="detail.address" label="Address" :counter="200" required></v-textarea>
              </div>
            </v-flex>
          </v-layout>
        </v-form>
      </v-layout>
    </v-card>
  </div>
</template>

<style scoped>
.two-column {
  column-count: 2;
  column-gap: 15px;
}
</style>

<style>
.c-title { font-size: 20px; line-height: 35px; position: relative; margin-bottom: 20px; } .c-title:after { position: absolute; content: ""; width: 100%; height: 1.5px; background-color: #e0e0e0; bottom: -5px; left: 0; } .c-list-lable { display: inline-block; width: 33%; color: #6f6f6f; padding: 0 5px 0 0px; } .c-list-content { display: inline-block; width: 67%; padding: 0 5px 0 0px; } .c-list { margin: 0 10px 25px 10px; padding: 10px 5px; width: calc(100% - 56px); position: relative; } .c-list::after { content: ""; position: absolute; width: calc(100% - 65px); height: 1.5px; background: #dadada; left: 0; bottom: 0; } .c-list-lable::before { content: ""; position: absolute; background: #77b8fb; height: 3px; width: 24%; bottom: -1px; left: 0px; z-index: 1; } .c-list-action { position: absolute; right: 4px; top: 0; width: 42px; opacity: 0; transition: 0.3s; } /* .c-list:hover .c-list-action{opacity: 1;} */ .c-list-action .v-icon { font-size: 17px; } .c-right-date { display: inline-block; float: right; position: absolute; right: 18px; top: 25px; } .dn { display: none; } .c-list-content-input input { width: calc(100% - 60px); border-bottom: 1px solid #fff0; } .c-list-content-input input:focus { border-bottom: 1px solid #77b8fb; box-shadow: 0px 5px 5px -7px #0042ff; } .block { display: block; width: 100%; } .form-box { width: calc(100% -65px); width: 90%; } /*  input  */ .ic-list input, .ic-list textarea, .ic-list select { border: 1px solid #c6c6c6; width: calc(100% - 105px); padding: 8px 5px; margin-bottom: 15px; border-radius: 3px; margin-top: 3px; } .ic-list input:focus, .ic-list textarea:focus, .ic-list select:focus { border-color: #799df5; box-shadow: 0px 0px 3px #799df5; } .ic-list-lable { color: rgba(114, 114, 114, 1); } #empd .v-input__prepend-outer { display: none !important; }
</style>



<script>
import swal from "sweetalert2";
import router from "../../router";

export default {
  data() {
    return {
      detail: [],
      dn: true,
      //  push to database
      valid: true,
      // languages
      items: [ "English", "Hindi", "Malayalam", "Kannada", "Tamil", "Telugu", "Urdu", " Gujarati", "Punjabi", "Assamese", "Odia", "Bengali", "Marathi" ],
      search: null,
      // date picker
      modal1: false,
      modal: false,
      dob: "",
      doj: "",
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
    this.getdetails();
  },
  computed: {},
  methods: {
    getdetails() {
      var ts = window.location.pathname.split("/");
      var parQuery = ts[ts.length - 1];
      var self = this;
      axios
        .get(this.$apiUrl+"employee/" + parQuery)
        .then(function(response) {
          self.detail = response.data;
          self.language = [response.data.languages_known]
          console.log(self.detail);
          
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    validate: function() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        var self = this;
        var newtxt = "";
        Object.keys(this.language).forEach(key => {
          newtxt += this.language[key] + ", ";
        });
        var ts = window.location.pathname.split("/");
        var parQuery = ts[ts.length - 1];
        var self = this;
        
        axios({
          method: "put",
          url: this.$apiUrl+"/employee/" + parQuery,
          data: {
            name_of_the_Employee: self.detail.name_of_the_Employee,
            address: self.detail.address,
            employee_ID: self.detail.employee_ID,
            fathers_name: self.detail.fathers_name,
            date_of_birth: self.detail.date_of_birth,
            qualification: self.detail.qualification,
            date_of_join: self.detail.date_of_join,
            languages_known: self.detail.languages_known,
            position: self.detail.position
          }
        })
          .then(function(response) {
            self.dn = !response.dn;
            swal({
              title: "Success",
              type: "success",
              text: "Successfully edited",
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
    deleteData() {
      var ts = window.location.pathname.split("/");
      var parQuery = ts[ts.length - 1];
      var self = this;
      swal({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
      }).then(result => {
        if (result.value) {
          axios
            .delete(
              this.$apiUrl+"employee/" + parQuery 
            )
            .then(function(response) {
              swal({
                title: "Success",
                text: "Successfully Delete",
                type: "success",
                showConfirmButton: false,
                showCloseButton: false,
                timer: 3000
              });
              router.push("/employee");
            })
            .catch(function(error) {
              swal({
                type: "error",
                title: "Oops...",
                text: "Something went wrong!",
                showConfirmButton: false,
                showCloseButton: false,
                timer: 3000
              });
            });
        }
      });
    }
  }
};
</script>

